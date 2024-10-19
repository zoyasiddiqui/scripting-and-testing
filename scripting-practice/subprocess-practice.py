import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command Output:")
        print(result.stdout)
    else:
        print("Error:")
        print(result.stderr)
        
if __name__ == "__main__":
    command = ['ls', '-l']  
    run_command(command)
