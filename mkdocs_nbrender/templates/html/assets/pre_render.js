var mjpage = require("mathjax-node-page").mjpage;
var jsdom = require("jsdom");
var fs = require("fs");
var path = require("path");

const {JSDOM} = jsdom;

var renderMathjaxForFile = (dir, fileName, callback) => {
  var fullPath = path.join(dir, fileName);
  var html = fs.readFile(fullPath, (err, data) => {
    const dom = new JSDOM(data);
    var document = dom.window.document;
    console.log("Rendering:", fileName);

    mjpage(document.body.innerHTML, 
      {format: ["TeX"]},
      {svg:true},  // do not put equation number
    function(result) {
      "use strict";
      document.body.innerHTML = result;
      var HTML = "<!DOCTYPE html>\n" + document.documentElement.outerHTML.replace(/^(\n|\s)*/, "");
      fs.writeFileSync(fullPath, HTML);
      callback();
      console.log("Rendering is DONE");
    });
  });
};


// Current directory: /home/zou/Github/mkdocs-nbrender
var file_path = "docs/notebooks/"
var file_name = "ch4_test.html"

var pending = 50;

var closeWhenDone = () => {
    pending -= 1;
    if (pending === 0) {
        console.log("Rendering is done");
        process.exit();
    }
  };

renderMathjaxForFile(file_path, file_name, closeWhenDone);

