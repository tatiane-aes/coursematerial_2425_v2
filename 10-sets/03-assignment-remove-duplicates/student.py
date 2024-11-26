def remove_duplicates(xs):
    seen = set()
    result = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

print(remove_duplicates([1]))
print(remove_duplicates([1, 2, 2, 1]))
print(remove_duplicates([1, 3, 2, 2, 4, 1]))
