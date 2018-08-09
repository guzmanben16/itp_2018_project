#Pseudocode
#1.Welcome Questions/Input
#2.Call the first function: intial_questions to start the program and the algorithm
#3.Call the triage_counter() to always see the number of triage at the start of the program
#4. intial_questions:
#     A. Ask if patient is ambulatory. If yes, categorized as Green. Everytime a categorization has been made, the category will be appended to triage_categories list
#     B. If not ambulatory, ask the age to determine if adult triage (>8) or pediatric triage (<8)
#5. Adult triage: each of the parameters asked are actual functions
#   A. respirations
#   B. perfusion
#   C. mental Status
#6. Pediatric triage: each of the parameters asked are actual functions
#   A. respirations
#   B. perfusion for breathing people
#   C. perfusion for non-breathing people
#   D. mental status
#7. validity_check
#   -checks the chracters input. If allowed, continue, else system exit
#8. triage_counter
# counts the number of each patient in each category and the number of ambulances needed using the list triage_categories and a defaultdict
#   A. Green=4 people allowed per ambulances
#   B. Black, Red, and Yellow= 2 people allowed per ambulance
#9. access_prog()
# allows user to exit or continue. If continue, answer=false.
import sys
from collections import defaultdict

triage_categories=[]
age_categories=[]

# 1. Welcome Questions
triage_officer_name=str(input("Welcome to the EMS Triage Software, Please Input Your Name: "))
time_and_date=input("Please Input the Date and Time: ")
location=str(input("Please Input the Location of the Incident: "))
incident=str(input("In a Few Words, Please Describe Nature of Incident: "))
print("Please proceed with triaging...")

#3. intial_questions()
#purpose: A. Categorize Green patients
#purpose: B. Take note of the age of patient to determne what type of triage to use
def initial_questions():
    user_input=input("Is the patient ambulatory?(able to walk) Answer Y if Yes and N if No.")
    validity_check(user_input)
    if user_input=="Y" or user_input=="y":
        print ("Triage: \033[1;42mGREEN\033[1;m:" , "Patient is classified as third priority(Walking Wounded).")
        triage="Green"
        triage_categories.append(triage)
        age=int(input("What is the patient's age? If patient's age is less than 1, enter as 0: "))
        if age>8:
            age_triage="Adult"
            age_categories.append(age_triage) #append to the age_categories list which will be used for triage_counter()
            access_prog()  #allows to exit or continue
        else:
            age_triage="Pediatric"
            age_categories.append(age_triage)
            access_prog()

    else: #Age now is asked to determine what type of triage to use(Pediatric or Adult)
        age=int(input("What is the patient's age? If patient's age is less than 1, enter as 0: "))
        if age>8:
            age_triage="Adult"
            age_categories.append(age_triage) #append to the age_categories list which will be used of triage_counter
            print("Redirecting to Adult Triage...")
            adult_triage() #moves to adult triage function
        else:
            age_triage="Pediatric"
            age_categories.append(age_triage)#append to the age_categories list which will be used of triage_counter
            print("Redirecting to Pediatric Triage...")
            pediatric_triage() #moves to pediatric triage

#Adult Triage:
#Divided into functions, which are the actual questions/vital signs that the responder should ask
def adult_triage():
    def resp_adult(): #Is the patient breathing?
        user_input=input("Is the patient breathing? Please check for chest rise. Answer Y if Yes and N if No: ")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            print("Try repositioning/opening the patient's airway")
            user_input=input("Is the patient now breathing? Answer Y if Yes and N if no: ") #Is the patient now breathing after repositioning?
            validity_check(user_input)
            if user_input=="N" or user_input=="n":
                triage="Black"
                triage_categories.append(triage) #if not breathing, categorized as black and appended to triage_categories list which will be used for triage counter()
                print("Triage:\033[1;47mBLACK\033[1;m","Patient is classified as fourth priority(Expectant/Deceased).")
                access_prog()
            else:
                triage="Yellow"
                triage_categories.append(triage) #if after repositioning, patient is breathing, categorized as yellow and appended to triage_categories list which will be used for triage_counter()
                print("Triage:\033[1;43mYELLOW\033[1;m" , "Patient is classified as second priority(Delayed Treatment).")
                access_prog()
        else: #Check number of respirations
            resp_rate=int(input("What is the respiration rate (breaths/min) of patient? Please input the number only."))
            if resp_rate > 30 or resp_rate <10:
                triage="Red"
                triage_categories.append(triage) #if low or high, categorized as black and appended to triage_categories list which will be used for triage counter()
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
                access_prog()
            else:
                perfusion_adult() #move to perfusion count

    def perfusion_adult(): #Does the patient have pulse?
        user_input=input("Does the patient have radial pulse? Please enter Y if Yes and N if No:")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            triage="Red"
            triage_categories.append(triage)
            print("Triage: \033[1;48mRED\033[1;m", "Patient is classified as first priority(Immediate Treatment).")
            access_prog()
        else: #Counting the heart rate
            heart_rate=int(input("What is the patient's heart rate (beats/min)?"))
            if heart_rate<60 or heart_rate>100:
                triage="Red"
                triage_categories.append(triage)
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
                access_prog()
            else:
                cap_refill=int(input("What is the capillary refill? (in seconds). Please enter the number only: "))
                if cap_refill >2:
                    triage="Red"
                    triage_categories.append(triage)
                    print("Triage:\033[1;48mRED\033[1;m", "Patient is is classfied as first priority(Immediate Treatment).")
                    access_prog()
                else:
                    ment_status_adult()
    def ment_status_adult(): #Checking the mental status of the patient
        user_input=input("Ask simple commands to the patient. Does the patient follow commands? Please enter Y if Yes and N if No: ")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            triage="Red"
            triage_categories.append(triage)
            print("Triage:\033[1;48mRED\033[1;m", "Patient is classified as first priority(Immediate Treatment).")
            access_prog()
        else:
            triage="Yellow"
            triage_categories.append(triage)
            print("Triage:\033[1;43mYELLOW\033[1;m" , "Patient is classified as second priority(Delayed Treatment).")
            access_prog()

    resp_adult()

