menu = ("Enter Options: \n 1- Entry from gate. 2-Exit from gate.")
print(menu)
menu = int(input("Select Options: "))
idNo = ['1', '2', '3', '4', '5']
name = ['Aqib', 'Muneeb', 'Waqas', 'Zain', 'Saqib']

password = "cantt@123"

sum = 0

if menu == 1:
    pas = input("Enter Details:\n Enter Password first: ")
    # print(person)
    if pas == password:
        print("Correct Password")
    else:
        print("Wrong Password or Enter again")
        
    
elif menu == 2:
    print("Goodbye!")
    
    
user = input("Enter Your Name:\n")
for i in range(0, 5):
    # print(name[i])
    
    if user == name[i]:
        sum+= 1

if sum == 1:
    print("correct name")
        
elif sum == 0:
        
    print("incorret")
        
            
what = input("Enter id number:\n")

for i in range(0, 5):
    # print(idNo[i])
    if what == idNo[i]:
        sum += 1
        
if sum == 1:
    print("correct id")
    
elif sum == 0:
    print("Incorrect id")
    
print("Welcome to islamabad cantt")
    



        