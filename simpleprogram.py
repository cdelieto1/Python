#Python 2.7 
#Author: Cassie Delieto
#January 3, 2017

dictionary = {"Cozmo robot":"$175","LG5":"$400","iPhone7":"$650","Fitbit":"$125"} #dict key:value

def show_inventory(name):
        if name!="":
            print("\nThank you for buying with ThingsYouDontNeed.com, {}!\n".format(name))
            print ("Here is a list of what we sell:\n")
            for item,value in dictionary.items():
                    print item,value

def what_user_picked_out(item,total):
        item=raw_input("\nPlease type in 1 item you'd like to place and we will calculate the price after tax for you:").lower()
        if item == "cozmo robot":
            totalnow = (total*175)
            print totalnow
            #return totalnow
        elif item == "lg5":
            totalnow = (total*400)
            print totalnow
            #return totalnow
        elif item == "iphone7":
            totalnow = (total*650)
            print totalnow
            #return totalnow
        elif item == "fitbit":
            totalnow = (total*125)
            print totalnow 
            #return totalnow
        else:
            print ("Pick something")

                
def get_shipping_costs(country,totalnow):   
    if country == "us":
        if totalnow <= 1:
            return 160.00
        elif totalnow <= 3:
            return 190.00
        elif totalnow <= 5:
            return 1200.00
        else:
            print "FREE!"
            return 0.00

    if country == "canada":
        if totalnow <= 1:
            return 160.00
        elif totalnow <= 3:
            return 190.00
        elif totalnow <= 5:
            return 1500.00
        else:
            print "FREE!"
            return 0.00
        
def return_to_basket(name):          
    stop = True
    while stop:
        choice = raw_input("\nDo you want to empty the basket and start over? y/n: ").lower()
        if choice == "y":
                print("\nLet's start over!")
                show_inventory(name)
                stop = False
        elif choice == "n":
           print("\nThank you for your purchase!")
           stop = False
           exit()
        else:
           print("\nPlease enter 'y' for 'yes', 'n' for 'no'...")
                

name = raw_input("What is your name?").capitalize()
show_inventory(name)
what_user_picked_out(item="",total=1.03)
country = raw_input('What country do you live in? (US/Canada): ').lower()
sum_total = int(raw_input('What is the total amount for your online shopping after tax?'))
shipping_cost = get_shipping_costs(country, sum_total)
print 'Your shipping costs to %s are $%s0' % (country.title(), str(shipping_cost))
return_to_basket(name)


