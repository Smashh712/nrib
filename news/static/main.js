const delay = (ms) => new Promise((res) => setTimeout(res, ms));
logo.onclick = async function () {
  intro.classList.add("ani");
  intro.style.visibility = "visible";

  test();
};

async function test() {
  await delay(0);
  intros.classList.add("ani");
  intros.style.visibility = "visible";
}

window.addEventListener("DOMContentLoaded", async function () {
  intro.classList.add("ani");
  intro.style.visibility = "visible";
  test();
});
