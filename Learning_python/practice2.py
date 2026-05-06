#practice q1
try:
    with open("missing.txt","r") as f:
       f.read()
        
except FileNotFoundError:
        print("File doe not exist")
finally:
        print("Operation attempted")
