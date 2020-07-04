#!/bin/bash



# opens matlab style python interactive mode
function pylab() {
  python3 -i ./imports.py
}


# opens jupyter notebook
function junote() {
 if [[ $1 = "-d" ]]; then
	conda config --set changeps1 False
 	osascript -e 'tell application "Terminal" to close first window' & exit
 else 
 	conda config --set changeps1 True
 	exec jupyter notebook /Users/henrikabrahamsson/Programming/"Summer Python Course"
 fi

}


# echoes 'polo'
function marco() {
 echo 'polo'
}



# runs note writing script
function note() {
 if [[ $1 = "-r" ]]; then
	python3 ./noteread.py
 else 
 if [[ $1 = "-w" ]]; then
	python3 ./notewrite.py
 fi
 fi

}

