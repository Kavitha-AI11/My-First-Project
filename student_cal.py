print("===== STUDENT CALCULATOR =====")

while True:
    try:

        a = float(input("\nEnter first number:"))
        b = float(input("Enter a second number"))

        print("\nChoose an operation")
        print("1.Adittion")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Divison")

        choice = int(input("Enter your choice:"))

        if choice ==1:
           print("result:",a+b)
        elif choice ==2:
           print("Result:",a-b)
        elif choice ==3:
           print("result:",a*b)
        elif choice ==4:
           if b!=0:
              print("result:",a/b)
           else:
              print("Error:Undefined")

        else:
           print("Invalid choice!")
    except ValueError:
       print("Please enter valid numbers")
    
    

    again = input("\nCalculate again?(yes/no):")

    if again.lower() !="yes":
        break
print("Thank you for using the calculator!")

     