import subprocess
import os

def run_command(command):
    result = subprocess.run(command, capture_output=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command Output:")
        results = result.stdout.decode('utf-8').splitlines() 
        for r in results:
            print(r)
    else:
        print("Error:")
        print(result.stderr)
        
if __name__ == "__main__":
    os.chdir('..')
    command = ['ls', '-l']  
    run_command(command)
