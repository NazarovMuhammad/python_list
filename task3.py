my_list = input().split()
min = 9999999
for i in my_list:
    numbers = i
    int_numbers = int(numbers)
    if int_numbers%2 != 0: 
          possitive_numbers = int(int_numbers)
    elif int_numbers%2==0 :
        print(0)
        break
    if possitive_numbers < min:
       min = possitive_numbers
       print(min)
       break