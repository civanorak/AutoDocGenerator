# Bounds

&gt; Auto-generated documentation for the **Bounds** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_Bounds`

**Namespace:** `Gorgon`

This class represents boundaries of 2D objects. A bounds object contains the starting boundary but not the ending boundary. Therefore, a bounds that has a Width() of 100 and Left of 0, has Right value as 100, not 99.  A Bounds object that has Left&lt;Right and Top&lt;Bottom is called normalized. Bounds should be normalized for its methods to work properly. Constructors normalizes input values, most methods leave bounds in normal state.

#### Methods

##### `basic_Bounds(—)`

**Returns:** ``

Base type of the bounds elements. Default constructor, does **not** zero initialize object

##### `Normalize(—)`

**Returns:** ``

Constructor that allows coordinates to be specified individually. Performs normalization therefore, left could be larger than right or top could be larger than bottom.

##### `Normalize(—)`

**Returns:** ``

Constructs minimum bounds that includes the given points

##### `Normalize(—)`

**Returns:** ``

Constructs bounds from the given coordinates and size

##### `Normalize(—)`

**Returns:** ``

Constructs bounds from the given coordinates and size

##### `Normalize(—)`

**Returns:** ``

Constructs bounds from the given coordinates and size

##### `basic_Bounds(const std::string &str)`

**Returns:** `explicit`

Conversion constructor that creates bounds from another type

##### `if(dash)`

**Returns:** ``

##### `Normalize(—)`

**Returns:** `void`

Compares two bounds objects Compares two bounds objects Normalizes bounds object so that Left and Right and Top and Bottom are ordered properly.

##### `TopLeft(—)`

**Returns:** `basic_Point<T_>`

Returns top left corner

##### `TopRight(—)`

**Returns:** `basic_Point<T_>`

Returns top right corner

##### `Center(—)`

**Returns:** `basic_Point<T_>`

Returns center of bounds

##### `BottomLeft(—)`

**Returns:** `basic_Point<T_>`

Returns bottom left corner

##### `BottomRight(—)`

**Returns:** `basic_Point<T_>`

Returns bottom right corner

##### `Width(—)`

**Returns:** `T_`

Calculates and returns the width of the bounds

##### `Height(—)`

**Returns:** `T_`

Calculates and returns the height of the bounds

##### `GetSize(—)`

**Returns:** `basic_Size<T_>`

Returns the size of the bounds object

##### `Resize(const basic_Size<T_> &size)`

**Returns:** `void`

##### `if(Left>Right || Top>Bottom)`

**Returns:** ``

Performs union operation. Returns a bounds that contains this bounds object as well as the given bounds Performs intersect operation. Returns a bounds that contains the region that this bounds and the given bounds covers. If they do not interact, an empty bounds &lt;0-0, 0-0&gt; is returned.

##### `SetWidth(const T_ &width)`

**Returns:** `void`

Performs union operation. Returns a bounds that contains this bounds object as well as the given bounds Performs intersect operation. Returns a bounds that contains the region that this bounds and the given bounds covers. If they do not interact, an empty bounds &lt;0-0, 0-0&gt; is returned. Changes the width of the bounds, anchor is the topleft

##### `SetHeight(const T_ &height)`

**Returns:** `void`

Changes the height of the bounds, anchor is the topleft

##### `Move(const basic_Point<T_> &p)`

**Returns:** `void`

Changes the position of the bounds

##### `Move(const T_ &x, const T_ &y)`

**Returns:** `void`

Changes the position of the bounds


---

## Functions

### `if(dash)`

**Returns:** ``


Creates a new bounds object that is the offset of this bounds by the given point Creates a new bounds object that is the offset of this bounds by the given point Creates a new bounds object that is larger by given size Creates a new bounds object that is smaller by given size the given point Creates a new bounds object that is the scaled version of this bounds by the given size. Origin of the operation is {0, 0} Creates a new bounds object that is the scale version of this bounds by the given size. Origin of the operation is {0, 0} Creates a new bounds object that is the scale version of this bounds by the given size. Origin of the operation is {0, 0} Creates a new bounds object that is the scale version of this bounds by the given size. Origin of the operation is {0, 0} Offsets this bounds objects by the given coordinates Offsets this bounds objects by the given coordinates Make this bounds larger by the given size Make this bounds smaller by the given size Resizes this bounds objects by the given size. Origin of the operation is {0, 0} Resizes this bounds objects by the given size. Origin of the operation is {0, 0} Resizes this bounds objects by the given size. Origin of the operation is {0, 0} Resizes this bounds objects by the given size. Origin of the operation is {0, 0} Left-most boundary Top-most boundary Right-most boundary Bottom-most boundary Allows streaming of bounds. in string representation, bounds is shown as [(l, t) - (r, b)] Stream extractor for bounds


### `if(par)`

**Returns:** ``



### `Intersect(const basic_Bounds<T_> &l, const basic_Bounds<T_> &r)`

**Returns:** `basic_Bounds<T_>`


Creates a new bounds that contains only the intersection of two bounds. If they do not intersect, a bounds of [0-0, 0-0] is returned. It is possible to use this function without referring to Geometry namespace.


### `if(b.Left>b.Right || b.Top>b.Bottom)`

**Returns:** ``



### `Union(const basic_Bounds<T_> &l, const basic_Bounds<T_> &r)`

**Returns:** `basic_Bounds<T_>`


Returns the smallest bounds that contains given bounds. It is possible to use this function without referring to Geometry namespace.


### `IsColliding(const basic_Bounds<T_> &l, const basic_Bounds<T_> &r)`

**Returns:** `bool`


Checks whether two bounds are colliding. It is possible to use this function without referring to Geometry namespace.


### `IsInside(const basic_Bounds<T_> &b, const basic_Point<T_> &p)`

**Returns:** `bool`


Checks whether the given point is inside this bounds.


### `Contains(const basic_Bounds<T_> &outer, const basic_Bounds<T_> &inner)`

**Returns:** `bool`


Checks whether the outer bounds contain inner bounds.


### `Translate(basic_Bounds<T_> &bounds, O_ x, O_ y)`

**Returns:** `void`


Translation moves the given bounds *by* the given amount


### `Translate(basic_Bounds<T_> &bounds, const basic_Point<T_> &other)`

**Returns:** `void`


Translation moves the given bounds *by* the given amount


### `Scale(basic_Bounds<T_> &bounds, const O_ &size)`

**Returns:** `void`


Scales the given bounds by the given factor. Center of the bounds is used as origin


### `Scale(basic_Bounds<T_> &bounds, const O_ &sizex, const O_ &sizey)`

**Returns:** `void`


Scales the given bounds by the given factors for x and y coordinates. Center of the bounds is used as origin


### `Scale(basic_Bounds<T_> &bounds, const basic_Size<O_> &size)`

**Returns:** `void`


Scales the given bounds by the given factors for x and y coordinates. Center of the bounds is used as origin


### `Scale(basic_Bounds<T_> &bounds, const O_ &size, const basic_Point<T_> &origin)`

**Returns:** `void`


Scales the given bounds by the given factor, considering specified point as origin


### `Scale(basic_Bounds<T_> &bounds, const O_ &sizex, const O_ &sizey, const basic_Point<T_> &origin)`

**Returns:** `void`


Scales the given bounds by the given factor, considering specified point as origin. This method variant is mostly there to allow scaling by Size.


### `Scale(basic_Bounds<T_> &bounds, const basic_Size<O_> &size, const basic_Point<T_> &origin)`

**Returns:** `void`


Scales the given bounds by the given factor, considering specified point as origin.


### `Rotate(basic_Bounds<T_> &bounds, Float angle)`

**Returns:** `void`


Rotates the given bounds by the given angle. Rotation is performed as if given bounds is a rectangle and the result is the bounds of this rotated rectangle. Center of the bounds is used as origin. @param  bounds object to be rotated @param  angle is the Euler rotation angle in radians


### `Rotate(tl, angle, cn)`

**Returns:** ``



### `Rotate(tr, angle, cn)`

**Returns:** ``



### `Rotate(bl, angle, cn)`

**Returns:** ``



### `Rotate(br, angle, cn)`

**Returns:** ``



### `Rotate(basic_Bounds<T_> &bounds, Float angle, const basic_Point<T_> &origin)`

**Returns:** `void`


Rotates the given bounds by the given angle around the given origin. @param  bounds object to be rotated @param  angle is the Euler rotation angle in radians @param  origin of the rotation


### `Rotate(tl, angle, origin)`

**Returns:** ``



### `Rotate(tr, angle, origin)`

**Returns:** ``



### `Rotate(bl, angle, origin)`

**Returns:** ``



### `Rotate(br, angle, origin)`

**Returns:** ``



### `SkewX(basic_Bounds<T_> &bounds, const O_ &rate)`

**Returns:** `void`


Skews the given bounds with the given rate along X axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram. Require normalized bounds.


### `if(rate>0)`

**Returns:** ``



### `SkewY(basic_Bounds<T_> &bounds, const O_ &rate)`

**Returns:** `void`


Skews the given bounds with the given rate along Y axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `if(rate>0)`

**Returns:** ``



### `SkewX(basic_Bounds<T_> &bounds, const O_ &rate, const basic_Point<T_> &origin)`

**Returns:** `void`


Skews the given bounds with the given rate along X axis considering given bounds as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `if(rate>0)`

**Returns:** ``



### `SkewY(basic_Bounds<T_> &bounds, const O_ &rate, const basic_Point<T_> &origin)`

**Returns:** `void`


Skews the given bounds with the given rate along Y axis considering given bounds as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `if(rate>0)`

**Returns:** ``



### `MirrorX(basic_Bounds<T_> &bounds)`

**Returns:** `void`


Reflects the bounds along X axis


### `MirrorY(basic_Bounds<T_> &bounds)`

**Returns:** `void`


Reflects the bounds along Y axis


### `FlipX(basic_Bounds<T_> &bounds)`

**Returns:** `void`


Flips the bounds along Y axis


### `FlipY(basic_Bounds<T_> &bounds)`

**Returns:** `void`


Flips the bounds along X axis