#pediatric triage
def pediatric_triage():
    def resp_peds(): #Is the patient breathing?
        user_input=input("Is the patient breathing? Please check for chest rise. Answer Y if Yes and N if No: ")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            print("Try repositioning/opening the patient's airway")
            user_input=input("Is the patient now breathing? Answer Y if Yes and N if no: ") #Is the patient now breathing after repositioning?
            validity_check(user_input)
            if user_input=="Y" or user_input=="y":
                triage="Red"
                triage_categories.append(triage)
                print("Triage:\033[1;48mRED\033[1;m:" , "Patient is classified as first priority(Immediate Treatment)")
                access_prog()
            else:
                perfusion_peds()
        else: #Check number of respirations
            resp_rate=int(input("What is the respiration rate (breaths/min) of patient? Please input the number only."))
            if resp_rate > 45 or resp_rate <15:
                triage="Red"
                triage_categories.append(triage)
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
                access_prog()
            else:
                perfusion_peds_resp() #move to perfusion count

    def perfusion_peds(): #Does the patient have pulse?
        user_input=input("Does the patient have palpable pulse? Please enter Y if Yes and N if No.")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            triage="Black"
            triage_categories.append(triage)
            print("Triage:\033[1;47mBLACK\033[1;m","Patient is classified as fourth priority(Expectant/Deceased).")
            access_prog()
        else:
            print("Perform five rescue breaths to the patient.")
            user_input=input("Is the patient now breathing? Please enter Y if Yes and N if No: ")
            validity_check(user_input)
            if user_input=="N" or user_input=="n":
                triage="Black"
                triage_categories.append(triage)
                print("Triage:\033[1;47mBLACK\033[1;m","Patient is classified as fourth priority(Expectant/Deceased).")
                access_prog()
            else:
                triage="Red"
                triage_categories.append(triage)
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
                access_prog()

    def perfusion_peds_resp(): #check perfusion for breathing patients
        user_input=input("Does the patient have palpable pulse? Please enter Y if Yes and N if No.")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            triage="Red"
            triage_categories.append(triage)
            print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
            access_prog()
        else:
            ment_status_peds()

    def ment_status_peds(): #Checking the mental status of the patient
        user_input=input("Use AVPU scale to check mental status. Is the patient alert and responsive to verbal commands or at least responsive to pain? Please enter Y if Yes and N if No: ")
        validity_check(user_input)
        if user_input=="N" or user_input=="n":
            triage="Red"
            triage_categories.append(triage)
            print("Triage:\033[1;48mRED\033[1;m:", "Patient is classified as first priority(Immediate Treatment).")
            access_prog()
        else:
            triage="Yellow"
            triage_categories.append(triage)
            print("Triage:\033[1;43mYELLOW\033[1;m:" , "Patient is classified as second priority(Delayed Treatment).")
            access_prog()

    resp_peds()

def validity_check(user_input):
    allowed_chars = set(['N', 'Y', 'n','y'])
    while True:
        if set(user_input).issubset(allowed_chars):
            break
        else:
            sys.exit("You have entered a wrong character.")
def triage_counter():
    age_catg_count = defaultdict(int)
    for ages in age_categories:
        age_catg_count[ages] += 1
    print("Age Category Counts: {} ".format(dict(age_catg_count)))
    tri_catg_count = defaultdict(int)
    for catg in triage_categories:
        tri_catg_count[catg] += 1
    if  tri_catg_count["Green"]==0< tri_catg_count["Green"] < 5:
        green_ambulance=1
    else:
        green_ambulance=1+((tri_catg_count["Green"]-1)//4)
    if tri_catg_count["Red"]==0 < tri_catg_count["Red"] < 3:
        red_ambulance=1
    else:
        red_ambulance=1+((tri_catg_count["Red"]-1)//2)
    if tri_catg_count["Yellow"]==0< tri_catg_count["Yellow"] <3:
        yellow_ambulance=1
    else:
        yellow_ambulance=1+((tri_catg_count["Yellow"]-1)//2)
    if tri_catg_count["Black"]==0<tri_catg_count["Black"]<3:
        black_ambulance=1
    else:
        black_ambulance=1+((tri_catg_count["Black"]-1)//2)

    print("Number of Green Category Patients: {}, Number of Ambulances Needed: {}".format(tri_catg_count["Green"], green_ambulance))
    print("Number of Red Category Patients: {}, Number of Ambulances Needed: {}".format(tri_catg_count["Red"], red_ambulance))
    print("Number of Yellow Category Patients: {}, Number of Ambulances Needed: {}".format(tri_catg_count["Yellow"], yellow_ambulance))
    print("Number of Black Category Patients: {}, Number of Ambulances Needed: {}".format(tri_catg_count["Black"], black_ambulance))

def access_prog():
    cont_quit=input("Do you Want to continue? Enter C if you want to triage another patient or Q if you want to quit: ")
    if cont_quit=="C" or cont_quit=="c":
        answer=False
    else:
        answer=True
        triage_counter()
        sys.exit("Thank you for using the EMS Triage Software. ")

#2. Calls both intial_intial questions and triage_counter()
# answer=true is set a such to allow for restarting the program
answer=True
while answer:
    initial_questions()
    triage_counter()
