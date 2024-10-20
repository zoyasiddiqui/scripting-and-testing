#!/bin/bash

echo "Python or Bash? (1 or 2)"
read option

oldPath=$(pwd)
cd bash-scripts
bashPath=$(pwd)
cd ..
cd python-scripts
pythonPath=$(pwd)
cd ..

if [ $option -eq 1 ]
then
    touch pythonFiles.txt
    ls -l | awk '{print $9}' | grep .py > pythonFiles.txt
    
    for line in $(cat pythonFiles.txt)
    do
        mv "$oldPath/$line" "$pythonPath/$line"
    done

    rm pythonFiles.txt

elif [ $option -eq 2 ]
then
    touch bashFiles.txt
    ls -l | awk '{print $9}' | grep *.sh > bashFiles.txt

    for line in $(cat bashFiles.txt)
    do
        mv "$oldPath/$line" "$bashPath/$line"
    done

    rm bashFiles.txt

else
    echo "Try Again"
fi

exit 0