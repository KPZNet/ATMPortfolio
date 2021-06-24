
import json
import os.path
import jsonpickle

class PotHole (  ) :

    def __init__(self):
        self.ID = 0
        self.streetAddress = "NONE"
        self.district = "NONE"
        self.location = "NONE"
        self.severity = "NONE"
        self.size = 0
        self.priority = "NONE"

    def CalculatePriority(self):
        self.priority = "LOW"
        if self.size > 3:
            self.priority = "MEDIUM"
        if self.size > 8:
            self.priority = "HIGH"

    def CaculateDistrict(self):
        self.district = "District-13"
        if "East" in self.streetAddress:
            self.district = "East District"
        if "West" in self.streetAddress:
            self.district = "West District"
        if "South" in self.streetAddress:
            self.district = "South District"
        if "North" in self.streetAddress:
            self.district = "North District"

class WorkOrder (  ) :
    hourRate = 20.00
    fillerMaterialCost = 56.75
    backHoeCost = 450.00
    shovelCost = 20.00
    pickCost = 15.00
    mixerCost = 150.00
    standardEquipCost = 100.00

    def __init__(self):
        self.ID = 0
        self.potHoleID = 0
        self.repairCrewID = 0
        self.numberOfWorkers = 0
        self.equipmentAssigned = ""
        self.hoursApplied = 0
        self.holeStatus = ""
        self.fillerMaterial = 0
        self.location = ""
        self.size = 0
        self.costEstimate = 0.0

    def CalculateCostEsimate(self):
        ceh = (self.hourRate * self.hoursApplied * self.numberOfWorkers)
        cem = (self.fillerMaterialCost*self.fillerMaterial)

        equipCost = self.standardEquipCost
        if "backhoe" in self.equipmentAssigned:
            equipCost = equipCost + self.backHoeCost
        if "mixer" in self.equipmentAssigned:
            equipCost = equipCost + self.mixerCost
        if "shovel" in self.equipmentAssigned:
            equipCost = equipCost + self.shovelCost
        if "pick" in self.equipmentAssigned:
            equipCost = equipCost + self.pickCost

        self.costEstimate = equipCost + cem + ceh

class DamageClaim (  ) :

    def __init__(self):
        self.ID = 0
        self.potHoleID = 0
        self.name = ""
        self.address = ""
        self.phone = ""
        self.damageType = ""
        self.dollarAmount = 0.0
        self.approved = False

class DataStore():

    def __init__(self) :
        self.potHoles = {}
        self.workOrders = {}
        self.damageClaims = {}
        self.nextPotHoleID = 0
        self.nextWorkOrderID = 0
        self.nextdamageClaimID = 0

    def __del__(self) :
        pass

    def WriteDataStore(self) :
        jp = jsonpickle.encode(self)
        with open ( "PotHoles.json", "w" ) as outfile :
            outfile.write ( jp )

    def GetAllPotHolesReport(self):
        return self.potHoles

    def GetAllWorkOrdersReport(self):
        return self.workOrders

    def GetAllDamageClaimReport(self):
        return self.damageClaims

    def AddPotHole(self, pothole):
       self.nextPotHoleID = self.nextPotHoleID + 1
       pothole.ID = self.nextPotHoleID
       self.potHoles[str(self.nextPotHoleID)] = pothole
       return pothole

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