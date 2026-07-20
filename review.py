quiz1 = float(input("Enter Quiz 1 score: "))
quiz2 = float(input("Enter Quiz 2 score: "))
average = (quiz1 + quiz2) / 2
print(f"Average: {average:.2f}")
print("At least 75?", average >= 75)
print("Both above 70?", quiz1 > 70 and quiz2 > 70)