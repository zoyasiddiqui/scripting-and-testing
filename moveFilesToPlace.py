import os
import subprocess

def moveToPython():
    curPath = os.path.dirname(__file__)
    path = os.path.join(curPath, 'python-scripts')
    ls_process = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
    awk_process = subprocess.Popen(['awk','{print $9}'], stdin=ls_process.stdout, stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(['grep', '.py'], stdin=awk_process.stdout, stdout=subprocess.PIPE, text=True)
    
    for file in grep_process.stdout:
        file = file.strip()
        
        if file != None:
            oldPath = os.path.join(curPath, file)
            newPath = os.path.join(path, file)
            mv_process = subprocess.Popen(['mv',oldPath,newPath])

def moveToBash():
    curPath = os.path.dirname(__file__)
    path = os.path.join(curPath, 'bash-scripts')
    ls_process = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
    awk_process = subprocess.Popen(['awk','{print $9}'], stdin=ls_process.stdout, stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(['grep', '.sh'], stdin=awk_process.stdout, stdout=subprocess.PIPE, text=True)
    
    for file in grep_process.stdout:
        print(file)
        file = file.strip()
        
        if file != None and file.endswith(".sh"):
            oldPath = os.path.join(curPath, file)
            newPath = os.path.join(path, file)
            mv_process = subprocess.Popen(['mv',oldPath,newPath])

if __name__ == "__main__":
    inputStr = "Python or Bash? (1 or 2): "
    choice = int(input(inputStr))
    
    if choice == 1:
        moveToPython()
    elif choice == 2:
        moveToBash()
    else:
        print("try again")