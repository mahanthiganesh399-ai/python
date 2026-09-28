def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)

print("Using Positional Arguments:")
student_info("Ravi", 101, "CSE")

print("\nUsing Keyword Arguments:")
student_info(branch="CSE", name="Ravi", roll_no=101)

# Output:
# Using positional  Arguments:
# Name: Ravi
# Roll No:101
# Branch: CSE

# Using Keyword Arguments:
# Name: ravi
# Roll No: 101
# Branch: CSE