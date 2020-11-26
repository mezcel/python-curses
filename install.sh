#!/bin/bash

## Install dependencies using Apt or Pacman

## Check if Apt is installed
command -v apt &>/dev/null
isApt=$?

## Check if Pacman is installed
command -v pacman &>/dev/null
isPacman=$?

## Install Python
if [ $isApt -eq 0 ]; then
    ## Linux package
    sudo apt-get install python-pip python3 python3-pip

    ## python package
    pip install term
elif [ $isPacman -eq 0 ]; then
    ## Linux package
    sudo pacman -S --needed python python2

    ## python package
    pip install term
fi

## Check if Python is installed
command -v python &>/dev/null
isPy=$?

## Install PIP Python package manager
if [ $isPy -eq 0 ]; then
    ## Linux package
    sudo pacman -S --needed python python2

    ## python package
    pip install term
fi

