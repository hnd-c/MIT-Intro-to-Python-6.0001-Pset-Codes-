## 6.0001 Pset 1: Part b
## Name:Hem N Chaudhary
## Time Spent:20 mins
## Collaborators:None

#####################################################################
## Get user input for salary, savings_percent and total_cost below ##
#####################################################################
salary=float(input("Please enter your anaul salary:"))
savings_percent=float(input("Please enter the saving percent you are getting in decimal format:"))
total_cost=float(input("Please enter the total cost of your dream house:"))
raise_percentage=float(input("Please enter the semi-annual salary raise in a decimal percentage:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
percent_down_payment = 0.15
amount_saved=0
r = 0.05 #rate of return on savings
months=0 
total_saving=0
downpayment_cost=total_cost*percent_down_payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
while downpayment_cost>total_saving:
    
    total_saving=total_saving*(1+r/12)+salary*savings_percent/12 #first part is compound return on saving and second part is saving each months but the salary is annual so dividing by 12 to convert into monthly sallary 
    months+=1
    if months%6==0: #raises the salary after every 6 months
        salary=salary*(1+raise_percentage)
        

#######################################################
## Print out the number of months it would take here ##
#######################################################

print("The number of months it would take is:",months)
