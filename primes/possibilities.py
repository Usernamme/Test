possibilities = [x for x in range(8, 10**6) if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0]
my_file = open("possibilities.txt", "r+")
for data in possibilities:
    my_file.write("%s\n" % str(data))
my_file.close()

#requires possibilities.txt in the same folder
