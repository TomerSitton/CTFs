#!/bin/bash

PASS='goodday'

USERS=('root' 'daemon' 'bin' 'sys' 'sync' 'games' 'man' 'lp' 'mail' 'news' 'uucp' 'proxy' 'www-data' 'backup' 'list' 'irc' 'gnats' 'nobody' 'libuuid' 'syslog' 'mysql' 'sshd' 'landscape' 'dan')

for user in ${USERS[@]}; do
	echo $user
	echo $PASS | bash -c 'su $user'
done





