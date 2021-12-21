def SumDigits(n):
    if n==0:
        return 0
    else:
        return n%10+SumDigits(n/10)
def main():
    n=int(input('Enter a natural no.: '))
    print(SumDigits(n))

if __name__=='__main__':
    main()
