document.addEventListener("DOMContentLoaded", function () {
  var elements = document.getElementsByClassName("copyButton");
  Array.from(elements).forEach(function (element) {
    element.addEventListener("click", (e) => {
      navigator.clipboard
        .writeText(
          element.parentNode.getElementsByClassName("clipboard-copy-txt")[0].textContent.trim()
          )
        .then(
          function () {
            console.log("Async: Copying to clipboard was successful!");
            var notificationBox = element.getElementsByClassName("noticeCopy")[0];
            notificationBox.removeAttribute("hidden");
            setTimeout(function () {
              notificationBox.setAttribute("hidden", "hidden");
            }, 2000);
          },
          function (err) {
            console.error("Async: Could not copy text: ", err);
          }
        );
    });
  });
});