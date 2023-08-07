keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# make a dictionary with the keys and values above
# and print it

# Expected output:  
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# -----------------------------
print(dict(zip(keys, values))) 

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# merge the two dictionaries and print the result
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# -----------------------------
dict1.update(dict2)
print(dict1)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# print the value history
# Expected output:  80
# -----------------------------
print(sampleDict["class"]["student"]["marks"]["history"])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# initialize the dictionary with default values
# Expected output:
# {'name': 'Kelly', 'designation': 'Developer', 'salary': 8000}
# {'name': 'Emma', 'designation': 'Developer', 'salary': 8000}
# -----------------------------
resDict = dict.fromkeys(employees, defaults)
print(resDict)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
# Expected output:
# {'name': 'Kelly', 'salary': 8000}
# -----------------------------
new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
# Expected output:
# {'city': 'New york', 'age': 25}   
# -----------------------------
new_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(new_dict)

sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:
# 200 present in a dict
# -----------------------------
if 200 in sample_dict.values():
    print("200 present in a dict")

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
# -----------------------------
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
