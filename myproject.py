import os
os.mkdir('files')
os.chdir('files')
for i in range(1,10):
  os.mkdir(str(i))
print(os.path.isfile('files/3/myfile.txt'))

print(os.getcwd())
os.chdir('files')
print(os.getcwd())
os.rmdir("7")
os.rmdir("8")
os.rmdir("9")
