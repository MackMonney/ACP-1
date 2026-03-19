#write in file using with() function
with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am Christopher and I am 20 year old")
file.close()

#split file into words
with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this files are....")
    for line in data:
        word = line.split()
        print(word)
file.close()

#check if a file exists
import os
print("Checking if my_file exists or not")
if os.path.exists("my file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

#create a new file if it doesn't 
my_file = open("my_file.txt", "w")
my_file.write("Hi I am Christopher and I am 20 year old")
my_file.close()

#delete file named codingal.txt
os.remove('codingal.txt')

my_file.close()