# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])





# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }










# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"] or thisdict.get(model)


# brand,model,year are keys             Ford, Mustnag, 1964 are values


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color","food"] = "white","apple"
# Eğer value ya da key sdc birini kaldırırısak hata VERMEZ

# print(x) #after the change




# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020 , "brand": BMW})


Countries= {
    "Turkmenistan" : {
        "Ahal" : "Ashgabat",
        "Mary" : "Garagum",
        "Balkan" : "Derweze"
    },
    "Turkey" : {
        "Konstantinapol" : "Istanbul",
        "Anğara" : "Ankara",
        "Tatil Köyü" : "Antalya"
    },
    "America" : {
        "New York City" : "New York",
        "Chicago Bulls" : "Chicago",
        "L.A" : "Los Angeles"
    }
}
print(Countries["Turkmenistan"].keys())
print(Countries["Turkey"]["Anğara"])
X= Countries["Turkmenistan"].values()
Y= Countries["Turkmenistan"].values()
C= Countries["Turkmenistan"].values()
A= list(X)
B= list(Y)
D= list(C)
New= A + B + D
print(New)


