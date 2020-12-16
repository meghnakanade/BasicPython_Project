# need to have some username and password pre-defined
userInfo={"Jeen":156,"Megh":134}
handle2=open("accounts","r")
userInfo=eval(handle2.read())
reviews=[]
choice=int(input("If you have an account press 0 else press 1:"))

if choice==0:
    userInput=input("Please enter your username: \n")
    userPass=int(input("Enter your password(numeric): \n"))
    for i in range(len(userInfo)):
        '''userInput==userName[i] and userPass==password[i]:'''
        if userInput==list(userInfo.keys())[i] and userPass==list(userInfo.values())[i]:
            print("granted")
            collegeName = ["DA-IICT", "Nirma", "L.D.", "M.S.U.", "D.D.U.", "B.V.M.", "AU", "PDPU"]
            for i in range(len(collegeName)):
                print(i, ":", collegeName[i])
                print()

            j = int(input("enter your choice: "))
            if choice==0:
                handle1=open("DA-IICT","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==1:
                handle1=open("Nirma","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==2:
                handle1=open("LD","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==3:
                handle1=open("MSU","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==4:
                handle1=open("DDU","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==5:
                handle1=open("BVM","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==6:
                handle1=open("AU","w")
                review=input("enter your review: ")
                handle1.write(review)
            if choice==7:
                handle1=open("PDPU","w")
                review=input("enter your review: ")
                handle1.write(review)
            break
        else:
            print("denied")
            break

if choice==1:
    class account():
        name:str
        passChoice:str
        email:str
    p1=account()
    p1.name=input("enter your name: ")
    p1.passChoice=input("enter password of your choice: ")
    p1.email=input("please provide your email id: ")
    userInfo[p1.name]=p1.passChoice
    handle=open("accounts","w")
    handle.write(p1.name)
    handle.write(p1.passChoice)
    handle.write(p1.email)
    print(userInfo)



