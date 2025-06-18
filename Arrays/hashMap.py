"""
| Operation      | Syntax                 | Output               |
| -------------- | ---------------------- | -------------------- |
| Access         | `student["name"]`      | `"Nishchay"`         |
| Insert/Update  | `student["age"] = 22`  | age becomes 22       |
| Check key      | `"age" in student`     | True                 |
| Delete key     | `del student["grade"]` | Removes grade        |
| Get all keys   | `student.keys()`       | dict_keys([...])   |
| Get all values | `student.values()`     | dict values([...]) |
"""

"""
hashM = {
    "name" : "MnM",
    "age" : 19,
    "weight" : 68,
    "year" : "ThirdYear" 
}

print(hashM)
del hashM['name']
print(hashM)
"""

# count frequency of each number
"""
arr = [2, 3, 2, 3, 3, 5]
count = {}

for i in arr:
    if(i in count):
        count[i] += 1
    else:
        count[i] = 1

print(count)

------------- OR ---------------

arr = [2, 3, 2, 3, 3, 5]
count = {}

for i in arr:
    count[i] = count.get(i,0) + 1

print(count)
"""

"""
str = "programming"
count = {}
for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count) 

---------------- OR ----------------

str = "prograMming"
count = {}
for i in str:
    count[i] = count.get(i,0) + 1

print(count) 
"""

# 2 SUM
"""
arr = [4,45,5,4,2,24,5,1,5]
target = 29

seen = {}

for ind,val in enumerate(arr):
    diff = target - val
    if diff in seen:
        print(f"pair found : {seen[diff]} and {ind}")
    seen[val] = ind
"""

# 2 SUM - UNIQUE PAIR COUNT - using SETS
arr = [3, 7, 5, 1, 9, 2, 8, 4, 6]
target = 10
seen = set()
output = set()

for val in arr:
    diff = target - val
    if diff in seen:
        output.add(tuple(sorted((val,diff))))
    seen.add(val)

print(output)



    