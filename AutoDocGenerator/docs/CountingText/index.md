# CountingText

> Auto-generated documentation for the **CountingText** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `CountingText`

**Namespace:** `gge`

/This effect displays a counting number going from a given value to another one.

#### Methods

##### `CountingText(animation::Timer &controller, bool owner=false)`

**Returns:** ``

/Color of the text, default is black /Text shadow, default is none /Alignment of the text, default is left /Width of the text /Number of decimal places, default is 0 /Customized printing format, printf style that can feature a %f as the current value /The font to be used /Initializes the effect

##### `CountingText(bool create=false)`

**Returns:** `explicit`

/Initializes the effect

##### `Current(—)`

**Returns:** `float`

##### `Setup(float From, float To, int Time)`

**Returns:** `void`

/Sets source and destination to the given values and allows time duration to reach the destination

##### `Setup(float To, int Time)`

**Returns:** `void`

/Sets current destination to the given value and allows time duration to reach it

##### `Print(graphics::ColorizableImageTarget2D *target, int X, int Y)`

**Returns:** `void`

/Prints the current text to a layer

##### `Print(graphics::ColorizableImageTarget2D &target, int X, int Y)`

**Returns:** `void`

/Prints the current text to a layer

##### `Print(&target, X, Y)`

**Returns:** ``

##### `virtual` `Progress(—)`

**Returns:** `virtual animation::ProgressResult::Type`


---

## Functions

### `if(from>to)`

**Returns:** ``


