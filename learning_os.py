import os
import subprocess

print(os.getcwd())
print(os.listdir(os.getcwd()))

try:
    newPath = os.getcwd() + "\practice"
    os.mkdir(newPath)
except FileExistsError:
    pass    

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)