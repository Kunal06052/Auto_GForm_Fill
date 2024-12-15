# Auto_GForm_Fill
1.	Environment Setup: 
o	Python and Selenium: To begin, we ensure that Python and the necessary Selenium WebDriver are installed on the system. 
o	Chrome WebDriver: We use Chrome as the browser for automation. Therefore, we need to ensure the correct version of the Chrome WebDriver is downloaded and matched with the installed version of Google Chrome. 
Required Python Libraries: 
o	selenium: For browser automation. o 	time: To handle waits between actions. 
2.	Opening the Google Form: 
Using the selenium package, we open the target Google Form URL. This is done using the get() method of the webdriver object, which launches the Chrome browser and navigates to the specified URL. 
3.	Filling the Google Form: 
o	To fill the form fields, we identify each input element using XPath. These can be obtained by inspecting the Google Form HTML structure and locating the unique identifiers for each form field. 
o	Once we have the element identifiers, we use the appropriate Selenium WebDriver methods ( send_keys() ) to input data into the form fields. 
4.	Submitting the Form: 
Once all the fields are filled, we submit the form by identifying the submit button (usually with an XPath selector for the "Submit" button) and clicking it. 
5.	Capturing a Screenshot: 
After the form is successfully submitted, we wait for the confirmation page to load. Once it loads, we capture a screenshot of the page using the get_screenshot_as_file() method from Selenium. 
6.	Closing the Browser: 
After completing the task and capturing the screenshot, we close the browser session using the quit() method of the WebDriver to free up system resources. 
driver.quit() 
7.	Sending the Email with Attachment: 
As per the assignment requirement, the automation script must also send an email with the screenshot as an attachment. This can be done using Django's email functionality or Python's built-in email libraries. 
 
