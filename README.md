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

```markdown
## class rec

A wrapper class for `pygame.Rect` to simplify rectangle operations.

This class provides a convenient way to work with rectangles, offering methods for movement, scaling, collision detection, drawing, and more. It is designed to be used with Pygame and assumes you have a `core.screen` surface available for drawing operations.

```python
class rec:
    def __init__(self, x, y, width, height):
```

### `__init__(self, x, y, width, height)`

Initializes a new `rec` object.

**Args:**

*   `x` (int): The x-coordinate of the top-left corner.
*   `y` (int): The y-coordinate of the top-left corner.
*   `width` (int): The width of the rectangle.
*   `height` (int): The height of the rectangle.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
```

---

```python
    def __repr__(self):
```

### `__repr__(self)`

Returns a string representation of the `rec` object.

This method provides a human-readable string that represents the rectangle's properties, useful for debugging and logging.

**Returns:**

*   str: A string in the format `rec(x=..., y=..., width=..., height=...)`.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
print(my_rect)  # Output: rec(x=10, y=20, width=50, height=30)
```

---

```python
    def move_to(self, x, y):
```

### `move_to(self, x, y)`

Moves the rectangle to a new position.

**Args:**

*   `x` (int): The new x-coordinate for the top-left corner.
*   `y` (int): The new y-coordinate for the top-left corner.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
my_rect.move_to(100, 150)
```

---

```python
    def scale(self, width, height):
```

### `scale(self, width, height)`

Scales the rectangle to a new size.

**Args:**

*   `width` (int): The new width of the rectangle.
*   `height` (int): The new height of the rectangle.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
my_rect.scale(100, 60)
```

---

```python
    def collide(self, other):
```

### `collide(self, other)`

Checks if this rectangle collides with another rectangle.

**Args:**

*   `other` (rec or pygame.Rect): The rectangle to check collision with.

**Returns:**

*   bool: `True` if the rectangles collide, `False` otherwise.

**Raises:**

*   TypeError: If `other` is not a `rec` or `pygame.Rect` object.

**Example:**

```python
rect1 = rec(10, 20, 50, 30)
rect2 = rec(40, 10, 60, 40)
if rect1.collide(rect2):
    print("Rectangles collide!")
```

---

```python
    def center(self, x, y):
```

### `center(self, x, y)`

Moves the center of the rectangle to a new position.

**Args:**

*   `x` (int): The new x-coordinate for the center of the rectangle.
*   `y` (int): The new y-coordinate for the center of the rectangle.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
my_rect.center(100, 100)
```

---

```python
    def inflate(self, width, height):
```

### `inflate(self, width, height)`

Inflates the rectangle by the specified width and height.

This method modifies the rectangle in-place, expanding it outwards from its center.

**Args:**

*   `width` (int): The amount to inflate horizontally (can be negative to deflate).
*   `height` (int): The amount to inflate vertically (can be negative to deflate).

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
my_rect.inflate(20, 10)  # Inflates by 20 pixels horizontally and 10 pixels vertically
```

---

```python
    def intersection(self, other):
```

### `intersection(self, other)`

Calculates the intersection of this rectangle with another rectangle.

**Args:**

*   `other` (rec or pygame.Rect): The rectangle to intersect with.

**Returns:**

*   rec: A new `rec` object representing the intersection of the two rectangles. If there is no intersection, the returned rectangle will have a width or height of 0.

**Raises:**

*   TypeError: If `other` is not a `rec` or `pygame.Rect` object.

**Example:**

```python
rect1 = rec(10, 20, 50, 30)
rect2 = rec(40, 10, 60, 40)
intersection_rect = rect1.intersection(rect2)
print(intersection_rect)
```

---

```python
    def move(self, x_offset, y_offset):
```

### `move(self, x_offset, y_offset)`

Moves the rectangle by a given offset.

This method modifies the rectangle's position in-place.

**Args:**

*   `x_offset` (int): The horizontal offset to move by.
*   `y_offset` (int): The vertical offset to move by.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
my_rect.move(5, -10) # Move 5 pixels right and 10 pixels up
```

---

```python
    def contains(self, x, y):
```

### `contains(self, x, y)`

Checks if a point is inside the rectangle.

**Args:**

*   `x` (int): The x-coordinate of the point.
*   `y` (int): The y-coordinate of the point.

**Returns:**

*   bool: `True` if the point is inside the rectangle, `False` otherwise.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
if my_rect.contains(30, 30):
    print("Point is inside the rectangle.")
```

---

```python
    def get_position(self):
```

### `get_position(self)`

Returns the current position of the rectangle.

**Returns:**

*   tuple: A tuple `(x, y)` representing the top-left corner coordinates.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
position = my_rect.get_position()
print(position) # Output: (10, 20)
```

---

