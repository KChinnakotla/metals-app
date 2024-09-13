def onMousePress(mouseX,mouseY):
    #if the app is in the "title" mode, then these execute
    if(app.mode == 'title'):
        if(playButton.hits(mouseX,mouseY) == True):
            app.group.clear()
            directions.visible = True
            alkaliButton.visible = True
            alkalineButton.visible = True
            app.mode = 'selection'
        elif(bondButton.hits(mouseX,mouseY) == True):
            app.group.clear()
            otherDisplay.visible = True
            switchButton1.visible = True
            selectButton1.visible = True
            app.mode = 'interactionSelection'
    
    #if the app is in the interaction select mode, then these execute
    elif(app.mode == 'interactionSelection'):
        if(switchButton1.hits(mouseX,mouseY) == True):
            app.index += 1
            if(app.index > 2):
                app.index = 0
            otherDisplay.value = otherList[app.index]
        elif(selectButton1.hits(mouseX,mouseY) == True):
            app.group.clear()
            tempDisplay.visible = True
            tempDecrease.visible = True
            tempIncrease.visible = True
            temp.visible = True
            neutronDisplay.visible = True
            neutronDecrease.visible = True
            neutronIncrease.visible = True
            neutronNum.visible = True
            otherDisplay.visible = True
            stateOfMatter.visible = True
            stateOfMatterDesc.visible = True
            massDesc.visible = True
            massNum.visible = True
            energyDesc.visible = True
            energy.visible = True
            if(otherDisplay.value == 'Au'):
                neutronNum.value = 79
            elif(otherDisplay.value == 'Ag'):
                neutronNum.value = 47
            else:
                neutronNum.value = 28
            otherDisplay.size = 75
            otherDisplay.centerY = 230
            app.mode = 'interaction'
    
    #if app goes into the actual interaction mode, then these execute
    elif(app.mode == 'interaction'):
        if(tempDecrease.hits(mouseX,mouseY) == True):
            temp.value -= 100
        elif(tempIncrease.hits(mouseX,mouseY) == True):
            temp.value += 100
        if(neutronDecrease.hits(mouseX,mouseY) == True):
            if(neutronNum.value != 0):
                neutronNum.value -= 1
        elif(neutronIncrease.hits(mouseX,mouseY) == True):
            neutronNum.value += 1
        if(otherDisplay.value == 'Au'):
            if(neutronNum.value > 90):
                massNum.value = 'High'
            elif(neutronNum.value > 70):
                massNum.value = 'Mid'
            else:
                massNum.value = 'Low'
            if(temp.value > 2800):
                stateOfMatter.value = 'Gas'
                stateOfMatter.fill = 'red'
            elif(temp.value > 1100):
                stateOfMatter.value = 'Liquid'
                stateOfMatter.fill = 'blue'
            else: 
                stateOfMatter.value = 'Solid'
                stateOfMatter.fill = 'black'
        elif(otherDisplay.value == 'Ag'):
            if(neutronNum.value > 60):
                massNum.value = 'High'
            elif(neutronNum.value > 40):
                massNum.value = "Mid"
            else:
                massNum.value = 'Low'
            if(temp.value > 2200):
                stateOfMatter.value = 'Gas'
                stateOfMatter.fill = 'red'
            elif(temp.value > 1000):
                stateOfMatter.value = 'Liquid'
                stateOfMatter.fill = 'blue'
            else:
                stateOfMatter.value = 'Solid'
                stateOfMatter.fill = 'black'
        else:
            if(neutronNum.value > 40):
                massNum.value = 'High'
            elif(neutronNum.value > 20):
                massNum.value = 'Mid'
            else:
                massNum.value = 'Low'
            if(temp.value > 3000):
                stateOfMatter.value = 'Gas'
                stateOfMatter.fill = 'red'
            elif(temp.value > 1500):
                stateOfMatter.value = 'Liquid'
                stateOfMatter.fill = 'blue'
            else:
                stateOfMatter.value = 'Solid'
                stateOfMatter.fill = 'black'
        if(temp.value > 2000):
            energy.value = 'High'
            energy.fill = 'red'
            energy.size = 35
        elif(temp.value > 1000):
            energy.value = 'Mid'
            energy.size = 35
            energy.fill = 'orange'
        elif(temp.value >= 0):
            energy.value = 'Low'
            energy.size = 35
            energy.fill = 'skyBlue'
        else:
            energy.value = 'Very low'
            energy.size = 30
            energy.fill = 'black'
    
    #if app is in the selection mode for the alkali and alkaline earth modes, then these execute    
    elif(app.mode == 'selection'):
        if(alkaliButton.hits(mouseX,mouseY) == True):
            app.group.clear()
            alkaliDisplay.visible = True
            switchButton1.visible = True
            selectButton1.visible = True
            app.mode = 'gameAlkali'
        if(alkalineButton.hits(mouseX,mouseY) == True):
            app.group.clear()
            switchButton1.visible = True
            selectButton1.visible = True
            alkalineDisplay.visible = True
            app.mode = 'gameAlkaline'
  
    #if the app goes into the alkaline mode, then these activate
    elif(app.mode == 'gameAlkaline'):
        if(switchButton1.hits(mouseX,mouseY) == True):
            app.index += 1
            if(app.index > 5):
                app.index = 0
            alkalineDisplay.value = alkalineList[app.index]
        if(selectButton1.hits(mouseX,mouseY) == True):
            app.group.clear()
            drawElement(alkalineDisplay.value,app.index + 2)
            retryButton.visible = True
            app.mode = 'finish'
    
    #if app goes into the alkali metal mode, then these activate
    elif(app.mode == 'gameAlkali'):
        if(switchButton1.hits(mouseX,mouseY) == True):
            app.index += 1
            if(app.index > 5):
                app.index = 0
            alkaliDisplay.value = alkaliList[app.index]
            
        if(selectButton1.hits(mouseX,mouseY) == True):
            app.group.clear()
            drawElement(alkaliDisplay.value,app.index + 2)
            retryButton.visible = True
            app.mode = 'finish'
    
    #if the app finishes, then these execute
    elif(app.mode == 'finish'):
        if(retryButton.hits(mouseX,mouseY) == True):
            app.group.clear()
            directions.visible = True
            alkaliButton.visible = True
            alkalineButton.visible = True
            alkaliDisplay.value = alkaliList[0]
            alkalineDisplay.value = alkalineList[0]
            app.mode = 'selection'
