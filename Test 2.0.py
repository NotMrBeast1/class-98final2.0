def countWords():
    fileName=input("Please Enter the File Name :- ")
    
    numberWords=0
    files = open(fileName, "r")
    for line in files:
        words=line.split()
        numberWords = numberWords+len(words)
    print("Number of Words :- ")
    print(numberWords)

countWords()
    





