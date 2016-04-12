import requests

def main():

    apikey = '7ce4357d5461cb54c0e8da53a03fa862:18:74619061'
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'

    payload = {'q': 'Obama', 'fq':{'source':['Reuters','AP', 'The New York Times']}, 'begin_date': 20150407, 'end_date': 20160409,'sort':'oldest', 'api-key': apikey}

    r = requests.get(url, params=payload)
    print(r.url)

if __name__== "__main__":
    main()
