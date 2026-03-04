# SizeProperty

> Auto-generated documentation for the **SizeProperty** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_SizeProperty`

**Namespace:** `Gorgon`

#### Methods

##### `T_(—)`

**Returns:** `operator`

##### `T_(—)`

**Returns:** `operator const`

##### `CrossProduct(const T_ &value)`

**Returns:** `T_`

Negates this point Adds another point to this one and returns the result Multiply this point with a scalar value. This is effectively scales the point Multiplies two points. This is essentially a dot product Divides this point to a scalar value. This is effectively scales the point Subtracts another point from this point. Result is assigned to this point Adds another point from this point. Result is assigned to this point Scales this point Scales this point Calculates cross product of two points

##### `DotProduct(const T_ &value)`

**Returns:** `T_`

Calculates dot product of two points

##### `Distance(const T_ &target)`

**Returns:** `Float`

Calculates Euclidean distance from this point to the given target

##### `EuclideanSquare(const T_ &target)`

**Returns:** `Float`

Calculates EuclideanSquare  distance from this point to the given target

##### `Distance(—)`

**Returns:** `Float`

Calculates Euclidean distance from this point to origin

##### `EuclideanSquare(—)`

**Returns:** `Float`

Calculates EuclideanSquare  distance from this point to the given target

##### `ManhattanDistance(const T_ &target)`

**Returns:** `Float`

Calculates Manhattan distance from this point to the given target

##### `ManhattanDistance(—)`

**Returns:** `Float`

Calculates Manhattan distance from this point to origin

##### `Normalize(—)`

**Returns:** `T_`

Normalizes the point as a unit vector

##### `Perpendicular(—)`

**Returns:** `T_`

Calculates perpendicular vector to this point

##### `Angle(const T_ &origin)`

**Returns:** `Float`

Calculates the angle of the line formed from the given point to this point. @param  origin is the starting point of the line @return angle in radians

##### `Angle(—)`

**Returns:** `Float`

Calculates the angle of the line formed from the origin to this point. @return angle in radians

##### `Slope(const T_ &point)`

**Returns:** `Float`

Calculates the slope of the line formed from the given point to this point. @param  point is the starting point of the line

##### `Slope(—)`

**Returns:** `Float`

Calculates the slope of the line formed from the origin to this point.

##### `Compare(const T_ &point)`

**Returns:** `bool`

Compares two points

##### `Compare(point)`

**Returns:** `return`

Compares two points

##### `GetWidth(—)`

**Returns:** `typename T_::BaseType`

Compares two points Returns Width component

##### `SetWidth(const typename T_::BaseType &value)`

**Returns:** `void`

Sets Width component

##### `GetHeight(—)`

**Returns:** `typename T_::BaseType`

Returns Height component

##### `SetHeight(const typename T_::BaseType &value)`

**Returns:** `void`

Sets Height component


---

## Functions

### `Scale(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const basic_Size<O_> &size)`

**Returns:** `void`


Scales the given point by the given factor


### `Scale(p, size)`

**Returns:** ``



### `Scale(basic_SizeProperty<C_, T_, Getter_, Setter_> &l, const O_ &size)`

**Returns:** `void`


Scales the given size by the given factor


### `Scale(s, size)`

**Returns:** ``



### `Scale(basic_SizeProperty<C_, T_, Getter_, Setter_> &l, const O1_ &sizex, const O2_ &sizey)`

**Returns:** `void`


Scales the given size by the given factors for x and y coordinates.


### `Scale(s, sizex, sizey)`

**Returns:** ``



### `Scale(basic_SizeProperty<C_, T_, Getter_, Setter_> &l, const basic_Size<O_> &size)`

**Returns:** `void`


Scales the given l by the given factor


### `Scale(s, size)`

**Returns:** ``


