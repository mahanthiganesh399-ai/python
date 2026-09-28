grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks = [35, 78, 42, 25, 90, 39]

for m in marks:
    print(m, ":", grade(m))