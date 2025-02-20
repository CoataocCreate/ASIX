# ASIX
The Asix Graphics Library

## Introduction
Asix is a user-friendly 2D Python graphics library built upon the robust foundation of the Pygame engine. It offers seamless integration with Pygame, meaning you can directly utilize familiar Pygame methods within Asix's core functionalities.  Asix is designed with simplicity and power in mind, providing straightforward yet effective tools for 2D game development and graphical applications.  Its methods are intentionally easy to learn and use, without sacrificing the capability to create impressive and performant visuals.

1. Extends Pygame's capabilities with simplified functions and classes.
2. Aims to provide a more intuitive interface for Pygame.
3. Provides added tools and functions for more efficient pygame use.

! you can use any pygame function without import pygame and can get core.screen to do anything

## Version : Asix 7.8

### Install

There are multiple ways to install and use `asix`:

**1. Install via pip (Recommended for most users):**

   The easiest way to install `asix` is using pip, the Python package installer. Open your terminal or command prompt and run one of the following commands:

   *   **To install the latest version:**

       ```bash
       pip install asix
       ```

   *   **To install a specific version (if needed):**

       Replace `version` with the desired version number. For example, to install version `1.2.3`:

       ```bash
       pip install asix==1.2.3
       ```

   Pip will automatically download and install `asix` and any required dependencies from the Python Package Index (PyPI).

**2. Install from Source (For latest features and potential bug fixes):**

   For users who want to access the most recent updates, bug fixes, or contribute to the development of `asix`, installing from the source code is recommended.

   *   **Download `asix.py`:**

       Obtain the `asix.py` file directly from the source repository (e.g., GitHub, GitLab, or wherever the source code is hosted).  Refer to the project's README or website for the source code location.

   *   **Place `asix.py` in your project:**

       Move the downloaded `asix.py` file into the same directory as your Python script where you intend to use `asix`.

   *   **Import `asix` in your script:**

       You can now import and use `asix` in your Python code using a standard import statement:

       ```python
       from asix import *  # Imports all functions and classes from asix
       # or
       import asix       # Imports the asix module, access members using asix.member
       ```

**Important Note Regarding Updates:**

   While pip installation provides a convenient way to manage packages, updates to `asix` on PyPI might be less frequent than updates to the source code repository.  If you require the absolute latest features or bug fixes, downloading `asix.py` directly from the source and using it in your project is the most direct way to ensure you are using the most up-to-date version.  Check the project's source repository for the latest commits and release information.

---

# Table of Contents

