def create_profile(name, age, country="unknown"):
    profile = {}
    profile["name"] = name
    profile["age"] = age
    profile["country"] = country
    return profile

def display_profile(profile):
    print("user profile:")
    print("name: "+profile["name"])
    print("age: "+str(profile["age"]))
    print("country:"+profile["country"])

users = []
users.append(create_profile("john",21))
users.append(create_profile("frank", 69,"china"))
users.append(create_profile("lily", 34,"canada"))
for user in users:
    display_profile(user)
