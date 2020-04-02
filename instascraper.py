from selenium import webdriver
from bs4 import BeautifulSoup as bs

userlist=['triangl0321','_iamhritik']#Add all your usernames here to get their data very easily.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
for username in userlist:
	postdata=[]
	profiledata=[]
	driver.get('https://www.instagram.com/'+username+'/?hl=en')
	Pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	source = driver.page_source
	data=bs(source, 'html.parser')
	body = data.find('body')
	profiles = driver.find_elements_by_class_name('_6q-tv')
	posts = driver.find_elements_by_class_name('FFVAD')
	Title1 = ['PROFILE PICTURE URL']
	Title2 = ['POSTS URL']
	newline = ['  ']
	print("Found data for this user: "+username)
	filename=username+".csv"
	with open(filename, 'w')as csvfile: 
	    	csvwriter=csv.writer(csvfile,delimiter=',')
	    	csvwriter.writerow(Title1) 
	    	for profile in profiles:
	    		sourceprofile = (profile.get_attribute('src'))
	    		profiledata.append(sourceprofile)
	    		csvwriter.writerow(profiledata)
	    		csvwriter.writerow(newline)
			profiledata=[]
	    	csvwriter.writerow(Title2) 
	    	for post in posts:
	    		sourceposts = (post.get_attribute('src'))
	    		postdata.append(sourceposts)
	    		csvwriter.writerow(postdata)
			postdata=[]
driver.close()  
print("Successfully stored all the data in the csv file format.\nThanks for using it.")
#made by hritik. :)
         



