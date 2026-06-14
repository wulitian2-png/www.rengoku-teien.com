<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head><meta charset="utf-8"/>
<meta content="text/html; charset=utf-8" http-equiv="content-type"/>
<meta content="text/javascript" http-equiv="content-script-type"/>
<meta content="text/css" http-equiv="content-style-type"/>
<meta content="no-cache" http-equiv="Pragma"/>
<meta content="no-cache" http-equiv="Cache-Control"/>
<meta content="Mon, 1 Jan 1990 01:01:01 GMT" http-equiv="Expires"/>
<meta content="0" http-equiv="Expires"/>
<style type="text/css">
<!--
body,tr,td,th { font-size:13px; font-family:"MS UI Gothic, Osaka, ＭＳ Ｐゴシック"; }
a:link    { text-decoration:none; }
a:visited { text-decoration:none; }
a:active  { text-decoration:none; }
a:hover {
	text-decoration: underline;
	color: #FF6600;
}
.num          { font-family:Verdana,Helvetica,Arial; }
.obi          { background-color:#000000; color:#ffffff; }
.topdisp { display: none; }
-->
</style>
<script type="text/javascript">
 //
function address(){
user_name=address.arguments[0] + "@" + address.arguments[1];
document.write(user_name.link("mailto:" + address.arguments[0] + "@" + address.arguments[1]));
}
function fcheck(){
document.write(fcheck.arguments[1] + fcheck.arguments[2] + fcheck.arguments[0] + fcheck.arguments[3]);
}

</script>
<title>煉獄板</title></head>
<body alink="#FF6600" bgcolor="#000000" link="#FF6600" text="#ffffff" vlink="#FF6600">
<br/>
<b class="topdisp" style="font-size:24px; color:#ff0000; background-color:#ffffff; text-align: center;">このフォームからは投稿できません。</b>
<form action="./wforum.cgi" class="topdisp" method="POST">
<input class="topdisp" name="mode" type="hidden" value="wana"/>
<table class="topdisp"><tr class="topdisp"><td class="topdisp">name</td>
<td class="topdisp"><input class="topdisp" name="name" size="28" type="text" value=""/></td></tr>
<tr class="topdisp"><td class="topdisp">e-mail</td>
<td class="topdisp"><input class="topdisp" name="email" size="28" type="text" value=""/></td></tr>
<tr class="topdisp"><td class="topdisp">url</td>
<td class="topdisp"><input class="topdisp" name="url" size="36" type="text" value=""/></td></tr>
<tr class="topdisp"><td class="topdisp">subject</td>
<td class="topdisp"><input class="topdisp" name="subject" size="36" type="text" value=""/></td></tr>
<tr class="topdisp"><td class="topdisp">comment</td>
<td class="topdisp"><textarea class="topdisp" cols="56" name="comment" rows="7" wrap="soft"></textarea></td></tr>
<tr class="topdisp"><td class="topdisp" colspan="2">
<input class="topdisp" type="submit" value="Write"/>
<input class="topdisp" type="reset" value="Reset"/>
</td></tr></table>
</form>
<div align="left">
<input class="post" onclick='window.open("http://www.rengoku-teien.com/","_top")' type="button" value="<< TOP"/>
</div>
<br/>
<div align="center">
<h2>掲示板の利用がないため閉鎖中です。管理者までお問い合わせ下さい。</h2>
<p>
</p><form action="./admin.cgi" method="post">
<input name="mode" type="hidden" value="admin"/>
管理PASS: <input name="pass" size="12" type="password"/>
<input type="submit" value=" 認証 "/></form>
<script type="text/javascript">
//
self.document.forms[0].pass.focus();

</script>
</div>
</body>
</html>
