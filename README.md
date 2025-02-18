# ASIX
The Asix Graphics Library

## Introduction
Asix is a 2d python library build on top pygame engine its fully support pygame methods in its Core and also some methods of asix work with pygame
methods are simple but powerfull

## Version : Asix 7.7

## Install
Run `pip install asix`

### Core
Core is the main Object of Screen and contains all methods you can use it like :

`var = Core(width, height, flags)`

its take `width` of screen and take `height` of screen
and last flags so flags are like special effects we can put on window and rendering 
flags are `borderless` makes screen without any border title buttons 
`resizeable` makes screen resizeable and `optimize` 
is a perfomance enchancer

! important to note `optimize` or `optimized` flag may not work on all devices and cause proformance issue like on gpu its only hardware accelarate

### Core Built-in's

#### avents
this function return access to event all of pygame like:
```python
while True:
    for event in avents():
       if event.type == QUIT:
          sys.exit()
```

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

#### pie
in asix pie is math pi/pie function
```
angle += pie / 60
```

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

# Easter Eggs 🎊

### Screenshot
used to get a pic of window 
```
def screenshot(surface: pygame.Surface, filename: str = 'screenshot.png') -> None:
```
no `core.` required

# Pyvec
### A Multi-Dimensional Array Vector Extension For Asix 

## vec 

The `Vector` class provides a flexible representation of mathematical vectors in N-dimensional space. It supports operations like addition, subtraction, scalar multiplication, dot product, and calculating magnitude, while also allowing access to vector components dynamically via attributes like `p1`, `p2`, `p3`, etc.

You can create vectors with any number of components (2D, 3D, 4D, 5D, etc.) and access them either by passing individual arguments or by using lists and tuples.

Creating a Vector
You can create a vector by passing individual components, lists to the vec function:
```
v = vec(100, 100, 100)  # 3D Vector
v2 = vec([1, 2, 3], [3, 6, 9)  # Combine lists and tuples
```

The vec function will flatten lists automatically and create a vector from the individual components.

#### Accessing Vector Components

The components of the vector are accessible dynamically with attributes like p1, p2, p3, etc.

`print(v.p1, v.p2, v.p3)  # Output: 100.0 100.0 100.0`

#### Vector Operations

##### Addition
```python
v1 = vec(1, 2, 3)
v2 = vec(4, 5, 6)
v3 = v1 + v2
print(v3.p1, v3.p2, v3.p3)  # Output: 5.0 7.0 9.0

```

##### Subtraction
```python
v1 = vec(5, 6, 7)
v2 = vec(1, 2, 3)
v3 = v1 - v2
print(v3.p1, v3.p2, v3.p3)  # Output: 4.0 4.0 4.0

```

##### Scalar Multiplication
```python
v1 = vec(1, 2, 3)
v2 = v1 * 2
print(v2.p1, v2.p2, v2.p3)  # Output: 2.0 4.0 6.0

```

##### Dot Product
```python
v1 = vec(1, 2, 3)
v2 = vec(4, 5, 6)
result = v1.dot(v2)
print(result)  # Output: 32.0
```

##### Magnitude
```python
v = vec(3, 4)
magnitude = v.magnitude()
print(magnitude)  # Output: 5.0
```

#### Example Usage
```python 
# Example: Creating a 5D vector and accessing its components
v = vec(100, 100, 100, 100, 100)
print(v.p1, v.p2, v.p3, v.p4, v.p5)  # Output: 100.0 100.0 100.0 100.0 100.0
```

---

# Asix Release Notes

## [v7.7] -2025

### Added

- Added Opengl Support

- Added 3d Methods

- Added math pie function

### Changed

- Improved Core Structure 

- Improved Speed 

- Improved Core Logic

### Fixed

- Fixed Opengl-Intregration Problems

---

## [v7.6] -2025

### Added

- Error Handling Added (CORE)

- Added Support for Math functions [sin, cos, tan] => (sic)

- Added Build-in Circle Drawer (Globe)

- Added Caption and Icon Changer functions (caption / icon)

- Added function to improve Image Handling (iload, isize) {iload loads image, isize resize image}

### Changed

- Removed unused Lib Modules (Imports)

- Improved CORE Structure

- Cache JIT Compiler Removed

- Removed Multi-Set ColorList (draw) improved speed, logic

- Removed unused EarlyTesting methods (fscript / mouse_button / mouse_pos / trn {used for Triangle Draw})

### Fixed

- Fixed Logic Error Not specified self on (Core.[width, height]) inside error handle
