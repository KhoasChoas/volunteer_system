$(document).ready(function(){
    // 加载活动信息
    $.ajax({
        url: 'http://127.0.0.1:5000/admin/projects', // 更新 URL
        method: 'GET',
        dataType: 'json', // 明确指定你期望从服务器接收 JSON 数据
        success: function(response) {
            console.log('请求成功:', response);
            // 检查响应状态是否为成功
            if (response.state === 1) {
                let Projects = response.data; // 直接访问 data 属性
                let projectRows = '';
                Projects.forEach(Project => {
                    // 使用活动对象的属性来构建 HTML 字符串
                    projectRows += `
                    <tr>
                        <td>${Project.title}</td>
                        <td>${Project.start_time}</td>
                        <td>${Project.end_time}</td>
                        <td>${Project.situation_province}</td>
                        <td>${Project.situation_city}</td>
                        <td>${Project.require_num}</td>
                        <td>${Project.value}</td>
                    </tr>`;
                });
                $('#activity-table tbody').html(projectRows);
            } else {
                // 处理非成功状态，例如显示错误消息
                console.error('获取活动信息失败');
            }
        },
    });

    // 添加活动按钮点击事件
    $('#add-activity').on('click', function() {
        // 实现添加活动的逻辑
        console.log('添加活动按钮被点击');
        let newProject = {
            id: prompt('请输入活动编号:'),
            title: prompt('请输入活动名称:'),
            start_time: prompt('请输入开始时间:'),
            end_time: prompt('请输入结束时间:'),
            situation_province: prompt('请输入地点-省份:'),
            situation_city: prompt('请输入地点-城市:'),
            require_num: prompt('请输入所需志愿者数量:'),
            value: prompt('请输入给予的志愿时长:')
        };
        $.ajax({
            url: 'http://127.0.0.1:5000/admin/add_project',
            method: 'POST',
            data: JSON.stringify(newProject),
            contentType: 'application/json',
            success: function(response) {
                if (response.state === 1) {
                    alert('活动添加成功');
                    location.reload();
                } else {
                    alert('添加活动失败');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error adding activity:', error);
                alert('添加活动失败');
            }
        });
    });

    // 修改活动按钮点击事件
    $('#edit-activity').on('click', function() {
        // 实现修改活动的逻辑
        console.log('修改活动按钮被点击');
        let projectId = prompt('请输入要修改的活动编号:');
        let updatedProject = {
            id: projectId,
            title: prompt('请输入新的活动名称:'),
            start_time: prompt('请输入新的开始时间:'),
            end_time: prompt('请输入新的结束时间:'),
            situation_province: prompt('请输入新的地点-省份:'),
            situation_city: prompt('请输入新的地点-城市:'),
            require_num: prompt('请输入新的所需志愿者数量:'),
            value: prompt('请输入新的给予的志愿时长:')
        };
        $.ajax({
            url: 'http://127.0.0.1:5000/admin/edit_project',
            method: 'POST',
            data: JSON.stringify(updatedProject),
            contentType: 'application/json',
            success: function(response) {
                if (response.state === 1) {
                    alert('活动修改成功');
                    location.reload();
                } else {
                    alert('修改活动失败');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error editing activity:', error);
                alert('修改活动失败');
            }
        });
    });
});
