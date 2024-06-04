$(document).ready(function() {
	const urlParams = new URLSearchParams(window.location.search);
	const adminaccount = urlParams.get('account');
	$.ajax({
        url: `http://192.168.163.167:5000/admin/activate?account=${adminaccount}`, // 更新 URL
        method: 'GET',
        success: function(response) {
            // 检查响应状态是否为成功
            if (response.state === 1) {
                let User = response.data; // 直接访问 data 属性
				// alert(response.data);
					$('#username').val(User.username);
					$('#sex').val(User.sex);
					$('#account').val(User.account);
					$('#phone').val(User.phone);
					$('#email').val(User.email);
					$('#intro').val(User.intro);
                    // 使用活动对象的属性来构建 HTML 字符串
			}
		}
	});
});

