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
`resizeable` makes screen resizeable and `coreinf` just shows all info about window and `optimize` 
is a perfomance enchancer like :
```
width : 800
height : 600
flags : coreinf
clock : <Clock(fps=0.00)>
font : <pygame.font.Font object at 0x0000017138B2EFA0>
type : <Asix.Core>
version : 7.1
```
! important to note `optimize` or `optimized` flag may not work on all devices and cause proformance issue and 
only works on (WINDOWS OS)
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

#### polygon

this function draw on points like for traingle we need 3 points 
this function points not flipped like pygame.draw.polygon have unside down points
its auto correct them like 
```
points = [(100, 100), (200, 100), (150, 200)]
core.polygon(color, points)
```
Draws a Triangle

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

#### blit :
blit used for drawing images in mainloop like :

```
core.blit(*args)
```
works like pygame one like a surface and img or just img with x, y

#### key / K
the key is a function that we can use with K to written very short input management script like 
```
# init it ! Optional
ky = key()

# Use K for Keys and ky for Detection of that key like
if key[K("W")]
  print('pressed W')
  ...

...
```
or can use without init like `key()[K('W')]: ...`

#### text
text function is a basic text renderer like 
```
core.text(size, color, text, x, y, font_type: optional, rotation: require a angle var)
```
its just print that text in window

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

#### caption
used to set window title like
```
core.caption(str)
```

#### icon
used to set window icon like 
```
core.icon(loaded_img)
```

#### Font
this function used to make simple font like :
```
newfont = core.Font(fontpath=None, size)
```
if you want custom font .ttf or .otf do like this
```
# add your font path and create a font object
newfont = core.Font(fontpath="myfont.ttf", size)

# use that font to render text
text = newfont.render("Hello, Asix!", True, color(r, g, b))

# get its rect and Set up the position for the text
text_rect = text.get_rect(center=(400, 300))

# now draw it with core.blit
core.blit(text, text_rect)
```
thats it

---

### Additional Methods
these methods can get called direct without `core.`

#### sic :
sic is a sin cos tan calcultion function its structure 
```python
def sic(center:int, radius:int, angle:int, typ:str, startmul:int=0, endmul:int=0):
          if typ == 's':
           return center + radius * sin(angle)
          if typ == 'c':
           return center + radius * cos(angle)
          if typ == 't':
           return center + radius * tan(angle)
```
its can be used for examples :

a circle moving in a circle
```
from asix import *

_ = Core(600, 600, 'optimize')

angle = 0

while True:
    _.quit('esc')
    _.color(0, 0, 0)

    _.globe(sic(300, 100, angle, 'c'), sic(300, 100, angle, 's'), 70, (255, 255, 255))

    angle += 0.001

    _.flip()

_.exit()
```
its just calculate the radius x, y of a circle and have arg selector 's' for sin and 'c' for cos and 't' for tan


#### iload 
iload loads an image like
```
img = iload(path)
```

#### isize
isize resize a loaded img like 
```
isize(img, width, height)
```
or can be used with iload mentioned before
```
img = isize(iload(path), width, height)
```

### DTYPE Local DataClass
its a local DataClass can use it to `store`, `fetch`, `delete` can store any datatype
and its key, value nature like 
```
dt = DTYPE()

dt.store(key, value)

dt.fetch(key)

dt.delete(key)

! you can make as many as wanted like

doreamon = DTYPE()

this one is not linked to dt

```
! Its Optional

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

---

## Details 

### Core Object
```
self.GLSO = {
                     'width':self.width,
                     'height':self.height,
                     'flags':self.flag,
                     'clock':self.clock, 
                     'font':self.font,
                     'type':"<Asix.Core>", 
                     'version': "7.1"
                     }
```
GLSO (Global Library System Object)
Core have these and you can access them by `core.screen` and use that to use pygame function directly on the surface on asix
