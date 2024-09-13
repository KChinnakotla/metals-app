title = Label('Metals, Metals, Metals!',200,80,size = 35,bold = True)
description = Label('Learn and interact with metals.',200,140,size = 20,bold = True)
playButton = Group(
    Rect(100,290,200,100,border = 'white'),
    Label("Start",200,320,fill = 'cyan',size = 25,bold = True),
    Label("Learning",200,360,fill = 'cyan',size = 25,bold = True)
    )
bondButton = Group(
    Rect(100,180,200,100,border = 'white'),
    Label("Start",200,210,fill = 'cyan',size = 25,bold = True),
    Label("Interacting",200,250,fill = 'cyan',size = 25,bold = True)
    )
directions = Group(
    Label('Pick what group of metals that you',200,80,size = 20,bold = True),
    Label('would like to learn about!',200,100,size = 20,bold = True)
    )
directions.visible = False
alkaliButton = Group(
    Rect(100,160,200,80,border = 'white'),
    Label('Alkali metals',200,200,fill = 'cyan',size = 20,bold = True)
    )
alkaliButton.visible = False
alkalineButton = Group(
    Rect(100,280,200,80,border = 'white'),
    Label('Alkaline metals',200,320,fill = 'cyan',size = 20,bold = True)
    )
alkalineButton.visible = False
switchButton1 = Group(
    Rect(120,280,160,80,border = 'white'),
    Label('Next Element',200,320,size = 25,fill = 'yellow')
    )
switchButton1.visible = False
selectButton1 = Group(
    Rect(80,40,240,80,border = 'white'),
    Label('Select',200,80,size = 30,fill = 'cyan')
    )
selectButton1.visible = False
retryButton = Group(
    Rect(120,340,160,60,border = 'blue'),
    Label('Back',200,370,size = 20,fill = 'white')
    )
retryButton.visible = False

tempDisplay = Group(
    Label('Control the temperature of the',90,20),
    Label('metal and see what happens:',90,35),
    Rect(5,5,175,155,fill = None,border = 'black'),
    Line(5,45,180,45),
    Label("Temp (~C)",90,180,size = 25)
    )
tempDisplay.visible = False
tempDecrease = Polygon(85,60,25,80,85,100)
tempDecrease.visible = False
tempIncrease = Polygon(100,60,160,80,100,100)
tempIncrease.visible = False
temp = Label(0,90,130,size = 30)
temp.visible = False
neutronDisplay = Group(
    Rect(220,5,175,155,fill = None,border = 'black'),
    Label("Control the amount of neutrons",308,20),
    Label("and see what happens",308,35),
    Line(220,45,395,45),
    Label("Neutrons",308,180,size = 25)
    ) 
neutronDisplay.visible = False
neutronDecrease = Polygon(303,60,243,80,303,100)
neutronDecrease.visible = False
neutronIncrease = Polygon(318,60,378,80,318,100)
neutronIncrease.visible = False
neutronNum = Label(0,308,130,size = 30)
neutronNum.visible = False
stateOfMatterDesc = Group(
    Label('State:',70,300,size = 25),
    Rect(5,280,130,110,fill = None,border = 'black')
    )
stateOfMatterDesc.visible = False
stateOfMatter = Label('Solid',70,360,size = 35)
stateOfMatter.visible = False
massDesc = Group(
    Label('Mass(g):',200,300,size = 25),
    Rect(135,280,130,110,fill = None,border = 'black')
    )
massDesc.visible = False
massNum = Label('Mid',200,360,size = 35)
massNum.visible = False
energyDesc = Group(
    Label('Energy(KE):',330,300,size = 20),
    Rect(265,280,130,110,fill = None,border= 'black')
    )
energy = Label('Low',330,360,size = 35,fill = 'skyBlue')
energy.visible = False
energyDesc.visible = False
