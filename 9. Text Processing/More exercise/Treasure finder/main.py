key = [int(i) for i in input().split()]
i = 0
message = input()
message_edited = ""
material = ""
coordinates = ""


def encode(message_edited, i):
    for char in message:
        message_edited += chr(ord(char) - key[i])
        if not i == 3:
            i += 1
        else:
            i = 0
    return message_edited


def extract_material(message_edited, material):
    for char in message_edited:
        if char == "&":
            for j in range(message_edited.index(char) + 1, len(message_edited)):
                if not message_edited[j] == "&":
                    material += message_edited[j]
                else:
                    break
            break
    return material


def extract_coordinates(message_edited, coordinates):
    for char in message_edited:
        if char == "<":
            for i in range(message_edited.index(char) + 1, len(message_edited)):
                if not message_edited[i] == ">":
                    coordinates += message_edited[i]
                else:
                    break
            break
    return coordinates


while not message == "find":
    message_edited = encode(message_edited, i)
    material = extract_material(message_edited, material)
    coordinates = extract_coordinates(message_edited, coordinates)
    print(f"Found {material} at {coordinates}")
    material = ""
    coordinates = ""
    message_edited = ""
    message = input()