<ul style="list-style-type: none; padding-left: 0px;">
  <li>
    <details>
      <summary style="cursor: pointer; font-weight: bold;">1. ASIX - The Asix Graphics Library</summary>
      <ul style="list-style-type: none; padding-left: 20px;">
        <li><a href="#introduction" style="text-decoration: none; color: #333;">1.1. Introduction</a></li>
        <li><a href="#version--asix-78" style="text-decoration: none; color: #333;">1.2. Version : Asix 7.8</a></li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.3. Install</summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li><a href="#install-via-pip-recommended-for-most-users" style="text-decoration: none; color: #333;">1.3.1. Install via pip (Recommended for most users)</a></li>
              <li><a href="#install-from-source-for-latest-features-and-potential-bug-fixes" style="text-decoration: none; color: #333;">1.3.2. Install from Source (For latest features and potential bug fixes)</a></li>
            </ul>
          </details>
        </li>
        <li><a href="#core" style="text-decoration: none; color: #333;">1.4. Core</a></li>
        <li><a href="#flags" style="text-decoration: none; color: #333;">1.4.1. Flags</a></li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.5. Core Built-in's</summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li><a href="#staticmethod-consoleargs-ed0-capturefalse" style="text-decoration: none; color: #333;">1.5.1. <code>@staticmethod console(*args, ed=0, capture=False)</code></a></li>
              <li><a href="#once-decorator" style="text-decoration: none; color: #333;">1.5.2. <code>@once</code> Decorator</a></li>
              <li><a href="#avents" style="text-decoration: none; color: #333;">1.5.3. avents</a></li>
              <li><a href="#polygon" style="text-decoration: none; color: #333;">1.5.4. polygon</a></li>
              <li><a href="#globe" style="text-decoration: none; color: #333;">1.5.5. globe</a></li>
              <li><a href="#blit" style="text-decoration: none; color: #333;">1.5.6. blit</a></li>
              <li><a href="#key--k" style="text-decoration: none; color: #333;">1.5.7. key / K</a></li>
              <li><a href="#text" style="text-decoration: none; color: #333;">1.5.8. text</a></li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.6. <code>class rec</code></summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li><a href="#initself-x-y-width-height" style="text-decoration: none; color: #333;">1.6.1. <code>__init__(self, x, y, width, height)</code></a></li>
              <li><a href="#reprself" style="text-decoration: none; color: #333;">1.6.2. <code>__repr__(self)</code></a></li>
              <li><a href="#move_toself-x-y" style="text-decoration: none; color: #333;">1.6.3. <code>move_to(self, x, y)</code></a></li>
              <li><a href="#scaleself-width-height" style="text-decoration: none; color: #333;">1.6.4. <code>scale(self, width, height)</code></a></li>
              <li><a href="#collideself-other" style="text-decoration: none; color: #333;">1.6.5. <code>collide(self, other)</code></a></li>
              <li><a href="#centerself-x-y" style="text-decoration: none; color: #333;">1.6.6. <code>center(self, x, y)</code></a></li>
              <li><a href="#inflateself-width-height" style="text-decoration: none; color: #333;">1.6.7. <code>inflate(self, width, height)</code></a></li>
              <li><a href="#intersectionself-other" style="text-decoration: none; color: #333;">1.6.8. <code>intersection(self, other)</code></a></li>
              <li><a href="#moveself-x_offset-y_offset" style="text-decoration: none; color: #333;">1.6.9. <code>move(self, x_offset, y_offset)</code></a></li>
              <li><a href="#containsself-x-y" style="text-decoration: none; color: #333;">1.6.10. <code>contains(self, x, y)</code></a></li>
              <li><a href="#get_positionself" style="text-decoration: none; color: #333;">1.6.11. <code>get_position(self)</code></a></li>
              <li><a href="#get_sizeself" style="text-decoration: none; color: #333;">1.6.12. <code>get_size(self)</code></a></li>
              <li><a href="#drawself-surface-color-width0" style="text-decoration: none; color: #333;">1.6.13. <code>draw(self, surface, color, width=0)</code></a></li>
              <li><a href="#copyself" style="text-decoration: none; color: #333;">1.6.14. <code>copy(self)</code></a></li>
              <li><a href="#targetself-other-surface-color0-0-0-width1" style="text-decoration: none; color: #333;">1.6.15. <code>target(self, other, surface, color=(0, 0, 0), width=1)</code></a></li>
              <li><a href="#is_nearself-other-distance" style="text-decoration: none; color: #333;">1.6.16. <code>is_near(self, other, distance)</code></a></li>
              <li><a href="#alignself-alignment-width-height" style="text-decoration: none; color: #333;">1.6.17. <code>align(self, alignment, width, height)</code></a></li>
              <li><a href="#collides_with_anyself-others" style="text-decoration: none; color: #333;">1.6.18. <code>collides_with_any(self, others)</code></a></li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.7. Core Methods</summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li><a href="#quit-1" style="text-decoration: none; color: #333;">1.7.1. quit</a></li>
              <li><a href="#color-1" style="text-decoration: none; color: #333;">1.7.2. color</a></li>
              <li><a href="#flip-1" style="text-decoration: none; color: #333;">1.7.3. flip</a></li>
              <li><a href="#caption-1" style="text-decoration: none; color: #333;">1.7.4. caption</a></li>
              <li><a href="#icon-1" style="text-decoration: none; color: #333;">1.7.5. icon</a></li>
              <li><a href="#font-1" style="text-decoration: none; color: #333;">1.7.6. Font</a></li>
            </ul>
          </details>
        </li>
        <li><a href="#packaging" style="text-decoration: none; color: #333;">1.8. Packaging</a></li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.9. Additional Methods</summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li><a href="#efload---image-loading-and-manipulation-class-documentation" style="text-decoration: none; color: #333;">1.9.1. <code>efload - Image Loading and Manipulation Class Documentation</code></a></li>
              <li><a href="#colliderect1-rect2" style="text-decoration: none; color: #333;">1.9.2. <code>collide(rect1, rect2)</code></a></li>
              <li><a href="#sic" style="text-decoration: none; color: #333;">1.9.3. sic</a></li>
              <li><a href="#pie" style="text-decoration: none; color: #333;">1.9.4. pie</a></li>
              <li><a href="#iload" style="text-decoration: none; color: #333;">1.9.5. iload</a></li>
              <li><a href="#isize" style="text-decoration: none; color: #333;">1.9.6. isize</a></li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.10. Easter Eggs 🎊</summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li><a href="#screenshot" style="text-decoration: none; color: #333;">1.10.1. Screenshot</a></li>
            </ul>
          </details>
        </li>
        <li><a href="#example-game-in-asix" style="text-decoration: none; color: #333;">1.11. Example Game in asix</a></li>
        <li><a href="#explaination" style="text-decoration: none; color: #333;">1.12. Explaination</a></li>
        <li>
          <details>
            <summary style="cursor: pointer; font-weight: bold;">1.13. Asix Release Notes</summary>
            <ul style="list-style-type: none; padding-left: 20px;">
              <li>
                <details>
                  <summary style="cursor: pointer; font-weight: bold;">1.13.1. [v7.8] -2025</summary>
                  <ul style="list-style-type: none; padding-left: 20px;">
                    <li><a href="#added-1" style="text-decoration: none; color: #333;">1.13.1.1. Added</a></li>
                    <li><a href="#changed-1" style="text-decoration: none; color: #333;">1.13.1.2. Changed</a></li>
                    <li><a href="#removed-1" style="text-decoration: none; color: #333;">1.13.1.3. Removed</a></li>
                  </ul>
                </details>
              </li>
              <li>
                <details>
                  <summary style="cursor: pointer; font-weight: bold;">1.13.2. [v7.7] -2025</summary>
                  <ul style="list-style-type: none; padding-left: 20px;">
                    <li><a href="#added-2" style="text-decoration: none; color: #333;">1.13.2.1. Added</a></li>
                    <li><a href="#changed-2" style="text-decoration: none; color: #333;">1.13.2.2. Changed</a></li>
                    <li><a href="#fixed-1" style="text-decoration: none; color: #333;">1.13.2.3. Fixed</a></li>
                  </ul>
                </details>
              </li>
              <li>
                <details>
                  <summary style="cursor: pointer; font-weight: bold;">1.13.3. [v7.6] -2025</summary>
                  <ul style="list-style-type: none; padding-left: 20px;">
                    <li><a href="#added-3" style="text-decoration: none; color: #333;">1.13.3.1. Added</a></li>
                    <li><a href="#changed-3" style="text-decoration: none; color: #333;">1.13.3.2. Changed</a></li>
                    <li><a href="#fixed-2" style="text-decoration: none; color: #333;">1.13.3.3. Fixed</a></li>
                  </ul>
                </details>
              </li>
              <li><a href="#note-from-developer" style="text-decoration: none; color: #333;">1.13.4. Note From Developer</a></li>
            </ul>
          </details>
        </li>
      </ul>
    </details>
  </li>
