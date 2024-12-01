def calculate (a,b,c):#making an function using def 
    if (b == "+"):   # math opraters idk what to say about them but i will try to make it short maybe ;)
        return (a+c)
    elif(b=="-"):
        return(a-c)
    elif(b == "*"):
        return(a*c)
    elif(b=="%"):
        return(a%c)
    elif (b=="/"):
        return(a/c) #it's that long i know 
    else:
        return("it's not allowed try to put the given oprations please") #for smart people who like poke into things
for i in range(0,2): #well a loop that would go till 5 tries and then this will stop automatically
    print("attempt",i+1)
    a = int(input("Enter your first number: ")) 
    b = input("Enter oprations( +,-,*,%,/): ")
    c = int(input("enter your second number: "))
    r  = calculate(a,b,c)
    print(r)
    print("thanks for using".capitalize()) 
'''thanks for using this ik its stupid but i am showing that i am learning something huh
what world do i love where i have to upload things in order to get a nod from the mask or the reflection of mine idk '''