#def contains_duplicates(xs):
#   return len(set(xs)) != len(xs)

# nao sei qual o mais rapido

def contains_duplicates_dict(xs):
    seen = {}
    for x in xs:
        if x in seen:
            return True
        seen[x] = True
    return False

xs = [3, 1, 2]
print(contains_duplicates_dict(xs))