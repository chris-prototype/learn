# unpack lists
nums = [1, 2, 3]
print(nums)
print(*nums)
combined = [*nums, 4, 5]
print('combined - ', combined)

# unpack dictionaries
defaults = {"color": "red", "size": "M"}
overrides = {"color": "white", "size": "L", "notes": "fine"}
merged = {**defaults, **overrides}
print('merged - ', merged)

# function defenitions - packs instead of unpacks
def f(*args, **kwargs):
    print('packs - arguments and keyed arguments')
    print(args)
    print(kwargs)

f(1, 2, x=3)