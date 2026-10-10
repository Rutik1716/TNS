def make_node(value):
    return {"value": value, "left": None, "right": None}


def build():
    root = make_node(50)

    root["left"] = make_node(30)
    root["right"] = make_node(70)

    root["left"]["left"] = make_node(20)
    root["left"]["right"] = make_node(40)

    root["right"]["left"] = make_node(60)
    root["right"]["right"] = make_node(80)

    return root


tree = build()

print(tree["value"])
print(tree["left"]["value"], tree["right"]["value"])
print(
    tree["left"]["left"]["value"],
    tree["left"]["right"]["value"],
    tree["right"]["left"]["value"],
    tree["right"]["right"]["value"]
)