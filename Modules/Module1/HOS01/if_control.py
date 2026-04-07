print("Enter is your mid term test score?")
score = int(input())

result = ""

if score < 60:
    result = "Fail"
elif score >= 60 and score < 70:
    result = "Pass"
else:
    result = "Pass with distinction"

print(result)