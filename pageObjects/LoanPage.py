from Locators.locators import Locators

class LoanPage():
    loan_Error_Message_Id  = Locators.loanErrorMessageId
    loan_Succes_Message_Id = Locators.loanSuccesMessageId
    loanButton             = Locators.fundLoanButtonId
    
    def __init__(self,driver):
        self.driver= driver
        
    
    def clickLoanButton(self):
        self.driver.find_element_by_id(self.loanButton).click()
    
    def succesMessageAppears(self):
        succesMessage = self.driver.find_element_by_id(self.loan_Succes_Message_Id)
        if(succesMessage.isDisplayed()):
            return True
        else:
            return False
        
    def errorMessageAppears(self):
        errorMessage = self.driver.find_element_by_id(self.loan_Error_Message_Id)
        if(errorMessage.isDisplayed()):
            return True
        else:
            return False