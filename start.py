score = int(input("Kindly ENTER your SCORES here!\n"))
if score >= 0 and score <= 59:
    print(f"YOU FAILED THE COURSE,{score}F")
elif 60 <= score <= 69:
    print(f"YOU ESCAPED,{score}D")
elif 70 <= score <= 79:
    print(f"FAIR,{score}C")
elif 80 <= score <= 89:
    print(f"EXCELLENT,{score}B")
elif 90 <= score <= 100:
    print(f"SCHOLAR! {score}A")
else:
    print("DON'T WASTE MY TIME!")
