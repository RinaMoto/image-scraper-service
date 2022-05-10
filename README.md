# image-scraper-service
#### An image scraper microservice using serpApi.
* This program will read the keyword in the text file and rewrite it as an image URL 
* serpApi gives me a limit of 100 searches per month on the free plan. 
* You're welcome to create your own account and use your own API for more searches.
* For this reason, the program will continuously check to see if the content in the text file is a URL and will only run if it is NOT a URL

---
#### Activate the virtual environment before running the program to access the imported libraries.
```
To activate environment: source enviro/bin/activate
```
#### Enter keyword to be searched in the senator.txt file without quotations
```
For example: Senator [first_name] [last_name]
```
