import json

if __name__ == '__main__':
    # person_string = '{"name":"Ali","languages":["python","c#"]}'
    # JSON string to Dict
    # result = json.loads(person_string)

    # with open("person.json") as f:
    #     result = json.load(f)

    person_dict = {"name": "Ali", "languages": ["python", "c#"]}
    result = json.dumps(person_dict)

    # with open("person.json","w") as file:
    #     json.dump(person_dict, file)

    # print(result)
    # print(result["name"])

    result = json.dumps(person_dict, indent=4,sort_keys=False)
    print(result)
