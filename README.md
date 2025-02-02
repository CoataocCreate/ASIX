# ASIX
The Asix Graphics Library

## Introduction
Asix is a 2d python library build on top pygame engine its fully support pygame methods in its Core and also some methods of asix work with pygame
methods are simple but powerfull

! Its not on pip yet so dont run `pip install asix`

### Core
Core is the main Object of Screen and contains all methods you can use it like :

`var = Core(width, height, flags)`

its take `width` of screen and take `height` of screen
and last flags so flags are like special effects we can put on window and rendering 
flags are `borderless` makes screen without any border title buttons 
`resizeable` makes screen resizeable and `coreinf` just shows all info about window like :
```
width : 800
height : 600
flags : coreinf
clock : <Clock(fps=0.00)>
font : <pygame.font.Font object at 0x0000017138B2EFA0>
type : <Asix.Core>
version : 7.1
```
! important to note optimize may not work on all devices and cause proformance issue and only works on (WINDOWS OS)

---

### Core Built-in's

#### R specifier

this can use to create a rect like 
```
rect = R(100, 100, 100, 100)
```

#### draw 

this function used to draw rects its takes two args one `color` and `rect` like
```
core.draw((r, g, b), rect, ...)
```
its can accept multiple rects at once like shown up

#### globe

this function used to create circles its have multiple args 
```python
def globe(
    x: Any,
    y: Any,
    radius: Any,
    fill_color: Any,
    border_color: Any | None = None,
    border_width: int = 0
) -> None
```
its takes x-pos and y-pos and radius means size of circles and fill_color means color of circle 
and border_color means border color of circle 
and border_width of circle like

```
core.globe(100, 100, 70, (255, 255, 255), (r, g ,b), 10)

!Note If you dont want border skip border_color and border_width args
```

---

### Core Methods

#### quit :

quit is a function that automatically quit the window with x close window button but also support any pygame key like 
```
core.quit('esc', ...)
```

#### color :

color is a function that sets color of the window like
```
core.color(r, g, b)
```

#### flip :

flip is a function that flips the screen like 
```
core.flip()
```

#### exit :
exit is a function that get set at the outside of the loop at end its terminate all window and resources like 
```
core.exit() 
```

---

basic structure
```
from asix import *

_ = Core(800, 600, 'optimized')

while True:
    _.quit('esc')
    _.color(250, 250, 250)
 

    _.flip()

_.exit()
```
