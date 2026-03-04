# Point

> Auto-generated documentation for the **Point** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_Point`

**Namespace:** `Geometry`

This class represents a 2D point. Points are serialized to string as (X, Y) form. However, unserialization, by default, accepts X, Y as well.

#### Methods

##### `basic_Point(—)`

**Returns:** ``

Base type of the point elements. Default constructor, does not zero initialize point.

##### `static` `FromVector(Float magnitute, Float angle, const basic_Point<O_> &origin={0, 0})`

**Returns:** `static basic_Point`

Filling constructor Conversion from a different point type Conversion from string Assignment from a different point type Converts this object to string. Creates a new point from the given vector data @param  magnitute is the magnitute of the vector @param  angle is the direction of the vector in radians @param  origin is the source origin to calculate new point

##### `static` `Parse(const std::string &str, bool require_parenthesis=false)`

**Returns:** `static basic_Point`

Properly parses given string into a point. Throws errors if the point is not well formed. Works only on types that can be parsed using strtod. Following error codes are reported by this parse function:  * *IllegalTokenError* **111001**: Illegal token while reading X coordinate * *IllegalTokenError* **111002**: Illegal token while looking for coordinate separator * *IllegalTokenError* **111003**: Illegal token while reading Y coordinate * *IllegalTokenError* **111004**: Illegal token(s) at the end * *IllegalTokenError* **111005**: Unmatched parenthesis * *ParseError* **110006**: Missing parenthesis, only if require_parenthesis is set to true * *ParseError* **110007**: Missing operand

##### `if(par==-1 && require_parenthesis)`

**Returns:** ``

##### `if(endptr==&*s)`

**Returns:** ``

##### `if(endptr==&*s)`

**Returns:** ``

##### `if(par!=-1)`

**Returns:** ``

##### `if(par>0)`

**Returns:** ``

##### `basic_Point(X-point.X, Y-point.Y)`

**Returns:** `return`

Subtracts another point from this one

##### `CrossProduct(const basic_Point<T_> &value)`

**Returns:** `T_`

Negates this point Adds another point to this one and returns the result Multiply this point with a scalar value. This is effectively scales the point Multiplies two points. This is essentially a dot product Divides this point to a scalar value. This is effectively scales the point Subtracts another point from this point. Result is assigned to this point Adds another point from this point. Result is assigned to this point Scales this point Scales this point Calculates cross product of two points

##### `DotProduct(const basic_Point<T_> &value)`

**Returns:** `T_`

Calculates dot product of two points

##### `Distance(const basic_Point &target)`

**Returns:** `Float`

Calculates Euclidean distance from this point to the given target

##### `EuclideanSquare(const basic_Point &target)`

**Returns:** `Float`

Calculates EuclideanSquare  distance from this point to the given target

##### `Distance(—)`

**Returns:** `Float`

Calculates Euclidean distance from this point to origin

##### `EuclideanSquare(—)`

**Returns:** `Float`

Calculates EuclideanSquare  distance from this point to the given target

##### `ManhattanDistance(const basic_Point &target)`

**Returns:** `T_`

Calculates Manhattan distance from this point to the given target

##### `ManhattanDistance(—)`

**Returns:** `T_`

Calculates Manhattan distance from this point to origin

##### `Normalize(—)`

**Returns:** `basic_Point`

Normalizes the point as a unit vector

##### `Perpendicular(—)`

**Returns:** `basic_Point`

Calculates perpendicular vector to this point

##### `Angle(const basic_Point &origin)`

**Returns:** `Float`

Calculates the angle of the line formed from the given point to this point. @param  origin is the starting point of the line @return angle in radians

##### `Angle(—)`

**Returns:** `Float`

Calculates the angle of the line formed from the origin to this point. @return angle in radians

##### `Slope(const basic_Point &point)`

**Returns:** `Float`

Calculates the slope of the line formed from the given point to this point. @param  point is the starting point of the line

##### `Slope(—)`

**Returns:** `Float`

Calculates the slope of the line formed from the origin to this point.

##### `Compare(const basic_Point &point)`

**Returns:** `bool`

Compares two points

##### `Compare(point)`

**Returns:** `return`

Compares two points

##### `Move(const T_ &x, const T_ &y)`

**Returns:** `void`

Compares two points Moves this point to the given coordinates


---

## Functions

### `if(par)`

**Returns:** ``


X coordinate Y coordinate Allows this point to be accessed as a vector Allows streaming of point. A point will be printed inside parenthesis with a comma separating X and Y values. Reads a point from a stream. Requires comma in between x and y. parentheses are optional. They wont even be matched to each other. A point entry should not contain space before closing parenthesis otherwise, parenthesis will not be extracted.


### `Translate(basic_Point<T_> &point, O_ x, O_ y)`

**Returns:** `void`


Translation moves the given point *by* the given amount


### `Translate(basic_Point<T_> &point, const basic_Point<T_> &other)`

**Returns:** `void`


Translation moves the given point *by* the given amount


### `Scale(basic_Point<T_> &point, const O_ &size)`

**Returns:** ``


Scales the given point by the given factor


### `Scale(basic_Point<T_> &point, const O_ &sizex, const O_ &sizey)`

**Returns:** ``


Scales the given point by the given factors for x and y coordinates.


### `Scale(basic_Point<T_> &point, const O_ &size, const basic_Point<T_> &origin)`

**Returns:** ``


Scales the given point by the given factor, considering given point as origin


### `Scale(basic_Point<T_> &point, const O_ &sizex, const O_ &sizey, const basic_Point<T_> &origin)`

**Returns:** ``


Scales the given point by the given factor, considering given point as origin.


### `Rotate(basic_Point<T_> &point, Float angle)`

**Returns:** `void`


Rotates the given point by the given angle. @param  point the point to rotate @param  angle is the Euler rotation angle in radians


### `Rotate(basic_Point<T_> &point, Float angle, const basic_Point<T_> &origin)`

**Returns:** `void`


Rotates the given point by the given angle around the given origin. @param  point the point to rotate @param  angle is the Euler rotation angle in radians @param  origin is the origin of rotation


### `SkewX(basic_Point<T_> &point, const O_ &rate)`

**Returns:** `void`


Skews the given point with the given rate along X axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewY(basic_Point<T_> &point, const O_ &rate)`

