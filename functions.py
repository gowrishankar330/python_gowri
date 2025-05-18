#def how_do_i_look (person, mood):
#    print(f"you look cool {person}!")
#    print(f"you look cool {person}! {mood}")
#how_do_i_look("gowri" , "happy")
#how_do_i_look("harish", "bored")
#how_do_i_look("hari", "otha")
#how_do_i_look("darsan", "sad")


#def display_invoice(username,amount,invoice):
#    print(f"hello {username}")
#    print(f"your due amount is {amount}, which is to be paid on {invoice}")
#display_invoice("gowri", 430 , "01/02")
#display_invoice("harish", 650 , "09/10")
#display_invoice("prathi", 780 ,"02/05")


#def add(x,y):
#    z= x+y
#return z
#def sub(x,y):
#    z =x-y
#    return z
#def multiply(x,y):
#    z =x*y
#    return z
#print(add(4,7))
#print(sub(5,2))
#print(multiply(4,4))


#def create_name(first, last):
#    first = first.capitalize()
#    last = last.lower()
#    return first + " " + last
#full_name = create_name("gowri", "shankar")
#print(full_name)


#def net_price(price , discount = 0.5, tax=0.5):
#    return price*(1-discount)*(1+tax)
#print(net_price(333))

#import time
#def timer(end, start=0):
#    for x in range(start, end):
#        print(x)
#        time.sleep(1)
#    print("done!")    
#timer(10,5)

#def call(greetings,title,first_name,last_name):
#    first_name= first_name.capitalize()
#    last_name= last_name.capitalize()
#    print(f"{greetings} {title} {first_name} {last_name}")
    
#call("bonjour",last_name="shankar",first_name="gowri",title="master")

#def phone_num(country_code,area_code,first_digit,last_digit):
#    return f"{country_code}-{area_code}{first_digit}{last_digit}"
#ccode = int(input("enter ur country code: "))
#acode = int(input("enter ur area code: "))
#firstnum = int(input("enter ur first three digit: "))
#lastnum = int(input("enter ur last five digit: "))
#number = phone_num(first_digit=firstnum,last_digit=lastnum,country_code=ccode,area_code=acode)
#print(number)

#def add(*value):
#    total = 0
#    for x in value:
#        total = total+x
#    return total

#print(add(1,2,4,5,6))


#def display_name(*name):
#    for x in name:
#        y= x.capitalize()
#        print(y, end=" ")
#    print()
#display_name("Dr.","kavi","deva"," ","MEM")

#def adress(**type):
#    for x, y in type.items():
#        print(f"{x}-{y}")
#adress(area="thiruvanmiyur",state="tamilnadu",pincode=614804)



#def label(*person, **adress):
#    for x in person:
#        print(x,end=" ")
#    print()
#    for x , y in adress.items():
#        print(f"{x}-{y}")
#label("Dr.","kavi","deva"," ","MEM",area="thiruvanmiyur",state="tamilnadu",pincode=614804)




def label(*person, **adress):
    for x in person:
        print(x,end="")
    print()
    print(f"{adress.get('area')} {adress.get('state')} {adress.get('pincode')}")
label("Dr.","kavi","deva"," ","MEM",area="thiruvanmiyur",state="tamilnadu",pincode=614804)