# 1 average
# average= sum of all the values/ number of values
tree1= 98
tree2= 94
tree3= 41
tree4= 96
tree5= 11
sum=( tree1+tree2+tree3+tree4+tree5)
print(sum)
average=sum/5
print("average value of all the trees are: ",average)
# Activity2 count the notes.
amount=int(input("please enter the amount: "))
note10=amount//10
note50=amount//50
note100=amount//100
print("the required rs. 10 notes are: ",note10)
print(" the requred rs. 50 notes are: ",note50)
print(" the required rs.100 notes are: ",note100)
# activity3 percentage
maths=int(input("enter your math marks: "))
english=int(input("enter your english marks: "))
science=int(input("enter your science marks: "))
chemistry=int(input("enter your chemistry marks: "))
sum=(maths+english+science+chemistry)
print("sum  of all the subjects: ",sum)
percentage=(sum/400)*100
print("percentage=",percentage)