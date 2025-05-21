# Functions with input

def greet_with_name(name, location ):
    print(f"Hello {name}")
    print(f"How is it in {location}?")


greet_with_name("Jack Bauer","bangalore")


def calculate_love_score(name1, name2):
    combine_names = name1 + name2
    lower_name = combine_names.lower()

    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")

    score1 = t + r + u + e

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")

    score2 = l+o+v+e
    final_score =(f"{score1}"+ f"{score2}")
    print(final_score)
calculate_love_score(name1="likith", name2="ashok")