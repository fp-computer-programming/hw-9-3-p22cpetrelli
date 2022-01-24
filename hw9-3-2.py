#author CJP 1/18/2022
print('Enter the net sales for')

try:
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'
    print(result)
except ValueError:
    print("Invalid you must enter a number.")
except ZeroDivisionError:
    print("Invalid, do not enter zero.")
finally:
    print("Thank you!")