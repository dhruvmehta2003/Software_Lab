# %% NEW FILE ProductSource BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 10 "../../model.ump"
# line 80 "../../model.ump"
import os

class ProductSource():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #ProductSource Attributes
    #ProductSource Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aAdvertisedCostPerUnit, aProduct, aSupplier):
        self._supplier = None
        self._product = None
        self._supplierOrderLineItems = None
        self._advertisedCostPerUnit = None
        self._advertisedCostPerUnit = aAdvertisedCostPerUnit
        self._supplierOrderLineItems = []
        didAddProduct = self.setProduct(aProduct)
        if not didAddProduct :
            raise RuntimeError ("Unable to create productSource due to product. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddSupplier = self.setSupplier(aSupplier)
        if not didAddSupplier :
            raise RuntimeError ("Unable to create productSource due to supplier. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setAdvertisedCostPerUnit(self, aAdvertisedCostPerUnit):
        wasSet = False
        self._advertisedCostPerUnit = aAdvertisedCostPerUnit
        wasSet = True
        return wasSet

    def getAdvertisedCostPerUnit(self):
        return self._advertisedCostPerUnit

    # Code from template association_GetMany 
    def getSupplierOrderLineItem(self, index):
        aSupplierOrderLineItem = self._supplierOrderLineItems[index]
        return aSupplierOrderLineItem

    def getSupplierOrderLineItems(self):
        newSupplierOrderLineItems = tuple(self._supplierOrderLineItems)
        return newSupplierOrderLineItems

    def numberOfSupplierOrderLineItems(self):
        number = len(self._supplierOrderLineItems)
        return number

    def hasSupplierOrderLineItems(self):
        has = len(self._supplierOrderLineItems) > 0
        return has

    def indexOfSupplierOrderLineItem(self, aSupplierOrderLineItem):
        index = (-1 if not aSupplierOrderLineItem in self._supplierOrderLineItems else self._supplierOrderLineItems.index(aSupplierOrderLineItem))
        return index

    # Code from template association_GetOne 
    def getProduct(self):
        return self._product

    # Code from template association_GetOne 
    def getSupplier(self):
        return self._supplier

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfSupplierOrderLineItems():
        return 0

    # Code from template association_AddManyToOne 
    def addSupplierOrderLineItem1(self, aNumberOrdered, aDateExpected, aOrderToSupplier):
        from SupplierOrderLineItem import SupplierOrderLineItem
        return SupplierOrderLineItem(aNumberOrdered, aDateExpected, self, aOrderToSupplier)

    def addSupplierOrderLineItem2(self, aSupplierOrderLineItem):
        wasAdded = False
        if (aSupplierOrderLineItem) in self._supplierOrderLineItems :
            return False
        existingProductSource = aSupplierOrderLineItem.getProductSource()
        isNewProductSource = not (existingProductSource is None) and not self == existingProductSource
        if isNewProductSource :
            aSupplierOrderLineItem.setProductSource(self)
        else :
            self._supplierOrderLineItems.append(aSupplierOrderLineItem)
        wasAdded = True
        return wasAdded

    def removeSupplierOrderLineItem(self, aSupplierOrderLineItem):
        wasRemoved = False
        #Unable to remove aSupplierOrderLineItem, as it must always have a productSource
        if not self == aSupplierOrderLineItem.getProductSource() :
            self._supplierOrderLineItems.remove(aSupplierOrderLineItem)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addSupplierOrderLineItemAt(self, aSupplierOrderLineItem, index):
        wasAdded = False
        if self.addSupplierOrderLineItem(aSupplierOrderLineItem) :
            if index < 0 :
                index = 0
            if index > self.numberOfSupplierOrderLineItems() :
                index = self.numberOfSupplierOrderLineItems() - 1
            self._supplierOrderLineItems.remove(aSupplierOrderLineItem)
            self._supplierOrderLineItems.insert(index, aSupplierOrderLineItem)
            wasAdded = True
        return wasAdded

    def addOrMoveSupplierOrderLineItemAt(self, aSupplierOrderLineItem, index):
        wasAdded = False
        if (aSupplierOrderLineItem) in self._supplierOrderLineItems :
            if index < 0 :
                index = 0
            if index > self.numberOfSupplierOrderLineItems() :
                index = self.numberOfSupplierOrderLineItems() - 1
            self._supplierOrderLineItems.remove(aSupplierOrderLineItem)
            self._supplierOrderLineItems.insert(index, aSupplierOrderLineItem)
            wasAdded = True
        else :
            wasAdded = self.addSupplierOrderLineItemAt(aSupplierOrderLineItem, index)
        return wasAdded

    # Code from template association_SetOneToMany 
    def setProduct(self, aProduct):
        wasSet = False
        if aProduct is None :
            return wasSet
        existingProduct = self._product
        self._product = aProduct
        if not (existingProduct is None) and not existingProduct == aProduct :
            existingProduct.removeProductSource(self)
        self._product.addProductSource(self)
        wasSet = True
        return wasSet

    # Code from template association_SetOneToMany 
    def setSupplier(self, aSupplier):
        wasSet = False
        if aSupplier is None :
            return wasSet
        existingSupplier = self._supplier
        self._supplier = aSupplier
        if not (existingSupplier is None) and not existingSupplier == aSupplier :
            existingSupplier.removeProductSource(self)
        self._supplier.addProductSource(self)
        wasSet = True
        return wasSet

    def delete(self):
        i = len(self._supplierOrderLineItems)
        while i > 0 :
            aSupplierOrderLineItem = self._supplierOrderLineItems[i - 1]
            aSupplierOrderLineItem.delete()
            i -= 1

        placeholderProduct = self._product
        self._product = None
        if not (placeholderProduct is None) :
            placeholderProduct.removeProductSource(self)
        placeholderSupplier = self._supplier
        self._supplier = None
        if not (placeholderSupplier is None) :
            placeholderSupplier.removeProductSource(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "advertisedCostPerUnit" + ":" + str(self.getAdvertisedCostPerUnit()) + "]" + str(os.linesep) + "  " + "product = " + str(((format(id(self.getProduct()), "x")) if not (self.getProduct() is None) else "null")) + str(os.linesep) + "  " + "supplier = " + ((format(id(self.getSupplier()), "x")) if not (self.getSupplier() is None) else "null")

    def addSupplierOrderLineItem(self, *argv):
        from SupplierOrderLineItem import SupplierOrderLineItem
        if len(argv) == 3 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], OrderToSupplier) :
            return self.addSupplierOrderLineItem1(argv[0], argv[1], argv[2])
        if len(argv) == 1 and isinstance(argv[0], SupplierOrderLineItem) :
            return self.addSupplierOrderLineItem2(argv[0])
        raise TypeError("No method matches provided parameters")





# %% NEW FILE ReceivedLineItem BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 45 "../../model.ump"
# line 57 "../../model.ump"
import os

class ReceivedLineItem():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #ReceivedLineItem Attributes
    #ReceivedLineItem Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNumberReceived, aActualCostPerUnit, aReceivedDelivery, aSupplierOrderLineItem):
        self._supplierOrderLineItem = None
        self._receivedDelivery = None
        self._actualCostPerUnit = None
        self._numberReceived = None
        self._numberReceived = aNumberReceived
        self._actualCostPerUnit = aActualCostPerUnit
        didAddReceivedDelivery = self.setReceivedDelivery(aReceivedDelivery)
        if not didAddReceivedDelivery :
            raise RuntimeError ("Unable to create receivedLineItem due to receivedDelivery. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddSupplierOrderLineItem = self.setSupplierOrderLineItem(aSupplierOrderLineItem)
        if not didAddSupplierOrderLineItem :
            raise RuntimeError ("Unable to create receivedLineItem due to supplierOrderLineItem. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setNumberReceived(self, aNumberReceived):
        wasSet = False
        self._numberReceived = aNumberReceived
        wasSet = True
        return wasSet

    def setActualCostPerUnit(self, aActualCostPerUnit):
        wasSet = False
        self._actualCostPerUnit = aActualCostPerUnit
        wasSet = True
        return wasSet

    def getNumberReceived(self):
        return self._numberReceived

    def getActualCostPerUnit(self):
        return self._actualCostPerUnit

    # Code from template association_GetOne 
    def getReceivedDelivery(self):
        return self._receivedDelivery

    # Code from template association_GetOne 
    def getSupplierOrderLineItem(self):
        return self._supplierOrderLineItem

    # Code from template association_SetOneToMany 
    def setReceivedDelivery(self, aReceivedDelivery):
        wasSet = False
        if aReceivedDelivery is None :
            return wasSet
        existingReceivedDelivery = self._receivedDelivery
        self._receivedDelivery = aReceivedDelivery
        if not (existingReceivedDelivery is None) and not existingReceivedDelivery == aReceivedDelivery :
            existingReceivedDelivery.removeReceivedLineItem(self)
        self._receivedDelivery.addReceivedLineItem(self)
        wasSet = True
        return wasSet

    # Code from template association_SetOneToMany 
    def setSupplierOrderLineItem(self, aSupplierOrderLineItem):
        wasSet = False
        if aSupplierOrderLineItem is None :
            return wasSet
        existingSupplierOrderLineItem = self._supplierOrderLineItem
        self._supplierOrderLineItem = aSupplierOrderLineItem
        if not (existingSupplierOrderLineItem is None) and not existingSupplierOrderLineItem == aSupplierOrderLineItem :
            existingSupplierOrderLineItem.removeReceivedLineItem(self)
        self._supplierOrderLineItem.addReceivedLineItem(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderReceivedDelivery = self._receivedDelivery
        self._receivedDelivery = None
        if not (placeholderReceivedDelivery is None) :
            placeholderReceivedDelivery.removeReceivedLineItem(self)
        placeholderSupplierOrderLineItem = self._supplierOrderLineItem
        self._supplierOrderLineItem = None
        if not (placeholderSupplierOrderLineItem is None) :
            placeholderSupplierOrderLineItem.removeReceivedLineItem(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "numberReceived" + ":" + str(self.getNumberReceived()) + "," + "actualCostPerUnit" + ":" + str(self.getActualCostPerUnit()) + "]" + str(os.linesep) + "  " + "receivedDelivery = " + str(((format(id(self.getReceivedDelivery()), "x")) if not (self.getReceivedDelivery() is None) else "null")) + str(os.linesep) + "  " + "supplierOrderLineItem = " + ((format(id(self.getSupplierOrderLineItem()), "x")) if not (self.getSupplierOrderLineItem() is None) else "null")





# %% NEW FILE OrderToSupplier BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 39 "../../model.ump"
# line 74 "../../model.ump"
import os

class OrderToSupplier():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #OrderToSupplier Attributes
    #OrderToSupplier Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aPoNumber, aDateOrdered, aSupplier):
        self._supplier = None
        self._supplierOrderLineItems = None
        self._dateOrdered = None
        self._poNumber = None
        self._poNumber = aPoNumber
        self._dateOrdered = aDateOrdered
        self._supplierOrderLineItems = []
        didAddSupplier = self.setSupplier(aSupplier)
        if not didAddSupplier :
            raise RuntimeError ("Unable to create orderToSupplier due to supplier. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setPoNumber(self, aPoNumber):
        wasSet = False
        self._poNumber = aPoNumber
        wasSet = True
        return wasSet

    def setDateOrdered(self, aDateOrdered):
        wasSet = False
        self._dateOrdered = aDateOrdered
        wasSet = True
        return wasSet

    def getPoNumber(self):
        return self._poNumber

    def getDateOrdered(self):
        return self._dateOrdered

    # Code from template association_GetMany 
    def getSupplierOrderLineItem(self, index):
        aSupplierOrderLineItem = self._supplierOrderLineItems[index]
        return aSupplierOrderLineItem

    def getSupplierOrderLineItems(self):
        newSupplierOrderLineItems = tuple(self._supplierOrderLineItems)
        return newSupplierOrderLineItems

    def numberOfSupplierOrderLineItems(self):
        number = len(self._supplierOrderLineItems)
        return number

    def hasSupplierOrderLineItems(self):
        has = len(self._supplierOrderLineItems) > 0
        return has

    def indexOfSupplierOrderLineItem(self, aSupplierOrderLineItem):
        index = (-1 if not aSupplierOrderLineItem in self._supplierOrderLineItems else self._supplierOrderLineItems.index(aSupplierOrderLineItem))
        return index

    # Code from template association_GetOne 
    def getSupplier(self):
        return self._supplier

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfSupplierOrderLineItems():
        return 0

    # Code from template association_AddManyToOne 
    def addSupplierOrderLineItem1(self, aNumberOrdered, aDateExpected, aProductSource):
        from SupplierOrderLineItem import SupplierOrderLineItem
        return SupplierOrderLineItem(aNumberOrdered, aDateExpected, aProductSource, self)

    def addSupplierOrderLineItem2(self, aSupplierOrderLineItem):
        wasAdded = False
        if (aSupplierOrderLineItem) in self._supplierOrderLineItems :
            return False
        existingOrderToSupplier = aSupplierOrderLineItem.getOrderToSupplier()
        isNewOrderToSupplier = not (existingOrderToSupplier is None) and not self == existingOrderToSupplier
        if isNewOrderToSupplier :
            aSupplierOrderLineItem.setOrderToSupplier(self)
        else :
            self._supplierOrderLineItems.append(aSupplierOrderLineItem)
        wasAdded = True
        return wasAdded

    def removeSupplierOrderLineItem(self, aSupplierOrderLineItem):
        wasRemoved = False
        #Unable to remove aSupplierOrderLineItem, as it must always have a orderToSupplier
        if not self == aSupplierOrderLineItem.getOrderToSupplier() :
            self._supplierOrderLineItems.remove(aSupplierOrderLineItem)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addSupplierOrderLineItemAt(self, aSupplierOrderLineItem, index):
        wasAdded = False
        if self.addSupplierOrderLineItem(aSupplierOrderLineItem) :
            if index < 0 :
                index = 0
            if index > self.numberOfSupplierOrderLineItems() :
                index = self.numberOfSupplierOrderLineItems() - 1
            self._supplierOrderLineItems.remove(aSupplierOrderLineItem)
            self._supplierOrderLineItems.insert(index, aSupplierOrderLineItem)
            wasAdded = True
        return wasAdded

    def addOrMoveSupplierOrderLineItemAt(self, aSupplierOrderLineItem, index):
        wasAdded = False
        if (aSupplierOrderLineItem) in self._supplierOrderLineItems :
            if index < 0 :
                index = 0
            if index > self.numberOfSupplierOrderLineItems() :
                index = self.numberOfSupplierOrderLineItems() - 1
            self._supplierOrderLineItems.remove(aSupplierOrderLineItem)
            self._supplierOrderLineItems.insert(index, aSupplierOrderLineItem)
            wasAdded = True
        else :
            wasAdded = self.addSupplierOrderLineItemAt(aSupplierOrderLineItem, index)
        return wasAdded

    # Code from template association_SetOneToMany 
    def setSupplier(self, aSupplier):
        wasSet = False
        if aSupplier is None :
            return wasSet
        existingSupplier = self._supplier
        self._supplier = aSupplier
        if not (existingSupplier is None) and not existingSupplier == aSupplier :
            existingSupplier.removeOrderToSupplier(self)
        self._supplier.addOrderToSupplier(self)
        wasSet = True
        return wasSet

    def delete(self):
        i = len(self._supplierOrderLineItems)
        while i > 0 :
            aSupplierOrderLineItem = self._supplierOrderLineItems[i - 1]
            aSupplierOrderLineItem.delete()
            i -= 1

        placeholderSupplier = self._supplier
        self._supplier = None
        if not (placeholderSupplier is None) :
            placeholderSupplier.removeOrderToSupplier(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "poNumber" + ":" + str(self.getPoNumber()) + "," + "dateOrdered" + ":" + str(self.getDateOrdered()) + "]" + str(os.linesep) + "  " + "supplier = " + ((format(id(self.getSupplier()), "x")) if not (self.getSupplier() is None) else "null")

    def addSupplierOrderLineItem(self, *argv):
        from SupplierOrderLineItem import SupplierOrderLineItem
        if len(argv) == 3 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], ProductSource) :
            return self.addSupplierOrderLineItem1(argv[0], argv[1], argv[2])
        if len(argv) == 1 and isinstance(argv[0], SupplierOrderLineItem) :
            return self.addSupplierOrderLineItem2(argv[0])
        raise TypeError("No method matches provided parameters")





# %% NEW FILE SupplierOrderLineItem BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 34 "../../model.ump"
# line 68 "../../model.ump"
import os

class SupplierOrderLineItem():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #SupplierOrderLineItem Attributes
    #SupplierOrderLineItem Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNumberOrdered, aDateExpected, aProductSource, aOrderToSupplier):
        self._orderToSupplier = None
        self._productSource = None
        self._receivedLineItems = None
        self._dateExpected = None
        self._numberOrdered = None
        self._numberOrdered = aNumberOrdered
        self._dateExpected = aDateExpected
        self._receivedLineItems = []
        didAddProductSource = self.setProductSource(aProductSource)
        if not didAddProductSource :
            raise RuntimeError ("Unable to create supplierOrderLineItem due to productSource. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddOrderToSupplier = self.setOrderToSupplier(aOrderToSupplier)
        if not didAddOrderToSupplier :
            raise RuntimeError ("Unable to create supplierOrderLineItem due to orderToSupplier. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setNumberOrdered(self, aNumberOrdered):
        wasSet = False
        self._numberOrdered = aNumberOrdered
        wasSet = True
        return wasSet

    def setDateExpected(self, aDateExpected):
        wasSet = False
        self._dateExpected = aDateExpected
        wasSet = True
        return wasSet

    def getNumberOrdered(self):
        return self._numberOrdered

    def getDateExpected(self):
        return self._dateExpected

    # Code from template association_GetMany 
    def getReceivedLineItem(self, index):
        aReceivedLineItem = self._receivedLineItems[index]
        return aReceivedLineItem

    def getReceivedLineItems(self):
        newReceivedLineItems = tuple(self._receivedLineItems)
        return newReceivedLineItems

    def numberOfReceivedLineItems(self):
        number = len(self._receivedLineItems)
        return number

    def hasReceivedLineItems(self):
        has = len(self._receivedLineItems) > 0
        return has

    def indexOfReceivedLineItem(self, aReceivedLineItem):
        index = (-1 if not aReceivedLineItem in self._receivedLineItems else self._receivedLineItems.index(aReceivedLineItem))
        return index

    # Code from template association_GetOne 
    def getProductSource(self):
        return self._productSource

    # Code from template association_GetOne 
    def getOrderToSupplier(self):
        return self._orderToSupplier

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfReceivedLineItems():
        return 0

    # Code from template association_AddManyToOne 
    def addReceivedLineItem1(self, aNumberReceived, aActualCostPerUnit, aReceivedDelivery):
        from ReceivedLineItem import ReceivedLineItem
        return ReceivedLineItem(aNumberReceived, aActualCostPerUnit, aReceivedDelivery, self)

    def addReceivedLineItem2(self, aReceivedLineItem):
        wasAdded = False
        if (aReceivedLineItem) in self._receivedLineItems :
            return False
        existingSupplierOrderLineItem = aReceivedLineItem.getSupplierOrderLineItem()
        isNewSupplierOrderLineItem = not (existingSupplierOrderLineItem is None) and not self == existingSupplierOrderLineItem
        if isNewSupplierOrderLineItem :
            aReceivedLineItem.setSupplierOrderLineItem(self)
        else :
            self._receivedLineItems.append(aReceivedLineItem)
        wasAdded = True
        return wasAdded

    def removeReceivedLineItem(self, aReceivedLineItem):
        wasRemoved = False
        #Unable to remove aReceivedLineItem, as it must always have a supplierOrderLineItem
        if not self == aReceivedLineItem.getSupplierOrderLineItem() :
            self._receivedLineItems.remove(aReceivedLineItem)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addReceivedLineItemAt(self, aReceivedLineItem, index):
        wasAdded = False
        if self.addReceivedLineItem(aReceivedLineItem) :
            if index < 0 :
                index = 0
            if index > self.numberOfReceivedLineItems() :
                index = self.numberOfReceivedLineItems() - 1
            self._receivedLineItems.remove(aReceivedLineItem)
            self._receivedLineItems.insert(index, aReceivedLineItem)
            wasAdded = True
        return wasAdded

    def addOrMoveReceivedLineItemAt(self, aReceivedLineItem, index):
        wasAdded = False
        if (aReceivedLineItem) in self._receivedLineItems :
            if index < 0 :
                index = 0
            if index > self.numberOfReceivedLineItems() :
                index = self.numberOfReceivedLineItems() - 1
            self._receivedLineItems.remove(aReceivedLineItem)
            self._receivedLineItems.insert(index, aReceivedLineItem)
            wasAdded = True
        else :
            wasAdded = self.addReceivedLineItemAt(aReceivedLineItem, index)
        return wasAdded

    # Code from template association_SetOneToMany 
    def setProductSource(self, aProductSource):
        wasSet = False
        if aProductSource is None :
            return wasSet
        existingProductSource = self._productSource
        self._productSource = aProductSource
        if not (existingProductSource is None) and not existingProductSource == aProductSource :
            existingProductSource.removeSupplierOrderLineItem(self)
        self._productSource.addSupplierOrderLineItem(self)
        wasSet = True
        return wasSet

    # Code from template association_SetOneToMany 
    def setOrderToSupplier(self, aOrderToSupplier):
        wasSet = False
        if aOrderToSupplier is None :
            return wasSet
        existingOrderToSupplier = self._orderToSupplier
        self._orderToSupplier = aOrderToSupplier
        if not (existingOrderToSupplier is None) and not existingOrderToSupplier == aOrderToSupplier :
            existingOrderToSupplier.removeSupplierOrderLineItem(self)
        self._orderToSupplier.addSupplierOrderLineItem(self)
        wasSet = True
        return wasSet

    def delete(self):
        i = len(self._receivedLineItems)
        while i > 0 :
            aReceivedLineItem = self._receivedLineItems[i - 1]
            aReceivedLineItem.delete()
            i -= 1

        placeholderProductSource = self._productSource
        self._productSource = None
        if not (placeholderProductSource is None) :
            placeholderProductSource.removeSupplierOrderLineItem(self)
        placeholderOrderToSupplier = self._orderToSupplier
        self._orderToSupplier = None
        if not (placeholderOrderToSupplier is None) :
            placeholderOrderToSupplier.removeSupplierOrderLineItem(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "numberOrdered" + ":" + str(self.getNumberOrdered()) + "," + "dateExpected" + ":" + str(self.getDateExpected()) + "]" + str(os.linesep) + "  " + "productSource = " + str(((format(id(self.getProductSource()), "x")) if not (self.getProductSource() is None) else "null")) + str(os.linesep) + "  " + "orderToSupplier = " + ((format(id(self.getOrderToSupplier()), "x")) if not (self.getOrderToSupplier() is None) else "null")

    def addReceivedLineItem(self, *argv):
        from ReceivedLineItem import ReceivedLineItem
        if len(argv) == 3 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], ReceivedDelivery) :
            return self.addReceivedLineItem1(argv[0], argv[1], argv[2])
        if len(argv) == 1 and isinstance(argv[0], ReceivedLineItem) :
            return self.addReceivedLineItem2(argv[0])
        raise TypeError("No method matches provided parameters")





# %% NEW FILE Product BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
#*

#   * Positioning

#   
# line 15 "../../model.ump"
# line 51 "../../model.ump"

class Product():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Product Attributes
    #Product Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aOurCode, aDescription, aPicture, aOurListPricePerunit, aNumberInInventory, aNumberToKeepInv):
        self._productSources = None
        self._numberToKeepInv = None
        self._numberInInventory = None
        self._ourListPricePerunit = None
        self._picture = None
        self._description = None
        self._ourCode = None
        self._ourCode = aOurCode
        self._description = aDescription
        self._picture = aPicture
        self._ourListPricePerunit = aOurListPricePerunit
        self._numberInInventory = aNumberInInventory
        self._numberToKeepInv = aNumberToKeepInv
        self._productSources = []

    #------------------------
    # INTERFACE
    #------------------------
    def setOurCode(self, aOurCode):
        wasSet = False
        self._ourCode = aOurCode
        wasSet = True
        return wasSet

    def setDescription(self, aDescription):
        wasSet = False
        self._description = aDescription
        wasSet = True
        return wasSet

    def setPicture(self, aPicture):
        wasSet = False
        self._picture = aPicture
        wasSet = True
        return wasSet

    def setOurListPricePerunit(self, aOurListPricePerunit):
        wasSet = False
        self._ourListPricePerunit = aOurListPricePerunit
        wasSet = True
        return wasSet

    def setNumberInInventory(self, aNumberInInventory):
        wasSet = False
        self._numberInInventory = aNumberInInventory
        wasSet = True
        return wasSet

    def setNumberToKeepInv(self, aNumberToKeepInv):
        wasSet = False
        self._numberToKeepInv = aNumberToKeepInv
        wasSet = True
        return wasSet

    def getOurCode(self):
        return self._ourCode

    def getDescription(self):
        return self._description

    def getPicture(self):
        return self._picture

    def getOurListPricePerunit(self):
        return self._ourListPricePerunit

    def getNumberInInventory(self):
        return self._numberInInventory

    def getNumberToKeepInv(self):
        return self._numberToKeepInv

    # Code from template association_GetMany 
    def getProductSource(self, index):
        aProductSource = self._productSources[index]
        return aProductSource

    def getProductSources(self):
        newProductSources = tuple(self._productSources)
        return newProductSources

    def numberOfProductSources(self):
        number = len(self._productSources)
        return number

    def hasProductSources(self):
        has = len(self._productSources) > 0
        return has

    def indexOfProductSource(self, aProductSource):
        index = (-1 if not aProductSource in self._productSources else self._productSources.index(aProductSource))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfProductSources():
        return 0

    # Code from template association_AddManyToOne 
    def addProductSource1(self, aAdvertisedCostPerUnit, aSupplier):
        from ProductSource import ProductSource
        return ProductSource(aAdvertisedCostPerUnit, self, aSupplier)

    def addProductSource2(self, aProductSource):
        wasAdded = False
        if (aProductSource) in self._productSources :
            return False
        existingProduct = aProductSource.getProduct()
        isNewProduct = not (existingProduct is None) and not self == existingProduct
        if isNewProduct :
            aProductSource.setProduct(self)
        else :
            self._productSources.append(aProductSource)
        wasAdded = True
        return wasAdded

    def removeProductSource(self, aProductSource):
        wasRemoved = False
        #Unable to remove aProductSource, as it must always have a product
        if not self == aProductSource.getProduct() :
            self._productSources.remove(aProductSource)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addProductSourceAt(self, aProductSource, index):
        wasAdded = False
        if self.addProductSource(aProductSource) :
            if index < 0 :
                index = 0
            if index > self.numberOfProductSources() :
                index = self.numberOfProductSources() - 1
            self._productSources.remove(aProductSource)
            self._productSources.insert(index, aProductSource)
            wasAdded = True
        return wasAdded

    def addOrMoveProductSourceAt(self, aProductSource, index):
        wasAdded = False
        if (aProductSource) in self._productSources :
            if index < 0 :
                index = 0
            if index > self.numberOfProductSources() :
                index = self.numberOfProductSources() - 1
            self._productSources.remove(aProductSource)
            self._productSources.insert(index, aProductSource)
            wasAdded = True
        else :
            wasAdded = self.addProductSourceAt(aProductSource, index)
        return wasAdded

    def delete(self):
        i = len(self._productSources)
        while i > 0 :
            aProductSource = self._productSources[i - 1]
            aProductSource.delete()
            i -= 1

    def __str__(self):
        return str(super().__str__()) + "[" + "ourCode" + ":" + str(self.getOurCode()) + "," + "description" + ":" + str(self.getDescription()) + "," + "picture" + ":" + str(self.getPicture()) + "," + "ourListPricePerunit" + ":" + str(self.getOurListPricePerunit()) + "," + "numberInInventory" + ":" + str(self.getNumberInInventory()) + "," + "numberToKeepInv" + ":" + str(self.getNumberToKeepInv()) + "]"

    def addProductSource(self, *argv):
        from ProductSource import ProductSource
        if len(argv) == 2 and isinstance(argv[0], str) and isinstance(argv[1], Supplier) :
            return self.addProductSource1(argv[0], argv[1])
        if len(argv) == 1 and isinstance(argv[0], ProductSource) :
            return self.addProductSource2(argv[0])
        raise TypeError("No method matches provided parameters")





# %% NEW FILE ReceivedDelivery BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 28 "../../model.ump"
# line 62 "../../model.ump"
import os

class ReceivedDelivery():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #ReceivedDelivery Attributes
    #ReceivedDelivery Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNumberReceived, aActualCostPerUnit, aSupplier):
        self._supplier = None
        self._receivedLineItems = None
        self._actualCostPerUnit = None
        self._numberReceived = None
        self._numberReceived = aNumberReceived
        self._actualCostPerUnit = aActualCostPerUnit
        self._receivedLineItems = []
        didAddSupplier = self.setSupplier(aSupplier)
        if not didAddSupplier :
            raise RuntimeError ("Unable to create receivedDelivery due to supplier. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setNumberReceived(self, aNumberReceived):
        wasSet = False
        self._numberReceived = aNumberReceived
        wasSet = True
        return wasSet

    def setActualCostPerUnit(self, aActualCostPerUnit):
        wasSet = False
        self._actualCostPerUnit = aActualCostPerUnit
        wasSet = True
        return wasSet

    def getNumberReceived(self):
        return self._numberReceived

    def getActualCostPerUnit(self):
        return self._actualCostPerUnit

    # Code from template association_GetMany 
    def getReceivedLineItem(self, index):
        aReceivedLineItem = self._receivedLineItems[index]
        return aReceivedLineItem

    def getReceivedLineItems(self):
        newReceivedLineItems = tuple(self._receivedLineItems)
        return newReceivedLineItems

    def numberOfReceivedLineItems(self):
        number = len(self._receivedLineItems)
        return number

    def hasReceivedLineItems(self):
        has = len(self._receivedLineItems) > 0
        return has

    def indexOfReceivedLineItem(self, aReceivedLineItem):
        index = (-1 if not aReceivedLineItem in self._receivedLineItems else self._receivedLineItems.index(aReceivedLineItem))
        return index

    # Code from template association_GetOne 
    def getSupplier(self):
        return self._supplier

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfReceivedLineItems():
        return 0

    # Code from template association_AddManyToOne 
    def addReceivedLineItem1(self, aNumberReceived, aActualCostPerUnit, aSupplierOrderLineItem):
        from ReceivedLineItem import ReceivedLineItem
        return ReceivedLineItem(aNumberReceived, aActualCostPerUnit, self, aSupplierOrderLineItem)

    def addReceivedLineItem2(self, aReceivedLineItem):
        wasAdded = False
        if (aReceivedLineItem) in self._receivedLineItems :
            return False
        existingReceivedDelivery = aReceivedLineItem.getReceivedDelivery()
        isNewReceivedDelivery = not (existingReceivedDelivery is None) and not self == existingReceivedDelivery
        if isNewReceivedDelivery :
            aReceivedLineItem.setReceivedDelivery(self)
        else :
            self._receivedLineItems.append(aReceivedLineItem)
        wasAdded = True
        return wasAdded

    def removeReceivedLineItem(self, aReceivedLineItem):
        wasRemoved = False
        #Unable to remove aReceivedLineItem, as it must always have a receivedDelivery
        if not self == aReceivedLineItem.getReceivedDelivery() :
            self._receivedLineItems.remove(aReceivedLineItem)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addReceivedLineItemAt(self, aReceivedLineItem, index):
        wasAdded = False
        if self.addReceivedLineItem(aReceivedLineItem) :
            if index < 0 :
                index = 0
            if index > self.numberOfReceivedLineItems() :
                index = self.numberOfReceivedLineItems() - 1
            self._receivedLineItems.remove(aReceivedLineItem)
            self._receivedLineItems.insert(index, aReceivedLineItem)
            wasAdded = True
        return wasAdded

    def addOrMoveReceivedLineItemAt(self, aReceivedLineItem, index):
        wasAdded = False
        if (aReceivedLineItem) in self._receivedLineItems :
            if index < 0 :
                index = 0
            if index > self.numberOfReceivedLineItems() :
                index = self.numberOfReceivedLineItems() - 1
            self._receivedLineItems.remove(aReceivedLineItem)
            self._receivedLineItems.insert(index, aReceivedLineItem)
            wasAdded = True
        else :
            wasAdded = self.addReceivedLineItemAt(aReceivedLineItem, index)
        return wasAdded

    # Code from template association_SetOneToMany 
    def setSupplier(self, aSupplier):
        wasSet = False
        if aSupplier is None :
            return wasSet
        existingSupplier = self._supplier
        self._supplier = aSupplier
        if not (existingSupplier is None) and not existingSupplier == aSupplier :
            existingSupplier.removeReceivedDelivery(self)
        self._supplier.addReceivedDelivery(self)
        wasSet = True
        return wasSet

    def delete(self):
        i = len(self._receivedLineItems)
        while i > 0 :
            aReceivedLineItem = self._receivedLineItems[i - 1]
            aReceivedLineItem.delete()
            i -= 1

        placeholderSupplier = self._supplier
        self._supplier = None
        if not (placeholderSupplier is None) :
            placeholderSupplier.removeReceivedDelivery(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "numberReceived" + ":" + str(self.getNumberReceived()) + "," + "actualCostPerUnit" + ":" + str(self.getActualCostPerUnit()) + "]" + str(os.linesep) + "  " + "supplier = " + ((format(id(self.getSupplier()), "x")) if not (self.getSupplier() is None) else "null")

    def addReceivedLineItem(self, *argv):
        from ReceivedLineItem import ReceivedLineItem
        if len(argv) == 3 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], SupplierOrderLineItem) :
            return self.addReceivedLineItem1(argv[0], argv[1], argv[2])
        if len(argv) == 1 and isinstance(argv[0], ReceivedLineItem) :
            return self.addReceivedLineItem2(argv[0])
        raise TypeError("No method matches provided parameters")





# %% NEW FILE Supplier BEGINS HERE %%

#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 21 "../../model.ump"
# line 86 "../../model.ump"

class Supplier():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Supplier Attributes
    #Supplier Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aId, aName, aAddress):
        self._receivedDeliveries = None
        self._orderToSuppliers = None
        self._productSources = None
        self._address = None
        self._name = None
        self._id = None
        self._id = aId
        self._name = aName
        self._address = aAddress
        self._productSources = []
        self._orderToSuppliers = []
        self._receivedDeliveries = []

    #------------------------
    # INTERFACE
    #------------------------
    def setId(self, aId):
        wasSet = False
        self._id = aId
        wasSet = True
        return wasSet

    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setAddress(self, aAddress):
        wasSet = False
        self._address = aAddress
        wasSet = True
        return wasSet

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getAddress(self):
        return self._address

    # Code from template association_GetMany 
    def getProductSource(self, index):
        aProductSource = self._productSources[index]
        return aProductSource

    def getProductSources(self):
        newProductSources = tuple(self._productSources)
        return newProductSources

    def numberOfProductSources(self):
        number = len(self._productSources)
        return number

    def hasProductSources(self):
        has = len(self._productSources) > 0
        return has

    def indexOfProductSource(self, aProductSource):
        index = (-1 if not aProductSource in self._productSources else self._productSources.index(aProductSource))
        return index

    # Code from template association_GetMany 
    def getOrderToSupplier(self, index):
        aOrderToSupplier = self._orderToSuppliers[index]
        return aOrderToSupplier

    def getOrderToSuppliers(self):
        newOrderToSuppliers = tuple(self._orderToSuppliers)
        return newOrderToSuppliers

    def numberOfOrderToSuppliers(self):
        number = len(self._orderToSuppliers)
        return number

    def hasOrderToSuppliers(self):
        has = len(self._orderToSuppliers) > 0
        return has

    def indexOfOrderToSupplier(self, aOrderToSupplier):
        index = (-1 if not aOrderToSupplier in self._orderToSuppliers else self._orderToSuppliers.index(aOrderToSupplier))
        return index

    # Code from template association_GetMany 
    def getReceivedDelivery(self, index):
        aReceivedDelivery = self._receivedDeliveries[index]
        return aReceivedDelivery

    def getReceivedDeliveries(self):
        newReceivedDeliveries = tuple(self._receivedDeliveries)
        return newReceivedDeliveries

    def numberOfReceivedDeliveries(self):
        number = len(self._receivedDeliveries)
        return number

    def hasReceivedDeliveries(self):
        has = len(self._receivedDeliveries) > 0
        return has

    def indexOfReceivedDelivery(self, aReceivedDelivery):
        index = (-1 if not aReceivedDelivery in self._receivedDeliveries else self._receivedDeliveries.index(aReceivedDelivery))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfProductSources():
        return 0

    # Code from template association_AddManyToOne 
    def addProductSource1(self, aAdvertisedCostPerUnit, aProduct):
        from ProductSource import ProductSource
        return ProductSource(aAdvertisedCostPerUnit, aProduct, self)

    def addProductSource2(self, aProductSource):
        wasAdded = False
        if (aProductSource) in self._productSources :
            return False
        existingSupplier = aProductSource.getSupplier()
        isNewSupplier = not (existingSupplier is None) and not self == existingSupplier
        if isNewSupplier :
            aProductSource.setSupplier(self)
        else :
            self._productSources.append(aProductSource)
        wasAdded = True
        return wasAdded

    def removeProductSource(self, aProductSource):
        wasRemoved = False
        #Unable to remove aProductSource, as it must always have a supplier
        if not self == aProductSource.getSupplier() :
            self._productSources.remove(aProductSource)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addProductSourceAt(self, aProductSource, index):
        wasAdded = False
        if self.addProductSource(aProductSource) :
            if index < 0 :
                index = 0
            if index > self.numberOfProductSources() :
                index = self.numberOfProductSources() - 1
            self._productSources.remove(aProductSource)
            self._productSources.insert(index, aProductSource)
            wasAdded = True
        return wasAdded

    def addOrMoveProductSourceAt(self, aProductSource, index):
        wasAdded = False
        if (aProductSource) in self._productSources :
            if index < 0 :
                index = 0
            if index > self.numberOfProductSources() :
                index = self.numberOfProductSources() - 1
            self._productSources.remove(aProductSource)
            self._productSources.insert(index, aProductSource)
            wasAdded = True
        else :
            wasAdded = self.addProductSourceAt(aProductSource, index)
        return wasAdded

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfOrderToSuppliers():
        return 0

    # Code from template association_AddManyToOne 
    def addOrderToSupplier1(self, aPoNumber, aDateOrdered):
        from OrderToSupplier import OrderToSupplier
        return OrderToSupplier(aPoNumber, aDateOrdered, self)

    def addOrderToSupplier2(self, aOrderToSupplier):
        wasAdded = False
        if (aOrderToSupplier) in self._orderToSuppliers :
            return False
        existingSupplier = aOrderToSupplier.getSupplier()
        isNewSupplier = not (existingSupplier is None) and not self == existingSupplier
        if isNewSupplier :
            aOrderToSupplier.setSupplier(self)
        else :
            self._orderToSuppliers.append(aOrderToSupplier)
        wasAdded = True
        return wasAdded

    def removeOrderToSupplier(self, aOrderToSupplier):
        wasRemoved = False
        #Unable to remove aOrderToSupplier, as it must always have a supplier
        if not self == aOrderToSupplier.getSupplier() :
            self._orderToSuppliers.remove(aOrderToSupplier)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addOrderToSupplierAt(self, aOrderToSupplier, index):
        wasAdded = False
        if self.addOrderToSupplier(aOrderToSupplier) :
            if index < 0 :
                index = 0
            if index > self.numberOfOrderToSuppliers() :
                index = self.numberOfOrderToSuppliers() - 1
            self._orderToSuppliers.remove(aOrderToSupplier)
            self._orderToSuppliers.insert(index, aOrderToSupplier)
            wasAdded = True
        return wasAdded

    def addOrMoveOrderToSupplierAt(self, aOrderToSupplier, index):
        wasAdded = False
        if (aOrderToSupplier) in self._orderToSuppliers :
            if index < 0 :
                index = 0
            if index > self.numberOfOrderToSuppliers() :
                index = self.numberOfOrderToSuppliers() - 1
            self._orderToSuppliers.remove(aOrderToSupplier)
            self._orderToSuppliers.insert(index, aOrderToSupplier)
            wasAdded = True
        else :
            wasAdded = self.addOrderToSupplierAt(aOrderToSupplier, index)
        return wasAdded

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfReceivedDeliveries():
        return 0

    # Code from template association_AddManyToOne 
    def addReceivedDelivery1(self, aNumberReceived, aActualCostPerUnit):
        from ReceivedDelivery import ReceivedDelivery
        return ReceivedDelivery(aNumberReceived, aActualCostPerUnit, self)

    def addReceivedDelivery2(self, aReceivedDelivery):
        wasAdded = False
        if (aReceivedDelivery) in self._receivedDeliveries :
            return False
        existingSupplier = aReceivedDelivery.getSupplier()
        isNewSupplier = not (existingSupplier is None) and not self == existingSupplier
        if isNewSupplier :
            aReceivedDelivery.setSupplier(self)
        else :
            self._receivedDeliveries.append(aReceivedDelivery)
        wasAdded = True
        return wasAdded

    def removeReceivedDelivery(self, aReceivedDelivery):
        wasRemoved = False
        #Unable to remove aReceivedDelivery, as it must always have a supplier
        if not self == aReceivedDelivery.getSupplier() :
            self._receivedDeliveries.remove(aReceivedDelivery)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addReceivedDeliveryAt(self, aReceivedDelivery, index):
        wasAdded = False
        if self.addReceivedDelivery(aReceivedDelivery) :
            if index < 0 :
                index = 0
            if index > self.numberOfReceivedDeliveries() :
                index = self.numberOfReceivedDeliveries() - 1
            self._receivedDeliveries.remove(aReceivedDelivery)
            self._receivedDeliveries.insert(index, aReceivedDelivery)
            wasAdded = True
        return wasAdded

    def addOrMoveReceivedDeliveryAt(self, aReceivedDelivery, index):
        wasAdded = False
        if (aReceivedDelivery) in self._receivedDeliveries :
            if index < 0 :
                index = 0
            if index > self.numberOfReceivedDeliveries() :
                index = self.numberOfReceivedDeliveries() - 1
            self._receivedDeliveries.remove(aReceivedDelivery)
            self._receivedDeliveries.insert(index, aReceivedDelivery)
            wasAdded = True
        else :
            wasAdded = self.addReceivedDeliveryAt(aReceivedDelivery, index)
        return wasAdded

    def delete(self):
        i = len(self._productSources)
        while i > 0 :
            aProductSource = self._productSources[i - 1]
            aProductSource.delete()
            i -= 1

        i = len(self._orderToSuppliers)
        while i > 0 :
            aOrderToSupplier = self._orderToSuppliers[i - 1]
            aOrderToSupplier.delete()
            i -= 1

        i = len(self._receivedDeliveries)
        while i > 0 :
            aReceivedDelivery = self._receivedDeliveries[i - 1]
            aReceivedDelivery.delete()
            i -= 1

    def __str__(self):
        return str(super().__str__()) + "[" + "id" + ":" + str(self.getId()) + "," + "name" + ":" + str(self.getName()) + "," + "address" + ":" + str(self.getAddress()) + "]"

    def addProductSource(self, *argv):
        from ProductSource import ProductSource
        if len(argv) == 2 and isinstance(argv[0], str) and isinstance(argv[1], Product) :
            return self.addProductSource1(argv[0], argv[1])
        if len(argv) == 1 and isinstance(argv[0], ProductSource) :
            return self.addProductSource2(argv[0])
        raise TypeError("No method matches provided parameters")

    def addOrderToSupplier(self, *argv):
        from OrderToSupplier import OrderToSupplier
        if len(argv) == 2 and isinstance(argv[0], str) and isinstance(argv[1], str) :
            return self.addOrderToSupplier1(argv[0], argv[1])
        if len(argv) == 1 and isinstance(argv[0], OrderToSupplier) :
            return self.addOrderToSupplier2(argv[0])
        raise TypeError("No method matches provided parameters")

    def addReceivedDelivery(self, *argv):
        from ReceivedDelivery import ReceivedDelivery
        if len(argv) == 2 and isinstance(argv[0], str) and isinstance(argv[1], str) :
            return self.addReceivedDelivery1(argv[0], argv[1])
        if len(argv) == 1 and isinstance(argv[0], ReceivedDelivery) :
            return self.addReceivedDelivery2(argv[0])
        raise TypeError("No method matches provided parameters")
