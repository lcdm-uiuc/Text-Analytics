import json
import requests
import os

def main():

    apikey = '<Your API KEY>'
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'

    for num in range(1,50):
        payload = {'section_name': 'Politics', 'fq':{'source':['Reuters','AP', 'The New York Times']}, 'page': num, 'begin_date': 20070101, 'end_date': 20160411,'sort':'oldest', 'api-key': apikey}
        r = requests.get(url, params=payload)
        print(r.url)
        os.system("wget '" + str(r.url) + "'")


if __name__== "__main__":
    main()


#Section Name Values

#Arts
#Automobiles
#Autos
#Blogs
#Books
#Booming
#Business
#Business Day
#Corrections
#Crosswords & Games
#Crosswords/Games
#Dining & Wine
#Dining and Wine
#Editors' Notes
#Education
#Fashion & Style
#Food
#Front Page
#Giving
#Global Home
#Great Homes & Destinations
#Great Homes and Destinations
#Health
#Home & Garden
#Home and Garden
#International Home
#Job Market
#Learning
#Magazine
#Movies
#Multimedia
#Multimedia/Photos
#N.Y. / Region
#N.Y./Region
#NYRegion
#NYT Now
#National
#New York
#New York and Region
#Obituaries
#Olympics
#Open
#Opinion
#Paid Death Notices
#Public Editor
#Real Estate
#Science
#Sports
#Style
#Sunday Magazine
#Sunday Review
#T Magazine
#T:Style
#Technology
#The Public Editor
#The Upshot
#Theater
#Times Topics
#TimesMachine
#Today's Headlines
#Topics
#Travel
#U.S.
#Universal
#UrbanEye
#Washington
#Week in Review
#World
#Your Money
