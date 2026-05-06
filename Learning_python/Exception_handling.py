

def safe_divide(a,b):
    try:
       x = a/b
       return x
    
    except ZeroDivisionError:
        print("Divide by zero has occurred")

    except TypeError:
        print("Invalid input")


    finally:
        print("Calculation complete")
    

print(safe_divide(10,2))
safe_divide(10,0)
safe_divide("hi",2)