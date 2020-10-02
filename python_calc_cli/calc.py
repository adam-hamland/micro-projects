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
    print("* sub - subtracts 2 or more space seperated integers from left to right")
    print("*")
    print("* ==Keywords")
    print("* prev - the last computed value")
    print("*")
    print("* ==Exampled")
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
    #Flag to exit shell
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
        try:
            for el in args:
                #Expand prev
                if el == "prev":
                    if prev != None:
                        numbers.append(prev)
                    else:
                        continue
                #Else add number to numbers list
                else:
                    numbers.append(float(el))
        except:
            print("ERROR: Invalid Argument")
            continue
        
        #Quit calc command
        if cmd == "quit" or cmd == "q":
            stop = True
            break

        #Help calc command
        elif cmd == "help" or cmd == "h":
            help()

        #prev command
        elif cmd == "prev":
            print(prev)

        #Add command
        elif cmd == "add":
            sum = numbers[0]

            #add up all numbers
            for i in range(1, len(numbers)):
                sum += numbers[i]

            #Cast to int if possible
            if sum == int(sum):
                sum = int(sum)
            
            #Print and store sum
            prev = sum
            print(sum)

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
            print(diff)

        #Unknown command
        else:
            print("Unknown Command")
           
#Calculator================================================
#First print greeting
print("Python CLI Calculator")
print()

#Print help message
print("Enter 'help' for instructions")
print()

#Start the shell
calc()
