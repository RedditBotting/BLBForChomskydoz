#Imports
import mechanize

#Properties
baseURL = "https://www.archive.is/"
browser = mechanize.Browser()
allowedAttempts = 3

#Functions
def archive(urlToArchive):
	attempt = 0
	returnValue = None
	while attempt < allowedAttempts:
		try: 
			browser.open(baseURL)	
			browser.select_form(nr=0)
			browser.form["url"] = urlToArchive

			req = browser.submit()
			returnValue = req.geturl()
			break
		except: 
			attempt += 1
	return returnValue