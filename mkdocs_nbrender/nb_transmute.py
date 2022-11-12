# nbconverter
import os
import re
import json 
from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.exporters import HTMLExporter
from nbconvert.filters.highlight import _pygments_highlight
from pygments.formatters import HtmlFormatter



# set file path
class Settings:
    def __init__(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.templates_dir = os.path.join(this_dir, "templates")

path_settings = Settings()


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
    # you can do so many things with this configuration 
    app.config.update(
         {
             "TemplateExporter" : { 
                "exclude_input_prompt": True,  # In[no_prompt]
                "exclude_output_prompt": True  # Out[no_prompt]
                },
             "HTMLExporter" : {
                 "sanitize_html": True,
                 "theme": 'light'
             },
             # add highlight settings
             "CSSHTMLHeaderPreprocessor": {
                "enabled": True,
                "highlight_class": ".highlight-ipynb",
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

    # ! Important: parsing raw string with '\n'
    # use it to copy 
    clipboard_copy_txt = f"""
    <div class="clipboard-copy-txt">
        <pre>
            <code>
                {source}
            </code>
        </pre>
    </div>
    """
    return output + clipboard_copy_txt


def _nb_md(file_path):
    """Convert a notebook to markdown
    We use a template that removed all code cells because if the body
    is to big ( with javascript and CSS) it takes to long to read and parse
    """
    app = _nbconverter_app()
    
    # template file 
    # path = nbtransfer/templates
    template_file = 'md/md.j2'
    # add extra template path 
    extra_template_paths = [path_settings.templates_dir]


def _get_nb_toc(fpath):
    """Returns a TOC for the Notebook
    It does that by converting first to MD
    """
    pass

def _latex_to_svg(source):
    """
    collect latex equations
    """
    latex_equations = {
        'inline': [],
        'display': []
    }
    return None


def nb_transmute(file_path, theme=None):
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
        "latex_to_svg": _latex_to_svg, 
    }
    
    # html exporter 
    html_exporter = HTMLExporter(
        config = app.config,
        template_file = template_file,
        extra_template_paths = extra_template_paths,
        filters=filters
        # theme=theme,
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
