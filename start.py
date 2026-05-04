person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    middle_skill = len(person['skills'])// 2
    print(person['skills'][middle_skill])
    if "Python" in person["skills"]:
        print(person['skills'])
    if "JavaScript" and "React" in person["skills"]:
        print("He is a FRONT END DEVELOPER!")
    if "Node" and  "Python" and "MongoDB" in person["skills"]:
        print("He is BACKEND DEVELOPER!")
    if "React" and "Node" and "MongoDB":
        print("He is a FULL STACK DEVELOPER!")
    else:
        print("UNKNOWN ERROR")
    if person["is_married"] == True and person["country"] == "Finland":
        print("Asabeneh Yetayeh lives in Finland. He is married.")
