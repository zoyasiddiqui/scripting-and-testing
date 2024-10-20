import os

def create_txt(filename, fileContents):
    
    curPath = os.path.dirname(__file__) 
    filenameTxt = os.path.join(curPath, filename + ".txt")  
    with open(filenameTxt, 'w') as file:
        file.write(fileContents)

def get_all_txt():
    curPath = os.path.dirname(__file__)  
    
    txtFiles = {}
    for filename in os.listdir(curPath):
        if filename.endswith(".txt"):
            file_path = os.path.join(curPath, filename)  
            with open(file_path, 'r') as file:
                contents = file.read()
                txtFiles[filename] = contents
    
    return txtFiles

def delete_all_txt():
    curPath = os.path.dirname(__file__)  
    
    for filename in os.listdir(curPath):
        if filename.endswith('.txt'):
            file_path = os.path.join(curPath, filename)  
            os.remove(file_path)
    
if __name__ == "__main__":
    create_txt("example1", "My name is Zoya.")
    create_txt("example2", "I have many apples.")
    create_txt("example3", "I like cats.")
    print(get_all_txt())
    delete_all_txt()
