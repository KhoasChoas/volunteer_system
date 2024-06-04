var swiper = new Swiper(".blog-slider", {
  spaceBetween: 30,
  effect: "fade",
  loop: true,
  mousewheel: {
    invert: false,
  },

  pagination: {
    el: ".blog-slider_pagination",
    clickable: true,
  },
});
var quitout = document.getElementById("quitout");
quitout.addEventListener("submit", function (event) {
  // 阻止表单的默认提交行为
  event.preventDefault();
  // 改变当前页面的URL，实现页面跳转
  window.location.href = "../sign_login/sign_login.html";
});
