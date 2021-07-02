
import json
import os.path
import jsonpickle

class Transaction (  ) :

    def __init__(self):
        self.accountNumber = 5
        self.ID = 9
        self.amount
        self.datetime

class EnterPIN (  ) :

    def __init__(self):
        self.ID = 0
        self.pin



class BankAccount():

    def __init__(self) :
        self.transactions = {}
        self.balance = 0
        self.nextTransactionID = 0
        self.cardNumber = "999"
        self.pin = 5566
        self.currentRetry = 0

    def __del__(self) :
        pass

    def WriteDataStore(self) :
        jp = jsonpickle.encode(self)
        with open ( "BankAccount.json", "w" ) as outfile :
            outfile.write ( jp )

    def AddTransaction(self, transaction):

       self.nextTransactionID = self.nextTransactionID + 1
       transaction.ID = self.nextTransactionID
       self.transactions[str(self.nextTransactionID)] = transaction
       return transaction


    @staticmethod
    def FactoryDataRestore():
        try :
            if os.path.isfile ( 'BankAccount.json' ) :
                with open ( 'BankAccount.json', 'r' ) as openfile :
                    json_object = openfile.read()
                    pt = jsonpickle.decode ( json_object )
                    return pt
            else:
                return BankAccount()
        except(Exception) as e:
            return BankAccount()
        finally :
            pass

    @staticmethod
    def FactoryDataSave(ds):
        try :
            jp = jsonpickle.encode ( ds )
            with open ( "BankAccount.json", "w" ) as outfile :
                outfile.write ( jp )
        except(Exception) as e:
            pass
        finally :
            pass