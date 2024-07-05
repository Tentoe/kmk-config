#!/usr/bin/env bash


KEYBOARD_PATH="/run/media/$USER/CIRCUITPY"



if [ ! -d $KEYBOARD_PATH ]; then
    echo "keyboard drive not found"
    exit
fi

cp -v ./*.py $KEYBOARD_PATH 

echo "keyboard config updated"
