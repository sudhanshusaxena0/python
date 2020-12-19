price_fruits={'mango':10,'orange':8,'balana':5}
print(price_fruits['mango'])

dict1={"key1":[1,2,3],"key2":['a','b','c'],"key3":{"key3_1":"value1","key3_2":"value2"}}
print(dict1["key1"])
print(dict1["key2"])
print(dict1["key3"])
print(dict1["key3"]["key3_1"])
dict1["key3"]["key3_1"]="new_value1"
print(dict1["key3"]["key3_1"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1["key3"]["key3_1"].upper())
