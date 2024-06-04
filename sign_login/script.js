// 获取按钮元素
const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
var tomain = document.getElementById("tomain");
const subsignup = document.getElementById("subsignup");
const container = document.querySelector(".container");
// 给按钮添加点击事件监听器
signInBtn.addEventListener("click", () => {
  // 从class 属性中移除一个或多个类名，进入登录页面
  container.classList.remove("right-panel-active"); //这个来自于网站的css
});

signUpBtn.addEventListener("click", () => {
  // 从class 属性添加一个或多个类名，进入注册页面
  container.classList.add("right-panel-active");
});
tomain.addEventListener("submit", function (event) {
  // 阻止表单的默认提交行为
  event.preventDefault();
  // 改变当前页面的URL，实现页面跳转
  window.location.href = "./main/main.html";
});

subsignup.addEventListener("submit", function (event) {
  // 阻止表单的默认提交行为
  event.preventDefault();

  // 你可以在这里添加处理表单数据的代码
  // 例如，验证表单字段或发送AJAX请求

  // 假设我们验证通过，并想要提交表单（通常你不会同时阻止提交和手动提交）
  // 但这里只是为了演示
  alert("注册成功！请点击左侧“返回登录”");
});
//提交数据
$("#submit_login_Button").click(function () {
  event.preventDefault(); // 阻止表单的默认提交行为

  // 获取用户输入的数据
  var formData = $("#tomain").serialize();

  // 使用 $.ajax 发送 POST 请求
  $.ajax({
    url: "http://192.168.163.167:5000/login", // 后端接收数据的 URL
    method: "POST",
    data: formData,
    success: function (response) {
      data = response.data;
      if (response.state === 1) {
        alert("登录成功");
        window.location.href = `main/main.html?account=${formData.account}`;
      } else {
        alert(data);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error publishing activity:", error);
      alert("登录失败");
    },
  });
});
$("#submit_sign_Button").click(function () {
  event.preventDefault(); // 阻止表单的默认提交行为

  // 获取用户输入的数据
  var formData = $("#subsignup").serialize();
  // 使用 $.ajax 发送 POST 请求
  $.ajax({
    url: "http://192.168.163.167:5000/register", // 后端接收数据的 URL
    method: "POST",
    data: formData,
    success: function (response) {
      data = response.data;
      if (response.state === 1) {
        alert("注册成功");
        location.reload(); // 刷新页面
      } else {
        alert(data);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error publishing activity:", error);
      alert(formData);
    },
  });
});
