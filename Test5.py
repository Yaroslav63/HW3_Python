import random
def number_list(file):
    num = 8
    with open(file, 'w') as file_two:
        for i in range(num):
            file_two.write(str(random.randint(1, num-1))+ '\n')
    with open(file, 'r') as file_two:
        for i in file_two:
            print(str(int(i))+ ' ')
    return

def odd_numbers(file):
    odd_list = []
    with open(file, 'r') as file_two:
        for i in file_two:
            if int(i)%2 != 0: odd_list.append(str(i))
    with open(file, 'w') as file_two:
        for i in odd_list:
            print(str(int(i))+ ' ')
            file_two.write(str(i))
    return

number_list('numbers.txt')
odd_numbers('numbers.txt')