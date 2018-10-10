by = int(input("Your Birthyear : "))
num = int(input("Your guessing number : "))
if(num <= 9 and num >= 2):
    ops = ((num*2)+5)*50
    isBDP = input("Your Birthday in this year pass ? : ")
    if(isBDP == 'yes'):
        guess = 2311 + ops - by
    elif(isBDP == 'no'):
        guess = 2310 + ops - by
    else:
        print("ERROR")
    guesstr = str(guess)
    print("Your Guess Number is {} and Your age is {}".format(guesstr[0],guesstr[1:]))
else:
    print("ERROR")