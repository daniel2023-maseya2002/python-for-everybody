import json

input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Dani",
        "phone" : {
            "type" : "intl",
            "number" : "+250 791 434 027"
        }
    },
    {   "id" : "009",
        "x" : "7",
        "name" : "Maseya",
        "phone" : {
            "type" : "intl",
            "number" : "+243 895 485 491"
        }
    }
]'''

info = json.loads(input)
print('User count:' ,len(info))
for item in info:
    print('Name:' ,item['name'])
    print('Id:' ,item['id'])
    print('Attribute:' ,item['x'])
    print('Phone:' ,item['phone']['number'])
