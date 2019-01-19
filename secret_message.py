import os

def rename_files():
    file_list = os.listdir(r"C:\Users\HP\Desktop\Coding\Projects\Udacity_U36\prank")
    #print (file_list)
    saved_path = os.getcwd()
    print ("Current working directory is " + saved_path)
    os.chdir(r"C:\Users\HP\Desktop\Coding\Projects\Udacity_U36\prank")
    for file_name in file_list:
        print ("Old Name - " + file_name)
        print ("New Name - " + file_name.translate({ord(c):'' for c in "1234567890"}))
        os.rename(file_name, file_name.translate({ord(c):'' for c in "1234567890"}))
    os.chdir(saved_path)

#os.rename(old_name, new_name)
#os.getcwd() cwd means current working directory
# os means operating system


rename_files()