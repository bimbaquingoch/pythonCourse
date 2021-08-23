def square(number):
    return number * number


number = int(input("write a number > "))
result = square(number)

print(result)


def emoji(message):
    words = message.split(" ")
    emojis = {
        ":)": "😄",
        ":(": "😥",
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output


message = input("> ")
print(emoji(message))
