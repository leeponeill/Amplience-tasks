# Amplience-tasks
Task 1

Attempt 1 user ID can be entered seperatly from URL.
When it is ran the request is made and made to the API and the response is defined as response
The response is then printed out for the catergories asked for in the text

Attempt 2 user ID can be entered seperatly from URL.
The user can then enter the expected values into the catogories listed
When it is ran the request is made and made to the API and the response is defined as response
The response is compared to the initial expected values using if statements. If the responce matches the initial expected value, then a message saying the category matches is printed. 
If they don't match then the amessage is printed allerting the user and displaying the value that was received from the API


Task 2

selenium was Pip installed
web driver for google Chrome was downloaded onto PC and saved in known path.
The path where the web driver was installed was defined as a string as PATH, so if ran on another machine PATH may need to be changed.
The input ID can be entered in ID
The code can be ran.
Results for category list is displayed as either matching or not matching.


When it is ran the request is made and made to the API and the response is defined as response
the results from the API for those Categories are defined as "category name"0 eg name0
A chrome page is opend to the Github page for the saame User as the API
The Name is read using Xpath to find it and asigned to name1
company is read using css_selector because the company can be in different places depending on how full the page is. there is also a Try check here if the page doesn't have a company then company1 is defined as "None"
location is read using the classnsaam because the location can be in different places depending on how full the page is. there is also a Try check here if the page doesn't have a location then location1 is defined as "None"
Public repos number is read using Xpath to find it and asigned to public_repos_1
following and followers are read using css_selector, because they were in two different places depending on the profile opened.

values from AIP are then compared to the values read from the browser and if they match that is prnted
if they don't match then both the AIP and Browser value is printed to compare them manualy.
