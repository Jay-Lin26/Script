from random import randrange

content = ["你", "我", "他", "她", "它", "文", "明", "从", "做", "起", "海", "淘"]
i = 0
text = ""
while i < 8:
    i += 1
    num = randrange(0, len(content))
    text += content[num]
print(text)