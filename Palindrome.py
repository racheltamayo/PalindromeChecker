
def main():
    i_nput=input("input:")  
    if(i_nput==i_nput[::-1]):  
          print("output: ",  str(i_nput) , " is a palindrome")
          main()
    else:  
          print("output: ",  str(i_nput) , " is  not a palindrome")
          main()

main()

