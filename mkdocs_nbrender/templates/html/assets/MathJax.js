window.MathJax = {
        loader: {
            load: ['ui/lazy', 'output/svg']
        }, 
        tex: {
            tags: "ams",
            useLabelIds: true,
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        options: {
            lazyMargin: '500px',
            // ignoreHtmlClass: ".*|",
            // processHtmlClass: "arithmatex"
        }, 
        startup: {
            input: ['tex'],
            output: 'svg'
        }
};
(function () {
        var script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
        script.async = true;
        document.head.appendChild(script);
})();