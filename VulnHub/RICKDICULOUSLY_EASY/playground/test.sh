#!/bin/bash


band=("The" "Flash" "Curtains")


i="i"
a="a"
b="b"

echo $i$a$b | su weaker -c "echo password is $i$a$b > /tmp/GreatSuccess"
i="we"
a="a"
b="ker"
echo $i$a$b | su weaker -c "echo password is $i$a$b > /tmp/GreatSuccess"

