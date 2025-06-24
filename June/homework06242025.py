def avglist(lst):
    try:
        total = 0
        count = 0
        for i in lst:
            total += int(i)
            count += 1
        avg = total / count
        return avg
    except(ValueError, TypeError) as e:
        return 'your list not valid'

listnum=[87, 23, 14, 59, 44, 91, 89, 35, 11, 62, 48, 8, 20, 73, 5, 38, 84, 31, 16, 90, 55, 26, 64, 12, 79, 6]
output = avglist(listnum)
print(output)

#10