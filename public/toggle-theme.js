const themeValue = "dark";

function applyTheme(doc = document) {
  doc.firstElementChild?.setAttribute("data-theme", themeValue);

  const bgColor =
    doc === document
      ? window.getComputedStyle(document.body).backgroundColor
      : document
          .querySelector("meta[name='theme-color']")
          ?.getAttribute("content");

  if (bgColor) {
    doc.querySelector("meta[name='theme-color']")?.setAttribute("content", bgColor);
  }
}

applyTheme();

window.addEventListener("load", () => {
  applyTheme();
});

document.addEventListener("astro:after-swap", () => {
  applyTheme();
});

document.addEventListener("astro:before-swap", event => {
  applyTheme(event.newDocument);
});
