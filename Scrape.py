from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import os
import sys

Directory = "Online_Course_Info"
try:
    os.mkdir(Directory)
except:
    pass

ML = 'https://www.coursera.org/learn/machine-learning'
pyth0n = 'https://www.coursera.org/learn/python' 

def scrape(url):
    
    # opening the url and grabbing all data
    
    
    data = urlopen(url)
    page_html = data.read()
    page_soup = soup(page_html, 'html.parser')
    
    return page_soup

def extracting_and_saving(page_soup):
    
    
    
    #course name
    cors = page_soup.findAll('h1', {'class' : "title display-3-text"})
    try:
        course_name = cors[0].text
    except:
        raise Exception("Please provide link of a course only, not Specialization or something else")
        sys.exit(1)

    #opening the file
    file_name = Directory + '/' + course_name + str('.text')
    my_file = open(file_name, "w")

    #extracting Informations
    overview = page_soup.findAll('div', {'class' : 'rc-Overview'})
    description = overview[0].p.text + "\n\n"
    my_file.write("Course Name: " + str(course_name) + "\n\n")
    my_file.write(str(description)) # saving info in file

    
    create = overview[0].findAll('div', {'class' : 'headline-1-text creator-names'})
    created_info = create[0].text.replace(u'\xa0\xa0', u' ') + "\n\n"
    my_file.write(str(created_info))

    #Extracting Teacher Info
    taught = overview[0].findAll('div', {'class' : 'instructor-info bt3-col-xs-8 bt3-col-sm-10'})
    teacher_info = taught[0].text.replace(u'\xa0\xa0', u' ') + "\n\n"
    my_file.write(str(teacher_info))
    
    #Extracting Rating
    rating = overview[0].findAll('div', 'ratings-text bt3-visible-xs')
    average_rating = rating[0].text + "\n\n"
    my_file.write("Average rating : " + str(average_rating))

    #Extracting the syllabus and Study content info
    syllabus = page_soup.findAll('div', {'class' : 'week-body'})
    for i in range(len(syllabus)):
        
        week = syllabus[i].findAll('div', {'class' : 'module-name headline-2-text'})
        topic = week[0].text + "\n"
        my_file.write("Week" + str(i + 1) + "\n")
        my_file.write("Topic Name : " + str(topic))

        contents = syllabus[i].findAll('div', {'class' : 'summary horizontal-box'})
        content = contents[0].text
        content = content[0:len(content) - 6] + "\n\n"
        
        my_file.write("Study material: " + str(content))

    print("Data Extracted and saved in file....")
    my_file.close() #Closing the file     

