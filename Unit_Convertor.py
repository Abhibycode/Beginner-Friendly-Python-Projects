#Give a summary of your application
print("""
Welcome Unit convertor
You can convert Celcius <--> Fahrenheit
You can also have option to other covertion like Miles <--> KiloMeter and Kilogram <--> Pounds
""")

Choose = int(input("""
1. To convert Celcius <--> Fahrenheit
2. To convert Kilogram <--> Pounds
3. To convert Miles <--> KiloMeter
Enter your choose (1/2/3): """))

if Choose == 1:
    choose2 = int(input("""
Enter your choose of conversion
1. To convert Celcius to Fahrenheit
2. To convert Fahrenheit to Celcius
Enter your choose (1/2): """))
    num = int(input("Please enter number: "))
    if choose2 ==1:
        print("Your convertion from Celcius to Fahrenheit is: ", (num*(9/5)+32))
    elif choose2 == 2:
        print("Your convertion from Fahrenheit to Celcius is: ", ((num-32)*(5/9)))
    else:
        print("You entered invalid number")

elif Choose == 2:
    choose2 = int(input("""
Enter your choose of conversion
1. To convert Kilogram to Pounds
2. To convert Pounds to Kilogram
Enter your choose (1/2): """))
    num = int(input("Please enter number: "))
    if choose2 == 1:
        print("Your Kilogram to Pounds value is: ", num*2.20462)
    elif choose2 == 2:
        print("Your Pounds to Kilogram value is: ", num/2.20462)
    else:
        print("You entered invalid number")

elif Choose == 3:
    choose2 = int(input("""
Enter your choose of conversion
1. To convert Miles to Kilometer
2. To convert Kilometer to Miles
Enter your choose (1/2): """))
    num = int(input("Please enter number: "))
    if choose2 == 1:
        print("Your Miles to Kilometer value is: ", num*1.60934)
    elif choose2 == 2:
        print("Your Kilometer to Miles value is: ", num/1.60934)
    else:
        print("You entered invalid number")

else:
    print("You entered invalid number")