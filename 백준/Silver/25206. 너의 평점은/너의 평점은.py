sub_avr = {"A+": 4.5, "A0" : 4.0, "B+": 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" :1.5, "D0" :1.0, "F": 0.0}
grade_total = 0
sub_total = 0 
while(True) :
    try :
        grade = list(input().split())
        if grade[2] in sub_avr :
            grade_total+=float(grade[1])
            sub_total+=sub_avr[grade[2]]*float(grade[1])
            # print("grade_total : ",grade_total)
            # print("sub_total : ",sub_total)

    except :
        break
print(float(sub_total)/grade_total)