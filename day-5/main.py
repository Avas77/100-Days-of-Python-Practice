stud_heights = input("Enter the height of the students:").split()
sum = 0

for height in stud_heights:
    sum += int(height)

average = sum/len(stud_heights)

print(f"Average of the numbers is", round(average))


