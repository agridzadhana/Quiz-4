ListofIP = [2.1,2.5,4,3]
def bns (IP):
    bonus = 500000
    bns = IP*bonus
    return bns

for IP in ListofIP:
    if IP > 2.5:
        print("Congratulation! You Win a Bonus : Rp", bns(IP))
    else :
        print("Sorry, Maybe Next Time!")