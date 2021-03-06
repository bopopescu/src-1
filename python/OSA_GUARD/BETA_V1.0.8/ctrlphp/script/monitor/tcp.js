$(document).ready(function(){
	
	
	//获取系统恢复值
	function getRemind(){
		if($(".remind").is(":checked")){
			return 1;
		}
		return 0;
	}
	
	//获取通知对象的值
	function getNotiObject(){
		var type = $(".notitype:checked").attr('value');
		if(type == '0'){
			return 'ALL';
		}else if(type == '1'){
			var users = $.trim($("#users").val());//可能为空值
			return users;
		}
	}
	
	
	//通知类型
	$(".notitype").bind('change',function(){
		var type = $(".notitype:checked").attr('value');
		if(type == '0'){
			$("#seleuser").hide();
		}else if(type == '1'){
			$("#seleuser").show();
		}
	});
	
	
	//判断输入是否为所需的端口串
	function isPortstr(portStr){
		if(/^[0-9]*[1-9][0-9]*(\,[0-9]*[1-9][0-9]*)?$/.test(portStr)){
			return true;
		}
		return false;
	}
	/*************************** ping 验证 *************************/
	$.ajaxSetup({
		  async: false
	}); 
	//proname urlname  prokey
	var flag = true;
	//项目名称验证
	$("#itemname").click(function(){
		$(this).parent().find(".tips").css({'color':'rgb(23,124,226)'}).html('');
	});
	$("#itemname").blur(function(){		
		var itemname = $.trim($(this).val());
		if(itemname == ''){
			$(this).parent().find(".tips").css({'color':'rgb(263,24,13)'}).html('请输入监控项目名称');
			flag = false;
			//return;
		}else if(itemname!=itemname.match(/^[a-zA-Z0-9\u4e00-\u9fa5][a-zA-Z0-9\u4e00-\u9fa5\.\_\@]+$/)){
			$(this).parent().find(".tips").css({'color':'rgb(263,24,13)'}).html('请输入正确格式的项目名称');
			flag = false;
		}else{
			$(this).parent().find(".tips").css({'color':'rgb(23,124,226)'}).html('');
		}
		
	});
	
	$("#tcp_port").click(function(){
		$(this).parent().find(".tips").css({'color':'rgb(23,124,226)'}).html('');	
	});
	
	$("#tcp_port").blur(function(){
		var port = $(this).val();
		if(port == ''){
			$(this).parent().find(".tips").css({'color':'rgb(263,24,13)'}).html('请输入端口号');		
			flag = false;
		}else if(!isPortstr(port)){		
			$(this).parent().find(".tips").css({'color':'rgb(263,24,13)'}).html('请输入规范的端口号');	
			flag = false;
		}else{
			$(this).parent().find(".tips").css({'color':'rgb(23,124,226)'}).html('');
		}
	});

	$("#tcp-save").click(function(){
		
		flag = true ;
		$("#itemname").blur();
		$("#tcp_port").blur();
		if(flag == false){
			tipsAlert('基本信息有错误');
			return false;
		}
		var itemip = $.trim($("#itemip").val());
		if(itemip == ''){
			tipsAlert('域名或IP不能为空');
			return false;		
		}
		var notiusers = getNotiObject();
		if(notiusers == ''){
			tipsAlert('指定用户不能为空');
			return false;
		}
		var port = $.trim($("#tcp_port").val());
		var checkrate = $(".checkrate:checked").attr('value');
		var alarmnum = $(".alarmnum:checked").attr('value');
		var itemname = $.trim($("#itemname").val());
		var repeatnum = $(".repeatnum:checked").attr('value');
		var remind = getRemind();
		
		var url = "index.php?c=monitor&a=tcp_monitor";
		$.post(url,{
			'itemname':itemname,
			'itemip':itemip,
			'port':port,
			'notiusers':notiusers,
			'checkrate':checkrate,
			'alarmnum':alarmnum,
			'repeatnum':repeatnum,
			'remind':remind
		},function(msg){
			if(msg.indexOf('success')!=-1){
				var callback = function(result){
					if(result == true){					
						window.location = "index.php?c=monitor&a=monitorlist";
					}
				};
				tipsAlert('监控项目创建成功,点击确定进入监控项目列表',callback);
			}else{
				tipsAlert('监控项目创建失败');
			}
		});
	});
	
	$("#tcp-edit").click(function(){
		
		flag = true ;
		$("#itemname").blur();
		$("#tcp_port").blur();
		if(flag == false){
			tipsAlert('基本信息有错误');
			return false;
		}
		var itemip = $.trim($("#itemip").val());
		if(itemip == ''){
			tipsAlert('域名或IP不能为空');
			return false;		
		}
		var notiusers = getNotiObject();
		if(notiusers == ''){
			tipsAlert('指定用户不能为空');
			return false;
		}
		var port = $.trim($("#tcp_port").val());
		var checkrate = $(".checkrate:checked").attr('value');
		var alarmnum = $(".alarmnum:checked").attr('value');
		var itemname = $.trim($("#itemname").val());
		var repeatnum = $(".repeatnum:checked").attr('value');
		var remind = getRemind();
		var itemid = $.trim($("#edit-itemid").val());
		var url = "index.php?c=monitor&a=monitor_tcp_edit";
		$.post(url,{
			'itemid':itemid,
			'itemname':itemname,
			'itemip':itemip,
			'port':port,
			'notiusers':notiusers,
			'checkrate':checkrate,
			'alarmnum':alarmnum,
			'repeatnum':repeatnum,
			'remind':remind
		},function(msg){
			if(msg.indexOf('success')!=-1){
				var callback = function(result){
					if(result == true){					
						window.location = "index.php?c=monitor&a=monitorlist";
					}
				};
				tipsAlert('监控项目编辑成功,点击确定进入监控项目列表',callback);
			}else{
				tipsAlert('监控项目编辑失败');
			}
		});
	});
	
	/**************************** osa box event *****************************/
	$("#server-search").click(function(){
		var ipStr = $.trim($("#itemip").val());
		boxShowIp(ipStr);
	});
	
	var boxShowDel = function(oldvalue,value){
		
		if(oldvalue == ''){
			return value ;
		}
		var arr = oldvalue.split(',');
		for(i in arr){
			if(value == arr[i]){
				delete arr[i];
			}		
		}
		var newvalue ='';
		for(n in arr){
			newvalue +=arr[n]+',';
		}
		newvalue = newvalue.replace(',,',',');
		return newvalue.replace(/(^\,*)|(\,*$)/g, "");
	};
	
	$(".server_close").live("click",function(){	
		var value = $(this).parent().find(".li_server").html();
		var oldvalue = $("#itemip").val();
		newvalue = boxShowDel(oldvalue,value);
		$("#itemip").attr('value',newvalue);
		$(this).parent().remove();
	});
	
	
	$("#user-select").click(function(){
		var userStr = $.trim($("#users").val());
		boxShowUser(userStr);	
	});
	
	$(".user_close").live("click",function(){	
		var value = $(this).parent().find(".li_users").html();
		var oldvalue = $("#users").val();
		newvalue = boxShowDel(oldvalue,value);
		$("#users").attr('value',newvalue);
		$(this).parent().remove();
	});
});