count = 0
total = 0
average = []
largest = None
smallest = None
while True:
            number = input("Enter Number:")
            if number == 'done':
                break
            try:
                
                num = int(number)                
                total += num
                count += (num + 1) - num
                times = 1
                for _ in range(times):
                    average.append(num)

                continue
            except:
                print("Invalid Entry")
                continue
                if number == 'done':
                    break
for insa in [average]:
    if largest is None or insa > largest:
        largest = insa

aaverage = sum(average) / len(average) if average else 0
print("Done!")
print("The total is", total)
print("With a count of", count)
print("Average of", aaverage)
print("Largest is", largest)

