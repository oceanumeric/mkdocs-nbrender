// clean body attribute 
body_dom = document.getElementsByTagName("BODY")[0]
// add class name
body_dom.classList.add("jupyter-body")

// change svg width
var div_svg = document.getElementsByClassName('jp-RenderedSVG');

for (const element of div_svg) {
    element.childNodes[3].setAttribute("width", "100%")
    element.childNodes[3].setAttribute("height", "auto")
}