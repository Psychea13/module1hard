grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)

grades_sr = [sum(grades[0])/len(grades[0]),
             sum(grades[1])/len(grades[1]),
             sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]),
             sum(grades[4])/len(grades[4])]

students = {'Johnny' : grades_sr[0],
            'Bilbo' : grades_sr[1],
            'Steve' : grades_sr[2],
            'Khendrik' : grades_sr[3],
            'Aaron' : grades_sr[4]}

print(students)