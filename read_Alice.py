filename = "C:\\Users\\FLAG\\Desktop\\Alice's Adventures in Wonderland.txt"

try:
    with open(filename, 'r') as obj_f:
        words = obj_f.read().split()
        print("The count of words in the '" + filename.split("\\")[-1] + "' is %d" % len(words))
except FileNotFoundError:
    msg = "Sorry, the file '" + filename.split("\\")[-1] + "' does not exist."
    print(msg)
