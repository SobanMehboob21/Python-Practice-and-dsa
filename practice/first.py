# calculation of any two integer numbers

num_1=input("Enter First Value: ")
num_2=input("Enter Second Value: ")


if num_1.isdigit() and num_2.isdigit():
    print("Proceeding...")
    sign=input("Select a sign: +,-,*,/  ")
    if sign == "+" :
       print(f"The result is:  {int(num_1)+int(num_2)}")
    elif sign=="-":
        print(f"result is {int(num_1)-int(num_2)}")
    elif sign=="*":
        print(f"result is {int(num_1)*int(num_2)}")
    elif sign == "/":
        if num_2 == "0":
            print("Cannot divide by zero!")
        else:
            print(f"result is {int(num_1) / int(num_2)}")
    else:
        print(f"'{sign}' is not a valid operator.")


elif not num_1.isdigit() and not num_2.isdigit():
    print("both arent valid")

elif not num_1.isdigit():
    print(f"enter a valid number in first field. {num_1} is not a number")

elif not num_2.isdigit():
    print(f"enter a valid number in second field. {num_2} is not a number")
