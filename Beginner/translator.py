# all vowels are converted to g

def translate(phrase):
    translation = ""
    for letter in phrase:

        # only have to check for lowercase
        if letter.lower() in "aeiou":

            # Keep the capitalized syntax
            # if letter is a vowel then convert to g
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:

            # of letter is not a vowel, then leave as is
            translation = translation + letter
    
    return translation


print(translate(input("Enter a phrase: ")))