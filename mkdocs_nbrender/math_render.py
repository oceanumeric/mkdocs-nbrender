"""
copyright @Python-Markdown 
          (https://github.com/Python-Markdown)
All processor are based on regular expression
Regular expressions allow us to not just match text but also to 
extract information for further processing. This is done by 
defining groups of characters and capturing them using the 
special parentheses ( and ) metacharacters. Any sub-pattern inside 
a pair of parentheses will be captured as a group. In practice, 
this can be used to extract information like phone numbers 
or emails from all sorts of data.
"""

# import markdown inline processor 
from markdown import util as md_util
from markdown.inlinepatterns import InlineProcessor



class InlineMath(InlineProcessor):
    """
    Inline Math Processor
    """
    # stx: start of a text
    # etx: end of a text 
    # ord: integer of unicode representation 
    ESCAPED_BSLASH = '%s%s%s' % (md_util.STX, ord('\\'), md_util.ETX)
    
    def __init__(self, pattern, config, latex2svg, md):
        """
        pattern : $ $ or \[ \]
        config : configuration file from InlineProcessor 
        """
        # reply on the configuration of markdown inline patterns
        self.inline_class = config.get('inline_class', '')
        # create an instance for latex2svg 
        self.latex2svg = latex2svg
        # initialize the InlineProcessor class 
        InlineProcessor.__init__(self, pattern, md)
        
    def hadleMatch(self, m, data):
        """
        Function taken from @Python-Markdown
        
        Python regex capturing groups match several distinct patterns 
        inside the same target string using group() and groups()
        """
        # Handle escapes
        




if __name__ == "__main__":

    print('%s%s%s' % (md_util.STX, ord('\\'), md_util.ETX))