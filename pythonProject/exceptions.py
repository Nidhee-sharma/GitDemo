ItemInCart = 0

if ItemInCart !=2:  # raise Exception("kkkk")
    pass
assert (ItemInCart == 0)

#try catch
#with open('filea.txt', 'r') as reader:
   # reader.read()

try:
    with open('file.txt', 'r') as reader:
        reader.read()


except:
    print("somehow i reached this block because there is failure in try block")


try:
    with open('filea.txt', 'r') as reader:
        reader.read()


except Exception as e:
    print(e)

finally:
    print("cleaning up resources")