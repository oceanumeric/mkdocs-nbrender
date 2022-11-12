
// change svg width
var div_svg = document.getElementsByClassName('jp-RenderedSVG');
for (const element of div_svg) {
    element.childNodes[3].setAttribute("width", "100%")
    element.childNodes[3].setAttribute("height", "100%")
}

// create a toc div
var toc_div = document.createElement("div")
toc_div.classList.add("toc")
document.body.insertBefore(toc_div, document.body.firstChild);