# PointProperty

> Auto-generated documentation for the **PointProperty** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_PointProperty`

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

##### `Move(const T_ &x, const T_ &y)`

**Returns:** `void`

Compares two points Moves this point to the given coordinates

##### `GetX(—)`

**Returns:** `typename T_::BaseType`

Returns X component

##### `SetX(const typename T_::BaseType &value)`

**Returns:** `void`

Sets X component

##### `GetY(—)`

**Returns:** `typename T_::BaseType`

Returns Y component

##### `SetY(const typename T_::BaseType &value)`

**Returns:** `void`

Sets Y component


---

## Functions

### `Translate(basic_PointProperty<C_, T_, Getter_, Setter_> &point, O_ x, O_ y)`

**Returns:** `void`


Translation moves the given point *by* the given amount


### `Translate(p, x, y)`

**Returns:** ``



### `Translate(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const T_ &other)`

**Returns:** `void`


Translation moves the given point *by* the given amount


### `Translate(p, other)`

**Returns:** ``



### `Scale(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O_ &size)`

**Returns:** `void`


Scales the given point by the given factor


### `Scale(p, size)`

**Returns:** ``



### `Scale(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O1_ &sizex, const O2_ &sizey)`

**Returns:** `void`


Scales the given point by the given factors for x and y coordinates.


### `Scale(p, sizex, sizey)`

**Returns:** ``



### `Scale(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O_ &size, const basic_Point<T_> &origin)`

**Returns:** `void`


Scales the given point by the given factor, considering given point as origin


### `Scale(p, size, origin)`

**Returns:** ``



### `Scale(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O1_ &sizex, const O2_ &sizey, const T_ &origin)`

**Returns:** `void`


Scales the given point by the given factor, considering given point as origin.


### `Scale(p, sizex, sizey, origin)`

**Returns:** ``



### `Rotate(basic_PointProperty<C_, T_, Getter_, Setter_> &point, Float angle)`

**Returns:** `void`


Rotates the given point by the given angle. @param  point the point to rotate @param  angle is the Euler rotation angle in radians


### `Rotate(p, angle)`

**Returns:** ``



### `Rotate(basic_PointProperty<C_, T_, Getter_, Setter_> &point, Float angle, const T_ &origin)`

**Returns:** `void`


Rotates the given point by the given angle around the given origin. @param  point the point to rotate @param  angle is the Euler rotation angle in radians @param  origin is the origin of rotation


### `Rotate(p, angle, origin)`

**Returns:** ``



### `SkewX(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O_ &rate)`

**Returns:** `void`


Skews the given point with the given rate along X axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewX(p, rate)`

**Returns:** ``



### `SkewY(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O_ &rate)`

**Returns:** `void`


Skews the given point with the given rate along Y axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewY(p, rate)`

**Returns:** ``



### `SkewX(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O_ &rate, const T_ &origin)`

**Returns:** `void`


Skews the given point with the given rate along X axis considering given point as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewY(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const O_ &rate, const basic_Point<T_> &origin)`

**Returns:** `void`


Skews the given point with the given rate along Y axis considering given point as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `ReflectX(basic_PointProperty<C_, T_, Getter_, Setter_> &point)`

**Returns:** `void`


Reflects the given point along the X axis


### `ReflectY(basic_PointProperty<C_, T_, Getter_, Setter_> &point)`

**Returns:** `void`


Reflects the given point along the Y axis


### `HorizontalMirror(basic_PointProperty<C_, T_, Getter_, Setter_> &point)`

**Returns:** `void`


Reflects the given point horizontally


### `ReflectX(point)`

**Returns:** ``



### `VerticalMirror(basic_Point<T_> &point)`

**Returns:** `void`


Reflects the given point vertically


### `ReflectY(point)`

**Returns:** ``



### `ReflectX(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const basic_Point<T_> &origin)`

**Returns:** `void`


Reflects the given point along the X axis considering given origin


### `ReflectY(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const basic_Point<T_> &origin)`

**Returns:** `void`


Reflects the given point along the Y axis considering given origin


### `HorizontalMirror(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const basic_Point<T_> &origin)`

**Returns:** `void`


Reflects the given point horizontally considering given origin


### `ReflectX(point, origin)`

**Returns:** ``



### `VerticalMirror(basic_PointProperty<C_, T_, Getter_, Setter_> &point, const basic_Point<T_> &origin)`

**Returns:** `void`


Reflects the given point vertically considering given origin


### `ReflectY(point, origin)`

**Returns:** ``


