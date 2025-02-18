# ASIX
The Asix Graphics Library

## Introduction
Asix is a 2d python library build on top pygame engine its fully support pygame methods in its Core and also some methods of asix work with pygame
methods are simple but powerfull

! you can use any pygame function without import pygame and can get core.screen to do anything

## Version : Asix 7.8

## Install
Run `pip install asix==version` or `pip install asix`

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

### `@staticmethod console(*args, ed=0, capture=False)`

The `console` static method allows you to execute shell commands from within your Python program. It provides functionality to add a delay between commands, capture the output of the command execution, and adjust command execution behavior based on the operating system.

#### Parameters:
- `*args` (varied types): 
  - **Command(s) to be executed**. The commands can be provided as either strings or lists.
    - If a **string** is provided, it represents the shell command to be executed.
    - If a **list** is provided, it is treated as an already split command (i.e., no need for the function to parse the command into arguments).
  - Multiple commands can be passed by separating them with commas in the `*args` list. Each command will be executed in the order they are passed.
  
- `ed` (int, default=0): 
  - **Delay** between executing each command in seconds.
  - Introduces a delay (`time.sleep(ed)`) after executing each command before executing the next one. Useful when you need to throttle command execution (e.g., avoid overwhelming a system with too many quick successive commands).
  
- `capture` (bool, default=False):
  - **Whether to capture the output of the command**. 
    - When set to `True`, the function will execute the command and capture the standard output (stdout) of the command.
    - When set to `False`, the function will run the command but **not capture** its output, meaning it will not return anything. It simply executes the command in the background.

#### Return Value:
- **If `capture=True`**:
  - The method will return the **output** of the command execution as a string, stripped of leading and trailing whitespace. This is useful when you need the result of a shell command for further processing in your Python program.
  
- **If `capture=False`**:
  - The method will return `None`, since the function is only executing the command without capturing the output.

#### Method Behavior:
1. **Command Execution**:
   - For each command in `*args`:
     - If the command is a **string**, it will be executed using `subprocess.run()`.
       - On **Windows (`os.name == "nt"`)**, the string command is passed to `subprocess.run()` with the `shell=True` argument to ensure correct execution in the shell.
       - On **Unix-based systems** (like Linux or macOS), the string command is split using `shlex.split()` to break the string into a list of arguments. The resulting list is passed to `subprocess.run()` for execution.
     - If the command is already a **list**, it is executed directly by passing it to `subprocess.run()` without modification.

2. **Output Capture**:
   - If `capture=True`, the function captures the output using `capture_output=True` and `text=True` in the `subprocess.run()` call.
     - The output is then returned as a string with any leading/trailing whitespace removed.
   - If `capture=False`, the function does not capture the output, and the command runs in the background without returning any result.

3. **Delay Between Commands**:
   - After each command execution, if `ed > 0`, the method introduces a pause using `time.sleep(ed)`. This delay is useful when you want to space out the execution of commands, especially when interacting with external systems or running multiple commands in sequence.

its return output string which you can store in var and put it anywhere like core.text 
```
my_console_string = core.console("echo Hello, World!") # now contains "Hello, World!"
```
  
---

#### `@once` Decorator

The `@once` decorator ensures that a function runs only once, regardless of how many times it is called — even in a loop.
Once the function has been executed, subsequent calls to that function will be ignored.
This decorator can be applied to any function where you want to guarantee that it only executes once.

#### avents
this function return access to event all of pygame like:
```python
while True:
    for event in avents():
       if event.type == QUIT:
          sys.exit()
```
its same like pygame just for event in avents()

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

# Rec Class Documentation

The `Rec` class is an extended wrapper around the `pygame.Rect` class, providing additional convenience methods for handling rectangles in Pygame. This class simplifies common operations such as collision detection, moving, resizing, drawing rectangles, and more.

## Constructor:
Rec(x, y, width, height)

Parameters:
- x (int): The x-coordinate of the rectangle’s top-left corner.
- y (int): The y-coordinate of the rectangle’s top-left corner.
- width (int): The width of the rectangle.
- height (int): The height of the rectangle.

Example:
rect = Rec(50, 50, 100, 200)

## Methods:

### move_to(x, y)
Moves the rectangle to the specified position (x, y).

Parameters:
- x (int): The new x-coordinate for the top-left corner.
- y (int): The new y-coordinate for the top-left corner.

Example:
rect.move_to(200, 300)

### scale(width, height)
Scales the rectangle to the specified width and height.

Parameters:
- width (int): The new width of the rectangle.
- height (int): The new height of the rectangle.

Example:
rect.scale(150, 250)

### collides_with(other)
Checks if the current rectangle collides with another `Rec` or a `pygame.Rect`.

Parameters:
- other (Rec or pygame.Rect): The other rectangle to check for collision.

Returns:
- `True` if the rectangles are colliding, otherwise `False`.

Example:
if rect.collides_with(another_rect):
    print("Collision detected!")

### center(x, y)
Moves the center of the rectangle to the specified position (x, y).

Parameters:
- x (int): The new x-coordinate for the center.
- y (int): The new y-coordinate for the center.

Example:
rect.center(400, 300)

### inflate(width, height)
Inflates the rectangle by the given width and height (modifies the current rectangle).

