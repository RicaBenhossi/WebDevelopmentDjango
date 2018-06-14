import os

ConnectPath = os.path.abspath(os.getcwd()) + '\DBConnect'
print(ConnectPath)
if (os.path.exists(ConnectPath)):
    if (os.path. file.exists('dbconnection.json')):
        print('Conection file exists.')
    else:
        print('Conection file does not exist. It will be create.')
else:
    os.mkdir(ConnectPath)
    os.chdir(ConnectPath)
    open('dbconnection.json', 'w')
