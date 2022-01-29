materials = {}
materials["motes"] = 0
materials["shards"] = 0
materials["fragments"] = 0

farm_unedited = input().split()
farm = []
for item in farm_unedited:
    if item.isdigit():
        farm.append(int(item))
    else:
        farm.append(item.lower())

while len(farm) > 0:
    key = farm.pop(1)
    value = farm.pop(0)

    if key in materials:
        materials[key] += value
    else:
        materials[key] = value

    if materials["motes"] >= 250:
        print("Dragonwrath obtained!")
        materials["motes"] -= 250
        break
    elif materials["shards"] >= 250:
        print("Shadowmourne obtained!")
        materials["shards"] -= 250
        break
    elif materials["fragments"] >= 250:
        print("Valanyr obtained!")
        materials["fragments"] -= 250
        break

key_materials = {}
key_materials["motes"] = materials.pop("motes")
key_materials["shards"] = materials.pop("shards")
key_materials["fragments"] = materials.pop("fragments")

key_materials = dict(sorted(key_materials.items(), key=lambda x: x[0], reverse=False))
key_materials = dict(sorted(key_materials.items(), key=lambda x: x[1], reverse=True))
for (key, value) in key_materials.items():
    print(f"{key}: {value}")

materials = dict(sorted(materials.items(), key=lambda x: x[0], reverse=False))
for (key, value) in materials.items():
    print(f"{key}: {value}")