#Exercise 1: Hello World 
print("Hello world\n"*4)

#Exercise 2: Some Math
 
print((99**3)*8)

#Exercise 3: What is the output?
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False      
print("3" > 3) #Error
print("Hello" == "hello") #False

#Exercise 4: Your Computer Brand

computer_brand = "DELL"
print(computer_brand)

#Exercise 5: Your Information
name = "Ouanko"
age = 27
shoe_size = 43
info = ("My name is " + name + " and I have " + str(age) + " years old. My shoe size is " + str(shoe_size))
print(info)

#Exercise 6: A & B
a = 7
b = 3
if a > b:
    print("Hello World")

#Exercise 7: Odd or Even
print("Enter a number: ")

number = int(input())
if number % 2 == 0:
    print("The number is even") 
else:    print("The number is odd") 

# Exercise 8: What’s your name?
print("What is your name?")
name = input()
if name == "justin" or name == "ouanko":
    print("Hello " + name + " we have the same name!")
else:    print("Hello " + name + " nice to meet you!")  

# Exercise 9: Tall enough to ride a roller coaster
print("What is your height in cm?")
height = int(input())
if height > 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("You need to grow some more to ride the roller coaster.")        



