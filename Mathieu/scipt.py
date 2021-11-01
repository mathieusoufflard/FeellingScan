import sys
from typing import Match
import webbrowser
import random

Angry = ["https://www.youtube.com/watch?v=UfcAVejslrU",
            "https://www.youtube.com/watch?v=-fFbeSykaJk",
            "https://www.youtube.com/watch?v=UDVtMYqUAyw",
            "https://www.youtube.com/watch?v=2EfLc_jP2g8",
            "https://www.youtube.com/watch?v=6PAeMgE1pEQ",
            "https://www.youtube.com/watch?v=d-diB65scQU"]
            

Sad = ["https://www.youtube.com/watch?v=pUZeSYsU0Uk",
            "https://www.youtube.com/watch?v=oN2Xs-MvxLw",
            "https://www.youtube.com/watch?v=SJsGISX8O8k&list=PLgzTt0k8mXzHcKebL8d0uYHfawiARhQja&index=2",
            "https://www.youtube.com/watch?v=lp-EO5I60KA",
            "https://www.youtube.com/watch?v=Sfqt2KtSj-Q&list=PLgzTt0k8mXzHcKebL8d0uYHfawiARhQja&index=9"]

Happy = ["https://www.youtube.com/watch?v=-bl7bEw3kgw",
            "https://www.youtube.com/watch?v=HgzGwKwLmgM",
            "https://www.youtube.com/watch?v=btPJPFnesV4",
            "https://www.youtube.com/watch?v=tx0b39P1XCs",
            "https://www.youtube.com/watch?v=qK5KhQG06xU"]

Tired = ["https://www.youtube.com/watch?v=nxGoVw0DTGs",
            "https://www.youtube.com/watch?v=C9IwBJYTwQ0",
            "https://www.youtube.com/watch?v=uSD4vsh1zDA",
            "https://www.youtube.com/watch?v=OPf0YbXqDm0",
            "https://www.youtube.com/watch?v=iSLwVaebsJg"]

if len(sys.argv) != 2:
    print("Usage: python3.10 scipt.py [FEELING]")
    sys.exit()

i = sys.argv[1]


def music(i):
    match i:
        case "Angry":
            webbrowser.open(Angry[random.randint(0, 4)])
            print(Angry[random.randint(0, 4)])
            return 0
        case "Sad":
            webbrowser.open(Sad[random.randint(0, 4)])
            return 0
        case "Happy":
            webbrowser.open(Happy[random.randint(0, 4)])
            return 0
        case "Tired":
            webbrowser.open(Tired[random.randint(0, 4)])
            return 0
        case _:
            print("Usage: [FEELING] must be Angry, Sad, Happy or Tired")   
            return 1
music(i)

#print(sys.argv[1])
#webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


