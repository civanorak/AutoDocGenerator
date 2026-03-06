# Console

&gt; Auto-generated documentation for the **Console** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Console`

**Namespace:** `Gorgon`

Console manipulation functions. Not thread safe. Current only std::cout is supported.

#### Methods

##### `StdOutConsole(—)`

**Returns:** `Console`

##### `ColorSupport(—)`

**Returns:** `ColorSupportLevel`

Returns if color is supported in this terminal

##### `IsColorSupported(—)`

**Returns:** `bool`

Returns if the color is supported by this console

##### `IsReady(—)`

**Returns:** `bool`

Returns if the console is usable

##### `bool(—)`

**Returns:** `explicit operator`

Returns if the console is usable

##### `IsStylesSupported(—)`

**Returns:** `bool`

Returns if color is supported in this terminal. Even if this is false, bold can be emulated.

##### `SetColor(Color color)`

**Returns:** `void`

Sets the color to the given value, avoid, black and white as console can have its background color reversed. Use Default to set it to default color.

##### `SetColor(Graphics::RGBA color)`

**Returns:** `void`

Sets the color to the given value, avoid, black and white as console can have its background color reversed. Use Default to set it to default color.

##### `SetBackground(Color color)`

**Returns:** `void`

Sets the background color to the given value. Use Default to set it to default color.

##### `SetBackground(Graphics::RGBA color)`

**Returns:** `void`

Sets the background color to the given value. Use Default to set it to default color.

##### `Reset(—)`

**Returns:** `void`

Resets terminal attributes

##### `SetBold(bool bold=true)`

**Returns:** `void`

Sets terminal font to bold or normal

##### `SetUnderline(bool underline=true)`

**Returns:** `void`

Enable/disable underline. Not all consoles support underline

##### `SetItalic(bool italic=true)`

**Returns:** `void`

Enable/disable italic. Not all consoles support italic

##### `SetNegative(bool negative=true)`

**Returns:** `void`

Background/foreground is switched.

##### `GetSize(—)`

**Returns:** `Geometry::Size`

Returns the size of the console window in cols/rows

##### `GetWidth(—)`

**Returns:** `int`

Returns the size of the console window in cols/rows

##### `GetHeight(—)`

**Returns:** `int`

Returns the size of the console window in cols/rows

##### `GotoXY(Geometry::Point location)`

**Returns:** `void`

Changes the position of the caret to the given position

##### `GotoXY(int x, int y)`

**Returns:** `inline void`

Changes the position of the caret to the given position

##### `ClearScreen(—)`

**Returns:** `void`

Clears the console screen

##### `HideCaret(—)`

**Returns:** `void`

Hides input cursor

##### `ShowCaret(—)`

**Returns:** `void`

Shows input cursor


### `ConsoleBackend`

**Namespace:** `Gorgon`

@cond internal

#### Methods

##### `virtual` `ColorSupport(—)`

**Returns:** `virtual Console::ColorSupportLevel`

##### `virtual` `IsStylesSupported(—)`

**Returns:** `virtual bool`

##### `virtual` `SetColor(Console::Color color)`

**Returns:** `virtual void`

##### `virtual` `SetColor(Graphics::RGBA color)`

**Returns:** `virtual void`

##### `virtual` `SetBackground(Console::Color color)`

**Returns:** `virtual void`

##### `virtual` `SetBackground(Graphics::RGBA color)`

**Returns:** `virtual void`

##### `virtual` `Reset(—)`

**Returns:** `virtual void`

##### `virtual` `SetBold(bool value)`

**Returns:** `virtual void`

##### `virtual` `SetUnderline(bool value)`

**Returns:** `virtual void`

##### `virtual` `SetItalic(bool value)`

**Returns:** `virtual void`

##### `virtual` `SetNegative(bool value)`

**Returns:** `virtual void`

##### `virtual` `GetSize(—)`

**Returns:** `virtual Geometry::Size`

##### `virtual` `GotoXY(Geometry::Point location)`

**Returns:** `virtual void`

##### `virtual` `ClearScreen(—)`

**Returns:** `virtual void`

##### `virtual` `HideCaret(—)`

**Returns:** `virtual void`

##### `virtual` `ShowCaret(—)`

**Returns:** `virtual void`


### `StdOutBackend`

**Namespace:** `Gorgon`


---

## Enums

### `ColorSupportLevel`

**Namespace:** `Gorgon`

Empty console, nothing can be done with it. Creates a new console with the specified backend Console objects can be copied. They are reference counted Console objects can be copied. They are reference counted Level of support for color


### `Color`

**Namespace:** `Gorgon`

Color is not supported Only colors in the safelist can be used Graphics::RGBA can be used for color The colors that can be used for console coloring. This is a safe list


---

## Functions

### `StdConsole()`

**Returns:** `inline Console`


Creates a standard IO console


### `if(refcount)`

**Returns:** ``


