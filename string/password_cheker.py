def pass_checker(pswrd):
    upcs, lwrcs, num, spc = False, False, False, False
    spc_string = "!@#$%^&*()-_+=\|][}{'" ";:/?.>,<"
    for c in pswrd:
        if (c>='A' and c<= 'Z'):
            upcs = True
        elif (c>='a' and c<= 'z'):
            lwrcs = True
        elif (c>='0' and c<= '9'):
            num = True
        if any(c in spc_string for c in pswrd):
            spc = True

    if upcs == True and lwrcs == True and num == True and spc == True:
        return True
    else:
        return False

        

if __name__ == '__main__':
    password = input("Enter your password: ")
    valid = pass_checker(password)
    
    if valid == True:
        print("Your password is strong.")
    else:
        print("Your password is weak.")
    

    