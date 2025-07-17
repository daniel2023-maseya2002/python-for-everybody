import json

data = '''{
    "name" : "Daniel",
    "phone" : {
        "type" : "intl",
        "number" : "+250 791 434 027"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:' ,info["name"])
print('Phone:' ,info["phone"]["number"])
print('Hide:' ,info["email"]["hide"])
