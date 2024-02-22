with open('file.txt','r') as reader:
    content = reader.readlines() #[reading lines]
    reversed(content)
    with open('file.txt' ,'w') as writer:
        for line in reversed(content):
            writer.write(line)


 #read the file and store all the lines in file
 #reverse the list
 #write the list back to the file