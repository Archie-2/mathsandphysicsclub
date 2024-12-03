with open("C:\\Users\\dircr\\Downloads\\student_records.csv", 'r') as file:

    lines = file.readlines()


    for i in range(10):
        print(lines[i].strip())