Parameters:
- width (int): The amount to inflate the width.
- height (int): The amount to inflate the height.

Example:
rect.inflate(20, 40)

### intersection(other)
Returns a new `Rec` that represents the intersection of the current rectangle and another.

Parameters:
- other (Rec or pygame.Rect): The other rectangle to find the intersection with.

Returns:
- A new `Rec` representing the intersection area.

Example:
intersection_rect = rect.intersection(another_rect)

### move(x_offset, y_offset)
Moves the rectangle by the specified x and y offsets.

Parameters:
- x_offset (int): The amount to move the rectangle along the x-axis.
- y_offset (int): The amount to move the rectangle along the y-axis.

Example:
rect.move(10, -5)

### contains(x, y)
Checks if a point (x, y) is inside the rectangle.

Parameters:
- x (int): The x-coordinate of the point to check.
- y (int): The y-coordinate of the point to check.

Returns:
- `True` if the point is inside the rectangle, otherwise `False`.

Example:
if rect.contains(60, 80):
    print("Point is inside the rectangle.")

### get_position()
Returns the current position (x, y) of the rectangle’s top-left corner.

Returns:
- A tuple (x, y) representing the top-left corner of the rectangle.

Example:
x, y = rect.get_position()

### get_size()
Returns the current size (width, height) of the rectangle.

Returns:
- A tuple (width, height) representing the size of the rectangle.

Example:
width, height = rect.get_size()

### draw(surface, color)
Draws the rectangle on a Pygame surface with the specified color.

Parameters:
- surface (pygame.Surface): The Pygame surface to draw the rectangle on.
- color (tuple): The color to draw the rectangle (e.g., (255, 0, 0) for red).

Example:
rect.draw(screen, (255, 0, 0))

## Example Usage:
import pygame

pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Create Rec objects
rect1 = Rec(100, 100, 150, 200)
rect2 = Rec(250, 150, 100, 120)

# Check for collision
if rect1.collides_with(rect2):
    print("Rectangles are colliding!")

# Draw the rectangles
rect1.draw(screen, (255, 0, 0))  # Red rectangle
rect2.draw(screen, (0, 255, 0))  # Green rectangle

---

### Core Methods

#### quit 
for quiting use avents() like 
```
while True:
  for event in avents():
     if event.type == QUIT:
        sys.exit()
```

#### color :

color is a function that sets color of the window like
```
core.color(r, g, b)
```
its has default white color means if you want white just call it empty like core.color()

#### flip :

flip is a function that flips the screen like 
```
core.flip(clock=value) # like 60
```
its has global clock you can set means the time you created your Core a clock also get created core.clock so its always have a clock
but you can also create your own

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

### Packaging
use `package__asio__()` call it anywhere in code and run the file with `python file package` 
and a standalone exe generated of app
can place it anywhere after the asix import 

---

### Additional Methods
these methods can get called direct without `core.`

### `collide(rect1, rect2)`

The `collide` function checks if two rectangles are overlapping or colliding with each other.

#### Parameters:
- `rect1` (pygame.Rect): The first rectangle to check for collision. This should be a `pygame.Rect` object.
- `rect2` (pygame.Rect): The second rectangle to check for collision. This should also be a `pygame.Rect` object.

#### Return Value:
- **bool**: The function returns `True` if the two rectangles are colliding (overlapping), and `False` if they are not.

#### How It Works:
- The function uses the `colliderect` method of `pygame.Rect` objects to determine if the two rectangles overlap.
- `colliderect` checks if the area of the first rectangle (`rect1`) intersects with the area of the second rectangle (`rect2`).
- If the rectangles overlap, the function will return `True`; otherwise, it will return `False`.

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

basic structure
```
from asix import *

_ = Core(800, 600, 'optimize')

while True:
    for event in avents():
       if event.type == QUIT:
          sys.exit()
    _.color(250, 250, 250)

    _.flip(60)
```

---

# Easter Eggs 🎊

### Screenshot
used to get a pic of window 
```
def screenshot(surface: pygame.Surface, filename: str = 'screenshot.png') -> None:
```
no `core.` required

---

# Asix Release Notes

## [v7.8] -2025

### Added

- new rec class
- new avents for manual events handling for more powerfull access
- improved structure
- improved proformance
- new function GLS show all info about window realtime like its placed on top of flip
- fully functional core packager__asio__()
```
[width] → 800
[height] → 600
[screen] → <Surface(800x600x32 SW)>
[flags] → optimize
[clock] → <Clock(fps=0.00)>
[font] → <pygame.font.Font object at 0x0000019F532B1AA0>
[type] → <asix.core>
[version] → 7.8
[rendering-engine] → <pygame.render>
[color] → (250, 250, 250)
[Backend] → windows
[Video-Display] → <built-in function Info>
```
- new @once decorator
- new collison function collide()

### Changed

- removed specifer R for rect R(x, y, w, h)
- removed auto quit function core.quit()
- removed draw function for rects
- removed unused functions
- removed config mode flag=config

---

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

## Note From Developer
i removed them in latest version because if we make it look good its have no power if its complex and no power its not useless if it simple and powerfull then its good
i am trying to find a balance between power and simple
