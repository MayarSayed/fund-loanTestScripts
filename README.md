# Fund Loan Test Scripts

## Used Language and Packages
* Python Language
* Selenium: selenium libraries for automation
* Pytest: python unit test Framework
* OpenPyXL : to read input data

## Folder Structure
**Fund-loanTestScripts** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pageObjects<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loanPage.py -> Class for a Loan page <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Configurations <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config.ini -> containing data values so no hard coded values will be included in testcases <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Drivers<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chromedriver.exe -> exe for using Chrome driver  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;geckodriver ->exe for using Firefox driver <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Locators<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;locators.py -> Containing the pages element locators to abstract them outside the code<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;testCases<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains all testCase.py files to be performed<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains DDT_Data.xlsx file which contains Data-Driven Test data to be used as data inputs <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Utilities <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;readProperties.py -> to read common data from ini file <br />


## Test Cases
* Valid Path (Happy Path)
* Invalid Path (Sad Path)






