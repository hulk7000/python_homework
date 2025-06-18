print("Calculating sum from 1 to 10, skipping 5:")
total = 0
i = 10  # start point for example
for i in range(1, 11):
    if i == 5:
        print("Skipping 5...")
        continue
    else:
        total += i
        print(f"Adding {i}, current total: {total}")
print("Final total (excluding 5):", total)