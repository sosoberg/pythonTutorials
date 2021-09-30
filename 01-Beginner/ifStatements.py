is_male = False
is_tall = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short man")
elif not(is_male) and is_tall:
    print("You are not a man, but you are tall")
else:
    print("You are not a male or tall")

