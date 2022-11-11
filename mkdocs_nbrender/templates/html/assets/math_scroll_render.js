
var browserHt = window.innerHeight;

var observer_mj = new IntersectionObserver(handler_mj, {
    root: null,
    rootMargin: '500px 0px',
    threshold: 0
});

function handler_mj(entries, observer_mj) {
    //for (entry of entries) {
    entries.forEach(function(entry) {
        if(entry.isIntersecting) {
            if( typeof(MathJax) == "undefined" ) {
                window.MathJax = {
                    startup: {
                        typeset: false,
                    },
                    tex: {
                        inlineMath: [['$', '$'], ['\\(', '\\)']],
                        displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                        tags: 'ams',
                    },
                    chtml: {
                        scale: 0.975
                    }
                };
                // Need to add these for pages with \boldsymbol
                if(gebi("content").innerHTML.indexOf("boldsymbol") > -1) {
                    window.MathJax['loader'] = {load: ['[tex]/boldsymbol']};
                    window.MathJax['tex']['packages'] = {'[+]': ['boldsymbol']};
                }
                var mjScript = document.createElement('script');
                mjScript.setAttribute('src','https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js');
                document.head.appendChild(mjScript);

                var waitCycles = 0;

                function waitForMj() {

                    if(typeof(MathJax) != 'undefined' && typeof(MathJax.typesetPromise) == 'function' ) {

                        console.log("MJ loaded.");

                        // Loop through on-screen (and close by) entries
                        // for (entry of entries) {
                        entries.forEach(function(entry) {
                            if(entry.isIntersecting) {
                                MathJax.typesetPromise([entry.target]).then(function() {
                                    // Done after processing

                                    console.log("Eqn proc by MJ (init)");
                                    
                                    addOverflowXauto();
                                    // Stop watching the element
                                    observer_mj.unobserve(entry.target);
                                });
                            }
                        });
                        cancelAnimationFrame(raf);
                    } else {
                        
                        console.log("MJ loading...");
                        
                        waitCycles++;
                        if(waitCycles<20) {
                            window.requestAnimationFrame(waitForMj);
                        } else {
                            // Give up on MathJax
                            cancelAnimationFrame(raf);
                        }
                    }
                }
                var raf = window.requestAnimationFrame(waitForMj);

                //break;

            } else if( typeof(MathJax.typesetPromise) != "undefined" ){

                if(entry.isIntersecting && entry.target.innerHTML.indexOf('mjx-math') == -1) {

                    // This processes the math in the node
                    MathJax.typesetPromise([entry.target]).then(function() {
                        // Done after processing						
                        console.log("Eqn proc by MJ");
                        
                        addOverflowXauto();
                        // Stop watching the element
                        observer_mj.unobserve(entry.target);
                    });
                }
            }
        }
    });
}

var contentDivs = document.querySelectorAll('#grnBorder, #content');

contentDivs.forEach(function(contentDiv) {
    contentDiv.querySelectorAll('p, div, ul, ol, li, table').forEach(function(node) {
        if(node.textContent.indexOf("$") > -1 ) {
            observer_mj.observe(node);
        }
    });
});
