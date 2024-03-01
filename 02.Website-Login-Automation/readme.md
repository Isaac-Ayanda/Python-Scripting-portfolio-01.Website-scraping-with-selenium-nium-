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
### Next is to perform other functions after login like clicking on the Home menu for insntance. To do this, we use the xpath of the home menu
![Login](./images/xpathh.png)