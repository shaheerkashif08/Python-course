def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairswhich were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Numair=72, sania=85, ayesha=91)