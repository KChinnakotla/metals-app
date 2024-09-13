def drawElement(element,shells):
    Label(element,270,130,size = 30)
    numProtons = 0
    numNeutrons = 0
    radius = 0
    Rect(10,20,120,40,fill = None,border = 'black')
    name = Label('name',70,40,size = 20)
    descriptionElement = Label('',200,295,size = 15)
    distance = 30
 
    for i in range(shells):
        Circle(270,130,distance,fill = None, border = 'black')
        distance += 15
   
    if(element == 'Li'):
        name.value = "Lithium"
        numProtons = 3
        numNeutrons = 4
        radius = 167
        descriptionElement.value = 'Lithium is used in many rechargeable batteries.'
    elif(element == 'Na'):
        name.value = "Sodium"
        numProtons = 11
        numNeutrons = 12
        radius = 190
        descriptionElement.value = 'Sodium is used to make almost every salt in the world.'
    elif(element == 'K'):
        name.value = "Potassium"
        numProtons = 19
        numNeutrons = 20
        radius = 243
        descriptionElement.value = 'Potassium is utilized in many different plant fertilizers.'
    elif(element == 'Rb'):
        name.value = "Rubidium"
        numProtons = 37
        numNeutrons = 48
        radius = 265
        descriptionElement.value = 'Rubidium can be used within ion engines in space vehicles.'
    elif(element == 'Cs'):
        name.value = 'Cesium'
        numProtons = 55
        numNeutrons = 78
        radius = 298
        descriptionElement.value = 'Cesium explodes when reacted with cold water.'
    elif(element == 'Fr'):
        name.value = 'Francium'
        numProtons = 87
        numNeutrons = 137
        radius = 348
        descriptionElement.value = 'Francium is one of the most unstable elements ever.'
    elif(element == 'Be'):
        name.value = 'Beryllium'
        numProtons = 4
        numNeutrons = 4
        radius = 112
        descriptionElement.value = 'Salts made with Beryllium have a very sweet taste.'
    elif(element == 'Mg'):
        name.value = 'Magnesium'
        numProtons = 12
        numNeutrons = 12
        radius = 145
        descriptionElement.value = 'Magnesium can be used to kill many different bacterias.'
    elif(element == 'Ca'):
        name.value = 'Calcium'
        numProtons = 20
        numNeutrons = 20 
        radius = 194
        descriptionElement.value = '99% of Calcium stored in our body is in our bones.'
    elif(element == 'Sr'):
        name.value = 'Strontium'
        numProtons = 38
        numNeutrons = 50
        radius = 219
        descriptionElement.value = 'Strontium can change colors when exposed to air.'
    elif(element == 'Ba'):
        name.value = 'Barium'
        numProtons = 56
        numNeutrons = 81
        radius = 253
        descriptionElement.value = 'Some Barium isotopes are very toxic to humans.'
    elif(element == 'Ra'):
        name.value = 'Radium'
        numProtons = 88
        numNeutrons = 138
        radius = 283
        descriptionElement.value = 'Radium is the first ever synthetic radioactive element.'
    Label('Protons: ' + str(numProtons),70,100,size = 20)
    Label('Electrons: ' + str(numProtons),70,140,size = 20)
    Label('Neutrons: ' + str(numNeutrons),70,180,size = 20)
    Label('Radius: ' + str(radius) + "pm",70,220,size = 20)
    Line(0,265,400,265,fill = 'blue')
    Line(0,325,400,325,fill = 'blue')
