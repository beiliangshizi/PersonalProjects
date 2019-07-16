# #coding:utf-8
#
# from lxml import etree
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# htmldoc = '''
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml">
# <head>
# <title>【苏州计算机软件招聘_最新苏州计算机软件招聘信息】-前程无忧</title>
# <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
# <meta name="description" content="前程无忧为您提供最新最全的苏州计算机软件招聘、求职信息，找工作、找人才就上苏州前程无忧招聘专区！掌握前程，职场无忧！">
# <meta name="keywords" content="苏州计算机软件,苏州计算机软件招聘,最新苏州计算机软件招聘信息">
# <meta name="robots" content="all">
# <meta http-equiv="Expires" content="0">
# <meta http-equiv="Cache-Control" content="no-cache">
# <meta http-equiv="Pragma" content="no-cache">
# <link href="http://js.51jobcdn.com/in/css/style.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/search.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/my.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/jobs/base.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/jobs/reset.css?20170328" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/jobs/tForm.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/jobs/tSearch-layout.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/graycss0.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/2017/public/base.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/2017/public/form.css?20170420" rel="stylesheet" type="text/css" />
# <link href="http://js.51jobcdn.com/in/css/2017/public/panel-pop.css?20170420" rel="stylesheet" type="text/css" />
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/jquery.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2009/login.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2009/Base.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2009/Base.ZzLayer.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2009/Base.ZzLayer.ExtZzLayer.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2009/JsBase.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2009/search/Base.Search_Transition.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/layer.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/common_layer.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/common_select.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/layer_main_map.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/layer_main.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/layer_main_navigation.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/layer/layer_c.js?20170420"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/delivery/delivery.js?20161121"></script>
# <script language="javascript" src="http://js.51jobcdn.com/in/js/2016/my/my_collection.js?20170420"></script>
# </head>
# <body>
# <div class="header">
#     <!-- bar start -->
#     <div class="bar">
#         <div class="in">
#             <div class="language">
#                 <ul id="languagelist">
#                     <li class="tle"><span class="list">简</span><em class="icon_arrow"></em></li>
#                     <li><a href="http://big5.51job.com/gate/big5/www.51job.com/">繁</a></li>
# 					<li class="last"><a href="http://www.51job.com//default-e.php">EN</a></li>
#                     <script language="javascript">
#                         if(location.hostname == "big5.51job.com")
#                         {
#                             $('#languagelist li span').html("繁");
#                             $('#languagelist li:nth-child(2) a').html("简");
#                             $('#languagelist li:nth-child(2) a').attr('href','javascript:void(0)');
#                             $('#languagelist li:nth-child(2) a').click(function(){location.href="ht" + "tp://www.51job.com"});
#                             $('#languagelist li:nth-child(3) a').attr('href','javascript:void(0)');
#                             $('#languagelist li:nth-child(3) a').click(function(){location.href="ht" + "tp://www.51job.com/default-e.php"});
#                         }
#                     </script>
#                 </ul>
#             </div>
#             <span class="l">|</span>
#             <div class="app">
#                 <ul>
#                     <li><em class="e_icon"></em><a href="http://www.51job.com/pm/app/index.html">APP下载</a><em class="icon_arrow"></em></li>
#                     <li>
#                         <img width="80" height="80" src="http://img01.51jobcdn.com/im/2016/code/app_download.png" alt="app download">
#                         <p><a href="http://www.51job.com/pm/app/index.html">APP下载</a></p>
#                     </li>
#                 </ul>
#             </div>
#
#             <p class="rlk">
#                 <a href="http://jobs.51job.com/">招聘信息</a>
#                 <span class="l">|</span>
#                 <a href="http://ehire.51job.com/">企业服务</a>
#             </p>
#             <div class="uer">
#                 <p class="op">
#                                             <a href="https://login.51job.com/login.php?url=http%3A%2F%2Fjobs.51job.com%2Fsuzhou%2Fjisuanjiruanjian%2Fp1%2F">登录</a> / <a href="https://login.51job.com/register.php?url=http%3A%2F%2Fjobs.51job.com%2Fsuzhou%2Fjisuanjiruanjian%2Fp1%2F">注册</a>
#                                     </p>
#                 <span class="l">|</span>
#                 <ul>
#                     <li class="tle"><span><a href="http://i.51job.com/userset/my_51job.php">我的51Job</a><em class="icon_arrow"></em></span></li>
#                     <li class="e1 e_icon"><a href="http://i.51job.com/resume/resume_center.php">简历中心</a></li>
#                     <li class="e2 e_icon"><a href="http://i.51job.com/userset/resume_browsed.php">谁看过我</a></li>
#                     <li class="e3 e_icon"><a href="http://i.51job.com/userset/my_collection.php">我的收藏</a></li>
#                     <li class="e4 e_icon last2"><a href="http://i.51job.com/userset/my_apply.php">我的申请</a></li>
#                                     </ul>
#             </div>
#         </div>
#     </div>
#     <!-- top end -->
#     <!-- nag start -->
# 	<div class="pop-city" style="display:none;position: absolute; z-index: 1000;" id="area_channel_layer">
#     <div class="tle">
#         地区选择
#         <em class="close" onclick="jvascript:$('#area_channel_layer,#area_channel_layer_backdrop').hide();"></em>
#     </div>
#     <div class="pcon">
#         <div class="ht">
#             <label>热门城市</label>
#                 <a href="http://www.51job.com/beijing">北京</a>
#                 <a href="http://www.51job.com/shanghai">上海</a>
#                 <a href="http://www.51job.com/guangzhou">广州</a>
#                 <a href="http://www.51job.com/shenzhen">深圳</a>
#                 <a href="http://www.51job.com/wuhan">武汉</a>
#                 <a href="http://www.51job.com/xian">西安</a>
#                 <a href="http://www.51job.com/hangzhou">杭州</a>
#                 <a href="http://www.51job.com/nanjing">南京</a>
#                 <a href="http://www.51job.com/chengdu">成都</a>
#                 <a href="http://www.51job.com/chongqing">重庆</a>
#         </div>
#         <div class="cbox">
#             <ul  id="area_channel_layer_list">
#                 <li class="on" onclick="areaChannelChangeTab('abc', this)">A B C</li>
#                 <li onclick="areaChannelChangeTab('def', this)">D E F</li>
#                 <li onclick="areaChannelChangeTab('ghj', this)">G H J</li>
#                 <li onclick="areaChannelChangeTab('klm', this)">K L M</li>
#                 <li onclick="areaChannelChangeTab('nqs', this)">N Q S</li>
#                 <li onclick="areaChannelChangeTab('twx', this)">T W X</li>
#                 <li onclick="areaChannelChangeTab('yz', this)">Y Z</li>
#             </ul>
#             <div class="clst"  id="area_channel_layer_all">
#             	<div class="e" name="area_channel_div_abc">
#                     <span><a href="http://www.51job.com/anshan">鞍山</a></span>
#                     <span><a href="http://www.51job.com/beijing">北京</a></span>
#                     <span><a href="http://www.51job.com/baotou">包头</a></span>
#                     <span><a href="http://www.51job.com/baoding">保定</a></span>
#                     <span><a href="http://www.51job.com/changchun">长春</a></span>
#                     <span><a href="http://www.51job.com/changsha">长沙</a></span>
#                     <span><a href="http://www.51job.com/chengdu">成都</a></span>
#                     <span><a href="http://www.51job.com/chongqing">重庆</a></span>
#                     <span><a href="http://www.51job.com/changzhou">常州</a></span>
#                     <span><a href="http://www.51job.com/changde">常德</a></span>
#                     <span><a href="http://www.51job.com/changshu">常熟</a></span>
#                 </div>
#                 <div class="e" name="area_channel_div_def" style="display:none">
#                     <span><a href="http://www.51job.com/dalian">大连</a></span>
#                     <span><a href="http://www.51job.com/dongguan">东莞</a></span>
#                     <span><a href="http://www.51job.com/dandong">丹东</a></span>
#                     <span><a href="http://www.51job.com/daqing">大庆</a></span>
#                     <span><a href="http://www.51job.com/eerduosi">鄂尔多斯</a></span>
#                     <span><a href="http://www.51job.com/fuzhou">福州</a></span>
#                     <span><a href="http://www.51job.com/foshan">佛山</a></span>
#                     <span><a href="http://www.51job.com/fushun">抚顺</a></span>
#                 </div>
#                 <div class="e" name="area_channel_div_ghj" style="display:none">
#                     <span><a href="http://www.51job.com/guangzhou">广州</a></span>
#                     <span><a href="http://www.51job.com/guiyang">贵阳</a></span>
#                     <span><a href="http://www.51job.com/ganzhou">赣州</a></span>
#                     <span><a href="http://www.51job.com/harbin">哈尔滨</a></span>
#                     <span><a href="http://www.51job.com/hangzhou">杭州</a></span>
#                     <span><a href="http://www.51job.com/hefei">合肥</a></span>
#                     <span><a href="http://www.51job.com/haikou">海口</a></span>
#                     <span><a href="http://www.51job.com/huhhot">呼和浩特</a></span>
#                     <span><a href="http://www.51job.com/huizhou">惠州</a></span>
#                     <span><a href="http://www.51job.com/hengyang">衡阳</a></span>
#                     <span><a href="http://www.51job.com/huaian">淮安</a></span>
#                     <span><a href="http://www.51job.com/huzhou">湖州</a></span>
#                     <span><a href="http://www.51job.com/handan">邯郸</a></span>
#                     <span><a href="http://www.51job.com/jinan">济南</a></span>
#                     <span><a href="http://www.51job.com/jiaxing">嘉兴</a></span>
#                     <span><a href="http://www.51job.com/jinhua">金华</a></span>
#                     <span><a href="http://www.51job.com/jilin">吉林</a></span>
#                     <span><a href="http://www.51job.com/jiangmen">江门</a></span>
#                     <span><a href="http://www.51job.com/jingzhou">荆州</a></span>
#                     <span><a href="http://www.51job.com/jiangyin">江阴</a></span>
#                     <span><a href="http://www.51job.com/jining">济宁</a></span>
#                     <span><a href="http://www.51job.com/jiujiang">九江</a></span>
#                 </div>
#                 <div class="e" name="area_channel_div_klm" style="display:none">
#                     <span><a href="http://www.51job.com/kunming">昆明</a></span>
#                     <span><a href="http://www.51job.com/kunshan">昆山</a></span>
#                     <span><a href="http://www.51job.com/lanzhou">兰州</a></span>
#                     <span><a href="http://www.51job.com/langfang">廊坊</a></span>
#                     <span><a href="http://www.51job.com/linyi">临沂</a></span>
#                     <span><a href="http://www.51job.com/luoyang">洛阳</a></span>
#                     <span><a href="http://www.51job.com/lianyungang">连云港</a></span>
#                     <span><a href="http://www.51job.com/liuzhou">柳州</a></span>
#                     <span><a href="http://www.51job.com/mianyang">绵阳</a></span>
#                 </div>
#                 <div class="e" name="area_channel_div_nqs" style="display:none">
#                     <span><a href="http://www.51job.com/nanjing">南京</a></span>
#                     <span><a href="http://www.51job.com/ningbo">宁波</a></span>
#                     <span><a href="http://www.51job.com/nanchang">南昌</a></span>
#                     <span><a href="http://www.51job.com/nantong">南通</a></span>
#                     <span><a href="http://www.51job.com/nanning">南宁</a></span>
#                     <span><a href="http://www.51job.com/qingdao">青岛</a></span>
#                     <span><a href="http://www.51job.com/quanzhou">泉州</a></span>
#                     <span><a href="http://www.51job.com/qinhuangdao">秦皇岛</a></span>
#                     <span><a href="http://www.51job.com/qingyuan">清远</a></span>
#                     <span><a href="http://www.51job.com/shanghai">上海</a></span>
#                     <span><a href="http://www.51job.com/shenzhen">深圳</a></span>
#                     <span><a href="http://www.51job.com/shenyang">沈阳</a></span>
#                     <span><a href="http://www.51job.com/shijiazhuang">石家庄</a></span>
#                     <span><a href="http://www.51job.com/suzhou">苏州</a></span>
#                     <span><a href="http://www.51job.com/sanya">三亚</a></span>
#                     <span><a href="http://www.51job.com/shaoxing">绍兴</a></span>
#                     <span><a href="http://www.51job.com/shantou">汕头</a></span>
#                     <span><a href="http://www.51job.com/shunde">顺德</a></span>
#                 </div>
#                 <div class="e" name="area_channel_div_twx" style="display:none">
#                     <span><a href="http://www.51job.com/tianjin">天津</a></span>
#                     <span><a href="http://www.51job.com/taiyuan">太原</a></span>
#                     <span><a href="http://www.51job.com/tz">台州</a></span>
#                     <span><a href="http://www.51job.com/tangshan">唐山</a></span>
#                     <span><a href="http://www.51job.com/taizhou">泰州</a></span>
#                     <span><a href="http://www.51job.com/tieling">铁岭</a></span>
#                     <span><a href="http://www.51job.com/wuhan">武汉</a></span>
#                     <span><a href="http://www.51job.com/wuxi">无锡</a></span>
#                     <span><a href="http://www.51job.com/wenzhou">温州</a></span>
#                     <span><a href="http://www.51job.com/urumqi">乌鲁木齐</a></span>
#                     <span><a href="http://www.51job.com/wuhu">芜湖</a></span>
#                     <span><a href="http://www.51job.com/weifang">潍坊</a></span>
#                     <span><a href="http://www.51job.com/weihai">威海</a></span>
#                     <span><a href="http://www.51job.com/xian">西安</a></span>
#                     <span><a href="http://www.51job.com/xiamen">厦门</a></span>
#                     <span><a href="http://www.51job.com/xuzhou">徐州</a></span>
#                     <span><a href="http://www.51job.com/xiangyang">襄阳</a></span>
#                     <span><a href="http://www.51job.com/xiangtan">湘潭</a></span>
#                     <span><a href="http://www.51job.com/xianyang">咸阳</a></span>
#                 </div>
#                 <div class="e" name="area_channel_div_yz" style="display:none">
#                     <span><a href="http://www.51job.com/yantai">烟台</a></span>
#                     <span><a href="http://www.51job.com/yangzhou">扬州</a></span>
#                     <span><a href="http://www.51job.com/yichang">宜昌</a></span>
#                     <span><a href="http://www.51job.com/yancheng">盐城</a></span>
#                     <span><a href="http://www.51job.com/yiwu">义乌</a></span>
#                     <span><a href="http://www.51job.com/yingkou">营口</a></span>
#                     <span><a href="http://www.51job.com/yinchuan">银川</a></span>
#                     <span><a href="http://www.51job.com/zhangzhou">漳州</a></span>
#                     <span><a href="http://www.51job.com/zhengzhou">郑州</a></span>
#                     <span><a href="http://www.51job.com/zhongshan">中山</a></span>
#                     <span><a href="http://www.51job.com/zhuhai">珠海</a></span>
#                     <span><a href="http://www.51job.com/zhenjiang">镇江</a></span>
#                     <span><a href="http://www.51job.com/zhuzhou">株洲</a></span>
#                     <span><a href="http://www.51job.com/zhanjiang">湛江</a></span>
#                     <span><a href="http://www.51job.com/zhaoqing">肇庆</a></span>
#                     <span><a href="http://www.51job.com/zhangjiagang">张家港</a></span>
#                     <span><a href="http://www.51job.com/zibo">淄博</a></span>
#                 </div>
#             </div>
#             <div class="clear"></div>
#         </div>
#     </div>
# </div>
#
# <div id="area_channel_layer_backdrop" class="layer_back_drop_class" style="z-index:999;position:absolute;z-index:999;left:0;top:0;display:none"></div>
#
# <script>
#     function areaChannelChangeTab(sName, oEvent)
#     {
#         $("#area_channel_layer_all").children().hide();
#         $("#area_channel_layer_list").children().removeClass("on");
#         $(oEvent).addClass("on");
#         $("#area_channel_layer_all").children("div[name='area_channel_div_" + sName + "']").show();
#         $("#area_channel_layer_backdrop").show();
#     }
#
#     function openAreaChannelLayer()
#     {
#         setLayerPosition();
#         $("#area_channel_layer,#area_channel_layer_backdrop").show();
#     }
#
#     function setLayerPosition()
#     {
#         var dl = $(document).scrollLeft();
#         var dt = $(document).scrollTop();
#         var ww = $(document).width();
#         var dwh = $(document).height();
#         var wwh = $(window).height();
#         var ow = $("#area_channel_layer").width();
#         var oh = $("#area_channel_layer").height();
#         var fLeft = (ww - ow) / 2 + dl;
#         var fTop = (wwh - oh) * 382 / 1000 + dt;//黄金比例
#         $("#area_channel_layer").css({'left': Math.max(parseInt(fLeft), dl), 'top': Math.max(parseInt(fTop), dt)});
#         $("#area_channel_layer_backdrop").css({'width': ww + 'px', 'height': dwh + 'px'});
#     }
#
#     $(window).resize(function(){
#         if(!$("#area_channel_layer").is(":hidden"))
#         {
#             setLayerPosition();
#         }
#     });
# </script>
#     <div class="nag">
#         <div class="in">
#             <a href="http://www.51job.com/"><img class="logo" width="90" height="40" src="http://img01.51jobcdn.com/im/2016/logo/logo_90x40.png" alt="前程无忧"></a>
# 			<!--LOGO-->
# 							<img class="slogen" width="162" height="17" src="http://img05.51jobcdn.com/im/2016/header/slogen.png">
# 								       	<a  class="ctlink" target="_blank" href="http://www.51job.com/suzhou/" class="lareaurl">苏州招聘频道</a>
# 							<p class="nlink">
#                 <a class="" href="http://www.51job.com/">首页</a>
#                 <a class="" href="http://search.51job.com/jobsearch/search_result.php">职位搜索</a>
#                 <a class="" href="javascript:openAreaChannelLayer()">地区频道</a>
#                 <a class="" href="http://www.51job.com/default_res.php">职场资讯</a>
#                 <a class="" href="http://xy.51job.com/default-xs.php">校园招聘</a>
#                 <a href="http://my.51job.com/my/gojingying.php?direct=http%3A%2F%2Fwww.51jingying.com%2Fcommon%2Fsearchcase.php%3F5CC4CE%3D1008" target="_blank">无忧精英</a>
#             </p>
#         </div>
#     </div>
#     <!-- nag end -->
# </div>	<div class="bdnav">
# 		您所在的位置：<a href="http://jobs.51job.com/">最新招聘信息</a><span>&gt;</span><a href="http://jobs.51job.com/all/">全国职位信息</a><span>
# 						&gt;</span><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/">苏州招聘网</a><span>
#
#
# 			&gt;</span><a href="javascript:;">苏州计算机软件招聘信息</a>
# 					</div>
#
# 	<div class="maincenter">
# 			 		<form name="searchForm" id="searchForm" method="post" action="http://search.51job.com/jobsearch/search_result.php">
# 		<div class="shox">
# 			<input type="hidden" name="stype" value="1">
# 			<input type="hidden" name="lang" value="c">
# 			<input type="hidden"  name="fromType" value="102">
# 			<input name="keywordtype" id="keywordtype" type="hidden" value="2" />
# 			<p class="tp" id="tab-title"><font>|</font><span id="co" valkey="1">公司名</span><font>|</font><span  id="all" class="mk" valkey="2">全文</span><font>|</font></p>
# 			<div class="bx">
# 				<p class="ipt">
# 					<input type="text" id="keyword" name="keyword" class="default" value="请输入关键字"  onfocus="on(this,'请输入关键字')"  onblur="out(this,'请输入关键字')" />
# 				</p>
# 				<div  id="expect_area_trigger">
# 				<span class="chty" id="" >
# 					<input  preval style="cursor: pointer;width:80px;height: 22px;background-color:transparent;border:none;padding-top: 3px;white-space:nowrap;text-overflow:ellipsis;overflow:hidden" type="button"  autocomplete="off" name="btnJobarea"   value="工作地点" id="Jobareachoose"  readonly="readonly"/>
# 					<div id="expect_area_trigger_layer" class="select_layer"></div>
# 					<input name="jobarea" id="jobarea" type="hidden" value="" />
# 				</span>
# 				</div>
# 				<a href="javascript:void(0);" onclick="checkSearchForm();return false;">
# 					<img src="http://img03.51jobcdn.com/im/jobs/find.png" >
# 				</a>
#
# 				<div class="clear"></div>
# 			</div>
# 		</div>
# 		</form>
# 		<script>
# 				$('#tab-title span').click(function(){
# 					$(this).addClass("mk").siblings().removeClass();
# 					$('#keywordtype').val($(this).attr("valkey"));
# 				});
# 				//on
# 				function on(clickon,word)
# 				{
# 					if(clickon.value==word)
# 					{
# 						clickon.value="";
# 						$('#keyword').removeClass("default");
# 					}
# 				}
# 				//out
# 				function out(clickout,word)
# 				{
# 					if(clickout.value==""||clickout.value.replace(/\s/g,"")=="")
# 					{
# 						clickout.value=word;
# 						$('#keyword').addClass("default");
# 					}
# 				}
#
# 			  function checkSearchForm()
# 			  {
# 			  	 var area_code = $("#expect_area_code").val();
# 			  	 var keyword = $("#keyword").val();
# 			  	if(area_code == "" && (keyword  == "" || keyword  == "请输入关键字") ){
# 			  		  alert("请选择城市或输入搜索关键字");
# 			  		}else{
# 			  			$("#searchForm").submit();
# 			  			}
# 			  }
#
# 			$("#Jobareachoose").areaLayer({
#             'id'                        : 'Jobareachoose',
#             'code_id'                   : 'jobarea',
#             'layer_id'                  : 'work_position_layer',
#             'text_id'                   : 'Jobareachoose',
#             'data_multiple'             : true,
#             'special_type'              : '2',
#             'save_type'                 : '1',
#             'data_map'                  : {},
#             'layer_after_close'         : function(){
#                 if($("#Jobareachoose").val() == "")
#                 {
#                     $("#Jobareachoose").val("工作地点");
#                 }
#             }
#
# 			});
# 		</script>
# 		<div class="filter">
# 			<div class="tp">
#
# 				<div class="clear"></div>
# 			</div>
# 			<div class="e">
# 				<p>
# 					<strong>主要城市：</strong>
# 					<a class=""  href="http://jobs.51job.com/jisuanjiruanjian/">不限</a>
# 				</p>
# 				<div class="lkst close">
#
# 					 					<a class="" href="http://jobs.51job.com/jiangsusheng/jisuanjiruanjian/">江苏省</a>
# 										<a class="" href="http://jobs.51job.com/nanjing/jisuanjiruanjian/">南京</a>
# 										<a class="mk" href="http://jobs.51job.com/suzhou/jisuanjiruanjian/">苏州</a>
# 										<a class="" href="http://jobs.51job.com/wuxi/jisuanjiruanjian/">无锡</a>
# 										<a class="" href="http://jobs.51job.com/changzhou/jisuanjiruanjian/">常州</a>
# 										<a class="" href="http://jobs.51job.com/kunshan/jisuanjiruanjian/">昆山</a>
# 										<a class="" href="http://jobs.51job.com/changshu/jisuanjiruanjian/">常熟</a>
# 										<a class="" href="http://jobs.51job.com/yangzhou/jisuanjiruanjian/">扬州</a>
# 										<a class="" href="http://jobs.51job.com/nantong/jisuanjiruanjian/">南通</a>
# 										<a class="" href="http://jobs.51job.com/zhenjiang/jisuanjiruanjian/">镇江</a>
# 										<a class="" href="http://jobs.51job.com/xuzhou/jisuanjiruanjian/">徐州</a>
# 										<a class="" href="http://jobs.51job.com/lianyungang/jisuanjiruanjian/">连云港</a>
# 										<a class="" href="http://jobs.51job.com/yancheng/jisuanjiruanjian/">盐城</a>
# 										<a class="" href="http://jobs.51job.com/zhangjiagang/jisuanjiruanjian/">张家港</a>
# 										<a class="" href="http://jobs.51job.com/taicang/jisuanjiruanjian/">太仓</a>
# 										<a class="" href="http://jobs.51job.com/taizhou/jisuanjiruanjian/">泰州</a>
# 										<a class="" href="http://jobs.51job.com/huaian/jisuanjiruanjian/">淮安</a>
# 										<a class="" href="http://jobs.51job.com/suqian/jisuanjiruanjian/">宿迁</a>
# 										<a class="" href="http://jobs.51job.com/danyang/jisuanjiruanjian/">丹阳</a>
# 										<a class="" href="http://jobs.51job.com/taixing/jisuanjiruanjian/">泰兴</a>
# 										<a class="" href="http://jobs.51job.com/jingjiang/jisuanjiruanjian/">靖江</a>
# 									</div>
# 				<div class="clear"></div>
# 				<i class="sicon Dm down">更多</i>
# 			</div>
# 						<div class="e e3 nb">
# 				<p>
# 					<strong>热门地区：</strong>
# 					<a class="mk"  href="http://jobs.51job.com/suzhou/jisuanjiruanjian/">不限</a>
# 				</p>
# 				<div class="lkst">
# 											<a class=""  href="http://jobs.51job.com/suzhou-gsq/jisuanjiruanjian/">姑苏区</a>
#
# 												<a class=""  href="http://jobs.51job.com/suzhou-hqq/jisuanjiruanjian/">虎丘区</a>
#
# 												<a class=""  href="http://jobs.51job.com/suzhou-wzq/jisuanjiruanjian/">吴中区</a>
#
# 												<a class=""  href="http://jobs.51job.com/suzhou-xcq/jisuanjiruanjian/">相城区</a>
#
# 												<a class=""  href="http://jobs.51job.com/suzhou-wjq/jisuanjiruanjian/">吴江区</a>
#
# 												<a class=""  href="http://jobs.51job.com/suzhou-gyyq/jisuanjiruanjian/">工业园区</a>
#
# 												<a class=""  href="http://jobs.51job.com/suzhou-gxq/jisuanjiruanjian/">高新区</a>
#
# 										</div>
# 				<div class="clear"></div>
# 			</div>
# 					<div class="e">
# 				<p>
# 					<strong>职位分类：</strong>
# 					<a class=""  href="http://jobs.51job.com/suzhou/">不限</a>
# 				</p>
# 				<div class="lkst close">
# 										<a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/" class="mk">计算机软件</a>
# 									</div>
# 				<div class="clear"></div>
# 				<i class="down sicon Dm">更多</i>
# 			</div>
# 						<div class="e e3 nb">
# 				<p>
# 					<strong>&nbsp;</strong>
# 					<a class="mk"  href="http://jobs.51job.com/suzhou/jisuanjiruanjian/">不限</a>
# 				</p>
# 				<div class="lkst">
# 										<a href="http://jobs.51job.com/suzhou/gaojiruanjian/"  class="" >高级软件工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/ruanjian/"  class="" >软件工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/ruanjiansheji/"  class="" >软件UI设计师/工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/suanfagongchengshi/"  class="" >算法工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/fangzhenyingyong/"  class="" >仿真应用工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/erp-shishi/"  class="" >ERP实施顾问</a>
# 										<a href="http://jobs.51job.com/suzhou/erp-jishukaifa/"  class="" >ERP技术开发</a>
# 										<a href="http://jobs.51job.com/suzhou/xuqiugongchengshi/"  class="" >需求工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/xitongjicheng/"  class="" >系统集成工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/xitongfenxi/"  class="" >系统分析员</a>
# 										<a href="http://jobs.51job.com/suzhou/xitong/"  class="" >系统工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/xitongjiagou/"  class="" >系统架构设计师</a>
# 										<a href="http://jobs.51job.com/suzhou/shujukuguanli/"  class="" >数据库工程师/管理员</a>
# 										<a href="http://jobs.51job.com/suzhou/jisuanjifuzhusheji/"  class="" >计算机辅助设计工程师</a>
# 										<a href="http://jobs.51job.com/suzhou/jsjrj-others/"  class="" >其他</a>
#
# 				</div>
# 				<div class="clear"></div>
# 			</div>
# 						<div class="bt b2" style="z-index:2">
# 				<strong>更多：</strong>
# 				<div class="flst">
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>行业分类</span>
# 							<ul class="bx">
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy01/jisuanjiruanjian/">计算机软件</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy37/jisuanjiruanjian/">计算机硬件</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy38/jisuanjiruanjian/">计算机服务(系统、数据服务、维修)</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy31/jisuanjiruanjian/">通信/电信/网络设备</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy39/jisuanjiruanjian/">通信/电信运营、增值服务</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy32/jisuanjiruanjian/">互联网/电子商务</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy40/jisuanjiruanjian/">网络游戏</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy02/jisuanjiruanjian/">电子技术/半导体/集成电路</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy35/jisuanjiruanjian/">仪器仪表/工业自动化</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy41/jisuanjiruanjian/">会计/审计</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy03/jisuanjiruanjian/">金融/投资/证券</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy42/jisuanjiruanjian/">银行</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy43/jisuanjiruanjian/">保险</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy62/jisuanjiruanjian/">信托/担保/拍卖/典当</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy04/jisuanjiruanjian/">贸易/进出口</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy22/jisuanjiruanjian/">批发/零售</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy05/jisuanjiruanjian/">快速消费品(食品、饮料、化妆品)</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy06/jisuanjiruanjian/">服装/纺织/皮革</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy44/jisuanjiruanjian/">家具/家电/玩具/礼品</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy60/jisuanjiruanjian/">奢侈品/收藏品/工艺品/珠宝</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy45/jisuanjiruanjian/">办公用品及设备</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy14/jisuanjiruanjian/">机械/设备/重工</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy33/jisuanjiruanjian/">汽车及零配件</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy08/jisuanjiruanjian/">制药/生物工程</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy46/jisuanjiruanjian/">医疗/护理/卫生</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy47/jisuanjiruanjian/">医疗设备/器械</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy12/jisuanjiruanjian/">广告</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy48/jisuanjiruanjian/">公关/市场推广/会展</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy49/jisuanjiruanjian/">影视/媒体/艺术/文化传播</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy13/jisuanjiruanjian/">文字媒体/出版</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy15/jisuanjiruanjian/">印刷/包装/造纸</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy26/jisuanjiruanjian/">房地产</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy09/jisuanjiruanjian/">建筑/建材/工程</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy50/jisuanjiruanjian/">家居/室内设计/装潢</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy51/jisuanjiruanjian/">物业管理/商业中心</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy34/jisuanjiruanjian/">中介服务</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy63/jisuanjiruanjian/">租赁服务</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy07/jisuanjiruanjian/">专业服务(咨询、人力资源、财会)</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy59/jisuanjiruanjian/">外包服务</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy52/jisuanjiruanjian/">检测，认证</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy18/jisuanjiruanjian/">法律</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy23/jisuanjiruanjian/">教育/培训/院校</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy24/jisuanjiruanjian/">学术/科研</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy11/jisuanjiruanjian/">餐饮业</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy53/jisuanjiruanjian/">酒店/旅游</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy17/jisuanjiruanjian/">娱乐/休闲/体育</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy54/jisuanjiruanjian/">美容/保健</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy27/jisuanjiruanjian/">生活服务</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy21/jisuanjiruanjian/">交通/运输/物流</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy55/jisuanjiruanjian/">航天/航空</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy19/jisuanjiruanjian/">石油/化工/矿产/地质</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy16/jisuanjiruanjian/">采掘业/冶炼</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy36/jisuanjiruanjian/">电气/电力/水利</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy61/jisuanjiruanjian/">新能源</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy56/jisuanjiruanjian/">原材料和加工</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy28/jisuanjiruanjian/">政府/公共事业</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy57/jisuanjiruanjian/">非盈利机构</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy20/jisuanjiruanjian/">环保</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy29/jisuanjiruanjian/">农/林/牧/渔</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/hy58/jisuanjiruanjian/">多元化业务集团公司</a></li>
# 															</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>工作经验</span>
# 							<ul>
# 																							<li><a class="" href="http://jobs.51job.com/suzhou/we01/jisuanjiruanjian/">无经验</a></li>
# 																							<li><a class="" href="http://jobs.51job.com/suzhou/we02/jisuanjiruanjian/">1-3年</a></li>
# 																							<li><a class="" href="http://jobs.51job.com/suzhou/we03/jisuanjiruanjian/">3-5年</a></li>
# 																							<li><a class="" href="http://jobs.51job.com/suzhou/we04/jisuanjiruanjian/">5-10年</a></li>
# 																							<li><a class="" href="http://jobs.51job.com/suzhou/we05/jisuanjiruanjian/">10年以上</a></li>
# 															</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>薪酬福利</span>
# 							<ul class="bx">
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc01/jisuanjiruanjian/">五险一金</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc02/jisuanjiruanjian/">带薪年假</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc03/jisuanjiruanjian/">节日福利</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc04/jisuanjiruanjian/">周末双休</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc05/jisuanjiruanjian/">绩效奖金</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc06/jisuanjiruanjian/">员工旅游</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc07/jisuanjiruanjian/">立即上岗</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc08/jisuanjiruanjian/">专业培训</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc09/jisuanjiruanjian/">全勤奖</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc10/jisuanjiruanjian/">年终双薪</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc11/jisuanjiruanjian/">定期体检</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc12/jisuanjiruanjian/">交通补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc13/jisuanjiruanjian/">通讯补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc14/jisuanjiruanjian/">出差补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc15/jisuanjiruanjian/">包住</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc16/jisuanjiruanjian/">人才推荐奖</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc17/jisuanjiruanjian/">高温补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc18/jisuanjiruanjian/">包吃包住</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc19/jisuanjiruanjian/">弹性工作</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc20/jisuanjiruanjian/">补充医疗保险</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc21/jisuanjiruanjian/">年终分红</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc22/jisuanjiruanjian/">免费班车</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc23/jisuanjiruanjian/">出国机会</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc24/jisuanjiruanjian/">住房补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc25/jisuanjiruanjian/">包吃</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc26/jisuanjiruanjian/">股票期权</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc27/jisuanjiruanjian/">采暖补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc28/jisuanjiruanjian/">做一休一</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc29/jisuanjiruanjian/">加班补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc30/jisuanjiruanjian/">餐饮补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc31/jisuanjiruanjian/">补充公积金</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc32/jisuanjiruanjian/">补充养老保险</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc33/jisuanjiruanjian/">年终奖金</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc34/jisuanjiruanjian/">季度奖金</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc35/jisuanjiruanjian/">团队聚餐</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc36/jisuanjiruanjian/">每年多次调薪</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc37/jisuanjiruanjian/">落户办理</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc38/jisuanjiruanjian/">免息房贷</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc39/jisuanjiruanjian/">全员持股</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc40/jisuanjiruanjian/">子女教育津贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc41/jisuanjiruanjian/">子女保险</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc42/jisuanjiruanjian/">家人免费体检</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc43/jisuanjiruanjian/">家属免费医疗</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc44/jisuanjiruanjian/">外派津贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc45/jisuanjiruanjian/">电脑补助</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc46/jisuanjiruanjian/">油费补贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc47/jisuanjiruanjian/">职位津贴</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc48/jisuanjiruanjian/">配车</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc49/jisuanjiruanjian/">不加班</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc50/jisuanjiruanjian/">科研奖励</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc51/jisuanjiruanjian/">在职研究生培养</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc52/jisuanjiruanjian/">健身俱乐部</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc53/jisuanjiruanjian/">探亲假</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc54/jisuanjiruanjian/">母婴室</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc55/jisuanjiruanjian/">做五休二</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc56/jisuanjiruanjian/">做六休一</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc57/jisuanjiruanjian/">无试用期</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc58/jisuanjiruanjian/">工作服</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/xc59/jisuanjiruanjian/">夫妻房</a></li>
# 															</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>公司规模</span>
# 							<ul>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs01/jisuanjiruanjian/">少于50人</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs02/jisuanjiruanjian/">50-150人</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs03/jisuanjiruanjian/">150-500人</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs04/jisuanjiruanjian/">500-1000人</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs05/jisuanjiruanjian/">1000-5000人</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs06/jisuanjiruanjian/">5000-10000人</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cs07/jisuanjiruanjian/">10000人以上</a></li>
# 															</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>公司性质</span>
# 							<ul>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn01/jisuanjiruanjian/">外资（欧美）</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn02/jisuanjiruanjian/">外资（非欧美）</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn03/jisuanjiruanjian/">合资</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn04/jisuanjiruanjian/">国企</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn05/jisuanjiruanjian/">民营公司</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn06/jisuanjiruanjian/">外企代表处</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn07/jisuanjiruanjian/">政府机关</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn08/jisuanjiruanjian/">事业单位</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn09/jisuanjiruanjian/">非营利机构</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn10/jisuanjiruanjian/">上市公司</a></li>
# 																<li><a class="" href="http://jobs.51job.com/suzhou/cn11/jisuanjiruanjian/">创业公司</a></li>
# 															</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>月薪范围</span>
# 							<ul>
# 																								<li><a class="" href="http://jobs.51job.com/suzhou/yx01/jisuanjiruanjian/">2千以下</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx02/jisuanjiruanjian/">2-3千</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx03/jisuanjiruanjian/">3-4.5千</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx04/jisuanjiruanjian/">4.5-6千</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx05/jisuanjiruanjian/">6-8千</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx06/jisuanjiruanjian/">0.8-1万</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx07/jisuanjiruanjian/">1-1.5万</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx08/jisuanjiruanjian/">1.5-2万</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx09/jisuanjiruanjian/">2-3万</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx10/jisuanjiruanjian/">3-4万</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx11/jisuanjiruanjian/">4-5万</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/yx12/jisuanjiruanjian/">5万以上</a></li>
# 																</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>工作类型</span>
# 							<ul>
# 																		<li><a class="" href="http://jobs.51job.com/suzhou/wt01/jisuanjiruanjian/">全职</a></li>
# 																				<li><a class="" href="http://jobs.51job.com/suzhou/wt02/jisuanjiruanjian/">兼职/实习</a></li>
# 																				<li><a class="" href="http://jobs.51job.com/suzhou/wt03/jisuanjiruanjian/">实习全职</a></li>
# 																				<li><a class="" href="http://jobs.51job.com/suzhou/wt04/jisuanjiruanjian/">实习兼职</a></li>
# 																</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>发布时间</span>
# 							<ul>
# 																								<li><a class="mk" href="http://jobs.51job.com/suzhou/rt0/jisuanjiruanjian/">24小时内</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/rt1/jisuanjiruanjian/">近三天</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/rt2/jisuanjiruanjian/">近一周</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/rt3/jisuanjiruanjian/">近一月</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/rt4/jisuanjiruanjian/">其它</a></li>
# 																</ul>
# 						</div>
# 					</div>
# 					<div class="l">
# 						<div>
# 							<em class="sicon Dm"></em><font></font>
# 							<span>学历要求</span>
# 							<ul>
# 																								<li><a class="" href="http://jobs.51job.com/suzhou/ed01/jisuanjiruanjian/">初中及以下</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/ed02/jisuanjiruanjian/">高中/中技/中专</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/ed03/jisuanjiruanjian/">大专</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/ed04/jisuanjiruanjian/">本科</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/ed05/jisuanjiruanjian/">硕士</a></li>
# 																									<li><a class="" href="http://jobs.51job.com/suzhou/ed06/jisuanjiruanjian/">博士</a></li>
# 																</ul>
# 						</div>
# 					</div>
#
# 					<p class="clear"></p>
# 				</div>
# 			</div>
# 			<div class="bt" style="z-index:1">
# 				<strong class="or">已选条件：</strong>
# 				<div class="clist">
# 												<span>苏州<a href="http://jobs.51job.com/jisuanjiruanjian/" ><em class="sicon Dm"></em></a></span>
# 														<span>计算机软件<a href="http://jobs.51job.com/suzhou/" ><em class="sicon Dm"></em></a></span>
# 												<div class="clear"></div>
# 					<a class="qx sicon Dm" href="http://jobs.51job.com/all/">清除条件</a>
# 				</div>
# 			</div>
# 		</div>
#
# 		<div class="mcon">
# 			<div class="left">
# 										<div class="detlist gbox">
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="IT管理员" target="_blank" href="http://jobs.51job.com/suzhou-wzq/88051262.html?s=02">IT管理员</a></span>
# 							<a title="苏州宝丽洁日化有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-wzq/co2546226.html">苏州宝丽洁日化有限公司</a>
# 							<span class="location name">苏州-吴中区</span>
# 							<span class="location">4.5-6千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：3-4年<span>|</span>公司性质：合资<span>|</span>公司规模：500-1000人
# 						</p>
# 						<p class="text" title="岗位主要工作职责：1、公司办公软硬件及办公耗材的日常维护管理工作。2、公司邮件往来安全管理工作以及员工邮箱设置工作。3、公司网络稳定性管理工作。4、负责公司ERP系统各个模块的管理维护工作。5、上级交办的其它事项。任职要求：1、大专以上学历，计算机相关专业毕业。2、有一年以上IT管理工作经验，熟悉办公软硬件异常情况处理。3、对ERP系统熟悉。">
# 							岗位主要工作职责：1、公司办公软硬件及办公耗材的日常维护管理工作。2、公司邮件往来安全管理工作以及员工邮箱设置工作。3、公司网络稳定性管理工作。4、负责公司ERP系统各个模块的管理维护工作。5、上级交办的其它事项。任职要求：1、大专以上学历，计算机相关专业毕业。2、有一年以上IT管理工作经验，熟悉办公软硬件异常情况处理。3、对ERP系统熟悉。						</p>
# 						<p class="opat">
# 							<input value="88051262" name="hidJobID88051262" id="hidJobID88051262" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID88051262','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('88051262');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title=".NET软件工程师 (职位编号：4)" target="_blank" href="http://jobs.51job.com/suzhou/43643687.html?s=02">.NET软件工程师 (职位编号：4)</a></span>
# 							<a title="苏州技杰软件有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co2181041.html">苏州技杰软件有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">6-8千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：1年<span>|</span>公司性质：外资（欧美）<span>|</span>公司规模：50-150人
# 						</p>
# 						<p class="text" title="岗位职责&#160;1、 按软件开发流程和生命周期进行软件开发，根据开发计划，及时交付工作&#160;2、 开发大型Web应用系统3、 根据项目需求分析、设计系统，编写开发设计文档，参与系统的分析和研发4、 编写实现代码、进行单元测试，在技术经理的指导下优化系统性能5、 分析并解决程序产生的BUG&#160;6、 部署/发布系统&#160;7、 提供系统维护、扩展/升级的技术支持&#160;岗位要求&#160;1、 计算机及相关专业毕业，本科以上学历，英语四级或以上，或具有同等工作经历经验；&#160;2、&#160;精通ASP.Net MVC 4.0 编程，掌握C#、html、Javascript、XML、CSS、JQuery等编程语言；3、 熟悉SQL SERVER和ADO.NET编程，能熟练使用ADO.NET进行数据增删改查，熟悉存储过程；4、 具有良好的沟通能力和团队合作精神；&#160;5、有大型网站或完整项目参与开发工作经验者优先考虑。">
# 							岗位职责&#160;1、 按软件开发流程和生命周期进行软件开发，根据开发计划，及时交付工作&#160;2、 开发大型Web应用系统3、 根据项目需求分析、设计系统，编写开发设计文档，参与系统的分析和研发4、 编写实现代码、进行单元测试，在技术经理的指导下优化系统性能5、 分析并解决程序产生的BUG&#160;6、 部署/发布系统&#160;7、 提供系统维护、扩展/升级的技术支持&#160;岗位要求&#160;1、 计算机及相关专业毕业，本科以上学历，英语四级或以上，或具有同等工作经历经验；&#160;2、&#160;精通ASP.Net MVC 4.0 编程，掌握C#、html、Javascript、XML、CSS、JQuery等编程语言；3、 熟悉SQL SERVER和ADO.NET编程，能熟练使用ADO.NET进行数据增删改查，熟悉存储过程；4、 具有良好的沟通能力和团队合作精神；&#160;5、有大型网站或完整项目参与开发工作经验者优先考虑。						</p>
# 						<p class="opat">
# 							<input value="43643687" name="hidJobID43643687" id="hidJobID43643687" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID43643687','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('43643687');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="网站测试工程师" target="_blank" href="http://jobs.51job.com/suzhou/86803547.html?s=02">网站测试工程师</a></span>
# 							<a title="苏州碧格网络科技有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co2690611.html">苏州碧格网络科技有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">4.5-6千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：<span>|</span>工作经验：<span>|</span>公司性质：外资（欧美）<span>|</span>公司规模：50-150人
# 						</p>
# 						<p class="text" title="岗位职责：1、根据产品需求编写测试用例进行产品测试，发现产品缺陷，跟踪定位Bug；2、协助开发工程师解决问题，对产品、流程提出持续性改进意见,保证交付的产品质量。任职要求：1、性别不限，大专以上学历，计算机及互联网相关专业优先；2、工作认真细心、逻辑思维清晰严谨；3、高度的责任心和流程规范意识，善于在工作中发现并深挖问题；4、有良好的文档编写能力，有较强的逻辑分析能力和学习能力；5、责任心强，拥有良好的沟通技巧及团队合作精神。">
# 							岗位职责：1、根据产品需求编写测试用例进行产品测试，发现产品缺陷，跟踪定位Bug；2、协助开发工程师解决问题，对产品、流程提出持续性改进意见,保证交付的产品质量。任职要求：1、性别不限，大专以上学历，计算机及互联网相关专业优先；2、工作认真细心、逻辑思维清晰严谨；3、高度的责任心和流程规范意识，善于在工作中发现并深挖问题；4、有良好的文档编写能力，有较强的逻辑分析能力和学习能力；5、责任心强，拥有良好的沟通技巧及团队合作精神。						</p>
# 						<p class="opat">
# 							<input value="86803547" name="hidJobID86803547" id="hidJobID86803547" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID86803547','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('86803547');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title=".net开发工程师" target="_blank" href="http://jobs.51job.com/suzhou-gyyq/71535911.html?s=02">.net开发工程师</a></span>
# 							<a title="车巴达（苏州）网络科技有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-gyyq/co3729153.html">车巴达（苏州）网络科技有限公司</a>
# 							<span class="location name">苏州-工业园区</span>
# 							<span class="location">0.7-1.4万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：大专<span>|</span>工作经验：2年<span>|</span>公司性质：民营公司<span>|</span>公司规模：50-150人
# 						</p>
# 						<p class="text" title="岗位职责：1， 参与巴士管家APP的中间层功能的系统开发维护。2， 根据产品开发进度和任务分配，开发相应的软件模块。3， 根据公司技术文档规范编写相应的技术文档。任职要求：熟悉.net有2年及以上工作经验者优先, 有项目经验者优先。1，熟练掌握ASP.NET C# 开发技术，熟悉ASP.NET MVC，有一定开发经验。2，熟悉.Net Framework 3.5及以上框架，熟悉面向对象编程，了解设计模式。3，熟悉MS-SQL/MySql,熟练使用SQL语言，具备一定的SQL优化技巧更佳。4，具备良好的编码习惯、有良好的沟通能力及团队协作意识。5，了解HTML/XML/Json、Javascript/AJAX、CSS、接口开发等相关WEB技术。">
# 							岗位职责：1， 参与巴士管家APP的中间层功能的系统开发维护。2， 根据产品开发进度和任务分配，开发相应的软件模块。3， 根据公司技术文档规范编写相应的技术文档。任职要求：熟悉.net有2年及以上工作经验者优先, 有项目经验者优先。1，熟练掌握ASP.NET C# 开发技术，熟悉ASP.NET MVC，有一定开发经验。2，熟悉.Net Framework 3.5及以上框架，熟悉面向对象编程，了解设计模式。3，熟悉MS-SQL/MySql,熟练使用SQL语言，具备一定的SQL优化技巧更佳。4，具备良好的编码习惯、有良好的沟通能力及团队协作意识。5，了解HTML/XML/Json、Javascript/AJAX、CSS、接口开发等相关WEB技术。						</p>
# 						<p class="opat">
# 							<input value="71535911" name="hidJobID71535911" id="hidJobID71535911" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID71535911','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('71535911');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="IT专员" target="_blank" href="http://jobs.51job.com/suzhou/89100631.html?s=02">IT专员</a></span>
# 							<a title="明基电通有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co1986954.html">明基电通有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">6-8千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：<span>|</span>公司性质：外资（非欧美）<span>|</span>公司规模：500-1000人
# 						</p>
# 						<p class="text" title="岗位职责：1. 负责多个IT系统日常服务支持；2. 维护公司内部系统的稳定运行，对电话系统、邮件系统等设施进行日常维护，并能独立完成故障的深度排查；3.负责服务器、存储、HypeV虚拟化的日常管理和维护4. 熟悉主流存储厂商（EMC、HP、IBM、华为等）产品及解决方案; 具有存储的安装、配置、调优、排障、日志分析等能力5. 学习能力强，较好的沟通和协作能力，并有较强的创新意识和团队合作精神。6. 其它公司内部的软硬件维护、管理工作任职要求：1.计算机相关专业本科或以上学历（计算机及其相关专业）；2.两年以上工作经验，优秀应届生也可；3.熟悉 Windows Server/Windows AD/Windows Desktop/Linux的维护；4.掌握存储基本理论和主要技术；5. 具备良好的服务意识、职业素养和沟通能力，具备团队协作精神；职能类别：技术支持/维护工程师其他">
# 							岗位职责：1. 负责多个IT系统日常服务支持；2. 维护公司内部系统的稳定运行，对电话系统、邮件系统等设施进行日常维护，并能独立完成故障的深度排查；3.负责服务器、存储、HypeV虚拟化的日常管理和维护4. 熟悉主流存储厂商（EMC、HP、IBM、华为等）产品及解决方案; 具有存储的安装、配置、调优、排障、日志分析等能力5. 学习能力强，较好的沟通和协作能力，并有较强的创新意识和团队合作精神。6. 其它公司内部的软硬件维护、管理工作任职要求：1.计算机相关专业本科或以上学历（计算机及其相关专业）；2.两年以上工作经验，优秀应届生也可；3.熟悉 Windows Server/Windows AD/Windows Desktop/Linux的维护；4.掌握存储基本理论和主要技术；5. 具备良好的服务意识、职业素养和沟通能力，具备团队协作精神；职能类别：技术支持/维护工程师其他						</p>
# 						<p class="opat">
# 							<input value="89100631" name="hidJobID89100631" id="hidJobID89100631" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID89100631','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('89100631');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="JAVA架构师" target="_blank" href="http://jobs.51job.com/nanjing-qhq/88963662.html?s=02">JAVA架构师</a></span>
# 							<a title="中通国脉物联科技南京有限公司" target="_blank" class="name" href="http://jobs.51job.com/nanjing-qhq/co4378980.html">中通国脉物联科技南京有限公司</a>
# 							<span class="location name">异地招聘</span>
# 							<span class="location">20-30万/年</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：5-7年<span>|</span>公司性质：民营公司<span>|</span>公司规模：50-150人
# 						</p>
# 						<p class="text" title="1. 具有 2 年以上B/S 体系结构软件产品开发及架构和设计经验;2. 具有 3 年以上的JAVA代码编写工作经验;3. 具有丰富的大中型开发项目的总体规划、方案设计及技术队伍管理经验;4. 对JAVA 技 术 及 整 个 解 决 方 案 有 深 刻 的 理 解 及 熟 练 的 应 用 ， 并 且 精 通WebService/J2EE 架构和设计模式，并在此基础上设计产品框架;5. 具有面向对象分析、设计、开发能力（OOA、OOD、OOP），精通 UML 和 ROSE，熟练使用Rational Rose、PowerDesigner 等工具进行设计开发;6. 精通大型数据库,如 Oracle、Sql Server、MySQL 等的开发;7. 在应用系统开发平台和项目管理上有深厚的基础，有大中型应用系统开发和实施的成功案例;8. 良好的团队意识和协作精神，有较强的内外沟通能力.其他说明：1、上市企业平台及人性化的管理制度；2、领先的软件行业，顶尖的专业技术，优越的办公环境及舒适的工作氛围；3、入职即缴纳完善的五险一金，提供餐补15元/天，节日福利（端午、中秋、春节各500元/次）；4、具有绝对竞争力的薪酬福利，及较大的成长晋升空间。">
# 							1. 具有 2 年以上B/S 体系结构软件产品开发及架构和设计经验;2. 具有 3 年以上的JAVA代码编写工作经验;3. 具有丰富的大中型开发项目的总体规划、方案设计及技术队伍管理经验;4. 对JAVA 技 术 及 整 个 解 决 方 案 有 深 刻 的 理 解 及 熟 练 的 应 用 ， 并 且 精 通WebService/J2EE 架构和设计模式，并在此基础上设计产品框架;5. 具有面向对象分析、设计、开发能力（OOA、OOD、OOP），精通 UML 和 ROSE，熟练使用Rational Rose、PowerDesigner 等工具进行设计开发;6. 精通大型数据库,如 Oracle、Sql Server、MySQL 等的开发;7. 在应用系统开发平台和项目管理上有深厚的基础，有大中型应用系统开发和实施的成功案例;8. 良好的团队意识和协作精神，有较强的内外沟通能力.其他说明：1、上市企业平台及人性化的管理制度；2、领先的软件行业，顶尖的专业技术，优越的办公环境及舒适的工作氛围；3、入职即缴纳完善的五险一金，提供餐补15元/天，节日福利（端午、中秋、春节各500元/次）；4、具有绝对竞争力的薪酬福利，及较大的成长晋升空间。						</p>
# 						<p class="opat">
# 							<input value="88963662" name="hidJobID88963662" id="hidJobID88963662" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID88963662','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('88963662');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="Java软件工程师" target="_blank" href="http://jobs.51job.com/suzhou-gyyq/89102160.html?s=02">Java软件工程师</a></span>
# 							<a title="苏州斯威高科信息技术有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-gyyq/co3131679.html">苏州斯威高科信息技术有限公司</a>
# 							<span class="location name">苏州-工业园区</span>
# 							<span class="location">0.7-1.5万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：3-4年<span>|</span>公司性质：民营公司<span>|</span>公司规模：50-150人
# 						</p>
# 						<p class="text" title="1.负责Web系统/平台研发工作，业务需求分析和软件设计，并编码实现；2.负责数据库设计、系统详细设计和核心业务编码工作；  3.对产品需求进行理解，并从软件功能层面提出需增加或调整的内容；职位要求： 1.本科以上学历，3年以上JAVA软件开发项目工作经验，有参与开发过1个以上大中型JAVA软件项目； 2.熟练掌握Tomcat、Apache、Nginx等多种开源服务器，了解各类应用服务器，如如WebLogic、Tomcat、Resin、JBoss、WebSphere等； 3.熟练掌握J2EE体系架构，具有EJB、JSP、Servlet等开发经验；4.熟练掌握Java MVC开发架构模式，熟练掌握各种开源框架，如Struts、Spring、Hibernate等； 5.熟悉Web service理念，有相关设计、开发经验者优先； 6.熟悉Web 前端开发，掌握HTML5、CSS3、JavaScript/Ajax、jQuery等主要技术； 7.熟练掌握Oracle、MySQL等主流数据库，熟悉数据库建模，具备深厚的SQL功底； 8.能快速理解业务需求并进行相关逻辑设计，能熟练使用相关建模工具，并具有规范的开发、设计文档写作能力； 9.熟练掌握Java系统的故障排查和性能调优； 10.要求踏实、有责任心，具有良好的团队合作精神和沟通能力，并有很强的学习能力； 逻辑思路清晰，较强的创新能力，有良好的计划和执行能力；加分项： 1.有PHP开发经验 ；2.有工控系统开发经验优先考虑 ；3.愿意持续学习，挑战自己；职位诱惑： 1.舒适有趣的工作环境，融洽开放的工作氛围； 2.除了有竞争力的薪酬福利外，我们还提供可观的成长空间，公司处于快速成长期，你将有更多的机会挑战自己，收获未来；3.获得工作与生活的平衡，我们提倡高效的工作效率；">
# 							1.负责Web系统/平台研发工作，业务需求分析和软件设计，并编码实现；2.负责数据库设计、系统详细设计和核心业务编码工作；  3.对产品需求进行理解，并从软件功能层面提出需增加或调整的内容；职位要求： 1.本科以上学历，3年以上JAVA软件开发项目工作经验，有参与开发过1个以上大中型JAVA软件项目； 2.熟练掌握Tomcat、Apache、Nginx等多种开源服务器，了解各类应用服务器，如如WebLogic、Tomcat、Resin、JBoss、WebSphere等； 3.熟练掌握J2EE体系架构，具有EJB、JSP、Servlet等开发经验；4.熟练掌握Java MVC开发架构模式，熟练掌握各种开源框架，如Struts、Spring、Hibernate等； 5.熟悉Web service理念，有相关设计、开发经验者优先； 6.熟悉Web 前端开发，掌握HTML5、CSS3、JavaScript/Ajax、jQuery等主要技术； 7.熟练掌握Oracle、MySQL等主流数据库，熟悉数据库建模，具备深厚的SQL功底； 8.能快速理解业务需求并进行相关逻辑设计，能熟练使用相关建模工具，并具有规范的开发、设计文档写作能力； 9.熟练掌握Java系统的故障排查和性能调优； 10.要求踏实、有责任心，具有良好的团队合作精神和沟通能力，并有很强的学习能力； 逻辑思路清晰，较强的创新能力，有良好的计划和执行能力；加分项： 1.有PHP开发经验 ；2.有工控系统开发经验优先考虑 ；3.愿意持续学习，挑战自己；职位诱惑： 1.舒适有趣的工作环境，融洽开放的工作氛围； 2.除了有竞争力的薪酬福利外，我们还提供可观的成长空间，公司处于快速成长期，你将有更多的机会挑战自己，收获未来；3.获得工作与生活的平衡，我们提倡高效的工作效率；						</p>
# 						<p class="opat">
# 							<input value="89102160" name="hidJobID89102160" id="hidJobID89102160" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID89102160','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('89102160');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="软件开发工程师" target="_blank" href="http://jobs.51job.com/suzhou-gxq/74424677.html?s=02">软件开发工程师</a></span>
# 							<a title="苏州新导智能科技有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-gxq/co1739846.html">苏州新导智能科技有限公司</a>
# 							<span class="location name">苏州-高新区</span>
# 							<span class="location">8-10万/年</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：2年<span>|</span>公司性质：民营公司<span>|</span>公司规模：少于50人
# 						</p>
# 						<p class="text" title="岗位职责：1、参与项目启动、开发、实施、结束全过程；2、充分理解业务需求说明书描述内容；3、参与系统概要设备和详细设计，按设计文档完成开发编码工作；4、餐椅系统单元测试、系统测试及用户手册编写；5、对本职工作提出改进思路、建议；6、积极配合其他工程师完成开发任务；7、完成领导交代的其他工作；任职要求：1.2年以上的.net开发工作经验;2.熟悉.net平台,精通HTML,能熟悉使用HTML开发asp.net网站;3.熟悉就JaveScript,JQuery,Ajax,C#等;4.熟悉SQL Server数据库,有RFID等物联网硬件集成经验优先;5.良好的沟通、协调与书面表达能力，学习能力，创新能力强，具有团队合作精神，能承受较大的工作压力。">
# 							岗位职责：1、参与项目启动、开发、实施、结束全过程；2、充分理解业务需求说明书描述内容；3、参与系统概要设备和详细设计，按设计文档完成开发编码工作；4、餐椅系统单元测试、系统测试及用户手册编写；5、对本职工作提出改进思路、建议；6、积极配合其他工程师完成开发任务；7、完成领导交代的其他工作；任职要求：1.2年以上的.net开发工作经验;2.熟悉.net平台,精通HTML,能熟悉使用HTML开发asp.net网站;3.熟悉就JaveScript,JQuery,Ajax,C#等;4.熟悉SQL Server数据库,有RFID等物联网硬件集成经验优先;5.良好的沟通、协调与书面表达能力，学习能力，创新能力强，具有团队合作精神，能承受较大的工作压力。						</p>
# 						<p class="opat">
# 							<input value="74424677" name="hidJobID74424677" id="hidJobID74424677" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID74424677','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('74424677');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="项目实施工程师" target="_blank" href="http://jobs.51job.com/suzhou-gyyq/87812797.html?s=02">项目实施工程师</a></span>
# 							<a title="苏州工业园区思毅软件有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-gyyq/co2650043.html">苏州工业园区思毅软件有限公司</a>
# 							<span class="location name">苏州-工业园区</span>
# 							<span class="location">3-8千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：中技<span>|</span>工作经验：2年<span>|</span>公司性质：民营公司<span>|</span>公司规模：少于50人
# 						</p>
# 						<p class="text" title="1、熟悉ERP实施方法，具有一定的项目管理技能和生产管理知识2、能适应出差3、明确客户项目需求，引导客户进行快速实施和结项，完成项目验收及回款4、与客户保持良好的合作，确保项目进度与后期维护">
# 							1、熟悉ERP实施方法，具有一定的项目管理技能和生产管理知识2、能适应出差3、明确客户项目需求，引导客户进行快速实施和结项，完成项目验收及回款4、与客户保持良好的合作，确保项目进度与后期维护						</p>
# 						<p class="opat">
# 							<input value="87812797" name="hidJobID87812797" id="hidJobID87812797" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID87812797','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('87812797');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="嵌入式软件工程师" target="_blank" href="http://jobs.51job.com/suzhou-wzq/88755416.html?s=02">嵌入式软件工程师</a></span>
# 							<a title="天津晟越博思信息技术有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-wzq/co2824055.html">天津晟越博思信息技术有限公司</a>
# 							<span class="location name">苏州-吴中区</span>
# 							<span class="location">1-1.5万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：大专<span>|</span>工作经验：2年<span>|</span>公司性质：民营公司<span>|</span>公司规模：少于50人
# 						</p>
# 						<p class="text" title="2年以上工作经验 1.计算机相关专业，本科及以上学历 2.熟悉无线应用层、驱动移植；熟悉hostapd、wpa_supplicant配置； 3.熟悉Linux内核调试、驱动开发优先录用;4.熟悉HTTP/FTP/TCP/UDP等网络协议开发；6.积极主动、认真踏实、有良好的沟通能力和团队合作精神。 岗位职责： 1.无线模块的驱动移植。SoftAP、STA等模式配置及应用； 2.内核驱动开发、调试； 3.学习和研究新技术以满足产品的需求">
# 							2年以上工作经验 1.计算机相关专业，本科及以上学历 2.熟悉无线应用层、驱动移植；熟悉hostapd、wpa_supplicant配置； 3.熟悉Linux内核调试、驱动开发优先录用;4.熟悉HTTP/FTP/TCP/UDP等网络协议开发；6.积极主动、认真踏实、有良好的沟通能力和团队合作精神。 岗位职责： 1.无线模块的驱动移植。SoftAP、STA等模式配置及应用； 2.内核驱动开发、调试； 3.学习和研究新技术以满足产品的需求						</p>
# 						<p class="opat">
# 							<input value="88755416" name="hidJobID88755416" id="hidJobID88755416" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID88755416','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('88755416');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="计算机图形学视觉算法高级工程师" target="_blank" href="http://jobs.51job.com/suzhou/83526826.html?s=02">计算机图形学视觉算法高级工程师</a></span>
# 							<a title="苏州光之翼智能科技有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co4129294.html">苏州光之翼智能科技有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">0.6-1.5万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：5-7年<span>|</span>公司性质：民营公司<span>|</span>公司规模：少于50人
# 						</p>
# 						<p class="text" title="岗位职责：1、 参与控制系统的架构设计和开发2、 负责多视图几何、三维重建、SLAM相关算法的研发；3、 负责与嵌入式工程师对接完成算法的移植；4、 负责机器人计算机视觉前沿技术的预研。5、 配合嵌入式软件工程师联合调试并解决问题；6、 客户需求分析7、 参与部门的组织与团队建设；任职资格：1、 本专业领域硕士以上学历或者本科具有4年以上相关工作经验。2、 精通C/C++等编程语言，熟悉常用的数据结构；3、 数学基础良好，掌握常用的线性代数、矩阵分析相关知识和库；4、 至少具有以下一种专业背景（计算机视觉、多视图几何、移动机器人导航与控制、图像处理、数学），对本专业领域知识有良好的掌握；5、 至少具有以下一方面的开发经验（ROS、OpenCV、SLAM）,至少有一个项目在此基础上的进行算法实现或仿真；6、 熟悉linux系统，了解常用的算法开发平台；">
# 							岗位职责：1、 参与控制系统的架构设计和开发2、 负责多视图几何、三维重建、SLAM相关算法的研发；3、 负责与嵌入式工程师对接完成算法的移植；4、 负责机器人计算机视觉前沿技术的预研。5、 配合嵌入式软件工程师联合调试并解决问题；6、 客户需求分析7、 参与部门的组织与团队建设；任职资格：1、 本专业领域硕士以上学历或者本科具有4年以上相关工作经验。2、 精通C/C++等编程语言，熟悉常用的数据结构；3、 数学基础良好，掌握常用的线性代数、矩阵分析相关知识和库；4、 至少具有以下一种专业背景（计算机视觉、多视图几何、移动机器人导航与控制、图像处理、数学），对本专业领域知识有良好的掌握；5、 至少具有以下一方面的开发经验（ROS、OpenCV、SLAM）,至少有一个项目在此基础上的进行算法实现或仿真；6、 熟悉linux系统，了解常用的算法开发平台；						</p>
# 						<p class="opat">
# 							<input value="83526826" name="hidJobID83526826" id="hidJobID83526826" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID83526826','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('83526826');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="java初级开发工程师/工程师助理+双休5险1金" target="_blank" href="http://jobs.51job.com/suzhou/88365504.html?s=02">java初级开发工程师/工程师助理+双休5险1金</a></span>
# 							<a title="软世通集团苏州分公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co4381492.html">软世通集团苏州分公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">4.5-6千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：大专<span>|</span>工作经验：<span>|</span>公司性质：民营公司<span>|</span>公司规模：150-500人
# 						</p>
# 						<p class="text" title="一、岗位要求 1、大专及以上学历，专业不限，条件优秀者无经验亦可。 2、20-28岁，有较强的学习能力。 3、热爱软件开发，具备较强的逻辑思维能力。 4、具有较强的抗压能力，性格开朗、工作细致，善于沟通，团队协作能力强。 二、岗位职责 1、协助团队进行Java的应用设计及开发规划； 2、协助团队撰写设计开发及实现文档、流程； 3、完成软件的修改bug工作； 4、协助支持项目对产品的应用服务。   三、工作时间：5天7小时（朝九晚五）；   四、福利待遇 【工作时间】周一至周五，朝九晚五，周末双休； 【薪酬】富有竞争力的薪酬水平和项目提成； 【奖金】绩效奖金、项目奖金、年终奖金； 【社保】五险一金：医疗、生育、工伤、失业、养老保险及住房公积金； 【公司福利】年度体检、年度旅游，拓展培训，公司聚餐、年会等，活动丰富； 【假期福利】享受国家规定的带薪年假，法定节假日； 【成长进步】人性化的学习管理制度、一对一的指定帮助，让员工快速融入新环境并成长！">
# 							一、岗位要求 1、大专及以上学历，专业不限，条件优秀者无经验亦可。 2、20-28岁，有较强的学习能力。 3、热爱软件开发，具备较强的逻辑思维能力。 4、具有较强的抗压能力，性格开朗、工作细致，善于沟通，团队协作能力强。 二、岗位职责 1、协助团队进行Java的应用设计及开发规划； 2、协助团队撰写设计开发及实现文档、流程； 3、完成软件的修改bug工作； 4、协助支持项目对产品的应用服务。   三、工作时间：5天7小时（朝九晚五）；   四、福利待遇 【工作时间】周一至周五，朝九晚五，周末双休； 【薪酬】富有竞争力的薪酬水平和项目提成； 【奖金】绩效奖金、项目奖金、年终奖金； 【社保】五险一金：医疗、生育、工伤、失业、养老保险及住房公积金； 【公司福利】年度体检、年度旅游，拓展培训，公司聚餐、年会等，活动丰富； 【假期福利】享受国家规定的带薪年假，法定节假日； 【成长进步】人性化的学习管理制度、一对一的指定帮助，让员工快速融入新环境并成长！						</p>
# 						<p class="opat">
# 							<input value="88365504" name="hidJobID88365504" id="hidJobID88365504" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID88365504','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('88365504');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="数据分析师" target="_blank" href="http://jobs.51job.com/suzhou/89095724.html?s=02">数据分析师</a></span>
# 							<a title="荣阳铝业有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co4079613.html">荣阳铝业有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">6-8千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：2年<span>|</span>公司性质：民营公司<span>|</span>公司规模：
# 						</p>
# 						<p class="text" title="数据分析师&nbsp;岗位职责：1、负责基础数据的清洗和处理，并形成直观的分析报告，定期向上级领导、区域负责人反馈运营情况，追踪运营工作进展；2、熟悉并深入运营业务流程，通过项目执行，找出核心问题，并提出关键举措，推动运营指标及业务能力的提升；3、为运营制作营销工具和操作指南，为实际业务作业提供工具类帮助；4、挖掘并树立运营***实践，总结标杆们的工作经验，形成标准化动作加以推广。&nbsp;任职要求：1、统招二本及以上学历，统计学、金融学、经济学、数学等理科专业的优秀应届毕业生或从事至少一年以上数据分析者优先；2、精通Excel里各项数据处理工具及函数，熟悉数据建模、SPSS、R语言等优先；3、逻辑思维极强，做事严谨负责、条理清晰，善于从数据中寻找业务规律，并能结合实际业务操作有效支持运营工作的改善和提升。">
# 							数据分析师&nbsp;岗位职责：1、负责基础数据的清洗和处理，并形成直观的分析报告，定期向上级领导、区域负责人反馈运营情况，追踪运营工作进展；2、熟悉并深入运营业务流程，通过项目执行，找出核心问题，并提出关键举措，推动运营指标及业务能力的提升；3、为运营制作营销工具和操作指南，为实际业务作业提供工具类帮助；4、挖掘并树立运营***实践，总结标杆们的工作经验，形成标准化动作加以推广。&nbsp;任职要求：1、统招二本及以上学历，统计学、金融学、经济学、数学等理科专业的优秀应届毕业生或从事至少一年以上数据分析者优先；2、精通Excel里各项数据处理工具及函数，熟悉数据建模、SPSS、R语言等优先；3、逻辑思维极强，做事严谨负责、条理清晰，善于从数据中寻找业务规律，并能结合实际业务操作有效支持运营工作的改善和提升。						</p>
# 						<p class="opat">
# 							<input value="89095724" name="hidJobID89095724" id="hidJobID89095724" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID89095724','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('89095724');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="C++软件工程师" target="_blank" href="http://jobs.51job.com/suzhou-gxq/75753229.html?s=02">C++软件工程师</a></span>
# 							<a title="苏州本乔信息技术有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-gxq/co3368554.html">苏州本乔信息技术有限公司</a>
# 							<span class="location name">苏州-高新区</span>
# 							<span class="location">5-8千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：2年<span>|</span>公司性质：民营公司<span>|</span>公司规模：少于50人
# 						</p>
# 						<p class="text" title="职位描述：1.	负责产品服务端软件开发岗位要求：1.	本科2年以上Linux相关开发经验2.	技术基础扎实，了解内存、线程、IO底层机制3.	熟悉数据库、网络、多任务系统开发，良好的编程习惯4.	有图形图像、流媒体、嵌入式开发经验者优先5.	积极主动，良好的沟通能力和协作精神6.	有独立思考和解决问题的能力">
# 							职位描述：1.	负责产品服务端软件开发岗位要求：1.	本科2年以上Linux相关开发经验2.	技术基础扎实，了解内存、线程、IO底层机制3.	熟悉数据库、网络、多任务系统开发，良好的编程习惯4.	有图形图像、流媒体、嵌入式开发经验者优先5.	积极主动，良好的沟通能力和协作精神6.	有独立思考和解决问题的能力						</p>
# 						<p class="opat">
# 							<input value="75753229" name="hidJobID75753229" id="hidJobID75753229" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID75753229','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('75753229');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="java软件工程师(银行金融方向)" target="_blank" href="http://jobs.51job.com/suzhou-gyyq/77340787.html?s=02">java软件工程师(银行金融方向)</a></span>
# 							<a title="江苏银信融通信息科技有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou-gyyq/co3488505.html">江苏银信融通信息科技有限公司</a>
# 							<span class="location name">苏州-工业园区</span>
# 							<span class="location">0.6-1万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：本科<span>|</span>工作经验：<span>|</span>公司性质：民营公司<span>|</span>公司规模：少于50人
# 						</p>
# 						<p class="text" title="职位描述：1.负责公司银行金融类软件的功能模块开发以及程序框架的维护。2.进行项目的需求分析以及进行相应的概要设计和详细设计以及编码实现工作。3.完成上级安排的各项开发任务。4.接受人员外派的工作形式。岗位要求：1.计算机相关专业本科及以上学历。2.熟练使用java语言进行编程。3.熟悉java B/S结构的软件开发以及MVC。4.熟练运用DB2/Oracle等数据库。5.熟悉nutz框架以及miniui框架优先">
# 							职位描述：1.负责公司银行金融类软件的功能模块开发以及程序框架的维护。2.进行项目的需求分析以及进行相应的概要设计和详细设计以及编码实现工作。3.完成上级安排的各项开发任务。4.接受人员外派的工作形式。岗位要求：1.计算机相关专业本科及以上学历。2.熟练使用java语言进行编程。3.熟悉java B/S结构的软件开发以及MVC。4.熟练运用DB2/Oracle等数据库。5.熟悉nutz框架以及miniui框架优先						</p>
# 						<p class="opat">
# 							<input value="77340787" name="hidJobID77340787" id="hidJobID77340787" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID77340787','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('77340787');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="软件工程师" target="_blank" href="http://jobs.51job.com/suzhou/89087873.html?s=02">软件工程师</a></span>
# 							<a title="苏州青西资产管理有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co3633895.html">苏州青西资产管理有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">5-7千/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：大专<span>|</span>工作经验：1年<span>|</span>公司性质：民营公司<span>|</span>公司规模：150-500人
# 						</p>
# 						<p class="text" title="岗位职责：1.软件的程序设计与代码编写；2.有关技术方案、文档的编写，软件单元的测试；3.根据项目具体要求，承担开发任务，按计划完成任务目标；4.配合系统分析人员完成软件系统及模块的需求调研、需求分析；5.协助测试人员完成软件系统及模块的测试；6.独立完成软件系统及模块的编码；7.负责编制与项目相关的技术文档；8.根据项目具体要求，承担大型网站设计与开发；9.部分软件功能模块设计和软件界面美化任职要求：1、1年以上.Net开发工作经验； 2、熟悉.Net技术平台，精通C#语言、OOP和分层设计思想； 3、具备良好的编程能力、设计能力、撰写技术文档能力 4、熟悉BS、CS架构技术，熟练使用HTML、XML、Javascript、Css语言和AJAX技术； 5、熟悉SQL Server或MySQL等主流数据库系统，能够熟练使用SQL语言，掌握存储过程； 6、有RS232及TCPIP开发经验优先 7、有管理信息系统开发经验及相关网络配置经验优先。 8、有SMT行业相关系统开发经验优先。 9、热情，敬业，能够承受一定的工作压力，具备良好的交流能力及团队协作精神福利待遇：1、 工作时间：上五休二，国家法定节假日休息；2、公司有年度调薪，年终奖，中秋/春节/端午福利；3、公司定期组织生日会、下午茶及年度旅游活动；4、公司为员工提供宿舍安排；5、我们制度透明，团队气氛和谐，你将拥有更好的晋升空间及发展空间！公司网址：http://www.intelligent-stock.com/product.html">
# 							岗位职责：1.软件的程序设计与代码编写；2.有关技术方案、文档的编写，软件单元的测试；3.根据项目具体要求，承担开发任务，按计划完成任务目标；4.配合系统分析人员完成软件系统及模块的需求调研、需求分析；5.协助测试人员完成软件系统及模块的测试；6.独立完成软件系统及模块的编码；7.负责编制与项目相关的技术文档；8.根据项目具体要求，承担大型网站设计与开发；9.部分软件功能模块设计和软件界面美化任职要求：1、1年以上.Net开发工作经验； 2、熟悉.Net技术平台，精通C#语言、OOP和分层设计思想； 3、具备良好的编程能力、设计能力、撰写技术文档能力 4、熟悉BS、CS架构技术，熟练使用HTML、XML、Javascript、Css语言和AJAX技术； 5、熟悉SQL Server或MySQL等主流数据库系统，能够熟练使用SQL语言，掌握存储过程； 6、有RS232及TCPIP开发经验优先 7、有管理信息系统开发经验及相关网络配置经验优先。 8、有SMT行业相关系统开发经验优先。 9、热情，敬业，能够承受一定的工作压力，具备良好的交流能力及团队协作精神福利待遇：1、 工作时间：上五休二，国家法定节假日休息；2、公司有年度调薪，年终奖，中秋/春节/端午福利；3、公司定期组织生日会、下午茶及年度旅游活动；4、公司为员工提供宿舍安排；5、我们制度透明，团队气氛和谐，你将拥有更好的晋升空间及发展空间！公司网址：http://www.intelligent-stock.com/product.html						</p>
# 						<p class="opat">
# 							<input value="89087873" name="hidJobID89087873" id="hidJobID89087873" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID89087873','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('89087873');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="Software Support Engineer软件工程师" target="_blank" href="http://jobs.51job.com/suzhou/85954094.html?s=02">Software Support Engineer软件工程师</a></span>
# 							<a title="唯亚威应用光学（苏州）有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co3864980.html">唯亚威应用光学（苏州）有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">0.6-1万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：<span>|</span>工作经验：<span>|</span>公司性质：外资（非欧美）<span>|</span>公司规模：50-150人
# 						</p>
# 						<p class="text" title="Qualifications任职条件:1、Be good at English speaking&amp;listening, reading &amp; writing.英语基本口语沟通无障碍，有一定读写能力2、Master the programming language like C+/SQL/VB, Can read and modify some parts of them and transfer to the equipments. 掌握相关的编程语言例如C+/SQL/VB，能修改系统编程语言并运用到设备上；3.Be patient and Good communication skills.具备耐心与良好沟通能力；4.Can analyze and solve problems timely and accurately.具有较强的问题分析解决应对能力。Duties&amp;Responsibilities岗位职责：1、Be able to address a majority of technical questions concerning customization, integration, enterprise architecture and general feature基于客户定制、集成、企业架构和总体特性，能够解决大部分技术问题.2、 Provide timely, prioritized and complete customer-based feedback. Resolve client issues, exceeding their expectations for customer satisfaction提供即时、优化的技术支持并响应客户的反馈。解决客户问题,提升客户满意度3、Develop training materials or documentation on related topics, Learn and transfer advanced product knowledge to other team members根据相关课题准备相应的培训材料或文件，学习了解先进的产品知识并传授给团队。4、 Perform complex problem determination using system diagnostics, Manage complex &#39;System Down’ issues for critical client situations通过系统诊断复杂问题、设法为重要客户解决复杂的“系统崩溃”的情况5、Engage other technical teams to bring resolution to complex situations.与其他技术团队解决复杂的情况">
# 							Qualifications任职条件:1、Be good at English speaking&amp;listening, reading &amp; writing.英语基本口语沟通无障碍，有一定读写能力2、Master the programming language like C+/SQL/VB, Can read and modify some parts of them and transfer to the equipments. 掌握相关的编程语言例如C+/SQL/VB，能修改系统编程语言并运用到设备上；3.Be patient and Good communication skills.具备耐心与良好沟通能力；4.Can analyze and solve problems timely and accurately.具有较强的问题分析解决应对能力。Duties&amp;Responsibilities岗位职责：1、Be able to address a majority of technical questions concerning customization, integration, enterprise architecture and general feature基于客户定制、集成、企业架构和总体特性，能够解决大部分技术问题.2、 Provide timely, prioritized and complete customer-based feedback. Resolve client issues, exceeding their expectations for customer satisfaction提供即时、优化的技术支持并响应客户的反馈。解决客户问题,提升客户满意度3、Develop training materials or documentation on related topics, Learn and transfer advanced product knowledge to other team members根据相关课题准备相应的培训材料或文件，学习了解先进的产品知识并传授给团队。4、 Perform complex problem determination using system diagnostics, Manage complex &#39;System Down’ issues for critical client situations通过系统诊断复杂问题、设法为重要客户解决复杂的“系统崩溃”的情况5、Engage other technical teams to bring resolution to complex situations.与其他技术团队解决复杂的情况						</p>
# 						<p class="opat">
# 							<input value="85954094" name="hidJobID85954094" id="hidJobID85954094" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID85954094','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('85954094');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="生物信息工程师" target="_blank" href="http://jobs.51job.com/suzhou/83877158.html?s=02">生物信息工程师</a></span>
# 							<a title="首度生物科技（苏州）有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co4142812.html">首度生物科技（苏州）有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">0.8-1万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：<span>|</span>工作经验：<span>|</span>公司性质：外资（欧美）<span>|</span>公司规模：500-1000人
# 						</p>
# 						<p class="text" title="岗位要求：1.数学、计算机、物理、生物信息专业本科及以上学历，一年相关工作经验，优秀应届生也可2.了解Linux操作系统，熟悉perl、python、C/C++中一种或一种以上编程语言；3.具有高通量测序信息分析流程搭建经验者优先考虑；4.良好的团队协作能力及沟通能力；岗位职责：1.需求分析，算法设计及代码实现；2.负责DNA测序数据分析软件算法实现、自动化检测及报告流程搭建；3.流程测试，撰写相关文档；">
# 							岗位要求：1.数学、计算机、物理、生物信息专业本科及以上学历，一年相关工作经验，优秀应届生也可2.了解Linux操作系统，熟悉perl、python、C/C++中一种或一种以上编程语言；3.具有高通量测序信息分析流程搭建经验者优先考虑；4.良好的团队协作能力及沟通能力；岗位职责：1.需求分析，算法设计及代码实现；2.负责DNA测序数据分析软件算法实现、自动化检测及报告流程搭建；3.流程测试，撰写相关文档；						</p>
# 						<p class="opat">
# 							<input value="83877158" name="hidJobID83877158" id="hidJobID83877158" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID83877158','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('83877158');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="Android开发工程师" target="_blank" href="http://jobs.51job.com/suzhou/78774681.html?s=02">Android开发工程师</a></span>
# 							<a title="维信集团苏州总部" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co3856546.html">维信集团苏州总部</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">1-1.5万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：大专<span>|</span>工作经验：2年<span>|</span>公司性质：外资（非欧美）<span>|</span>公司规模：1000-5000人
# 						</p>
# 						<p class="text" title="岗位职责：1、负责android手机应用软件开发； 2、参与软件产品需求分析和设计，编写有关技术文档；3、按照项目计划，保证代码编写质量，按时完成开发任务；任职要求：1、有三年以上Android应用开发经验； 2、熟练掌握JAVA编程基础，具有J2ME或Java开发经验，熟悉android手机软件架构和开发、较强的学习能力；  3、熟悉Android系统UI设计，熟悉常用布局，熟悉Android控件，有自定义控件的能力； 4、熟练掌握熟练掌握XML、JSON的解析； 5、具备良好的职业素养和团队协作精神，以及较强的学习能力，承担独立开发的任务。">
# 							岗位职责：1、负责android手机应用软件开发； 2、参与软件产品需求分析和设计，编写有关技术文档；3、按照项目计划，保证代码编写质量，按时完成开发任务；任职要求：1、有三年以上Android应用开发经验； 2、熟练掌握JAVA编程基础，具有J2ME或Java开发经验，熟悉android手机软件架构和开发、较强的学习能力；  3、熟悉Android系统UI设计，熟悉常用布局，熟悉Android控件，有自定义控件的能力； 4、熟练掌握熟练掌握XML、JSON的解析； 5、具备良好的职业素养和团队协作精神，以及较强的学习能力，承担独立开发的任务。						</p>
# 						<p class="opat">
# 							<input value="78774681" name="hidJobID78774681" id="hidJobID78774681" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID78774681','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('78774681');" >收藏</a>
# 						</p>
# 					</div>
# 										<div class="e">
# 						<p class="info">
# 							<span class="title"><a title="软件集成工程师" target="_blank" href="http://jobs.51job.com/suzhou/89098064.html?s=02">软件集成工程师</a></span>
# 							<a title="上海宝宏软件有限公司" target="_blank" class="name" href="http://jobs.51job.com/suzhou/co2861221.html">上海宝宏软件有限公司</a>
# 							<span class="location name">苏州</span>
# 							<span class="location">0.8-1万/月</span>
# 							<span class="time">05-08 </span>
# 						</p>
# 						<p class="order">
# 							学历要求：<span>|</span>工作经验：<span>|</span>公司性质：民营公司<span>|</span>公司规模：150-500人
# 						</p>
# 						<p class="text" title="在客户现场参与如下开发：1.实现和维护软件需求、源代码、开发文档的软件版本控制系统2.实现和维护软件持续集成系统构建软件版本、执行验证方案，在生产系统中生成Release文档和发布软件3.验证软件的变更并正确地应用于软件基线中4.开发回归测试套件和软件工具5.验证软件在台架和实车中的使用可行性6.参考Automotive SPICE模型执行软件开发过程7.在执行过程中提出合理的改进建议任职资格：1.嵌入式软件开发至少1年工作经验，学士及以上学位的电子信息、车辆工程、计算机或者相关专业2.熟悉C/C++、软件配置管理过程和工具(CM synergy, Git, subversion)、软件验证和测试，有linux和Windows环境下开发经验3.有识别需求和开发脚本需要提高集成过程的效率和有效性的能力4.良好的分析、解决问题能力，能较好与内部成员及客户沟通5.熟练的英语口语和读写能力有以下经验者优先：1.集成服务技术(Jenkins)和协作工具(SharePoint)相2. 持续集成实践相关知识，包括自动化的构建和部署3.嵌入式系统或消费电子产品开发4.脚本语言，如Python, Perl, Shell5.团队和项目管理经验">
# 							在客户现场参与如下开发：1.实现和维护软件需求、源代码、开发文档的软件版本控制系统2.实现和维护软件持续集成系统构建软件版本、执行验证方案，在生产系统中生成Release文档和发布软件3.验证软件的变更并正确地应用于软件基线中4.开发回归测试套件和软件工具5.验证软件在台架和实车中的使用可行性6.参考Automotive SPICE模型执行软件开发过程7.在执行过程中提出合理的改进建议任职资格：1.嵌入式软件开发至少1年工作经验，学士及以上学位的电子信息、车辆工程、计算机或者相关专业2.熟悉C/C++、软件配置管理过程和工具(CM synergy, Git, subversion)、软件验证和测试，有linux和Windows环境下开发经验3.有识别需求和开发脚本需要提高集成过程的效率和有效性的能力4.良好的分析、解决问题能力，能较好与内部成员及客户沟通5.熟练的英语口语和读写能力有以下经验者优先：1.集成服务技术(Jenkins)和协作工具(SharePoint)相2. 持续集成实践相关知识，包括自动化的构建和部署3.嵌入式系统或消费电子产品开发4.脚本语言，如Python, Perl, Shell5.团队和项目管理经验						</p>
# 						<p class="opat">
# 							<input value="89098064" name="hidJobID89098064" id="hidJobID89098064" type="hidden" jt="0">
# 							<a class="sq sicon Dm" href="javascript:void(0);" onclick="delivery('hidJobID89098064','1','http://my.51job.com/','c','','','02','http://img03.51jobcdn.com/');return false;">立即申请</a><br />
# 							<a class="sc sicon Dm" href="javascript:void(0);" onclick="saveCollection('89098064');" >收藏</a>
# 						</p>
# 					</div>
# 											<div class="dw_page">
# 							<div class="p_box">
# 								<div class="p_wp">
# 									<div id="cppageno" class="p_in"><ul>
# <li class="bk"><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p1/">上一页</a></li><li class="on">1</li>
# <li><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p2/">2</a></li>
# <li><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p3/">3</a></li>
# <li><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p4/">4</a></li>
# <li><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p5/">5</a></li>
# <li><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p6/">6</a></li>
# <li class="bk"><a href="http://jobs.51job.com/suzhou/jisuanjiruanjian/p2/">下一页</a></li>
# </ul></div>
# 								</div>
# 							</div>
# 						</div>
# 					</div>
#
# 			</div>
# 			<div class="right">
#                 <div class="e gbox">
#                     <p class="btitle"><a href="http://auction.51jingying.com/?5CC4CE=1011" target="_blank" class="c_sblue">精英竞拍汇</a>-中高端人才求职平台</p>
# 					<div class="clist">
# 						<div class="c c0">
# 							<div class="p1">
# 								<label>年薪：30-80万</label>
# 								<em></em>
# 								<a href="http://it.51jingying.com/?5CC4CE=1011" target="_blank">互联网专场</a>
# 							</div>
# 							<div class="p2">
# 								<span>招聘职位：</span>
# 								后端开发，前端开发，移动端开发，测试，产品/设计/运营
# 							</div>
# 						</div>
# 						<div class="c c1">
# 							<div class="p1">
# 								<label>年薪：40-150万</label>
# 								<em></em>
# 								<a href="http://finance.51jingying.com/?5CC4CE=1011" target="_blank">金融专场</a>
# 							</div>
# 							<div class="p2">
# 								<span>招聘职位：</span>
# 								财务审计，合规与风险控制，后台运营，投行，销售
# 							</div>
# 						</div>
# 						<div class="c c2">
# 							<div class="p1">
# 								<label>年薪：40-60万</label>
# 								<em></em>
# 								<a href="http://fang.51jingying.com/?5CC4CE=1011" target="_blank">房地产专场</a>
# 							</div>
# 							<div class="p2">
# 								<span>招聘职位：</span>
#                                 房地产开发，建筑工程，规划设计，商业，市场营销
# 							</div>
# 						</div>
# 						<div class="c c3">
# 							<div class="p1">
# 								<label>年薪：20-40万</label>
# 								<em></em>
# 								<a href="http://auto.51jingying.com/?5CC4CE=1011" target="_blank">汽车专场</a>
# 							</div>
# 							<div class="p2">
# 								<span>招聘职位：</span>
# 								汽车新能源，软件与汽车电子，生产制造，质量管理，供应链管理
# 							</div>
# 						</div>
# 					</div>
# 					<div class="hmore">
# 						<a href="http://auction.51jingying.com/?5CC4CE=1011" target="_blank">&gt;&gt;&nbsp;更多</a>
# 					</div>
# 				</div>
# 				<div class="e gbox">
# 					<p class="btitle">最热行业招聘</p>
# 					<ul class="nlist">
# 												<li  class="tyd" ><span>1</span><a target="_blank" href="http://jobs.51job.com/hy01/">计算机软件</a></li>
# 												<li  class="tyd" ><span>2</span><a target="_blank" href="http://jobs.51job.com/hy32/">互联网/电子商务</a></li>
# 												<li  class="tyd" ><span>3</span><a target="_blank" href="http://jobs.51job.com/hy05/">快速消费品(食品、饮料、化妆品)</a></li>
# 												<li ><span>4</span><a target="_blank" href="http://jobs.51job.com/hy53/">酒店/旅游</a></li>
# 												<li ><span>5</span><a target="_blank" href="http://jobs.51job.com/hy26/">房地产开发</a></li>
# 												<li ><span>6</span><a target="_blank" href="http://jobs.51job.com/hy03/">金融/投资/证券</a></li>
# 												<li ><span>7</span><a target="_blank" href="http://jobs.51job.com/hy41/">会计/审计</a></li>
# 												<li ><span>8</span><a target="_blank" href="http://jobs.51job.com/hy02/">电子技术/半导体/集成电路</a></li>
# 												<li ><span>9</span><a target="_blank" href="http://jobs.51job.com/hy46/">医疗/护理/卫生</a></li>
# 												<li ><span>10</span><a target="_blank" href="http://jobs.51job.com/hy08/">制药/生物工程</a></li>
# 												<li ><span>11</span><a target="_blank" href="http://jobs.51job.com/hy14/">机械/设备/重工</a></li>
# 												<li ><span>12</span><a target="_blank" href="http://jobs.51job.com/hy04/">贸易/进出口</a></li>
# 												<li ><span>13</span><a target="_blank" href="http://jobs.51job.com/hy06/">服装/纺织/皮革</a></li>
# 												<li ><span>14</span><a target="_blank" href="http://jobs.51job.com/hy23/">教育/培训/院校</a></li>
# 												<li ><span>15</span><a target="_blank" href="http://jobs.51job.com/hy18/">法律</a></li>
# 												<li ><span>16</span><a target="_blank" href="http://jobs.51job.com/hy11/">餐饮业</a></li>
# 												<li ><span>17</span><a target="_blank" href="http://jobs.51job.com/hy21/">交通/运输/物流</a></li>
# 												<li ><span>18</span><a target="_blank" href="http://jobs.51job.com/hy22/">批发/零售</a></li>
# 												<li ><span>19</span><a target="_blank" href="http://jobs.51job.com/hy42/">银行</a></li>
# 												<li ><span>20</span><a target="_blank" href="http://jobs.51job.com/hy12/">广告</a></li>
# 												<li ><span>21</span><a target="_blank" href="http://jobs.51job.com/hy09/">建筑/建材/工程</a></li>
# 												<li ><span>22</span><a target="_blank" href="http://jobs.51job.com/hy54/">美容/保健</a></li>
# 												<li ><span>23</span><a target="_blank" href="http://jobs.51job.com/hy19/">石油/化工/矿产/地质</a></li>
# 												<li ><span>24</span><a target="_blank" href="http://jobs.51job.com/hy36/">电气/电力/水利</a></li>
# 												<li ><span>25</span><a target="_blank" href="http://jobs.51job.com/hy29/">农/林/牧/渔</a></li>
# 												<li ><span>26</span><a target="_blank" href="http://jobs.51job.com/hy28/">政府/公共事业</a></li>
# 												<li ><span>27</span><a target="_blank" href="http://jobs.51job.com/hy48/">公关/市场推广/会展</a></li>
# 												<li ><span>28</span><a target="_blank" href="http://jobs.51job.com/hy49/">影视/媒体/艺术/文化传播</a></li>
# 												<li ><span>29</span><a target="_blank" href="http://jobs.51job.com/hy37/">计算机硬件</a></li>
# 												<li ><span>30</span><a target="_blank" href="http://jobs.51job.com/hy51/">物业管理/商业中心</a></li>
# 											</ul>
# 				</div>
#
# 				<div class="e gbox">
# 					<p class="btitle">职场资讯</p>
# 					<p class="hflist">
# 						<span><a target="_blank" href="http://jianli.51job.com/">简历指导</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0503.html">职场气象</a></span>
# 						<span><a target="_blank" href="http://www.51job.com/careerpost/tiaocao/mianshi.php">面试技巧</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0502.html">劳动法苑</a></span>
# 						<span><a target="_blank" href="http://www.51job.com/careerpost/tiaocao/tiaocao.php">跳槽策略</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0505.html">无忧指数</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/99/index.html">无忧专题</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0504.html">职场话题</a></span>
# 						<span><a target="_blank" href="http://my.51job.com/bs/shalong/index.php">在线沙龙</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0506.html">个人加油站</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0501.html">无忧求职攻略</a></span>
# 						<span><a target="_blank" href="http://arts.51job.com/cls/class_0507.html">城市资讯</a></span>
# 						<span><a target="_blank" href="http://qiuzhixin.51job.com">求职信</a></span>
# 						<span><a target="_blank" href="http://qiuzhixin.51job.com/ziwopingjia/">自我评价</a></span>
# 					</p>
# 					<div class="hmore">
# 						<a target="_blank" href="http://www.51job.com/default_res.php">&gt;&gt;&nbsp;更多</a>
# 					</div>
# 				</div>
#
# 			</div>
#
# 			<div class="clear"></div>
# 		</div>
# 		<a href="#top" id="goTop">回到<br />顶部</a>
# 	</div>
# 	<script>
# 		$('.flst .l').hover(function(){
# 			$(this).addClass('on');
# 		},function(){
# 			$(this).removeClass('on');
# 		});
#
# 		$('.filter .up').live('click',function(){
# 			$(this).removeClass('up').addClass('down').html('更多').parent().find('.lkst').addClass('close');
# 		});
#
# 		$('.filter .down').live('click',function(){
# 			$(this).removeClass('down').addClass('up').html('收起').parent().find('.lkst').removeClass('close');
# 		});
# 	</script>
# 	<div class="footer">
#     <div class="in">
#         <div class="nag">
#             <div class="e e_first">
#                 <label>销售热线：</label>400-886-0051&nbsp;&nbsp;027-87810888<br>
#                 <label>客服热线：</label>400-620-5100<br>
#                 400-820-5100<br>
#                 <label>Email：</label><a href="mailto:club@51job.com">club@51job.com</a>（个人）<br>
#                 <a href="mailto:hr@51job.com">hr@51job.com</a>（企业）
#             </div>
#             <div class="e">
#                 <strong>简介</strong><br>
#                 <a href="http://www.51job.com/bo/AboutUs.php" target="_blank">关于我们</a><br>
#                 <a href="http://www.51job.com/bo/service.php" target="_blank">服务声明</a><br>
#                 <a href="http://www.51job.com/bo/media/media.php" target="_blank">媒体报道</a><br>
#                 <a href="http://ir.51job.com/" target="_blank">Investor Relations</a>
#             </div>
#             <div class="e">
#                 <strong>合作</strong><br>
#                 <a href="http://www.51job.com/bo/jobs/new_joinus.php" target="_blank">加入我们</a><br>
#                 <a href="http://www.51job.com/bo/contact.php" target="_blank">联系我们</a><br>
#                 <a href="http://www.51job.com/link.php" target="_blank">友情链接</a>
#             </div>
#             <div class="e">
#                 <strong>帮助</strong><br>
#                 <a href="http://www.51job.com/help/help.htm" target="_blank">帮助中心</a><br>
#                 <a href="http://www.51job.com/help/help.htm" target="_blank">常见问题</a><br>
#                 <a href="http://www.51job.com/help/help.htm" target="_blank">新手引导</a>
#             </div>
#             <div class="e">
#                 <strong>导航</strong><br>
#                 <a href="http://www.51job.com/bo/sitemap.php" target="_blank">网站地图</a><br>
#                 <a href="http://search.51job.com/jobsearch/search_result.php" target="_blank">职位搜索</a><br>
#                 <a href="http://my.51job.com/cv/CResume/CV_CResumeManage.php" target="_blank">简历中心</a>
#             </div>
#             <div class="code c_first">
#                 <img width="80" height="80" src="http://img01.51jobcdn.com/im/2016/code/app_download.png" alt="APP下载">
#                 <span><a href="http://www.51job.com/pm/app/index.html">APP下载</a></span>
#             </div>
#             <div class="code">
#                 <img width="80" height="80" src="http://img01.51jobcdn.com/im/2016/code/weixin.png" alt="官方微信">
#                 <span>官方微信</span>
#             </div>
#             <div class="clear"></div>
#         </div>
# 		<p class="note">
# 			<span>未经51job同意，不得转载本网站之所有招聘信息及作品 | 无忧工作网版权所有&copy;1999-2017</span>
# 		</p>
#     </div>
# </div>
# </body>
# </html>
#
# 			<script language='javascript'>
# 			<!--
# 				window.cfg = {
# 					fileName: '' ,
# 					lang : 'c' ,
# 					stype : '' ,
# 					fullLang : 'Chinese' ,
# 					langs : {
# 						sqzwml : 'applyjob' ,
# 						qzzwqdg : '请在要选择的职位前打勾!' ,
# 						myml : 'my' ,
# 						ts_qxjzw : '请选择职位' ,
# 						queren : '确认' ,
# 						guanbi : '关闭' ,
# 						nzdnxj : '您最多能选择' ,
# 						xiang : '项' ,
# 						xzdq : '选择地区' ,
# 						xj_xg : '选择/修改' ,
# 						zycs : '主要城市' ,
# 						sysf : '所有省份' ,
# 						tspd : '特殊频道' ,
# 						buxian : '不限' ,
# 						qingxj : '请选择' ,
# 						yixuan : '已选' ,
# 						znlb : '职能类别' ,
# 						hylb : '行业类别' ,
# 						gzdd : '工作地点' ,
# 						quanbu : '全部' ,
# 						zhineng : '职能' ,
# 						hangye : '行业' ,
# 						didian : '地点' ,
# 						qsrgjz : '请输入关键字' ,
# 						srpcgjz : '输入排除关键字'
# 					} ,
# 					url : {
# 						root : 'http://search.51job.com/jobsearch' ,
# 						image : 'http://img01.51jobcdn.com/im/2009' ,
# 						image_search : 'http://img01.51jobcdn.com/im/2009/search' ,
# 						image_search_lang : 'http://img01.51jobcdn.com/im/2009/search/c' ,
# 						image_search_c : 'http://img01.51jobcdn.com/im/2009/search/c' ,
# 						image_search_e : 'http://img01.51jobcdn.com/im/2009/search/e'
# 					} ,
# 					domain : {
# 						my : 'http://my.51job.com' ,
# 			            my_ssl : 'https://mylogin.51job.com',
# 						search : 'http://search.51job.com'
# 					} ,
# 					isJobview : '1' ,
# 					isAcStatRecJob : '1' ,
# 					acStatRecJobType : '0803111457',
# 					isSearchDomain : '1'
# 				};
#
# 				function searchInit() {
# 					if ( window.Search ) {
# 						clearInterval( intVal );
# 						window.zzSearch = new Search( {
# 							searchForm : document.searchForm ,
# 							pageForm : document.pageForm ,
# 							excludeForm : document.excludeForm ,
# 							pageJumpForm : document.pageJumpForm ,
# 							selJobPageForm : document.selJobPageForm ,
# 							cfg : cfg
# 						} );
# 						}
# 				}
# 				var intVal = window.setInterval( searchInit , 50 );
# 				//-->
# 			</script>
# '''
#
# Selector = etree.HTML(htmldoc)
#
# num = 0
#
# for con in  Selector.xpath('//div[@class="detlist gbox"]/div[@class="e"]'):
#     num = num + 1
#     jobname = con.xpath('p[1]/span[1]/a[1]/text()')[0]
# # jobname = Selector.xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/p[1]/span[1]/a/text()')[0]
#     company = con.xpath('p[1]/a[@class="name"]/text()')[0]
#     location = con.xpath('p[1]/span[@class="location name"]/text()')[0]
#     salary = con.xpath('p[1]/span[@class="location"]/text()')[0]
#     degree = con.xpath('p[2]/text()')[0].replace('\n','').replace(' ','')
#     exprience = con.xpath('p[2]/text()')[1].replace('\n','').replace(' ','')
#     nature = con.xpath('p[2]/text()')[2].replace('\n','').replace(' ','')
#     scale = con.xpath('p[2]/text()')[3].replace('\n','').replace(' ','')
#     askandduty = con.xpath('p[3]/text()')[0]
#
# print jobname,company,location,salary,degree,exprience,nature,scale,'\n',askandduty
#
# print type(location)
#
# #
# #     print con,"\n","000000000000000000000000000000000000","\n\n\n\n"
# #
# # print "[[[[[[[[[[[[[[[[[[[[[[[[[[---------",num,"----------]]]]]]]]]]]]]]]]]]]"
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