```python
    def get_size(self):
```

### `get_size(self)`

Returns the current size of the rectangle.

**Returns:**

*   tuple: A tuple `(width, height)` representing the dimensions of the rectangle.

**Example:**

```python
my_rect = rec(10, 20, 50, 30)
size = my_rect.get_size()
print(size) # Output: (50, 30)
```

---

```python
    def draw(self, surface, color, width=0):
```

### `draw(self, surface, color, width=0)`

Draws the rectangle on a Pygame surface.

**Args:**

*   `surface` (pygame.Surface): The surface to draw the rectangle on.  If using within the core framework, you can use `core.screen`.
*   `color` (tuple): The color of the rectangle in RGB format (e.g., `(255, 0, 0)` for red).
*   `width` (int, optional): The width of the rectangle's border. If `0`, the rectangle is filled. Defaults to `0`.

**Example:**

```python
import pygame
# Assuming you have initialized pygame and have a screen surface called 'core.screen'
my_rect = rec(10, 20, 50, 30)
my_rect.draw(core.screen, (255, 255, 255)) # Draw a white filled rectangle
my_rect.draw(core.screen, (0, 0, 255), width=2) # Draw a blue rectangle outline with thickness 2
pygame.display.flip() # Update the display to show the drawn rectangle
```

---

```python
    def copy(self):
```

### `copy(self)`

Creates and returns a copy of this `rec` object.

**Returns:**

*   rec: A new `rec` object with the same position and size as the original.

**Example:**

```python
rect1 = rec(10, 20, 50, 30)
rect2 = rect1.copy()
rect2.move_to(100, 100) # Modifying rect2 does not affect rect1
```

---

```python
    def target(self, other, surface, color=(0, 0, 0), width=1):
```

### `target(self, other, surface, color=(0, 0, 0), width=1)`

Draws a line from the center of this rectangle to the center of another rectangle.

**Args:**

*   `other` (rec or pygame.Rect): The target rectangle to draw a line to.
*   `surface` (pygame.Surface): The surface to draw the line on. If using within the core framework, you can use `core.screen`.
*   `color` (tuple, optional): The color of the line in RGB format. Defaults to black `(0, 0, 0)`.
*   `width` (int, optional): The thickness of the line. Defaults to `1`.

**Raises:**

*   TypeError: If `other` is not a `rec` or `pygame.Rect` object.

**Example:**

```python
import pygame
# Assuming you have initialized pygame and have a screen surface called 'core.screen'
rect1 = rec(10, 20, 50, 30)
rect2 = rec(150, 120, 40, 40)
rect1.target(rect2, core.screen, color=(255, 0, 0), width=3) # Draw a red line of thickness 3
pygame.display.flip()
```

---

```python
    def is_near(self, other, distance):
```

### `is_near(self, other, distance)`

Checks if this rectangle is within a certain distance of another rectangle.

**Args:**

*   `other` (rec or pygame.Rect): The rectangle to check proximity to.
*   `distance` (int): The maximum distance to consider "near".

**Returns:**

*   bool: `True` if the rectangles are within the specified distance, `False` otherwise.

**Raises:**

*   TypeError: If `other` is not a `rec` or `pygame.Rect` object.

**Example:**

```python
rect1 = rec(10, 20, 50, 30)
rect2 = rec(80, 50, 40, 40)
if rect1.is_near(rect2, 20):
    print("Rectangles are near each other.")
```

---

```python
    def align(self, alignment, width, height):
```

### `align(self, alignment, width, height)`

Aligns the rectangle to a specific position within a given area.

**Args:**

*   `alignment` (str): The alignment type. Valid options are:
    *   `'center'`
    *   `'top-left'`
    *   `'top-right'`
    *   `'bottom-left'`
    *   `'bottom-right'`
*   `width` (int): The width of the area to align within.
*   `height` (int): The height of the area to align within.

**Example:**

```python
my_rect = rec(50, 50, 30, 20)
my_rect.align('center', 800, 600) # Center the rectangle within an 800x600 area
my_rect.align('top-left', 800, 600) # Move to top-left corner of an 800x600 area
```

---

```python
    def collides_with_any(self, others):
```

### `collides_with_any(self, others)`

Checks if this rectangle collides with any rectangle in a list of rectangles.

**Args:**

*   `others` (list of rec): A list of `rec` objects to check for collisions with.

**Returns:**

*   bool: `True` if this rectangle collides with at least one rectangle in the list, `False` otherwise.

**Example:**

```python
rect1 = rec(10, 20, 50, 30)
rect2 = rec(40, 10, 60, 40)
rect3 = rec(200, 200, 30, 30)
rects_to_check = [rect2, rect3]

if rect1.collides_with_any(rects_to_check):
    print("rect1 collides with at least one rectangle in the list.")
```

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
