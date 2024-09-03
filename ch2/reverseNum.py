def reverse_integer(num):

    num_str = str(num)
    reversed_str = num_str[::-1]

    
    reversed_num = int(reversed_str)

    return reversed_num

num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(f"Reversed integer: {reversed_num}")


# def reverse_number(number):
#   reversed_number = 0
#   while number > 0:
#     reversed_number = reversed_number * 10 + number % 10
#     number //= 10
#   return reversed_number


# number = 1234
# reversed_number = reverse_number(number)
# print(reversed_number)
