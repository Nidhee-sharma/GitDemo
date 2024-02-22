file = open('file.txt')

#print(file.read(5)) #read all the content of file
#read nu number of characters by passing parameter

#print(file.readline()) #read one single lines at a time readline()
#print(file.readline())
#print(file.readlines())
line =file.readline()
#while line!= "":
 #   print(line)
  #  line =file.readline()
#print liny by line

for line in file.readlines():
    print(line)

file.close()