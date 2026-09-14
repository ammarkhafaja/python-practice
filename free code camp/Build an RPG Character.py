full_dot = '●'
empty_dot = '○'
def create_character(name,strength,intelligence,charisma):
    if type(name) is not str:
        return "The character name should be a string"
    elif len(name)>10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    elif type(intelligence) is not int or type(charisma) is not int or type(strength) is not int:
        return "All stats should be integers"
    elif not( strength >0 and intelligence >0 and charisma >0):
        return "All stats should be no less than 1"
    elif strength >4 or intelligence >4 or charisma >4:
        return "All stats should be no more than 4"
    elif intelligence+strength+charisma !=7:
        return "The character should start with 7 points"
    else:
        return f"{name}\nSTR {strength*full_dot+(10-strength)*empty_dot}\nINT {intelligence * full_dot + (10 - intelligence) * empty_dot}\nCHA {charisma * full_dot + (10 - charisma) * empty_dot}"


print(create_character("ren", 4, 2, 1))