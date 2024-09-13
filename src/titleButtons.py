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
