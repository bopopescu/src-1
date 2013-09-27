	<?php include 'views/header.php';?>
		  <!--content开始-->
		  <script src="script/highcharts.js" type="text/javascript"> </script>
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
			  <?php include 'views/operate/left.php';?>
			  <!--左边结束-->
			  <!--右边开始-->
			  <div class="main_right">
			      <div class="linkmlist">
				      <div class="home_icom">
					      <span>当前位置：</span>
						  <span><a href="#">运营分析</a></span>
						  <span class="font1">-图形详细分析</span>
					  </div>
				  </div>
				  <div class="statistics">
				  	
				      <div class="time_left">
				      	<form method="post" action="<?php echo $url;?>" >
					      <label class="label5" style="width:240px;"><?php echo $starttime;?>至<?php echo $endtime;?></label>
					      <label class="label5">根据IP查看：</label>
					      <select class="select1" style="width:130px;height:23px;" name="serverid" onchange="submit()">
					      	   <?php foreach ($ipinfo as $key) {?>
					      	   		<option value="<?php echo $key['id'];?>" <?php echo $ipid == $key['id']?"selected='selected'":"";?> ><?php echo $key['oIp'];?></option>
					      	   <?php }?>
					      </select>
					      </form>
				      </div>
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
					      <p><img src="../images/icon2.gif" />注：请在以下日历中分别点选开始日期和结束日期。</p>
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
<!--					      <p><label class="label7">关键词：</label><input type="text" class="style15" name="keyword" value="<?php echo $_SESSION['devsearch'];?>"/></p>      -->
					      <p class="style16"><label class="label7">时间范围：</label><input type="text" class="style15" id="date1" name="starttime" value="<?php echo $starttime;?>"/>-<input type="text" name="endtime" class="style15" id="date2" value="<?php echo $endtime;?>"/></p>
						  <p class="center"><input type="submit" value="查询" class="button3" />&nbsp;或&nbsp;&nbsp;<a href="#" id="cancelsearch">取消</a></p>
						  <p class="center"><a href="<?php echo $url.'&clean=1';?>" class="timea"><b>[清除查询条件]</b></a></p>
						  </form>
					  </div>
				  </div>
				  <div class="LogMinerimg" style="margin:20px 0px 20px 40px;">
		
				  	    <?php echo isset($errormsg)?$errormsg:"<table>".$graph."</table>";?>
				  </div>
			  </div>
			  <!--右边结束-->
		  </div><!--content结束-->
		  <script type="text/javascript" src="script/common/comlist.js"></script>
<?php include 'views/footer.php';?>
