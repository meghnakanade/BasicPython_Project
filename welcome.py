import os
file =open('WelcomeText.txt','r') # a text file containing a welcome message
print(file.read())
choice =(input("""Enter your choice: 
    a. College Predictor(get to know what branch in what college is open for you )
    b. College Information( get info on all top colleges)
    c. Add a review(give your inputs on an institution): 
    """))
if(choice=='a'):
    os.system("Predictor.py")
elif(choice=='b'):
    os.system("Information.py")
elif(choice=='c'):
    os.system("Review.py")
