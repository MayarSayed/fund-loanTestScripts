import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getLoanPageURL():
        url=config.get('common URls','loanPageUrl')
        return url

    @staticmethod
    def getBankAccountPageURL():
        url=config.get('common URls','bankAccountPageUrl')
        return url

    @staticmethod
    def getAddBalancePageURL():
        url=config.get('common URls','addBalancePageUrl')
        return url
    
    @staticmethod
    def getAddBankAccountPageURL():
        url=config.get('common URls','addBankAccountPageUrl')
        return url
