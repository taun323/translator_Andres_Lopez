import dictionary

text = "a cat a dog eat food in the house"
translate = ""
words = text.split()
try:
    for w in words:
        translate = translate + " " + dictionary.d[w]
        if w not in words:
            translate = translate + " " + w
except:
    "write only words in dictionary "

print(translate)

