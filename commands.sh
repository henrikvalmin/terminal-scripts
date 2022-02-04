#!/bin/bash

# initializes a git repo and pushes it
function gitIT() {
  git init -b main
  echo ".DS_Store" > .gitignore
  echo '#' $1 > README.md
  git add . && git commit -m "initial commit"
  gh repo create $1 --public 
  git push -u origin main
 
}

# opens matlab style python interactive mode
function pylab() {
  python3 -i ./Documents/terminal-scripts/pylab.py
}

function dmg() {
  python3 -i ./Documents/terminal-scripts/habitica_reqs.py
}


# opens jupyter notebook
function junote() {
 if [[ $1 = "-d" ]]; then
	conda config --set changeps1 False
 	osascript -e 'tell application "Terminal" to close first window' & exit
 else 
 	conda config --set changeps1 True
 	exec jupyter notebook ./Documents/Programming/"Database Course"
 	conda config --set changeps1 False
 fi

}


function dbproject() {
cd ./Documents/Programming/"Database Course"/"Database-project"
}

function krusty() {
 cd
 cd ./Documents/Programming/"Database Course"/"Database-project"
 sqlite3 krusty-db.sqlite < create-schema.sql 
 sqlite3 krusty-db.sqlite < initial-data.sql
 if [[ $1 = "-r" ]]; then
	python3 app.py
 else
	sqlite3 krusty-db.sqlite 
 fi
}


# echoes 'polo'
function marco() {
 echo 'polo'
}

function hack() {
 echo $1 'was hacked'
}


# runs note writing script
function note() {
 if [[ $1 = "-r" ]]; then
	python3 ./Documents/terminal-scripts/noteread.py
 else 
 if [[ $1 = "-w" ]]; then
	python3 ./Documents/terminal-scripts/notewrite.py
 fi
 fi

}

function marco2() {
	echo 'polo2'
}


function vijava() {
	echo "public class "
	vi $1.txt
}


# add a habitica todo
function habitica() {
	echo $1
	
	name=$1
	note=$2
	
	curl -X POST \
    -d "{
        'type': 'todo',
        'text': '$1,
		'notes': $2,
        }" \
    -H "Content-Type: application/json" \
    -H "x-api-user: 18733f50-7595-468b-a0e1-694d9534c7ea" \
    -H "x-api-key: bb64b369-64fd-400f-9566-72aea9f6fe63" \
    https://habitica.com/api/v3/tasks/user
}
