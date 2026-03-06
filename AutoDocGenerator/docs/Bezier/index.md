# Bezier

&gt; Auto-generated documentation for the **Bezier** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_Bezier`

**Namespace:** `Gorgon`

#### Methods

##### `Split(Float t)`

**Returns:** `std::pair<basic_Bezier, basic_Bezier>`

Default constructor does not initialize points Filling constructor Splits the curve into two from the given point

##### `Split(—)`

**Returns:** `std::pair<basic_Bezier, basic_Bezier>`

Splits the curve from the middle

##### `FlattenInverted(points, tolerance)`

**Returns:** ``

Returns the point on the curve at time t This function turns this curve to a flat point list. Tolerance is the maximum distance that the curve will deviate from the straight line. In reality, this deviation will be significantly less than this value.

##### `ASSERT(tolerance > 0, "Tolerance cannot be 0 or less")`

**Returns:** ``

This function turns this curve to a flat point list. Tolerance is the maximum distance that the curve will deviate from the straight line. In reality, this deviation will be significantly less than this value. This function mainly used internally to create joined segments

##### `l(seg.P0, seg.P3)`

**Returns:** `Geometry::Line<Point_>`

##### `if(d < tolerance)`

**Returns:** ``


### `basic_Curves`

**Namespace:** `Gorgon`

First point on the curve First control point Second control point Last point on the curve

#### Methods

##### `SetStartingPoint(const Point_ &pnt)`

**Returns:** `void`

Sets the starting point of the curves. This structure will still have no curves after this function. If starting point is already set, it will be replaced.

##### `Get(long ind)`

**Returns:** `basic_Bezier<Point_>`

Returns the bezier curve at the given index.

##### `Get(ind)`

**Returns:** `return`

Returns the bezier curve at the given index.

##### `GetSize(—)`

**Returns:** `long`

Returns the number of curves in this container

##### `GetCount(—)`

**Returns:** `auto`

Returns the number of curves in this container

##### `GetSize(—)`

**Returns:** `return`

##### `IsEmpty(—)`

**Returns:** `bool`

Returns if the container is empty

##### `Clear(—)`

**Returns:** `void`

Clears all points including the starting point.

##### `Push(const basic_Bezier<Point_> &bezier)`

**Returns:** `void`

Adds a bezier curve to this container. If the container is empty, P0 will be used as starting point. Otherwise, P0 will be ignored.

##### `Push(const Point_ &c1, const Point_ &c2, const Point_ &end)`

**Returns:** `void`

Adds a bezier curve to this container using given control points and end point. If the container is empty, (0, 0) will be used as starting point.

##### `Push(const Point_ &c, const Point_ &end)`

**Returns:** `void`

Adds a quadratic bezier curve to this container using given control point and end point. This curve will be converted to cubic bezier curve to be stored in this container. If the container is empty, (0, 0) will be used as starting point.

##### `Push(const Point_ &end)`

**Returns:** `void`

Adds a straight line to this container using given end point. This line will be converted to cubic bezier curve to be stored in this container. If the container is empty, (0, 0) will be used as starting point.

##### `for(long i=N-1; i>=0; i--)`

**Returns:** ``


---

## Functions

### `Translate(basic_Bezier<T_> &bezier, const Geometry::basic_Point<P_> &offset)`

**Returns:** `void`


Translates a given bezier curve


### `Translate(basic_Bezier<T_> &bezier, P_ x, P_ y)`

**Returns:** `void`


Translates a given bezier curve


### `Scale(basic_Bezier<T_> &bezier, S_ scale)`

**Returns:** `void`


Scales a given bezier curve


### `Scale(basic_Bezier<T_> &bezier, const Geometry::basic_Size<S_> &scale)`

**Returns:** `void`


Scales a given bezier curve


### `Scale(basic_Bezier<T_> &bezier, S_ w, S_ h)`

**Returns:** `void`


Scales a given bezier curve

