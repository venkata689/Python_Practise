marks = int(input("Enter the Marks to know the Grade: "))
if marks >= 75:
    print ("You have got 'Distinction'")
elif (marks >=70 and marks <75):
    print ("You have got 'First Class'")
elif (marks >=60 and marks <70):
    print ("You have got 'Second Class'")
elif (marks >=35 and marks < 60):
    print ("You have got 'Third Class'")
else:
    print ("Better Luck Next Time!!!")