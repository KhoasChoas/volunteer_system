$(document).ready(function() {
    // 加载活动信息
    $.ajax({
        url: 'http://192.168.163.167:5000/admin/projects?account=202205566627', // 更新 URL
        method: 'GET',
        success: function(response) {
            // 检查响应状态是否为成功
            if (response.state === 1) {
                let Projects = response.data; // 直接访问 data 属性
                let projectRows = '';
                Projects.forEach(Project => {
                    // 使用活动对象的属性来构建 HTML 字符串
					let judgeStatus = Project.is_start === true ? "已发布" : "未发布";
                    projectRows += `
                    <tr>
                        <td>${Project.title}</td>
						<td><img src="${Project.image_url}" alt="${Project.title}" style="width: 50px; height: 50px;"></td>
                        <td>${Project.start_time}</td>
                        <td>${Project.end_time}</td>
                        <td>${Project.situation_province}</td>
                        <td>${Project.situation_city}</td>
                        <td>${Project.require_num}</td>
                        <td>${Project.value}</td>
						<td>${judgeStatus}</td>
                        <td>
                            <button class="edit-button">修改</button>
                            <button class="publish-button">发布</button>
							<button class="delete-button">删除</button>
							<button class="infor-button">活动人员信息</button>
                        </td>
                    </tr>`;
                });
                $('#activity-table tbody').html(projectRows);

                // 添加修改和发布按钮的事件监听器
                $('.edit-button').click(function() {
                    // 获取当前行的数据
                    let row = $(this).closest('tr');
                    let projectTitle = row.find('td').eq(0).text();
					let st = row.find('td').eq(2).text();
					let et = row.find('td').eq(3).text();
					let sp = row.find('td').eq(4).text();
					let sc = row.find('td').eq(5).text();
					let rn = row.find('td').eq(6).text();
					let vl = row.find('td').eq(7).text();
					console.log(projectTitle);
                    // 跳转到修改页面，传递活动ID
                    window.location.href = `edit_activity.html?title=${projectTitle}&start_time=${st}&end_time=${et}&situation_province=${sp}&situation_city=${sc}&require_num=${rn}&value=${vl}`;
                });
				
				
				
				$('.publish-button').click(function() {
				                    // 获取当前行的数据
									let row = $(this).closest('tr');
									let projectTitle = row.find('td').eq(0).text();
				                    // let projectTitle= $(this).data('title');
									console.log(projectTitle);
				                    // 发送 AJAX 请求，将 is_start 设置为 1
				                    $.ajax({
				                        url: `http://192.168.163.167:5000/project/activate?title=${projectTitle}`,
										// &start_time&end_time&situation_province&situation_city&require_num&value
				                        method: 'POST',
				                        success: function(response) {
				                            if (response.state === 1) {
				                                alert('活动发布成功');
				                                location.reload(); // 刷新页面以显示发布状态
				                            } else {
				                                alert('发布活动失败');
				                            }
				                        },
				                        error: function(xhr, status, error) {
				                            console.error('Error publishing activity:', error);
				                            alert('发布活动失败');
				                        }
				                    });
				                });
								
				$('.delete-button').click(function() {
				                    // 获取当前行的数据
									let row = $(this).closest('tr');
									let projectTitle = row.find('td').eq(0).text();
				                    // let projectTitle= $(this).data('title');
									console.log(projectTitle);
				                    // 发送 AJAX 请求，将 is_start 设置为 1
				                    $.ajax({
				                        url: `http://192.168.163.167:5000/project/delete?title=${projectTitle}`,
										// &start_time&end_time&situation_province&situation_city&require_num&value
				                        method: 'POST',
				                        success: function(response) {
				                            if (response.state === 1) {
				                                alert('活动删除成功');
				                                location.reload(); // 刷新页面以显示发布状态
				                            } else {
				                                alert('活动删除失败');
				                            }
				                        },
				                        error: function(xhr, status, error) {
				                            console.error('Error publishing activity:', error);
				                            alert('删除活动失败');
				                        }
				                    });
				                });
				$('.infor-button').click(function() {
				    // 获取当前行的数据
				    let row = $(this).closest('tr');
				    let projectTitle = row.find('td').eq(0).text();
					let st = row.find('td').eq(1).text();
					let et = row.find('td').eq(2).text();
					let sp = row.find('td').eq(3).text();
					let sc = row.find('td').eq(4).text();
					let rn = row.find('td').eq(5).text();
					let vl = row.find('td').eq(6).text();
					console.log(projectTitle);
				    // 跳转到修改页面，传递活动ID
				    window.location.href = `applicants.html?title=${projectTitle}`;
				});
				
			}	               
        }
    });

});
