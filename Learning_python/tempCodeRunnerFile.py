#Lists and Loops

my_list = [45, 82, 17, 63, 90]

for num in my_list:
    if num > 60:
        print(f"Pass: {num}")
    else:
        print(f"Fail: {num}")


#Function

def calculate_average(*args):
    if not args:
        return 0
    else:
        return float(sum(args)/len(args))
x = calculate_average(10,20,30)
y = calculate_average(5,15)
z = calculate_average()

print(x)
print(y)
print(z)



#Lists,Dicts and Tuples
my_list = [3, 1, 2]

# append
result = my_list.append(5)
print(my_list)    # [3, 1, 2, 5]  — list changed
print(result)     # None          — returned nothing

# reverse
result = my_list.reverse()
print(my_list)    # [5, 2, 1, 3]  — list changed
print(result)     # None          — returned nothing

# sort
result = my_list.sort()
print(my_list)    # [1, 2, 3, 5]  — list changed
print(result)     # None          — returned nothing



#Phonebook

phonebook = {
    "Smarika":9847100000,
    "Parbati":9638527410,
    "Manisha":9874563210

    }

def add_contact(phonebook, name, number):
    phonebook[name] = number

def search_contact(phonebook,name):
    result = phonebook.get(name)
    if result:
        return result
    else :
        return ("Contact not found")


def delete_contact(phonebook,name):
     if phonebook.get(name):
         del phonebook[name]
     else:
         print("Contact not found")

x = add_contact(phonebook,"Benisha",9865322356)
print(x)
print(search_contact(phonebook,"Smarika"))
print(search_contact(phonebook,"Ramila"))
print(delete_contact(phonebook,"Smarika"))
print(phonebook)