document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const button = form.querySelector("button");
  
    form.addEventListener("submit", function () {
      button.disabled = true;
      button.textContent = "Searching...";
    });
  });
  