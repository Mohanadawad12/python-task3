#first we define the function divison
def division():

    n = int(input("enter the parameter"))
    for a in List:
      if (a%n==0) :
        print(a)

# we ask user to eneter the list elements
j = int(input("length of list"))
List = []
for i in range(j):
    ele= int(input("enter the list elements:"))
    List.append(ele)

print("elemnts of list are:", List)
division()

