# Margin

> Auto-generated documentation for the **Margin** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `basic_Margin`

**Namespace:** `Gorgon`

This class defines Margin of an object or an area. This class is designed to be used with Bounds object. Order of components are Left, Top, Right, Bottom. Negative margin values are allowed.

#### Methods

##### `basic_Margin(—)`

**Returns:** ``

Base type of the margin elements. Default constructor

##### `CombinePadding(const basic_Margin &other)`

**Returns:** `basic_Margin`

Sets all Margin to the given value. Intentionally left implicit as Margin can be represented as a simple integer Sets horizontal and vertical Margin separately Sets all Margin separately Converts this object to a string. TODO Combines two margins that are inside each other, basically taking the maximum margin from each side. Negative margins do not collapse

##### `CombineMargins(const basic_Margin &other)`

**Returns:** `basic_Margin`

Combines two margins that are next to each other, basically taking the maximum margin from each side with its opposite. Only one of the values should be used. Negative margins do not collapse

##### `TotalX(—)`

**Returns:** `T_`

Calculates and returns the total Margin in X axis

##### `TotalY(—)`

**Returns:** `T_`

Calculates and returns the total Margin in Y axis

##### `Horizontal(—)`

**Returns:** `T_`

Calculates and returns the total Margin in X axis

##### `Vertical(—)`

**Returns:** `T_`

Calculates and returns the total Margin in Y axis

##### `Total(—)`

**Returns:** `basic_Size<T_>`

Calculates and returns the total Margin in X axis

##### `basic_Margin(Left+right.Left, Top+right.Top, Right+right.Right, Bottom+right.Bottom)`

**Returns:** `return`

Adds two Margin

##### `basic_Margin(Left-right.Left, Top-right.Top, Right-right.Right, Bottom-right.Bottom)`

**Returns:** `return`

Subtracts two Margin

##### `AddToLeft(T_ width, basic_Margin Margin=0)`

**Returns:** `basic_Margin`

Adds a Margin to this one Subtracts a Margin from this one Compares two Margin Compares two Margin Adds an object to the left of this Margin to create a new Margin marking the used area. @param  width of the object @param  Margin to be applied to the object

##### `AddToTop(T_ height, const basic_Margin &Margin=0)`

**Returns:** `basic_Margin`

Adds an object to the top of this Margin to create a new Margin marking the used area. @param  height of the object @param  Margin to be applied to the object

##### `AddToRight(T_ width, basic_Margin Margin=0)`

**Returns:** `basic_Margin`

Adds an object to the right of this Margin to create a new Margin marking the used area. @param  width of the object @param  Margin to be applied to the object

##### `AddToBottom(T_ height, basic_Margin Margin=0)`

**Returns:** `basic_Margin`

Adds an object to the bottom of this Margin to create a new Margin marking the used area. @param  height of the object @param  Margin to be applied to the object

##### `TopLeft(—)`

**Returns:** `basic_Point<T_>`

Top left coordinate of the object that will be placed within a <0:inf, 0:inf> bounds that has this Margin.

