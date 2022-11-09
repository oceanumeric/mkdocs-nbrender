import re
import os
import json 
import unicodedata

import mkdocs
from mkdocs.config import config_options
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from mkdocs.structure.toc import get_toc
from mkdocs.tests.base import get_markdown_toc

# nbconverter
from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.exporters import HTMLExporter
from nbconvert.filters.highlight import _pygments_highlight

# high light
from pygments import highlight
from pygments.formatters import HtmlFormatter



# set file path
class Settings:
    def __init__(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.templates_dir = os.path.join(this_dir, "templates")

path_settings = Settings()

# read the jupyter notebook file
class NotebookFile(File):
    """
    Objects points to the source and destination locations of a file.
    """
    def __init__(self, file, use_directory_urls, site_dir, **kwargs):
        """
        file: file name
        use_directory_urls:
                    true - map to html index
                    false - use markdown directly
        """
        self.file = file
        # relative path
        self.dest_path = self._get_dest_path(use_directory_urls)
        # absolute path
        self.abs_dest_path = os.path.normpath(
            os.path.join(site_dir, self.dest_path)
        )
        # where the file will be linked
        self.url = self._get_url(use_directory_urls)

    def __getattr__(self, item):
        return self.file.__getattribute__(item)

    def is_documentation_page(self):
        return True


# slugify url 
def _slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


# nb converter app instance 
def _nbconverter_app():
    """
    a customized notebook converter 
    """
    # initialize the nb converter app 
    app = NbConvertApp()
    # load configure file 
    app.load_config_file()
    
    # update config file
    app.config.update(
         {
             "TemplateExporter" : { 
                "exclude_input_prompt": True,
                "exclude_output_prompt": True
                },
             "HTMLExporter" : {
                 "sanitize_html": True
             }
             
         }
    )
    
    return app


def _highlight_code(source, language='python', metadata=None):
    """
    Change CSS class names from .highlight to .highlight-ipynb.
    This are for the <div> that contains the <pre>
    This modifies only the HTML not CSS.
    On the `notebook.html.js` template we modify the CSS styles.
    """

    formatter = HtmlFormatter(cssclass="highlight-ipynb hl-" + language)
    output = _pygments_highlight(source, formatter, language, metadata)

    clipboard_copy_txt = f"""<div class="clipboard-copy-txt">{source}</div>
    """
    return output + clipboard_copy_txt


def nb_transmute(file_path):
    """
    transmute notebook with template
    """
    app = _nbconverter_app()
    
    # template file 
    # path = nbtransfer/templates
    template_file = 'html/notebook.html.j2'
    # add extra template path 
    extra_template_paths = [path_settings.templates_dir]
    
    # highlight code
    filters = {
        "highlight_code": _highlight_code,
        # "markdown2html": custom_markdown2html,
    }
    
    # html exporter 
    html_exporter = HTMLExporter(
        config = app.config,
        template_file = template_file,
        extra_template_paths = extra_template_paths,
        filters=filters
    )
    
    # get kernel language for highlight 
    kernel_language = "python"  # default language 
    with open(file_path, "r", encoding="utf-8") as f:
        nb_json = json.load(f)
        kernel_language = nb_json["metadata"]["kernelspec"]["language"]
        
    # export html 
    content, resources = html_exporter.from_filename(file_path)
    
    return content 


if __name__ == "__main__":
    # os
    print(os.getcwd())
    foo = Settings()
    print(foo.templates_dir)
    # test convert 
    content = nb_transmute("docs/notebooks/mynb.ipynb")
    with open("docs/notebooks/demo.html", "w") as f:
        f.write(content)
        
    content = nb_transmute("docs/notebooks/ch4.ipynb")
    with open("docs/notebooks/ch4_test.html", "w") as f:
        f.write(content)