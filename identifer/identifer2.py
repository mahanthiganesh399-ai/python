identifiers = ["2value", "value_2", "_hidden", "class", "my-var", "MyClass", "total$"]

for name in identifiers:
    if name.isidentifier():
        print(name, "is a valid identifier")
    else:
        print(name, "is an invalid identifier")

#output
#2value is an invalid identifier
#value_2 is a valid identifier
#_hidden is a valid identifier
#class is a valid identifier
#my-var is an invalid identifier
#MyClass is a valid identifier
#total$ is an invalid identifier