import os
import shutil

def copyFiles(path):
    backupPath = os.path.join(path, "backup")
    
    if os.path.exists(backupPath):
        shutil.rmtree(backupPath)
        
    os.mkdir(backupPath)
    
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            print(filename)
            srcPath = os.path.join(path, filename)
            dstPath = os.path.join(backupPath, filename)
            shutil.copyfile(srcPath, dstPath)

def deleteBackup(path):
    shutil.rmtree(os.path.join(path, "backup"))

if __name__ == "__main__":
    copyFiles(os.path.dirname(__file__))
    # deleteBackup(os.path.dirname(__file__))
