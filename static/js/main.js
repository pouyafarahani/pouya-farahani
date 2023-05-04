"use strict";

const cursorElem = document.querySelector(".cursor-elem");
const toggleThemeBtn = document.querySelector("#themeButton");

const lightIcon = document.querySelector("svg.lightIcon");
const darkIcon = document.querySelector("svg.darkIcon");

toggleThemeBtn.addEventListener("click", () => {
  document.documentElement.classList.toggle("dark");
  const theme = document.documentElement.classList.contains("dark")
    ? "dark"
    : "light";
  localStorage.setItem("theme", theme);
  toggleDarkLight();
});

function toggleDarkLight() {
  const defaultTheme = localStorage.getItem("theme");

  if (defaultTheme === "light") {
    document.documentElement.classList.remove("dark");
  } else if (defaultTheme === "dark") {
    document.documentElement.classList.add("dark");
  }

  lightIcon.style.display = "none";
  darkIcon.style.display = "none";

  if (document.documentElement.classList.contains("dark")) {
    darkIcon.style.display = "block";
  } else {
    lightIcon.style.display = "block";
  }
}

toggleDarkLight();

const navbar = document.querySelector(".navbar");
const divElem = document.createElement("div");
divElem.style.height = navbar.getBoundingClientRect().height.toString() + "px";

function makeNavbarFixed() {
  navbar.classList.replace("dark:bg-neutral-800/50", "dark:bg-neutral-800/95");
  navbar.classList.replace("bg-white/80", "bg-white/95");
  navbar.classList.replace("relative", "fixed");
  navbar.classList.add("top-0", "right-0", "left-0", "py-0", "shadow");
  navbar.firstElementChild.classList.replace("py-6", "py-3");
  document.body.insertBefore(divElem, document.body.firstChild);
}

function makeNavbarStatic() {
  navbar.classList.replace("dark:bg-neutral-800/95", "dark:bg-neutral-800/50");
  navbar.classList.replace("bg-white/95", "bg-white/80");
  navbar.classList.replace("fixed", "relative");
  navbar.classList.remove("top-0", "right-0", "left-0", "shadow");
  navbar.firstElementChild.classList.replace("py-3", "py-6");
  document.body.removeChild(divElem);
}

document.addEventListener("scroll", () => {
  const { scrollY } = window;
  if (scrollY > 100 && !navbar.classList.contains("fixed")) makeNavbarFixed();
  else if (scrollY <= 100 && navbar.classList.contains("fixed"))
    makeNavbarStatic();
});

const collapseToggle = document.querySelector("button.collapse-item");
const collapseElem = document.querySelector("ul.collapse-item");

collapseToggle.addEventListener("click", () => {
  if (collapseElem.classList.contains("hidden"))
    collapseElem.classList.replace("hidden", "flex");
  else collapseElem.classList.replace("flex", "hidden");
});

const speed = 0.08;

const stats = {
  mouseX: window.innerWidth / 2,
  mouseY: window.innerHeight / 2,
  ballX: window.innerWidth / 2,
  ballY: window.innerHeight / 2,
  bigMode: false,
};

function animate() {
  if (window.innerWidth < 1024)
    return setTimeout(() => requestAnimationFrame(animate), 200);

  const distanceX = stats.mouseX - stats.ballX;
  const distanceY = stats.mouseY - stats.ballY;

  stats.ballX = stats.ballX + distanceX * speed;
  stats.ballY = stats.ballY + distanceY * speed;

  cursorElem.style.left = stats.ballX + "px";
  cursorElem.style.top = stats.ballY + "px";

  const elementFromPoint = document.elementFromPoint(stats.ballX, stats.ballY);

  if (elementFromPoint)
    stats.bigMode =
      window.getComputedStyle(elementFromPoint).cursor === "pointer";

  if (stats.bigMode) cursorElem.style.padding = "0.5rem";
  else cursorElem.style.padding = "0";

  requestAnimationFrame(animate);
}

animate();

document.addEventListener("mousemove", (ev) => {
  stats.mouseX = ev.clientX;
  stats.mouseY = ev.clientY;
});
