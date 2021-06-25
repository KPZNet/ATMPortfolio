
import json
import os.path
import jsonpickle

class Transaction (  ) :

    def __init__(self):
        self.ID = 0
        self.amount

class EnterPIN (  ) :

    def __init__(self):
        self.ID = 0
        self.pin



class DataStore():

    def __init__(self) :
        self.workOrders = {}
        self.balance

    def __del__(self) :
        pass

    def WriteDataStore(self) :
        jp = jsonpickle.encode(self)
        with open ( "BankAccount.json", "w" ) as outfile :
            outfile.write ( jp )



    def AddWorkOrder(self, workOrder):

       if str(workOrder.potHoleID) in self.potHoles:
           ph = self.potHoles[str(workOrder.potHoleID)]
           workOrder.location = ph.streetAddress
           workOrder.size  = ph.size
           self.nextWorkOrderID = self.nextWorkOrderID + 1
           workOrder.ID = self.nextWorkOrderID
           self.workOrders[str(self.nextWorkOrderID)] = workOrder
       return workOrder

    def AddDamageClaim(self, damageClaim):
       self.nextdamageClaimID = self.nextdamageClaimID + 1
       damageClaim.ID = self.nextdamageClaimID
       self.damageClaims[str(self.nextdamageClaimID)] = damageClaim
       return damageClaim

    @staticmethod
    def FactoryDataRestore():
        try :
            if os.path.isfile ( 'PotHoles.json' ) :
                with open ( 'PotHoles.json', 'r' ) as openfile :
                    json_object = openfile.read()
                    pt = jsonpickle.decode ( json_object )
                    return pt
            else:
                return DataStore()
        except(Exception) as e:
            return DataStore()
        finally :
            pass

    @staticmethod
    def FactoryDataSave(ds):
        try :
            jp = jsonpickle.encode ( ds )
            with open ( "PotHoles.json", "w" ) as outfile :
                outfile.write ( jp )
        except(Exception) as e:
            pass
        finally :
            pass