**Returns:** `void`


Skews the given point with the given rate along Y axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewX(basic_Point<T_> &point, const O_ &rate, const basic_Point<T_> &origin)`

**Returns:** `void`


Skews the given point with the given rate along X axis considering given point as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewY(basic_Point<T_> &point, const O_ &rate, const basic_Point<T_> &origin)`

**Returns:** `void`


Skews the given point with the given rate along Y axis considering given point as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `FlipX(basic_Point<T_> &point)`

**Returns:** `void`


Reflects the given point along the X axis


### `FlipY(basic_Point<T_> &point)`

**Returns:** `void`


Reflects the given point along the Y axis


### `HorizontalMirror(basic_Point<T_> &point)`

**Returns:** `void`


Reflects the given point horizontally


### `ReflectX(point)`

**Returns:** ``



### `VerticalMirror(basic_Point<T_> &point)`

**Returns:** `void`


Reflects the given point vertically


### `ReflectY(point)`

**Returns:** ``



### `ReflectX(basic_Point<T_> &point, const basic_Point<T_> &origin = {0, 0})`

**Returns:** `void`


Reflects the given point along the X axis considering given origin


### `ReflectY(basic_Point<T_> &point, const basic_Point<T_> &origin = {0, 0})`

**Returns:** `void`


Reflects the given point along the Y axis considering given origin


### `HorizontalMirror(basic_Point<T_> &point, const basic_Point<T_> &origin)`

**Returns:** `void`


Reflects the given point horizontally considering given origin


### `ReflectX(point, origin)`

**Returns:** ``



### `VerticalMirror(basic_Point<T_> &point, const basic_Point<T_> &origin)`

**Returns:** `void`


Reflects the given point vertically considering given origin


### `ReflectY(point, origin)`

**Returns:** ``



### `Round(Pointf num)`

**Returns:** `inline Pointf`


@see basic_Point @see basic_Point Performs a rounding operation over a floating point point

