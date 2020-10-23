# Python cli calculator authored by Adam Hamilton-Sutherland

#Functions=================================================
#Help function---------------------------------------------
def help():
    print()
    print("----------------")
    print("* ==Commands:")
    print("* help - Shows help message")
    print("* quit - Quits calculator")
    print("* add - Adds 2 or more space separated integers together")
    print("* sub - Subtracts 2 or more space seperated integers from left to right")
    print("* mul - Multiplies 2 or more space seperated integers from left to right")
    print("* div - Divides 2 or more space seperated integers from left to right")
    print("*")
    print("* ==Keywords")
    print("* prev - The last computed value")
    print("*")
    print("* ==Examples")
    print("* calc~ add 12 8")
    print("* 20")
    print("* calc~ add prev 10")
    print("* 30")
    print("*")
    print("* calc~ sub 12 8")
    print("* 4")
    print("* calc~ sub prev 10")
    print("* -6")
    print("----------------")
    print()

#Main calculator function----------------------------------
def calc():
    #Flag to exit calculator
    stop = False

    #Var that holds result of previous command
    prev = None

    while stop == False:
        #Get input from user
        raw_input = input("calc~ ")

        #Parse raw input into a list
        input_list = raw_input.strip().split(' ')

        #Store command
        cmd = input_list[0]

        #Create list of args
        args = input_list[1:]

        #Expand parameters and create numbers lists
        numbers = []
        
        #Wrapped in a try, except block to catch all invalid input
        try:
            #Loop over arguments
            for el in args:
                #Expand prev
                if el == "prev":
                    if prev != None:
                        numbers.append(prev)
                    #If prev is empty just skip it
                    else:
                        continue
                #Otherwise add number to numbers list
                else:
                    numbers.append(float(el))
        except:
            #If the attempted operation failed, print error message
            print("ERROR: Invalid Argument(s)")
            continue
        
        #Quit calc command
        if cmd == "quit" or cmd == "q":
            stop = True
            break

        #Help command
        elif cmd == "help" or cmd == "h":
            help()

        #Previous command
        elif cmd == "prev":
            print(prev)

        #Add command
        elif cmd == "add":
            sum = numbers[0]

            #Add up all numbers
            for i in range(1, len(numbers)):
                sum += numbers[i]

            #Cast to int if possible
            if sum == int(sum):
                sum = int(sum)
            
            #Print and store sum
            prev = sum
            print(f"= {sum}")

        #Subtract command
        elif cmd == "sub":
            diff = numbers[0]

            #Subtract all the numbers
            for i in range(1, len(numbers)):
                diff -= numbers[i]

            #Cast to int if possible
            if diff == int(diff):
                diff = int(diff)

            #Print and store diff
            prev = diff
            print(f"= {diff}")

        #Multiply command
        elif cmd == "mul":
            result = numbers[0]

            #Multiply all the numbers
            for i in range(1, len(numbers)):
                result = result * numbers[i]

            #Cast to int if possible
            if result == int(result):
                result = int(result)

            #Print and store diff
            prev = result
            print(f"= {result}")

        #Divide command
        elif cmd == "div":
            quot = numbers[0]

            #Divide all the numbers
            for i in range(1, len(numbers)):
                if numbers[i] != 0:
                    quot = quot / numbers[i]
                else:
                    print("ERROR. Can't divide by 0. Skipping operation.")

            #Cast to int if possible
            if quot == int(quot):
                quot = int(quot)

            #Print and store diff
            prev = quot
            print(f"= {quot}")    

        #Unknown command
        else:
            print("Unknown Command")
           
#Calculator================================================
#First print greeting
print()
print("______      _   _                   _____  _     _____   _____       _            _       _             ")
print("| ___ \    | | | |                 /  __ \| |   |_   _| /  __ \     | |          | |     | |            ")
print("| |_/ /   _| |_| |__   ___  _ __   | /  \/| |     | |   | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ ")
print("|  __/ | | | __| '_ \ / _ \| '_ \  | |    | |     | |   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
print("| |  | |_| | |_| | | | (_) | | | | | \__/\| |_____| |_  | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   ")
print("\_|   \__, |\__|_| |_|\___/|_| |_|  \____/\_____/\___/   \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
print("       __/ |                                                                                            ")
print("      |___/                                                                                             ")
print()

#Print help message
print("Enter 'help' for instructions")
print()

#Start the calculator
calc()
