#open a file
file = open('Codingal.txt', 'r')
print(file.read)
file.close()

#print first 10 characters of the file
file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(10))
file.close()

#print the first line of the file
file = open('Codingal.txt', 'r')
print(file.readline())
file.close()

#print the first four lines of the file
file = open('Codingal.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#loop through the file and print each line
file = open('Codingal.txt', 'r')
for x in file:
    print(x)
file.close()