// create a toc div
var toc_div = document.createElement("nav")
toc_div.classList.add("nav-toc")
document.body.append(toc_div)

// add toc 
nav_toc = ""
all_h2 = document.getElementsByTagName('h2'); 
var new_line, h2_txt, h2_a; 

for (const element of all_h2) {
    h2_txt = element.textContent; 
    h2_a = "#" + element.attributes.id.textContent
    // slice the last tag
    h2_txt = h2_txt.slice(0, h2_txt.length-1)
    
    new_line =
    "<li>" + "<a href='" + h2_a + "'>" + h2_txt  + "</a>" + "</li>";

    nav_toc += new_line; 
}


// select nav-toc 

dom_nav_toc = document.getElementsByClassName("nav-toc");
dom_nav_toc[0].innerHTML += nav_toc; 