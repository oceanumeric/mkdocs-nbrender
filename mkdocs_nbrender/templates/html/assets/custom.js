
// change svg width
var div_svg = document.getElementsByClassName('jp-RenderedSVG');
for (const element of div_svg) {
    element.childNodes[3].setAttribute("width", "100%")
    element.childNodes[3].setAttribute("height", "100%")
}
