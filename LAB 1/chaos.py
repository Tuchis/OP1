#this program ilustrates chaotic function

def main():
    print("This program illustrates a chaotic function") 
    X = float(input("Enter a number between 0 and 1: "))
    
    for i in range(10) :
        X = 3.9 * X * (1 - X)
        print(X)
main()