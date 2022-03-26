def gradingStudents(grades):
    # Write your code here
    for index, value in enumerate(grades):
        if value < 38:
            grades[index] == value
        else:
            temp = (value//5 + 1)*5
            if temp - value < 3:
                grades[index] = temp
            else:
                grades[index] = value
                
            
    return grades            