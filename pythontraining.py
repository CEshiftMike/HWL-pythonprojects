from IPython.display import clear_output

def display(row1,row2,row3):
    # print(f"{row1} | {row2} | {row3}")
    print(row1)
    print(row2)
    print(row3)

while True:
    x = input("Please inter a value: ")

    try:
        num = int(x)
    except ValueError:
        print("Invalid input. Please enter a numeric value. Error code: " + str(ValueError))
        continue
    
    if num < 0:
        # print("\n" * 100)
        print("Please enter a positive number.")
        continue

    else:
        print("Thank you for entering a valid number.")
        break


display(f"x value is: {x}", f"x value multiplied by 2 is: {x*2}", f"x value multiplied by 3 is: {x*3}")
    

# print(int(x))
# display(f"x value is: {x}", f"x value multiplied by 2 is: {int(x)*2}", f"x value multiplied by 3 is: {int(x)*3}")