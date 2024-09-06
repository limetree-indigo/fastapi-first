def doh():
    return ["Homer: a", "Lisa: b", "Marge: c"]

for line in doh():
    print(line)

def doh2():
    yield "Homer: d"
    yield "Lisa: e"
    yield "Marge: f"

for line in doh2():
    print(line)