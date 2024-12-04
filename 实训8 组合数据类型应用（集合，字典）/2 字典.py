dict_demo = {"k1":"v1","k2":"v2","k3":"v3"}
print(dict_demo.keys())
print(dict_demo.values())
print(dict_demo.items())
dict_demo["k4"]="v4"
dict_demo["k5"]="v6"
print(dict_demo)
dict_demo["k5"]="v5"
print(dict_demo)
dict_demo.clear()
print(dict_demo)