# username and passwd *
# terms of application *
# applying for a job with a specefic abilites *
# Thankyou and appriciate it *
# time.sleep(2.4)
#####################
# In The name of Allah#
#####################
import time

# Username
# membership controls
admins = ["Osama", "Ahmed", "Ibrahim"]
jobs = ["pen-tester", "CyberSecurity-Expert"]
p_quality = ["BufferOverflow", "Cryptography"]
c_quality = ["RedTeam", "BlueTeam"]

name = input("Enter your Name From Admins List:# ").strip().capitalize()
passwd = input("Enter your password:# ")
if name in admins:
    # password checking
    if passwd == "osama_elzero":
        print("=" * 50)
        print(f"Hello {name}, welcome back")
        # Terms of the app
        print("=" * 50)
        print("We ara using a terms of our app like terminating cmd, cpu, ram, motherboard, Ay Habd.....^_^")
        accept = input("After reading our terms you can choose [yes/no]:# ").strip()
        if accept == "yes" or accept == "Y" or accept == "y":
            print("=" * 50)
            print("Ok, Hello in the app")
            print("=" * 50)
            job = input(
                "We have a several jobs that may be proper for you, Click [yes] to show them, Click [no] to terminate the app:# ").strip().capitalize()
            if job == "Yes" or job == "Y":
                print(jobs)
                choose = input("(Case insensitive please)" "Choose a job from listed jobs:# ")
                if choose == "pen-tester":
                    print("=" * 50)
                    print("Ok, perfect job")
                    print(p_quality)
                    ability = input("Choose from above what you can do for this job:# ")
                    if ability == "BufferOverflow":
                        email = input("Ok, We will contact you when It's done, but we need your E-mail:# ")
                        print("We will contact you soon, Thankyou for using our app, Bye!!")
                    if ability == "Cryptography":
                        print("Sorry, This job is full off applys we are very sorry")
                if choose == "CyberSecurity-Expert":
                    print("=" * 50)
                    print("Ok, perfect job")
                    print(c_quality)
                    ability1 = input("Choose from above what you can do for this job:# ")
                    if ability1 == "RedTeam":
                        email = input("Ok, We will contact you when It's done, but we need your E-mail:# ")
                        print("We will contact you soon, Thankyou for using our app, Bye!!")
                    if ability1 == "BlueTeam":
                        email = input(
                            "I don't think we have alot of places, Otherwise we will contact you Enter your E-mail:# ")
                        print("We will contact you soon, Thankyou for using our app, Bye!!")

        else:
            print("Sorry, Your should accept the agreements *Terminating the app*")
            exit()

    else:
        print("Sorry, Your password is incorrect *Terminating the app*")
        time.sleep(3)
        exit()
elif name not in admins:
    print("Sorry, your name is not in admins, contact your administrator")
    time.sleep(3)
    exit()

