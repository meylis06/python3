print("Welcome to my video game dictionaries.")
X= {
    "Mortal Kombat" : {
        "year" : "1992",
        "genre" : "Fighting, Action",
        "Established by" : "Midway Games",
        "Programmers" : "Ed Boon and John Tobias"
    },
    "Assassin's Creed" : {
        "year" : "2007",
        "genre" : "Action",
        "Established by" : "Ubisoft",
    },
    "Uncharted" :{
        "year" : ""
    }
}
Game=input("Which video game do you want to browse??")
Result= X[Game]
print(Result)