# QUESTION : You have to think the string as of collection of binary codes and if the bit 
    # is 0 then take the alphabet else if bit is 1 then exclude the alphabet and also if 2 or
    # more 1's are coming together then replace them by their sum.

# TEST CASE : "pep"
''' binary representation :   000 -> pep
                              001 -> pe1
                              010 -> p1p
                              011 -> p2
                              100 -> 1ep
                              101 -> 1e1
                              110 -> 2p
                              111 -> 3
'''
def permutation(s,ans="",x=0):
    if len(s)==0:           # base case
        if x==0:
            print(ans)
        else:
            print(ans+str(x))
        return

    # included
    if x==0:
        permutation(s[1:],ans+s[0],x)
    else:
        permutation(s[1:],ans+str(x)+s[0],0)

    permutation(s[1:],ans,x+1)      # excluded

    return 

string = input()
permutation(string)
