print("Welcome to the secret auction bidding!")
bidders = {

}    
name1 = input("What is your name? : ")
bid1 = int(input("Enter your bidding amount : $"))
bidders[name1] = bid1
q = input("Are there any other bidders? , type yes or no : ").lower()
while q == "yes" :
    print(" " *100000 )
    name = input("What is your name? : ")
    bid = int(input("Enter your bidding amount : $"))
    q = input("Are there any other bidders? , type yes or no : ").lower()
    bidders[name] = bid

highestbidder = max(bidders , key=bidders.get)
    
print(f"The item is sold to {highestbidder}")