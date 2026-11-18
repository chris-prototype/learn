# lists
nums = [1, 2, 3]
print(nums)
print(*nums)
combined = [*nums, 4, 5]
print(combined)

# dictionaries
defaults = {"color": "red", "size": "M"}
overrides = {"size": "L"}
merged = {**defaults, **overrides}

# function defenitions - packs instead of unpacks
def f(*args, **kwargs):
    print(args)
    print(kwargs)

f(1, 2, x=3)