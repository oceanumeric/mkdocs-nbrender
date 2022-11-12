from latex2svg import latex2svg


# template 
template = r"""
\documentclass[{{ fontsize }}pt,preview]{standalone}
{{ preamble }}
\begin{document}
\begin{preview}
{{ code }}
\end{preview}
\end{document}
"""

# preamble with mathjax fonts 
preamble = r"""
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{mathptmx}
\usepackage{mathjax}
"""

latex_cmd = 'latex -interaction nonstopmode -halt-on-error'
dvisvgm_cmd = 'dvisvgm --no-fonts'

parameters = {
    'fontsize': 12,  # pt
    'template': template,
    'preamble': preamble,
    'latex_cmd': latex_cmd,
    'dvisvgm_cmd': dvisvgm_cmd,
    'libgs': None,
}

# call the function 
out = latex2svg(r"""\( 
                F(X) = P(X \leq x)
                \)""",
                params=parameters
                )

print(out['svg'])  # rendered SVG