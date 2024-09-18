student=[]
with open("student.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student.append(f"{name} is in {house}")


for std in sorted(student):
    print(std)