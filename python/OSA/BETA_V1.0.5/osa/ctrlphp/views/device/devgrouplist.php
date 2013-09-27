	<?php include 'views/header.php';?>
		  <!--content开始-->
		  <link href="css/ui-lightness/jquery-ui-1.8.20.custom.css" rel="stylesheet" type="text/css"/>
		  <script src="script/jquery-ui-1.8.20.custom.min.js"></script>
		  <script type="text/javascript" >
		  	var picker = "<?php echo isset($picker)?$picker:''?>";
		  	$(document).ready(function(){
		  		if(picker !=''){
					$("#"+picker).addClass('optfor');
				}
			});
		  </script>
		  <div class="content">
		      <!--左边开始-->
			  	<?php include 'views/device/left.php';?>
			  <!--左边结束-->
			  <!--右边开始-->
			  <div class="main_right">
			      <div class="linkmlist">
				      <div class="home_icom">
					      <span>当前位置：</span>
						  <span><a href="#">设备管理</a></span>
						  <span class="font1">-分组信息</span>
					  </div>
					  <div class="setup">
					      <span class="setup_icon"><a href="index.php?c=device&a=groupadd">创建新分组</a></span>
					  </div>
				  </div>
				  <div class="statistics">
				      <div class="time_left"><?php echo $starttime;?>至<?php echo $endtime;?></div>
					  <div class="time_right">
					      <span><a href="<?php echo $url;?>&date=today" id="today" class="" >今日</a></span>   
					      <span><a href="<?php echo $url;?>&date=yesterday" id="yesterday" class="" >昨日</a></span>   
					      <span><a href="<?php echo $url;?>&date=lastweek" id="lastweek" class="" >最近7天</a></span>   
					      <span><a href="<?php echo $url;?>&date=last2week" id="last2week" class="">最近15天</a></span>   
					      <span><a href="#" id="showsearch">自定义搜索</a></span>   
					  </div>
				  </div>
				  <div class="clear"></div>
				  <div class="timepop" id="timepop" style="display:none;">
				      <div class="time_pro">
					      <p><img src="../images/icon2.gif" />注：请在以下日历中分别点选开始日期和结束日期，关键词可搜索分组名称。</p>
					  </div>
					  <div class="timecontent">
					      <p>
						      <div class="date1"><a href="#">&lt;&lt;上个月</a></div>
							  <div class="date2"><a href="#">今天</a></div>
							  <div class="date3"><a href="#">下个月&gt;&gt;</a></div>
						  </p>
						  <div id="datepicker"></div>
					  </div>
					  <div class="timeFrame">
					  	  <form method="post" action="<?php echo $url;?>">
					      <p><label class="label7">关键词：</label><input type="text" class="style15" name="keyword" value="<?php echo $_SESSION['grpsearch'];?>"/></p>      
					      <p class="style16"><label class="label7">时间范围：</label><input type="text" class="style15" id="date1" name="starttime" value="<?php echo $starttime;?>"/>-<input type="text" name="endtime" class="style15" id="date2" value="<?php echo $endtime;?>"/></p>
						  <p class="center"><input type="submit" value="查询" class="button3" />&nbsp;或&nbsp;&nbsp;<a href="#" id="cancelsearch">取消</a></p>
						  <p class="center"><a href="<?php echo $url.'&clean=1';?>" class="timea"><b>[清除查询条件]</b></a></p>
						  </form>
					  </div>
				  </div>
				  <div class="table_setup">
				      <table cellspacing="0" cellpadding="" width="100%">
					    <tr>
						    <th width="5%">选择</th>
							<th width="20%">分组名称</th>
							<th width="50%">分组描述</th>
							<th width="25%">操作</th>
						</tr>
						<?php foreach ($grpinfo as $key) {?>
							<tr>
							    <td><input type="checkbox" value="<?php echo $key['id'];?>"  class="checkbox"/></td>
								<td><?php echo $key['oGroupName'];?></td>
								<td><?php echo osa_show_info($key['oDescription']);?></td>
								<td>
									<a href="index.php?c=device&a=groupedit&id=<?php echo $key['id'];?>">编辑</a>
									<a href="#" ip="<?php echo $key['oServerList'];?>" class="looks">查看该组设备</a>
								</td>
							</tr> 
						<?php }?>						
						<tr>
						   <td class="td_chect" colspan="7">
							   <span class="checkall"><input type="checkbox" class="style11" id="checkall" />全选</span>
							   <span class="del"><input type="button" value="删除" class="delete" id="group_del" /></span>
						   </td>  
						</tr>
						<tr>
						    <td class="style2" colspan="7">
						    	<?php echo $page;?>
							</td>
						</tr>
					  </table>
				  </div>
			  </div>
			  <!--右边结束-->
		  </div><!--content结束-->
		  <div id="shadow"></div>
		  	<div class="window " id="lookIp" style="display:none;">
			    <div class="window_title">
				    <span class="window_text">查看数据库ip</span>
					<input type="button" class="windbutton" />
				</div>
				<div class="window_con" id="content_ip">
					 
				</div>
			</div>
		  <script type="text/javascript" src="script/common/comlayer.js"></script>
		  <script type="text/javascript" src="script/common/comlist.js"></script>
		  <script type="text/javascript" src="script/device/grouplist.js"></script>
<?php include 'views/footer.php';?>
