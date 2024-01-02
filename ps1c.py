## 6.0001 Pset 1: Part c
## Name:Hem N Chaudhary
## Time Spent:40 mins
## Collaborators:None

#############################################
## Get user input for starting_amount below ##
#############################################
starting_amount=float(input("Please enter the initial amount in your savings account:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
downpayment_cost=750000*0.25
max_r=1
min_r=0
r=(max_r+min_r)/2
current_savings=starting_amount*(1+r/12)**(12*3)
steps=0
########################################################################################################
## Determine the lowest return on investment needed to get the down payment for your dream home below ##
########################################################################################################
if starting_amount>=downpayment_cost-100: #first exception
    r=0 
elif downpayment_cost-starting_amount*(1+1/12)**(12*3)>100: #second excpetion
    r=None
      
else:                                                      #normal case
    while abs(downpayment_cost-current_savings)>=100:
        steps+=1
        if current_savings>downpayment_cost:
            max_r=r 
        else:
            min_r=r

        r=(max_r+min_r)/2
            
        #print(steps)
        current_savings=starting_amount*(1+r/12)**(12*3)


##########################################################
## Print out the best savings rate and steps taken here ##
##########################################################
print("The best saving rate is:",r)
