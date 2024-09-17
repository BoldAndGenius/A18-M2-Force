#################################################################################
#################################################################################
'''LIST METHODS'''

#append
watches = ["rolex", "fastract", "fossil", "titan", "casio"]
watches.append("sonata")
print(watches)

#copy
watches_copy = watches.copy()
print(watches_copy)

#clear
watches_copy.clear()
print(watches_copy)

#count
shoes = ["nike", "Puma", "adidas", "woodland", "puma"]
result = shoes.count("bata")
print(result)

#remove
countries = ["switzerland", "pakistan", "india", "usa", "russia", "pakistan"]
countries.remove("pakistan")
print(countries)

#insert
my_cartoons = ["tom and jerry", "doraemon", "ninja hattori", "spongebob", "pink panther"]
my_cartoons.insert(0, "noddy")
print(my_cartoons)


#extend
your_cartoons = ["ben 10", "shinchan", "chota bheem", "motupatlu", "oggy"]
my_cartoons.extend(your_cartoons)
print(my_cartoons)
my_cartoons.extend("micky")       #char by char
print(my_cartoons)

#pop
superheroes = ["ironman", "jai baalayya", "shaktimaan", "black panther", "deadpool"]
result = superheroes.pop()
print(result)
print(superheroes)
result = superheroes.pop(2)
print(result)
print(superheroes)

#index
animes = ["AOT", "one piece", "demon slayer", "death note", "DBZ", "naruto", "tokyo ghoul", "iq"]
result = animes.index("DBZ", 0, 3)
print(result)

#reverse
supervillains = ["thanos", "doctor doom", "hella", "rolex", "homelander","joker"]
supervillains.reverse()
print(supervillains)

#sort
bands = ["1D", "bts", "blackpink", "maroon 5", "imagine dragons"]
bands.sort()
print(bands)

##################################################################################
##################################################################################
'''TUPLE METHODS'''

#count
drinks = "j&d", "teachers", "old monk", "imperial blue", "blenders pride", "vat69"
result = drinks.count("old monk")
print(result)
print(type(drinks))

#index
companies = ("google", "facebook", "ms", "wipro", "amazon", "ibm", "tata")
result = companies.index("ibm")
print(result)

###################################################################################
###################################################################################
'''SET METHODS'''

#add
supercars = {"lambo", "bugatti", "porsche","ferrari", "bujji", "mustang", "ferrari"}
supercars.add("aston martin")
print(supercars)

#copy
supercars_copy = supercars.copy()
print(supercars_copy)
supercars_copy.clear()
print(supercars_copy)

games1 = {"gta", "far cry", "god of war", "assassins creed"}
games2 = {"fifa", "cricket 2007", "mario", "gta", "free fire"}

#union
result = games1.union(games2)
print(result)

#intersection
result = games1.intersection(games2)
print(result)

#difference
result = games1.difference(games2)
print(result)

#symmetric_difference
result = games1.symmetric_difference(games2)
print(result)

#remove
fruits = {"mango", "strawberry", "apple", "pomogranate", "orange", "grapes"}
fruits.remove("dragon fruit")     #error
print(fruits)

#discard
fruits.discard("dragon fruit")
print(fruits)
print("tata")

#pop
junkfoodchains = {"kfc", "mcd", "dominoes", "bk", "pizzahut", "tacobell"}
result = junkfoodchains.pop()
print(result)
print(junkfoodchains)


#update/ intersection_update/ difference_update/ symmetric_difference_update
set1 = {10, 20, 30}
set2 = {30, 40, 50}
set1.update(set2)
set1.intersection_update(set2)
set1.difference_update(set2)
set1.symmetric_difference_update(set2)

print(set1)


#issubset/ issuperset/ isdisjoint
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
result = set1.issubset(set2)      #False
result = set1.issuperset(set2)
result = set1.isdisjoint(set2)
print(result)

###################################################################################
###################################################################################
'''DICTIONARY METHODS'''

#copy
movie1 = {"name":"baahubali", "cast":("prabhas", "sweety", "raana"), "budget":250, "music":"keervani", "director":"raajmouli"}
movie1_copy = movie1.copy()
print(movie1_copy)

#clear
movie1_copy.clear()
print(movie1_copy)     #{}

#keys
result = movie1.keys()
print(result)

#values
result = movie1.values()
print(result)

#items
result = movie1.items()
print(result)

movie1["language"] = "telugu"
print(movie1["language"])

#pop
result = movie1.pop("language")
print(result)

#popitem
result = movie1.popitem()
print(result)
print(movie1)

#update
movie1 = {"cast":("prabhas", "sweety", "raana"), "budget":250, "music":"keervani", "director":"raajmouli"}
extra_info = {"songs":["saahore baahubali", "mamathala thalli"], "duration":3}
movie1.update(extra_info)
print(movie1)

#setdefault
result = movie1.setdefault("name", "bb")
print(result)

#fromkeys
planets = ["mercury", "venus", "earth", "mars", "jupitar", "saturn", "uranus", "neptune"]
dict1 = {}
result = dict1.fromkeys(planets, "sun")
print(result)

#####################################################################################
#####################################################################################