</ul>

---

### Core
Core is the main Object of Screen and contains all methods you can use it like :

`var = Core(width, height, flags)`

its take `width` of screen and take `height` of screen
and last flags so flags are like special effects we can put on window and rendering 
flags are `borderless` makes screen without any border title buttons 
`resizeable` makes screen resizeable and `optimize` 
is a perfomance enchancer
! important to note `optimize` or `optimized` flag may not work on all devices and cause proformance issue like on gpu its only hardware accelarate

---

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
  
<hr>

#### `@once` Decorator

The `@once` decorator is a powerful tool for ensuring that a function executes **only a single time** throughout the lifetime of your program, no matter how many times it is called. Even if invoked repeatedly, including within loops or from different parts of your code, the decorated function will run its code just once during the very first call. Subsequent calls will be effectively ignored, returning `None` (or the original return value of the first execution, depending on the implementation of `@once`, though typically it's designed to just prevent re-execution).

This decorator is particularly useful in scenarios where you need to perform initialization tasks, setup procedures, or any action that should only happen once and should not be repeated accidentally or unintentionally.

### Key Features and Benefits:

*   **Guaranteed Single Execution:**  Ensures a function's code block runs only on its first invocation.
*   **Prevents Redundant Operations:** Avoids unnecessary repetition of time-consuming or resource-intensive tasks that should only be performed once.
*   **Simplifies Initialization:**  Ideal for setting up global variables, establishing connections, loading configuration files, or any one-time setup required by your application.
*   **Enhances Code Clarity:**  Explicitly marks functions intended for single execution, improving code readability and maintainability.
*   **Robustness:** Protects against accidental or unintended multiple executions, especially in complex codebases or multithreaded environments (though thread-safety might depend on the specific implementation of `@once`).

### When to Use `@once`:

Consider using the `@once` decorator in situations like:

*   **Initializing Global Resources:**  Loading a configuration file, establishing a database connection, or setting up a logging system at the start of your program.
*   **Performing Setup Tasks:**  Running a function to initialize hardware, configure external libraries, or perform any setup that should only occur once.
*   **Caching Expensive Computations:**  Calculating a value that is computationally expensive and needs to be reused throughout the program. While `@once` will execute the function only once, you might need to adjust its implementation to actually *return* and *store* the computed value for later use if that's your primary goal (a simple `@once` might just prevent re-execution but not necessarily cache the result).
*   **Preventing Side Effects:**  Ensuring a function with side effects (like modifying global state) is executed only once to avoid unintended consequences from repeated calls.

<hr>

#### avents

The `avents()` function provides a straightforward and convenient way to access and process Pygame events, acting as a direct replacement for the standard `pygame.event.get()` method.  It simplifies the event handling process within your Pygame applications, allowing you to iterate through events in a clean and readable manner.

**Functionality:**

`avents()` effectively returns an iterable object that yields each Pygame event currently in the event queue. This behavior mirrors `pygame.event.get()`, ensuring compatibility with existing Pygame event handling patterns.  You can use `avents()` within a `for` loop to process each event individually, just as you would with `pygame.event.get()`.

**Usage:**

To use `avents()`, simply replace `pygame.event.get()` in your event loop with `avents()`.  The structure of your event handling code remains largely the same.

<hr>

#### polygon

polygon(color, points) Function: Intuitive Polygon Drawing
The polygon(color, points) function provides a simplified and user-friendly way to draw polygons on the Pygame screen. Unlike standard Pygame polygon drawing functions, polygon is designed to be more intuitive by directly accepting a list of points defining the polygon's vertices and automatically handling point ordering for correct rendering.

Functionality:

polygon() draws a filled polygon based on the provided list of points. It intelligently manages the point order, eliminating the need to manually ensure clockwise or counter-clockwise ordering, which can be a common source of confusion with pygame.draw.polygon. This function is versatile and can be used to draw triangles, quadrilaterals, and polygons with any number of vertices.

Parameters:

color

Type: tuple of int (R, G, B) or pygame.Color

Description: The color to fill the polygon. This should be specified as an RGB tuple (e.g., (255, 0, 0) for red) or a pygame.Color object.

points

Type: list or tuple of tuple or list of int

Description: A sequence of points that define the vertices of the polygon. Each point should be a tuple or list containing two integers representing the x and y coordinates (x, y).

Example: [(100, 100), (200, 100), (150, 200)] for a triangle, [(50, 50), (150, 50), (150, 150), (50, 150)] for a square.

Key Advantages over pygame.draw.polygon:

Point-Based Intuition: Directly define your polygon using its vertices, making it natural for shapes described by their corners.

Automatic Point Ordering: No need to worry about clockwise or counter-clockwise point order. polygon() handles point arrangement internally to ensure correct polygon rendering, simplifying the drawing process and reducing potential errors.

Simplified Usage: Focus on defining the shape with points and color, without the complexities of point flipping or ordering often encountered with pygame.draw.polygon.

Versatile Shape Drawing: Draw triangles, quadrilaterals, and complex polygons with ease by simply providing the corresponding list of vertices.

```
points = [(100, 100), (200, 100), (150, 200)]
core.polygon(color, points)
```
Draws a Triangle and you can put as many points as want 

<hr>

#### globe

## `globe(self, x, y, radius, fill_color, border_color=None, border_width=0)`

### Description

Draws a circle (often referred to as a "globe" in this context, implying a solid filled circle) on the Pygame screen associated with the current object (`self.screen`). This function offers customization for the circle's position, size, fill color, and optional border.

### Parameters

*   **`self`**
    *   *Type:*  Instance of the class containing this method.
    *   *Description:*  Refers to the current object instance. It's implicitly passed in Python method calls and is used here to access `self.screen`, which is assumed to be the Pygame surface where the circle will be drawn.

*   **`x`**
    *   *Type:* `int` or `float`
    *   *Description:* The x-coordinate of the center of the circle on the Pygame surface.

*   **`y`**
    *   *Type:* `int` or `float`
    *   *Description:* The y-coordinate of the center of the circle on the Pygame surface.

*   **`radius`**
    *   *Type:* `int` or `float`
    *   *Description:* The radius of the circle in pixels.  A larger value will result in a bigger circle.

*   **`fill_color`**
    *   *Type:* `tuple` of `int` (R, G, B) or `pygame.Color`
    *   *Description:* The color to fill the inside of the circle.  This should be specified as an RGB tuple where each value (Red, Green, Blue) is an integer between 0 and 255, or a `pygame.Color` object.
    *   *Example:* `(255, 0, 0)` for red, `(0, 255, 0)` for green, `(0, 0, 255)` for blue, `(255, 255, 255)` for white, `(0, 0, 0)` for black.

*   **`border_color`**
    *   *Type:* `tuple` of `int` (R, G, B) or `pygame.Color` or `None`
    *   *Description:* The color of the circle's border (outline).  Specified in the same RGB tuple or `pygame.Color` format as `fill_color`.
    *   *Default:* `None`
    *   *Note:* If `border_color` is set to `None`, no border will be drawn.

*   **`border_width`**
    *   *Type:* `int`
    *   *Description:* The width of the circle's border in pixels.
    *   *Default:* `0`
    *   *Note:* If `border_width` is `0`, no border will be drawn, regardless of whether `border_color` is set.  A positive integer value will draw a border of that thickness.

### Returns

*   `None`

    *   *Description:* This function does not return any value. It directly draws the circle onto the `self.screen` surface.

### Functionality

The `globe` function uses `pygame.draw.circle` to render a circle on the designated Pygame surface (`self.screen`).

*   **Border Drawing Logic:**
    *   If both `border_color` is not `None` and `border_width` is greater than `0`, the function first draws a circle with the specified `border_color` and the given `radius`.
    *   Then, it draws a second, smaller circle on top of the border circle, using the `fill_color` and a slightly reduced radius (`inner_radius = max(0, radius - border_width)`). This creates the visual effect of a border around the filled circle. The `max(0, ...)` ensures that `inner_radius` is never negative, preventing potential errors if `border_width` is larger than `radius`.
*   **Fill-Only Drawing:**
    *   If either `border_color` is `None` or `border_width` is `0`, the function directly draws a single filled circle with the `fill_color` and the specified `radius`.

```python
def globe(
    x: Any,
    y: Any,
    radius: Any,
    fill_color: Any,
    border_color: Any | None = None,
    border_width: int = 0,
    rotation = angle
) -> None

core.globe(100, 100, 70, (255, 255, 255), (r, g ,b), 10)

!Note If you dont want border skip border_color and border_width args
```
<hr>

#### blit :

blit(surface, position) Function: Simplified Image Drawing
The blit(surface, position) function offers a streamlined approach to drawing images (surfaces) onto the Pygame screen within your main game loop. It simplifies the process of image blitting, making it more concise and potentially more intuitive, especially for common use cases.

Functionality:

blit() is used to draw a Pygame Surface (which can represent an image loaded from a file or a dynamically created surface) onto the main display screen. It functions similarly to pygame.Surface.blit, but with a potentially simplified interface, especially in how it handles the destination surface (the screen).

Parameters:

surface

Type: pygame.Surface

Description: The Pygame Surface object that you want to draw (blit) onto the screen. This surface typically represents an image you've loaded or created.

position

Type: tuple of int

Description: A tuple (x, y) representing the top-left coordinates on the screen where the top-left corner of the surface will be positioned. These coordinates determine where the image will be drawn on the screen.

Simplified Usage and Screen Handling:

One of the key features of core.blit() is its potentially simplified usage regarding the destination surface. It may automatically assume that you want to blit onto the main display screen, potentially removing the need to explicitly specify the screen surface each time you call blit. This can lead to more concise code, especially in scenarios where you are primarily drawing onto the main game window.

```
core.blit(surface, (x, y))
```
works like pygame one like a surface and img or just img with x, y and the screen auto get added

<hr>

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

<hr>

#### text
text function is a basic text renderer like 
```
core.text(size, color, text, x, y, font_type: optional, rotation: require a angle var)
```
its just print that text in window 
size is text size
color is text color
x is text x pos
y is text y pos
font_type for custom .ttf fonts you can put file name or path in a string
rotation rotate the text

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

```markdown
# efload - Image Loading and Manipulation Class Documentation

This document explains how to use the `efload` class and the `conpy` function provided in the Python code.  `efload` is designed to simplify image loading and basic manipulation using the PIL (Pillow) library, making images ready for use, especially with Pygame. The `conpy` function then bridges the gap to Pygame by converting the manipulated image into a Pygame Surface.

## Getting Started

To use `efload` and `conpy`, you need to have the following Python libraries installed:

*   **Pillow (PIL):**  For image processing. Install using pip: `pip install Pillow`
*   **Pygame:** For game development and image display. Install using pip: `pip install pygame`

Make sure you have these libraries installed before using the code.

## Using the `efload` Class

The `efload` class is the core of this image handling system. It allows you to load an image and perform various operations on it.

### 1. Importing the Class

First, import the `efload` class and Pygame in your Python script:

```python
from efload_module import efload # Assuming you saved the code in efload_module.py
import pygame

pygame.init() # Initialize Pygame
```

### 2. Creating an `efload` Object

To start working with an image, create an instance of the `efload` class, providing the path to your image file:

```python
image_handler = efload("path/to/your/image.png") # Replace with your image path
```

This will load the image located at `"path/to/your/image.png"` and prepare it for manipulation.  The `efload` object now holds the image data and provides methods to modify it.

### 3. Available Methods for Image Manipulation

Once you have an `efload` object, you can use the following methods to manipulate the loaded image:

*   **`show()`**:  Displays the current image in your default image viewer. Useful for quickly previewing the image at any stage.

    ```python
    image_handler.show() # Shows the current image
    ```

*   **`resize(width, height)`**: Resizes the image to the specified `width` and `height` in pixels.

    ```python
    image_handler.resize(200, 150) # Resizes the image to 200 pixels wide and 150 pixels tall
    ```

*   **`rotate(deg)`**: Rotates the image by the given angle `deg` in degrees (counter-clockwise).

    ```python
    image_handler.rotate(45) # Rotates the image by 45 degrees
    ```

*   **`blur()`**: Applies a blur effect to the image.

    ```python
    image_handler.blur() # Applies a blur filter
    ```

*   **`sharp()`**: Sharpens the image, enhancing details.

    ```python
    image_handler.sharp() # Applies a sharpen filter
    ```

*   **`edgen()`**: Enhances the edges in the image, making them more prominent.

    ```python
    image_handler.edgen() # Applies an edge enhancement filter
    ```

*   **`clear()`**: Resets the image back to its original state as it was when first loaded. This undoes all manipulations performed since loading.

    ```python
    image_handler.clear() # Resets the image to its original loaded state
    ```

**Important Note:**  Most of these methods modify the `efload` object's image directly. They do not return a new image object.  If you want to keep the original image and work on a modified version, you would need to create a copy of the `efload` object (though this is not directly supported by the provided code as is).

### 4. Accessing Image Information

The `efload` object also stores information about the loaded image, which you can access as attributes:

*   **`image_handler.format`**:  The format of the image file (e.g., 'PNG', 'JPEG').
*   **`image_handler.size`**:  A tuple representing the image dimensions `(width, height)`.
*   **`image_handler.mode`**: The color mode of the image (e.g., 'RGBA'). 'RGBA' includes an alpha channel for transparency.
*   **`image_handler.data`**: The raw byte data of the image, often needed for lower-level graphics operations.

## Using the `conpy` Function

The `conpy` function is specifically designed to convert an `efload` object into a Pygame `Surface`. This is essential if you want to display or use the manipulated image within a Pygame application.

### 1. Importing the Function

Make sure the `conpy` function is available in your script (it should be in the same file as `efload` in the provided code).

### 2. Converting to Pygame Surface

To convert an `efload` object to a Pygame Surface, simply pass your `efload` object to the `conpy` function:

```python
pygame_surface = conpy(image_handler) # Converts the efload object to a Pygame Surface
```

Now, `pygame_surface` is a standard Pygame `Surface` object that you can use like any other Pygame Surface – for blitting onto the screen, further manipulation within Pygame, etc.

### 3. Using the Pygame Surface

Once you have the Pygame Surface, you can use standard Pygame methods to display it or work with it in your game or application. For example, to display it on a Pygame screen:

```python
screen = pygame.display.set_mode((800, 600)) # Create a Pygame display
screen.blit(pygame_surface, (100, 100)) # Blit the image at position (100, 100)
pygame.display.flip() # Update the display to show the blitted image

# Keep the window open until closed (example event loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

## Example Workflow

Here's a simple example demonstrating a typical workflow:

1.  Load an image using `efload`.
2.  Resize and blur the image.
3.  Convert the manipulated `efload` object to a Pygame Surface.
4.  Display the Pygame Surface on a Pygame window.

```python
from efload_module import efload # Assuming saved in efload_module.py
import pygame

pygame.init()

# Load the image
image_handler = efload("path/to/your/image.png")

# Resize and blur
image_handler.resize(150, 100)
image_handler.blur()

# Convert to Pygame Surface
pygame_surface = conpy(image_handler)

# Pygame display setup and blitting (as shown in the previous section)
screen = pygame.display.set_mode((800, 600))
screen.blit(pygame_surface, (100, 100))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

This documentation should help you understand how to use the `efload` class and `conpy` function to load, manipulate, and prepare images for use with Pygame. Remember to replace `"path/to/your/image.png"` with the actual path to your image file.
```

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

## Example Game in asix 
a space rocks avoiding game
```
from asix import *
import random

# Initialize the game
_ = Core(600, 400, 'optimize')
_.caption("Simple Dodge Game (Text Only)")

@cooldown(1)
def Score():
     global score
     score += 1

# Player setup
player_x = 300
player_y = 350
player_speed = 5
player_width = 20
player_height = 20

# Enemy setup
enemies = []  # List to store enemies
enemy_speed = 3
spawn_timer = 60  # Spawn a new enemy every 60 frames
enemy_width = 15
enemy_height = 15

# Score
score = 0

# Game loop
running = True
clock = _.clock

while running:
    clock.tick(60)
    for event in avents():
        if event.type == QUIT:
            running = False

    keys = key()
    if keys[K("LEFT")]:
        player_x -= player_speed
    if keys[K("RIGHT")]:
        player_x += player_speed

    # Spawn enemies
    spawn_timer -= 1
    if spawn_timer <= 0:
        enemy_x = random.randint(0, 585)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])
        spawn_timer = 60  # Reset timer

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Collision detection
    player_rect = rec(player_x, player_y, player_width, player_height)
    for enemy in enemies:
        enemy_rect = rec(enemy[0], enemy[1], enemy_width, enemy_height)
        if player_rect.collide(enemy_rect):
            running = False  # Game over

    # Remove off-screen enemies
    enemies = [enemy for enemy in enemies if enemy[1] < 400]

    # Draw everything
    _.color(0, 0, 0)  # Black background

    # Draw player (green rectangle)
    pygame.draw.rect(_.screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

    # Draw enemies (red rectangles)
    for enemy in enemies:
        pygame.draw.rect(_.screen, (255, 0, 0), (enemy[0], enemy[1], enemy_width, enemy_height))

    # Draw score
    _.text(20, (255, 255, 255), f"Score: {score}", 50, 20)
     
    Score()

    _.flip()

_.exit()
```
<img src="https://i.ibb.co/6RH8p0rm/Screenshot-2025-02-20-163913.png" alt="Screenshot-2025-02-20-163913" border="0">

---

0# Explaination

So Asix is a library build in pure python and you dont need to import python or math because they come with asix and
Core is just a class which contains everthing while still have without class methods and its a simple wrapper of pygame
you dont need to import anything except asix

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
