# write to a file
# f = open("funny.txt", "w")
# f.write("I am monkey d luffy.")
# f.close()

# append to a file
# f = open("funny.txt", "a")
# f.write("\nKaizok ne ore wa naru.")
# f.close()

# read file
# f = open("funny.txt", "r")
# f_out = open("funny_wc.txt", "w")
# Read the whole file
# print(f.read())

# read line by line
# for line in f:
#     tokens = line.split(" ")
#     f_out.write("Wordcount: " + str(len(tokens)) + " " + line)

# f.close()
# f_out.close()

# auto closed the file
with open("funny.txt", "r") as f:
    print(f.read())
