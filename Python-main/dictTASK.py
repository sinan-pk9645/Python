my_dict = {"name": "nikk", "age": 20}
print(my_dict) 

my_dict["city"] = "delhi"
print(my_dict) 

age = my_dict.pop("age")
print(age) 

print(my_dict.get("email")) 

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) 

count =len(my_dict)
print("number of keys:",count)

my_dict = {"name": "nikk", "age": 20}
my_dict1 = {"cource": "python", "place": "palakkad"}

my_dict.update(my_dict1)
print(my_dict1)

my_dict.clear()
print(my_dict) 

original = {"name": "nikk", "age": 20}
copy_dict =original.copy()
print(copy_dict) 

print(my_dict.get("salary")) 

# last_item = my_dict.popitem()
# print(last_item) 

student={"name":"rahul","marks":{"maths":90,"science":85}}
print(student["marks"],["science"])

my_dict.update({"name": " basheer", "maths": 95 } )
print(my_dict) 

my_dict.update({"marks":"englis"})
my_dict.update({"marks":"englis:"})

del my_dict["marks"]
print(my_dict) 
