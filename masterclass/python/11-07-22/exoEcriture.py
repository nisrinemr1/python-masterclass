firstname = input("Name : ")
lastname = input("Last name : ")
age = input("Age : ")

data_file = open("data.txt", "w")
data_file.write(firstname + "\n" + lastname + "\n" + age)
data_file.close

data_file = open("data.txt")
data = data_file.read()
print(data)
data_file.close()