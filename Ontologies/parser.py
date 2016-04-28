import requests
import json
import os
import codecs
import subprocess
from io import StringIO



def collect(section):

    for num in range(1,101):
            with open(str(num)+'.json') as data_file:
                data = json.load(data_file)

                for item in range(0,10):
                    final_data = (data["response"]["docs"][item][section])
                    print(final_data)


if __name__== "__main__":
    collect("lead_paragraph") #Whichever section you need information from (e.g. web_url, publication date, abstract, etc.)
