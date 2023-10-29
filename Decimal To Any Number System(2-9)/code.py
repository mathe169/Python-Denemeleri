
decimal_number = int(input("Decimal number: "))

number_system = int(input("Number system (2-9): "))

number = 0
power = 0
if(decimal_number < number_system):
    number  = decimal_number
else:
    for i in range(decimal_number,1,-1):
        while(i % number_system == 0):
            power += 1
            i /= number_system
        if(i == 1):
            break
        power = 0

    min_power_of_ten = 10**power
    number = min_power_of_ten

    if(number_system**power != decimal_number):    
        for i in range(number_system**power+1,decimal_number+1):
            if(int(str(number)[len(str(number))-1]) < number_system-1):
                number+=1
            else:
                lowest_number = number_system
                index = -1
                lowest_index = 0
                for i in str(number)[:len(str(number))-1]:
                    index += 1
                    if(int(i)<=lowest_number):
                        lowest_number = int(i)
                        lowest_index = index

                if(lowest_number != number_system-1):
                    list_number = list(str(number))
                    list_number[lowest_index] = str(int(list_number[lowest_index])+1)
                    for i in range(lowest_index+1,len(list_number)):
                        list_number[i] = "0"
                    number = int("".join(list_number))

                else:
                    break

print(number)