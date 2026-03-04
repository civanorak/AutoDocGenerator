# Dimension

> Auto-generated documentation for the **Dimension** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Dimension`

**Namespace:** `Gorgon`

Dimension data for components. Allows relative position and sizing.

#### Methods

##### `dimension_calc(double value, Unit unit)`

**Returns:** `constexpr int`

Fixed pixel based dimensions Dimension will be relative to the parent and given in percent. If higher resolution is necessary use BasisPoint. 1/1000th of a pixel, there are only few places that this will be used. Currently only rotation center use non-integer pixels Dimension will be relative to the parent and given in 1/10000. Dimension will be relative to the text size, given value is the percent of the width of an EM dash. If no font information is found, 10px will be used for EM dash. Thus, 1 unit will be 0.1 pixels. Size in units defined by UI scale. Uses UnitSize and spacing Size in units defined by UI scale. Uses UnitSize and spacing. Spaces defined by UI scale. Fractions of the container. Defaults to 6 if not set.

##### `switch(unit)`

**Returns:** ``

##### `Calculate(parentwidth, unitsize, spacing, emwidth, fractions, issize)`

**Returns:** `return`

Constructs a new dimension or type casts integer to dimension Constructs a new dimension or type casts real number to dimension Constructs a new dimension or type casts real number to dimension Returns the calculated dimension in pixels

##### `Calculate(int parentwidth, int unitsize, int spacing, int emwidth = 10, int fractions = 6, bool issize = false)`

**Returns:** `constexpr int`

Returns the calculated dimension in pixels

##### `if(issize)`

**Returns:** ``

##### `switch(unit)`

**Returns:** ``

##### `switch(unit)`

**Returns:** ``

##### `CalculateFloat(float parentwidth, int unitsize, int spacing, float emwidth = 10, int fractions = 6, bool issize = false)`

**Returns:** `constexpr float`

Returns the calculated dimension in pixels

##### `if(issize)`

**Returns:** ``

##### `switch(unit)`

**Returns:** ``

##### `float(value * unitsize)`

**Returns:** `return`

##### `float(value * spacing)`

**Returns:** `return`

##### `switch(unit)`

**Returns:** ``

##### `float(value * spacing)`

**Returns:** `return`

##### `IsRelative(—)`

**Returns:** `constexpr bool`

Returns if the dimension is relative to the parentwidth

##### `GetValue(—)`

**Returns:** `constexpr int`

Returns the value of the dimension, should not be considered as pixels

##### `GetUnit(—)`

**Returns:** `constexpr Unit`

Returns the unit of the dimension

##### `Set(int value)`

**Returns:** `constexpr void`

Changes the value of the dimension without modifying the units

##### `Set(int value, Unit unit)`

**Returns:** `constexpr void`

Changes the value and unit of the dimension.


### `UnitDimension`

**Namespace:** `Gorgon`

Similar to Dimension except default unit is UnitSize and supports floats and doubles for automatic conversion


### `DualDimension`

**Namespace:** `Gorgon`

#### Methods

##### `Point(—)`

**Returns:** `operator`

##### `UnitPoint(—)`

**Returns:** `operator`

##### `Size(—)`

**Returns:** `operator`

##### `UnitSize(—)`

**Returns:** `operator`


---

## Enums

### `Unit`

**Namespace:** `Gorgon`

Unit for dimensions. Dimensions in UI system does not allow floating point numbers as floating point numbers are not precise and may cause issues. Additionally, final values always rounded, so that the symbols are always on full pixels.


---

## Functions

### `Convert(const Point &p, const Geometry::Size &parent, int unitsize, int spacing, int emwidth = 10, int fractions = 6)`

**Returns:** `inline Geometry::Point`


This class stores the location information for a box object This class stores the size information for a box object This class stores the location information for a box object This class stores the size information for a box object This class stores the margin information for a box object Converts a dimension based point to pixel based point


### `Convert(const Size &s, const Geometry::Size &parent, int unitsize, int spacing, int emwidth = 10, int fractions = 6)`

**Returns:** `inline Geometry::Size`


Converts a dimension based size to pixel based size


### `Convert(const UnitPoint &p, const Geometry::Size &parent, int unitsize, int spacing, int emwidth = 10, int fractions = 6)`

**Returns:** `inline Geometry::Point`


Converts a dimension based point to pixel based point


### `Convert(const UnitSize &s, const Geometry::Size &parent, int unitsize, int spacing, int emwidth = 10, int fractions = 6)`

**Returns:** `inline Geometry::Size`


Converts a dimension based size to pixel based size


### `Convert(const Margin &m, const Geometry::Size &parent, int unitsize, int spacing, int emwidth = 10, int fractions = 6)`

**Returns:** `inline Geometry::Margin`


Converts a dimension based margin to pixel based margin


### `Pixels(int val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with pixel units


### `Percentage(int val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with percentage units


### `Percentage(double val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with percentage units


### `Percentage(float val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with percentage units


### `Fractions(int val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with fractions units


### `Units(int val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with unit size


### `Units(float val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with unit size


### `Units(double val)`

**Returns:** `inline constexpr Dimension`


Converts the given value to dimension with unit size


### `Pixels(int one, int two)`

**Returns:** `inline constexpr DualDimension`


Converts the given value to dimension with pixel units


### `Percent(int one, int two)`

**Returns:** `inline constexpr DualDimension`


Converts the given value to dimension with percentage units


### `Percent(double one, double two)`

**Returns:** `inline constexpr DualDimension`


Converts the given one, given twoue to dimension with percentage units


### `Percent(float one, float two)`

**Returns:** `inline constexpr DualDimension`


Converts the given one, given twoue to dimension with percentage units


### `Fractions(int one, int two)`

**Returns:** `inline constexpr DualDimension`


Converts the given value to dimension with percentage units


### `Units(int one, int two)`

**Returns:** `inline constexpr DualDimension`


Converts the given one, given twoue to dimension with unit size


### `Units(float one, float two)`

**Returns:** `inline constexpr DualDimension`


Converts the given one, given twoue to dimension with unit size


### `Units(double one, double two)`

**Returns:** `inline constexpr DualDimension`


Converts the given one, given twoue to dimension with unit size


### `Pixels(const Geometry::Point &val)`

**Returns:** `inline Point`


Converts the given value to dimension with pixel units


### `Percentage(const Geometry::Point &val)`

**Returns:** `inline Point`


Converts the given value to dimension with percentage units


### `Fractions(const Geometry::Point &val)`

**Returns:** `inline Point`


Converts the given value to dimension with percentage units


### `Units(const Geometry::Point &val)`

**Returns:** `inline Point`


Converts the given value to dimension with unit size


### `Pixels(const Geometry::Size &val)`

**Returns:** `inline Size`


Converts the given value to dimension with pixel units


### `Percentage(const Geometry::Size &val)`

**Returns:** `inline Size`


Converts the given value to dimension with percentage units


### `Fractions(const Geometry::Size &val)`

**Returns:** `inline Size`


Converts the given value to dimension with percentage units


### `Units(const Geometry::Size &val)`

**Returns:** `inline Size`


Converts the given value to dimension with unit size

