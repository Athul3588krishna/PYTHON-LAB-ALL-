# CO1 Q3(a): positive list from given integers

nums = list(map(int, input("Enter numbers (space separated): ").split()))
positive = [x for x in nums if x > 0]
print("Positive numbers:", positive)
