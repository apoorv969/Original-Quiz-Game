print("--------------Welcome In My Quiz Game----------------")
ans=input("Do you want to start the game?").upper()
if ans=="YES":
    score=0
    print("Let's begin")
    q1=input("What is 3+9?").lower()
    if q1=="12" or q1=="twelve":
        print("The answer is correct.")
        score+=1
    else:
        print("The answer is incorrect.")
        score=score-0.25
    q2=input("What is the color of sky?").lower()
    if q2=="blue":
        print("The answer is correct.")
        score+=1
    else:
        print("The answer is incorrect.")
        score-=0.25
else:
    print("Okay bye")
print("Score obtained is:",score)
