my_list = input().split()
min = 9999999
for i in my_list:
    numbers = i
    int_numbers = int(numbers)
    if int_numbers > 0:
     possitive_numbers = int(int_numbers)
     if possitive_numbers < min:
       min = possitive_numbers
print(min)