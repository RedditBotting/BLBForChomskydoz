#Imports
import requests

#Properties
baseURL = "https://www.archive.is/submit/"
allowedAttempts = 3


#Functions
def archive(urlToArchive):
    attempt = 0
    returnValue = None
    while attempt < allowedAttempts:
        try:
            req = requests.post(baseURL, data={'url': urlToArchive}, timeout=60)
            if req.status_code == 200:
                returnValue = req.url
                break
        except:
            attempt += 1
    return returnValue