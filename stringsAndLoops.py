import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(raw_input())
    for i in range(a):
        myline = raw_input()
        numChars=len(myline)
        evenString=[]
        oddString=[]
        for j in range (numChars): 
            evenCounter=0;
            oddCounter=0
            if (j%2==0): # even
                evenString.append(myline[j])
            else:#oddstring
                oddString.append(myline[j])
        for i in range(len(evenString)):
            sys.stdout.write(evenString[i])
            
        sys.stdout.write(" ")
        for j in range(len(oddString)):
            sys.stdout.write(oddString[j])
        sys.stdout.write("\n")
