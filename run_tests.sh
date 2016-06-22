#!/bin/bash

hiking_apps=("equipment" "hazards" "hikers" "hikes" "reviews" "search" "sights" "core" "middleware" "mixins")

function pause(){
   read -p "Press Enter to continue testing or Ctrl+c to quit"
}


function coverage_test(){
    echo "coverage run --source=$1 --omit="*/migrations*" manage.py test $1.tests --Hiking.settings.tests"
    coverage run --source=$1 --omit="*/migrations*" manage.py test $1.tests --settings=Hiking.settings.tests
    coverage report -m
}

function loop_tests(){
    echo "Press Enter to continue to next test, Ctrl+c to quit or 'r' to repeat last test >> "
    read character
    while [[ $character == "r" ]]; do
        coverage_test $1
        loop_tests $1
    done
}

function run_tests(){
    find . -type f -name '*.pyc' -delete
    for i in "${hiking_apps[@]}"
        do
            coverage_test $i
            loop_tests $i
        done
    flake8 --exclude='*zjunk/*' ../hiketheplanet/
}


run_tests

