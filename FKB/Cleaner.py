def CleanRules(listOfRules):
    newListRule = []
    listID = []
    for rul in listOfRules:
        id = rul.getIdRule()
        if(id not in listID):
            newListRule.append(rul)
            listID.append(id)
        else:
            print("Find dupl")
    return  newListRule