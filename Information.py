collegeName=["DA-IICT","Nirma","L.D.","M.S.U.","D.D.U.","B.V.M.","AU","PDPU"]
collegeFees=["1,72,000","1,80,000","1500","1500","1,50,000","70,000","1,73,000","2,31,000"]
collegeBranches=["1. ICT    2.ICT WITH CSE","1.Mechanical   2.Civil     3.Electrical    4.CS", "1.Mechanical   2.Civil     3.Electrical    4.CS","1.Mechanical   2.Civil     3.Electrical    4.CS","1.Mechanical   2.Civil     3.Electrical    4.CS","1.Mechanical   2.Civil     3.Electrical    4.CS","1.Chemical  2.Mechanical    3.CSE","1.ICT   2.Mechanical    3.CE    4.Civil     5.Electrical"]
collegeCity=["Gandhinagar","Ahmedabad","Ahmedabad","Vadodara","V.V. Nagar","V.V. Nagar","Ahmedabad","Ahmedabad"]
collegeHPackage=["40,00,000","22","18,00,000","18,00,000","13,00,000","13,00,000","15,50,000","12,30,000"]
collegeLpackage=["18,00,000","12,00,000","8,00,000","9,00,000","8,00,000","9,00,000","5,00,000","3,00,000"]
collegePlacementPercent=["95%","87%","76%","73%","74%","65%","60%","85%","70%"]


for i in range(len(collegeName)):
    print(i,":",collegeName[i])
    print()
j=int(input("enter your choice: "))
print(collegeName[j],"\n","City: ",collegeCity[j],"\n","college fees: ₹",collegeFees[j],"\n","branches: \n",collegeBranches[j],"\n"
,"Placement: \n","Highest package (in LPA):",collegeHPackage[j],"\n","Lowest Package          :",collegeLpackage[j],"\n","Placement percentage      : ",collegePlacementPercent[j])
if j== 0:
    handle1 = open("DA-IICT", "r")
    
    print("Review: ",handle1.read())
if j == 1:
    handle1 = open("Nirma", "r")
    
    print("Review: ",handle1.read())
if j == 2:
    handle1 = open("LD", "r")
    
    print("Review: ",handle1.read())
if j== 3:
    handle1 = open("MSU", "r")
    
    print("Review: ",handle1.read())
if j == 4:
    handle1 = open("DDU", "r")
    
    print("Review: ",handle1.read())
if j == 5:
    handle1 = open("BVM", "r")
    
    print(handle1.read())
if j == 6:
    handle1 = open("AU", "r")
    
    print("Review: ",handle1.read())
if j == 7:
    handle1 = open("PDPU", "r")
    
    print("Review: ",handle1.read())
