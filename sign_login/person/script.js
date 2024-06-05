$(document).ready(function() {
	const urlParams = new URLSearchParams(window.location.search);
	// const adminaccount = urlParams.get('account');
	const adminaccount = 202205566627;
	$.ajax({
        url: `http://192.168.163.167:5000/admin?account=${adminaccount}`, // 更新 URL
        method: 'GET',
        success: function(response) {
            // 检查响应状态是否为成功
            if (response.state === 1) {
                let Users = response.data; // 直接访问 data 属性
				// alert(Users.username);
				// alert(Users.sex);
				// alert(Users.account);
				// alert(Users.phone);
				// alert(Users.email);
				// alert(Users.intro);
				// alert(response.data);
				// $('#username').val(Users.username);
				// $('#sex').val(Users.sex);
				// $('#account').val(User.account);
				// $('#phone').val(User.phone);
				// $('#email').val(User.email);
				// $('#intro').val(User.intro);
				document.getElementById('username').textContent = Users.username;
				document.getElementById('sex').textContent = Users.sex;
				document.getElementById('account').textContent = Users.account;
				document.getElementById('phone').textContent = Users.phone;
				document.getElementById('email').textContent = Users.email;
				document.getElementById('intro').textContent = Users.intro;
                    // 使用活动对象的属性来构建 HTML 字符串
			}
		}
	});
});

