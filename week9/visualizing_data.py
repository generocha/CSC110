'''
This program will read a file and present the results as a bar chart.
with grade categories on the X axis, and # of students
in each category on the Y axis.
90 - 100  = A
80 - 89   = B
70 - 79   = C
60 - 69   = D
< 60      = F
Gene Rocha
12/3/2019
'''
import matplotlib.pyplot as plt
# add a dictionary for the grades. The values will be set as zero
grade_group = {'A':0,
    'B':0,
    'C':0,
    'D':0,
    'F':0}
# open the grades.txt
grades = open('grades.txt','r').read().splitlines()
# set the variables for total grades, min grade and max grade
totalGrades = 0
gradeMin = 100
gradeMax = 0
# iterate through collection of grade dictionary items
for grade in grades:
    score = float(grade) 
    totalGrades += score # add the grades for the total
    if float(grade) > gradeMax: # if the grade is greater than the current max grade, set as max grade
        gradeMax = float(grade)
    if float(grade) < gradeMin: # if the grade is less than the current min grade, set as the min grade
        gradeMin = float(grade)
    if score > 90: # increment the grade groups
        grade_group['A'] += 1
    elif score > 80:
        grade_group['B'] += 1
    elif score > 70:
        grade_group['C'] += 1
    elif score > 60: 
        grade_group['D'] += 1
    else:
        grade_group['F'] += 1
# set the average
average =  round(totalGrades/len(grades))
# set the plot bar
plt.bar(grade_group.keys(),grade_group.values(), label='Student Grades', align="center") # show vertical bars
# add ployt label and plot title with the min, max and average grades
plt.ylabel('# of students')
plt.title('{0:<30}'.format('Student Grades\n min =' + str(gradeMin)) + '{0:^10}'.format('max =' + str(gradeMax))  + '{0:>10}'.format('\u03BC = ' + str(average)))
# add the grade group keys
plt.xticks( range(5),grade_group.keys())
plt.xlabel('Grade')
# Show the plot
plt.show()