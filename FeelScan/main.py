import os
import webbrowser
import random
import ia

Angry = ["https://www.youtube.com/embed/UfcAVejslrU?rel=0&autoplay=1",
         "https://www.youtube.com/embed/-fFbeSykaJk?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=UDVtMYqUAyw?rel=0&autoplay=1",
         "https://www.youtube.com/embed/2EfLc_jP2g8?rel=0&autoplay=1",
         "https://www.youtube.com/embed/6PAeMgE1pEQ?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=d-diB65scQU?rel=0&autoplay=1"]

Sad = ["https://www.youtube.com/embed/pUZeSYsU0Uk?rel=0&autoplay=1",
       "https://www.youtube.com/embed/oN2Xs-MvxLw?rel=0&autoplay=1",
       "https://www.youtube.com/watch?v=SJsGISX8O8k?rel=0&autoplay=1",
       "https://www.youtube.com/embed/lp-EO5I60KA",
       "https://www.youtube.com/watch?v=Sfqt2KtSj-Q"]

Happy = ["https://www.youtube.com/watch?v=-bl7bEw3kgw?rel=0&autoplay=1",
         "https://www.youtube.com/embed/HgzGwKwLmgM?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=btPJPFnesV4?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=tx0b39P1XCs?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=qK5KhQG06xU?rel=0&autoplay=1"]

Tired = ["https://www.youtube.com/watch?v=nxGoVw0DTGs?rel=0&autoplay=1",
         "https://www.youtube.com/embed/C9IwBJYTwQ0?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=uSD4vsh1zDA?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=OPf0YbXqDm0?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=iSLwVaebsJg?rel=0&autoplay=1"]


def runnning_commands_shell():
    os.system(
        'imagesnap -d NexiGo N930AF FHD Webcam /Users/franciskouaho/PycharmProjects/pythonProject1/uploads/capture.jpg')
    return ia.main()


def main():
    feeling = runnning_commands_shell()

    print(f'emotion detecté : {feeling}')
    print(Happy[1])
    if feeling == "Happy":
        webbrowser.open(Happy[random.randint(0, 4)])
    elif feeling == "Sad":
        webbrowser.open(Sad[random.randint(0, 4)])
    elif feeling == "Angry":
        webbrowser.open(Angry[random.randint(0, 4)])
    elif feeling == "Tired":
        webbrowser.open(Tired[random.randint(0, 4)])
    else:
        webbrowser.open(Happy[random.randint(0, 4)])


main()
