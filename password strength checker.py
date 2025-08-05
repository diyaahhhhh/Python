def password(pw):
    strength=0
    suggestions=[]

#Length checker
    if len(pw)>=8:
        strength+=1
    else:
        suggestions.append("Make it at least 8 characters long.")

#Checking for uppercase
    if any(i.isupper() for i in pw):
        strength+=1
    else:
        suggestions.append("Must contain at least one uppercase letter.")
#Checking for lowercase
    if any(i.islower() for i in pw):
        strength+=1
    else:
        suggestions.append("Must contain at least one lowercase letter.")

#Checking for digits
    if any(i.isdigit() for i in pw):
        strength+=1
    else:
        suggestions.append("Must contain digits.")
#Checking for special characters
    if any(char in "!@#$%^&*-_+." for char in pw):
        strength+=1
    else:
        suggestions.append("Must include special characters.")
#Ratings
    if strength<=2:
        rating="Weak!"
    elif strength==3 or strength==4:
        rating="Moderate..."
    else:
        rating="STRONG!"
    print("Password strength:", rating)
    if suggestions:
        print("Improvements:\n")
        for i in suggestions:
            print(i)
pw=input("Enter a password:")
password(pw)

