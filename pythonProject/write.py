#file =open('file.txt')

#file.close()
#read the file and stored all the lines in the list
#reverse the list
#write the list back to the file

with open('file.txt','r') as reader:
    content = reader.readlines()   #we have captured all the data
    reversed(content)
    with open('file.txt' ,'w') as writer:
        for line in reversed(content):
            writer.write(line)
