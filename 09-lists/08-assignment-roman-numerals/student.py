def to_roman(n):
    val = [
        1000, 900, 500, 400,
        100,  90,  50,  40,
        10,   9,   5,   1
    ]
    syb = [
        "M",  "CM", "D",  "CD",
        "C",  "XC", "L",  "XL",
        "X",  "IX", "V",  "I"
    ]
    roman_num = ''
    i = 0
    while  n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

print(to_roman(1))
print(to_roman(2020))

#### que pesadelo

def from_roman(num):
    val = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'I': 1
    }
    integer = 0
    i = 0
    while i < len(num):
        if i + 1 < len(num) and num[i:i+2] in val:
            integer += val[num[i:i+2]]
            i += 2
        else:
            integer += val[num[i]]
            i += 1
    return integer

print(from_roman('MCMLXXXIV'))


# vai tomar no cu esse exercicio todo