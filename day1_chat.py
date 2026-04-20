#接收用户的输入并存入变量
current_status = input("What's your visa status right now?")
days_left = input("How many days until you fly to Sydney?")

#use the f-string 
print(f"\nDont worry, even if the status is {current_status}, you still have {days_left} days to get ready!")
print ("Everything will on track!")