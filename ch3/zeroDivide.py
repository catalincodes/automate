def divide42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(divide42by(2))
print(divide42by(12))
print(divide42by(0))
print(divide42by(1))
