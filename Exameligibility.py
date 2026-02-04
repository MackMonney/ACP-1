working = int(input("Total number of working days :"))
absent = int(input("Total number of days absent: "))
Attendance = ((working-absent) / working )*100
print("Your Attendance Percentage is", Attendance,"%")
if Attendance <=75: 
    print("You will not be able to sit in the exam.")
else:
    print("You will be able to sit in the exam.")
if absent > working:
        print("Error: Absent days cannot exceed working days.")