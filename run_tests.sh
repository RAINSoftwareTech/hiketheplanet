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

function flake8_test(){
    echo "flake8 --exclude='*zjunk/*' ../hiketheplanet/"
    flake8 --exclude='*zjunk/*' ../hiketheplanet/
}

function loop_tests(){
    echo "Press Enter to continue, Ctrl+c to quit or 'r' to repeat last test >> "
    read test_char
    while [[ $test_char == "r" ]]; do
        coverage_test $1
        loop_tests $1
    done
}

function loop_flake8(){
    flake8_test
    echo "Would you like to repeat the pep8 check? (y/n)"
    read pep_char
    while [[ $pep_char == "y" ]]; do
        flake8_test
    done
}

function test_all_apps(){
    for i in "${hiking_apps[@]}"
        do
            coverage_test $i
            loop_tests $i
        done
}

function check_app_name(){
    for i in "${hiking_apps[@]}"
        do
            if [[ $1 == $i ]]
            then
                valid=1
                break
            fi
            valid=0
        done
}

function which_test(){
    echo "Type in the name of the app you would like to test or 'all' to test all apps >> "
    read word
    if [[ $word == "all" ]]
    then
        test_all_apps
    else
        check_app_name $word
        if [[ $valid == 1 ]]
        then
           coverage_test $word
           loop_tests $word
        else
            echo "$word is not a valid app. Please check your spelling and try again. (note: app name should be all lower case)"
            which_test
        fi
    fi
}

function ask_tests_loop(){
    echo "Would you like to run another test? (y/n)"
    read character
    while [[ $character == "y" ]]; do
        which_test
        ask_tests_loop
    done
}

function run_tests(){
    find . -type f -name '*.pyc' -delete
    which_test
    ask_tests_loop
    loop_flake8
}


run_tests

