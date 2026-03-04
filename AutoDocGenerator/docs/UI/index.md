# UI

> Auto-generated documentation for the **UI** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `Initialize(float density, int min)`

**Returns:** `void`



### `Initialize(Widgets::Registry &reg)`

**Returns:** `void`



### `FontHeight(float density, int min)`

**Returns:** `int`



### `Initialize(float density = 7.5, int min = 9)`

**Returns:** `void`


Initializes the UI system. Creates a simple widget template generator based on the primary monitor resolution. Density controls the size of the widgets. Increased density leads to smaller widgets. 7.5 leads to 12pt/16px on a FullHD monitor. This is a very relaxed and easy to use and read. 10 is more or less standard density.


### `Initialize(Widgets::Registry &reg)`

**Returns:** `void`


Initializes the UI system with the supplied registry. The registry will be activated. Ensure registry is initialized before supplied to this function.


### `FontHeight(float density = 7.5, int min = 9)`

**Returns:** `int`


Calculates based on the primary monitor resolution. Density controls the size of the font. Increased density leads to smaller fonts. 7.5 leads to 12pt/16px on a FullHD monitor. This is a very relaxed and easy to use and read. 10 is more or less standard density.

