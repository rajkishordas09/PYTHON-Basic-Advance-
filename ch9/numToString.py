from num2words import num2words

def integer_to_words(num):
    return num2words(num, to='cardinal')

# Read integer from file
with open('file1.txt', 'r') as file:
    num = int(file.readline().strip())

num_words = integer_to_words(num)

with open('file1.txt', 'a') as file:
    #copy on file
   # file.write(f"{num} {num_words}\n")
    
 print(f"Converted and written to file: {num} => {num_words}")
