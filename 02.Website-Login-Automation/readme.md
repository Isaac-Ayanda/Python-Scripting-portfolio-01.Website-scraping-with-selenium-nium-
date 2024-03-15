#  Website  Login Automation

## The goal of this project is to create a script that will automate the login into a website using supplied credentials  and perform further functions such as clicking on the home menu:

![Login page](./images/loginpage.png)

### By inspecting the elements of the username and password input boxes on the webpage; we use find_element by  id since the input elements has an id attribute. 
![Inspect element username](./images/inspect.png)
![Inspect element password](./images/inspect2.png)
### Then write the script that uses the supplied credential to login to the page using the send.keys functions which expecting "automated" as username annd "automatedautomated" as the password.
![Script](./images/codeupdate.png)
### To see the script in action, add a delay in between both actions with 2 seconds using the time module. Then import an object from selenium that helps to press enter from the key board using RETURN key
![Script  with delay](./images/codeupdateWT.png)
![Script  with delay](./images/codeupdateWT.png)
### Action
![Login](./images/login.png)
![Login](./images/login2.png)
### Next is to perform other functions after login like clicking on the Home menu for insntance. To do this, we use the xpath of the home menu. Also we want to scrap the dynamic figure of the average world temporature:
![Login](./images/xpathh.png)
![Dynamic figure](./images/dynamic-output1.png)
![Dynamic output](./images/dynamic-output.png)

### Futher step would be to extract and save the temperature into generated files every two seconds.  We use a loop and modify the script accordingly to extract the values to a text file with the name of the file as the date and time the values that are saved.   
![generate file](./images/generatef.png)
### Action
![generate file](./images/generatef2.png)

## Another Login Automation Example
### Here we create an account on a retailer website and creat a script that login and click on the contact us menu

![Code Script](./images/login-retail-scripta.png)
![Code Script](./images/login-retail-script.png)

### Action
[Click to watch - Video of Runing Script](https://drive.google.com/file/d/1AEf8WZoZ9Lfm1HO4Az9eIbGdVofLVXbX/view?usp=sharing)
![Script run successfully](./images/script-ran.png)

## Futher Automation Example - Extracting Real-Time currency rates
### From x-rates we scrap real-time currency rates between two pair of currencies. The manual approach is to go to the currency calculator on the website and type in the desired currency pair to see the current rate. By observing  url changes we able to set appropriate url attributes. Then we can use beatiful soup library to scrap the rates directly. 
```
If you dont have it already, you can install beatiful soup using: >pip install beautifulsoup4
```
#### First we construct the url for dynamic currency rates and run it to test that it working
![url construct](./images/url-test.png)
![url construct](./images/url-test2.png)

### Then access the source code of the page using request
```
If you dont have it already, you can install request using: >pip install request
```
![Code Script](./images/get-url-content.png)
![Code Script](./images/get-url-content2.png)

