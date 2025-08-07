# def is_greater_than_9(x):
    # if x>9:
    #     return True
    # else:
    #     return False

a = [1, 2,5,8, 23, 21, 3, 56, 9.05,  98, 7, 6]
new = list(filter(lambda x: x > 9, a))
print(new)