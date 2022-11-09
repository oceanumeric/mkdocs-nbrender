import os
import sys

from mkdocs.structure.files import File, Files
from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

# local module
from nb_transmute import nb_transmute


# everything starts from the baseplugin
class NewPlugin(BasePlugin):
    config_scheme = (
        ("theme", config_options.Type(str, default=""))
        ("code_folding", config_options.Type(bool, default=True))
    )

    _supported_extensions = [".ipynb", ".py"]

    def __init__(self):
        # once it was called, it turn enabled on 
        self.enabled = True
    
    # no pre build 
    # def on_pre_build(self, config):
    #     return

    def on_files(self, files, config) ->Files:
        """
        The file event was called after the file collection is populated
        from the docs_dir (default: docs)
        Simply collect all ipynb files
            used mkdocs api Files (a collection of file objects)
        """
        nb_files = Files(
            [NbFile(file, **config) for file in files]
        )

        return nb_files

    #------- all following stages are not needed -------------# 
    # no on_nav as it was rendered by index.md
    # def on_nav(self, nav, config, files):
    #     return nav

    # def on_config(self, config):
    #     return config

    # def on_post_build(self, config):
    #     return

    # def on_pre_template(self, template, template_name, config):
    #     return template

    # def on_template_context(self, context, template_name, config):
    #     return context
    
    # def on_post_template(self, output_content, template_name, config):
    #     return output_content
    #------- we will use nbconverter to render html-------------# 
    
    def on_pre_page(self, page, config, files):
        """
        Populate page 
        """
        theme = self.config["theme"]

        def _nb_convert(self, config, files):
            _body = nb_transmute(page.file.abs_src_path, theme=theme)
            self.content = _body 

        return page



# convert ipynb file into the valid ones for mkdocs
class NbFile(File):
    """
    Wraps a regular File object to make .ipynb files appear as
    valid documentation files.
    author: @danielfrg (github)
    """
    def __init__(self, file, use_directory_urls, site_dir, **kwargs):
        self.file = file
        self.dest_path = self._get_dest_path(use_directory_urls)
        self.abs_dest_path = os.path.normpath(
            os.path.join(site_dir, self.dest_path)
        )
        self.url = self._get_url(use_directory_urls)

    def __getattr__(self, item):
        return self.file.__getattribute__(item)

    def is_documentation_page(self):
        return True

