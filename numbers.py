def check():
    #create an empty list
    result=[]
    #create variable which will dictate the number items(numbers) you will have
    ip = int(input("Enter Number of intergers to check on:" + " "))
    # ip = int(3)
    for i in range(0, ip): 
        #converts input to integer     
        num = int(input())
        #add num to result list
        result.append(num)
         
    print(result)

    #create a counter variable and assign initial value of zero
    counter=0
    # iterate through the list if it finds item greater than 0 it increases the counter
    # after it has finished if the value of counter is greater or equal to 2 it will return True else False
    for item in result:
        if item> 0:
            counter +=1
    print(counter ==2) 

    # print(all(number>0 for number in result)) 
    # print(any(number>0 for number in result))  
    # print(any(number< 0 for number in result))  
check()        