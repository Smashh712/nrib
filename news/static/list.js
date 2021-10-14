function boxsize() {
  var box = document.getElementById("boxx");
  box.style.height = 550;
}

function boxsize2() {
  var box = document.getElementById("boxx");
  box.style.height = 550;
}
document.getElementById("k1").onmouseover = function () {
  boxsize();
};
document.getElementById("k1").onmouseout = function () {
  boxsize2();
};
document.getElementById("k2").onmouseover = function () {
  boxsize();
};
document.getElementById("k2").onmouseout = function () {
  boxsize2();
};
document.getElementById("k3").onmouseover = function () {
  boxsize();
};
document.getElementById("k3").onmouseout = function () {
  boxsize2();
};
