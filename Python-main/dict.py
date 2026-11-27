empty_dict = {}
print(empty_dict) 

my_dict = {"name": "John", "age": 30}
print(my_dict["name"]) 

print(my_dict.get("age")) 
print(my_dict.get("salary")) 

my_dict = {"name": "John", "age": 30}
my_dict["age"] = 31
print(my_dict) 

my_dict["city"] = "New York"
print(my_dict) 

my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York"
print(my_dict) 

my_dict = {"name": "John", "age": 30, "city": "New York"}
age = my_dict.pop("age")
print(age) 

my_dict = {"name": "John", "age": 30}
last_item = my_dict.popitem()
print(last_item) 

my_dict = {"name": "John", "age": 30}
del my_dict["age"]
print(my_dict) 

my_dict.clear()
print(my_dict) 

original = {"name": "John", "age": 30}
copy_dict = original.copy()
print(copy_dict) 

copy_dict = dict(original)
print(copy_dict)

nested_dict = {
 "person1": {"name": "John", "age": 30},
 "person2": {"name": "Alice", "age": 25}
}
print(nested_dict["person1"]["name"]) 


my_dict = {"name": "John", "age": 30}
print(my_dict.keys()) 

print(my_dict.values()) 

print(my_dict.items()) 

my_dict = {"name": "John", "age": 30}
my_dict.update({"city": "New York", "age": 31})
print(my_dict) 

keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)

my_dict = {"name": "John", "age": 30}
city = my_dict.setdefault("city", "New York")
print(city)
print(my_dict)

nsd={
    "student1":{
        "name":"sinan",
        "age":20,
        "address":{
            "place":"malappuram",
            "state":"kerala"
        }

    },
    "student2":{
        "name":"basheer",
    "age":22
    }

}
print(nsd["student1"]["address"]["state"])
nsd["student1"]["address"]["place"]="kochi"
print(nsd)


