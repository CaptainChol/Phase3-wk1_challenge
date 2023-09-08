
# bdd


# pseudocode
# i) create a function called timeConverter
# ii) inside the function create a variable called time
# iii) time takes user input via terminal
# iv)check if the hour is equal to 12 and if is AM
# v) if true return "00:23"
# vi) check if the hour is equal to 12 and if is PM 
# vii) if true return "12:23"
# viii) if false return hours + 12 i.e 1:45 pm is  (1 + 12)= 13:45






def timeConverter():
    
    time = input("Enter  Time in this format H:M am/pm")
    
    if time[:2]=="12" and time[-2:] == "am":
        timer = "00" + time[2:-2]
    elif time[:2] == "12" and time[-2:] == "pm":
        timer = time[:-2]
    else:
        str(int(time[:2])+ 12) + time[2:-2]  
    print(timer)     

timeC()         
             