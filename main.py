# Exercise 1
print("Exercise 1")
st_num_1 = "123"
num_1 = int(st_num_1)
print(num_1)

# Exercise 2
print("Exercise 2")
num_2 = 123
fl_num_1 = float(num_2)
print(fl_num_1)

# Exercise 3
print("Exercise 3")
fl_num_2 = 12.345
num_3 = int(fl_num_2)
print(num_3)

# Exercise 4
print("Exercise 4")
num_of_credit_card = str(input("Enter a num of credit card(16 numbers): "))
NUM_OF_CREDIT_CARD_SIZE = len(num_of_credit_card)
if NUM_OF_CREDIT_CARD_SIZE < 16:
    print("Error: invalid num of credit card!")
list_of_numCreditCard = list(num_of_credit_card)
list_of_numCreditCard.pop(12)
list_of_numCreditCard.pop(12)
list_of_numCreditCard.pop(12)
list_of_numCreditCard.pop(12)
for i in list(list_of_numCreditCard):
   print(i, end="")

# Exercise 5
print("\nExercise 5")
td_num = str(input("Enter a three-digit number: "))
first_number = td_num[0]
second_number = td_num[1]
third_number = td_num[2]
first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)
print("Sum of three digits of num: ", first_number + second_number + third_number)

# Exercise 6
print("Exercise 6")
side_1 = float(input("Enter the length of first side: "))
side_2 = float(input("Enter the length of second side: "))
side_3 = float(input("Enter the length of third side: "))
area = side_1 * side_2 * side_3
print("The area of triangle: ", area)

# Exercise 7
print("Exercise 7")
num = int(input("Enter num: "))
summ = 0
while num > 0:
    digit = num % 10
    summ = summ + digit
    num = num // 10
print("Sum of digits:", summ)

# Exercise 8
print("Exercise 8")
num_8 = int(input("Enter num: "))
num_8 = str(num_8)
size_of_num_8 = len(num_8)
print("The value of digits in this num: ", size_of_num_8)

# Exercise 9
print("Exercise 9")
n1 = input("Enter num: ")
n2 = n1[::-1]
print("Reverse num: ", n2)
