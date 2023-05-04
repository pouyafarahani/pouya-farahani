const typingElem = document.querySelector(".typing");
const items = ["برنامه نویس وب", "برنامه نویس پایتون", "برنامه نویس بک اند"];

new Typed(typingElem, {
  strings: items,
  typeSpeed: 80,
  smartBackspace: false,
  loop: true,
  showCursor: false,
  backDelay: 3000,
});

const links = [...document.querySelectorAll('a[href^="#"]')];

window.addEventListener("hashchange", (e) => e.preventDefault());

for (let link of links) {
  link.addEventListener("click", function (ev) {
    ev.preventDefault();

    const elem =
      this.hash.trim() === "" ? undefined : document.querySelector(this.hash);

    if (elem) {
      window.scrollTo(
        0,
        elem.getBoundingClientRect().top + window.scrollY - 100
      );
    } else {
      window.scrollTo(0, 0);
    }
  });
}
