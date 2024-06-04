$(document).ready(function(){
    // 加载活动信息
    $.ajax({
        url: 'http://127.0.0.1:5000/admin/projects', // 更新 URL
        method: 'GET',
        success: function(response) {
            // 检查响应状态是否为成功
            if (response.state === 1) {
                let activities = response.data; // 直接访问 data 属性
                let activityRows = '';
                activities.forEach(activity => {
                    // 使用活动对象的属性来构建 HTML 字符串
                    activityRows += `
                    <tr>
                        <td>${activity.title}</td>
                        <td>${activity.start_time}</td>
                        <td>${activity.end_time}</td>
                        <td>${activity.situation_province}</td>
                        <td>${activity.situation_city}</td>
                        <td>${activity.require_num}</td>
                        <td>${activity.value}</td>
                    </tr>`;
                });
                $('#projects-table tbody').html(activityRows);
            } else {
                // 处理非成功状态，例如显示错误消息
                console.error('获取活动信息失败');
            }
        },
        error: function(xhr, status, error) {
            // 处理 AJAX 请求失败的情况
            console.error('Error fetching activities:', error);
        }
    });
});