#!/bin/bash

echo "Enter your name: "
read name
echo "Hi $name"

echo "Enter a number: "
read num

if [ $num -gt 5 ]
then
    echo "This number is greater than 5"
else
    echo "This number is less than 5"
fi

exit 0
