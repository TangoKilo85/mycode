#!/usr/bin/env python3

challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
nightmare = [
    {
        "slappy": "a",
        "text": "b",
        "kumquat": "goggles",
        "user": {
            "awesome": "c",
            "name": {"first": "eyes", "last": "toes"}
        },
        "banana": 15,
        "d": "nothing"
    }
]

def print_phrase(words):
    if isinstance(words[0], dict):
        user = words[0].get("user", {})
        name = user.get("name", {})
        a = name.get("first", "")
        b = words[0].get("kumquat", "")
        c = words[0].get("d", "")
    else:
        a = words[2][1]
        b = words[2][0]
        c = words[3]
    phrase = f"My {a}! The {b} do {c}!"
    print(phrase)

print_phrase(challenge)
print_phrase(trial)
print_phrase(nightmare)

