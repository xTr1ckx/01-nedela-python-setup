import sys

if len(sys.argv) < 2:
    print("# Lūdzu norādiet skaitli N. (piemēram python fizzbuzz.py 15)")
    sys.exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print("# N ir jābūt skaitlim!")
    sys.exit()

results = []

for i in range (1, N + 1):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        results.append("FizzBuzzJazz")
    elif i % 3 == 0 and i % 5 == 0:
        results.append("FizzBuzz")
    elif i % 3 == 0 and i % 7 == 0:
        results.append("FizzJazz")
    elif i % 5 == 0 and i % 7 == 0:
        results.append("BuzzJazz")
    elif i % 3 == 0:
        results.append("Fizz")
    elif i % 5 == 0:
        results.append("Buzz")
    elif i % 7 == 0:
        results.append("Jazz")
    else:
        results.append(str(i))

print(", ".join(results))
