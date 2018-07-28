from Scrape import scrape, extracting_and_saving

Ml_url = 'https://www.coursera.org/learn/machine-learning'
python_url = 'https://www.coursera.org/learn/python'
English_url = 'https://www.coursera.org/learn/speak-english-professionally'
Advanced_Modeling = 'https://www.coursera.org/learn/advanced-modeling'

samples = {'ML' : Ml_url, 'Python' : python_url, 'English' :  English_url, 'Modeling' : Advanced_Modeling}

choice = input("Would You like to scrape your own course or chose from sample courses?\n\nPress 'O' for own website else press 'S' and hit Enter\n>> ")


def Start(url):
    page_soup = scrape(url)
    extracting_and_saving(page_soup)


if choice == "O" or choice == "o":
    own = input("Enter Your Link\n: ")
    url = own
    Start(url)  

elif choice == "S" or choice == "s":

    for i in range(len(samples)):
        print(str(i + 1), list(samples)[i] +'\n')

    crs = input("Enter course Name\n >> ")
    url = crs
    Start(samples[url])

else :
    print("Please give correct input and try again:)")
    


