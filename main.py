# email = "admin@gmail.com"
# password = "admin123"

# input_email = input("Enter your email")
# input_password = input("Enter your password")

# if email == input_email  and password == input_password:
#     print("Login Success")
# else:
#     print("Invalid Email or Password")
    
# # guess the number

# numbers = ["1","2"]
# guess = input("Guess a number : ")
# if guess == numbers[0] or guess == numbers[1] :
#     print("You guessed it")


# while 


# a = 0

# while a < 10:
#     print(a)
#     a += 1


# # examples of while usage
# ages = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < 6:
#     print(ages[i])
#     i += 1

# z = 0
# while z < 6:
#     if ages[z]>=3 :
#         print("this is a child not a baby")
#     z += 1


students = [
    {"age": 20, "grade": 90},
    {"age": 22, "grade": 85},
    {"age": 21, "grade": 95},
    {"age": 20, "grade": 80}
]

i = 0
while i < len(students) :
    student = students[i]
    if student['age'] > 20 :
        print(f"welcome {student['grade']}")
    else :
        print(f"not welcome, {student['grade']}")
    i += 1


# Exercises 
# 1. Write a while loop that prints the numbers from 1 to 10.
# 2. Write a while loop that prints the numbers from 10 to 1.
# 3. Write a while loop that prints the numbers from 1 to 10, but
# skips the number 5.
# 4. Write a while loop that prints the numbers from 1 to 10, but
# stops when it reaches the number 5.
# 5. Write a loop that prints unpair numbers from 1 to 20

# a = 1
# while a <= 10 :
#     print(a)
#     a += 1

# b = 10
# while b>=1:
#     print(b)
#     b -= 1

# c = 1
# while c<= 10:
#     if c != 5 :
#         print(c)
#     c += 1

# c= 1
# while c <= 10 :
#     if c == 5 :
#         c += 1
#         continue
#     print(c)
#     c += 1

# d= 1
# while d <= 10 :
#     if d == 6 :
#         break
#     print(d)
#     d += 1

# e = 1
# while e<21:
#     print(e)
#     e += 2
# e = 0
# while e< 21:
#     if e%2 != 0:
#         print(e)
#     e += 1 


# 0 1 1 2 3 5 8 13 21
i = 0
numbers = [0, 1]
while i < 100:
    new_number = numbers[i] + numbers[i+1]
    numbers.append(new_number)
    i += 1

print(numbers)