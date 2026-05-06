#Personal Diary CLI App
from datetime import date

def add_entry(text):
    with open("diary.txt", "a") as f:
        f.write(f"{date.today()} | {text}\n")

def view_entries():
    try:
        with open("diary.txt", "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("No entries yet")



def search_entry(keyword):
        try:
            with open("diary.txt","r") as f:
                found = False
                for line in f:
                    if keyword in line:
                        print(line.strip())
                        found = True
                if not found:
                    print(f"No entries for keyword: {keyword}")

        except FileNotFoundError:
             print("No file found")



while(True):
    a = (input("Enter choices from 1-4 only:"))
    if a == "1":
         text = input("Enter your diary entry:")
         add_entry(text)
    elif a == "2":
         view_entries()
    elif a == "3":
         keyword = input("Enter the keyword:")
         search_entry(keyword)
    elif a == "4":
         print("Exit")
         break
    else:
         print("Invalid choice.enter from 1 to 4 only")
     


