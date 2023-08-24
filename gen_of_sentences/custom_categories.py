from wonderwords import RandomWord, Defaults


# generator of random words from list that we gave
fruits = ["apple", "pineapple", "orange", "banana", "blueberry", "strawberry"]
generator = RandomWord(fruit=fruits)
# random word from a generator that got list of words from us
print(generator.word())


print("+"*25)


# generator of random words from lists that we gave him
animals = ["cow", "parrot", "cat", "dog", "elephant", "horse"]
plants = ["tree", "cactus", "grass", "sunflower", "rose"]
generator2 = RandomWord(animal=animals, plant=plants)
# both lists are  enabled because we didnt choose any
print(generator2.word())
print(generator2.word())
# we chose a secific one so we get random animal
print(generator2.word(include_categories=["animal"]))


print("+"*25)

# almost the same as erlier but we can see tat new generator also can use deafault list, here adjectives
writing_utensils = ["graphite pencil", "pen", "marker", "colored pencil"]
generator = RandomWord(
    utensil=writing_utensils,
    adjective=Defaults.ADJECTIVES
)
# both lists are  enabled because we didnt choose any
print(generator.word())
# we chose a secific one so we get random item from choosen list
print(generator.word(include_categories=["utensil"]))
print(generator.word(include_categories=["adjective"]))

