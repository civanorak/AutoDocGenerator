# PointList

> Auto-generated documentation for the **PointList** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `PointList`

**Namespace:** `Gorgon`

#### Methods

##### `PointList(PointList &&other)`

**Returns:** ``

Empty constructor Implicit vector to PointList casting. You may move in the data using std::move Initializer list Due to relatively high cost, copying is disabled. Use Duplicate instead Move constructor

##### `Swap(other)`

**Returns:** ``

##### `Duplicate(—)`

**Returns:** `PointList`

Duplicates this PointList

##### `Swap(right)`

**Returns:** ``

Due to relatively high cost, copying is disabled. Use Duplicate instead Move assignment

##### `Destroy(—)`

**Returns:** `void`

Destroys the storage used by this list

##### `swap(n, Points)`

**Returns:** ``

##### `Clear(—)`

**Returns:** `void`

Clears the elements in this list

##### `GetSize(—)`

**Returns:** `auto`

Returns the number of elements in the list

##### `GetCount(—)`

**Returns:** `auto`

Returns the number of elements in the list

##### `IsEmpty(—)`

**Returns:** `bool`

Returns if the container is empty

##### `begin(—)`

**Returns:** `auto`

Begin iterator to underlying points vector

##### `end(—)`

**Returns:** `auto`

End iterator to underlying points vector

##### `begin(—)`

**Returns:** `auto`

Begin iterator to underlying points vector

##### `end(—)`

**Returns:** `auto`

End iterator to underlying points vector

##### `rbegin(—)`

**Returns:** `auto`

Begin iterator to underlying points vector

##### `rend(—)`

**Returns:** `auto`

End iterator to underlying points vector

##### `rbegin(—)`

**Returns:** `auto`

Begin iterator to underlying points vector

##### `rend(—)`

**Returns:** `auto`

End iterator to underlying points vector

##### `GetLine(long index)`

**Returns:** `Line<P_>`

Accesses the elements in the list Accesses the elements in the list Accesses the first element in the list Accesses the last element in the list Accesses the first element in the list Accesses the last element in the list Returns the element at the given index. This function treats the list as cyclic. Returns the element at the given index. This function treats the list as cyclic. Returns the line at the given index. This function treats the list as a cyclic line list. The list is assumed to be closed.

##### `Push(P_ point)`

**Returns:** `void`

Adds a new point to the end of the point list

##### `Push(T_&&... params)`

**Returns:** `void`

Adds a new point to the end of the point list

##### `Insert(long index, P_ point)`

**Returns:** `void`

Adds a new point to the end of the point list

##### `Insert(long index, T_&&... params)`

**Returns:** `void`

Adds a new point to the end of the point list

##### `Pop(—)`

**Returns:** `void`

Removes the last point from the list

##### `Erase(long index)`

**Returns:** `void`

Erase the specific index from the list

##### `for(const auto &p : *this)`

**Returns:** ``

Adds the coordinates of the points on the right list to the left. Right list is treated as cyclic. If right list is empty, nothing is done.

##### `for(auto &p : *this)`

**Returns:** ``

Adds the coordinates of the points on the right list to the left. Right list is treated as cyclic. If right list is empty, nothing is done.

##### `for(const auto &p : *this)`

**Returns:** ``

Subtracts the coordinates of the points on the right list to the left. Right list is treated as cyclic. If right list is empty, nothing is done.

##### `for(auto &p : *this)`

**Returns:** ``

Subtracts the coordinates of the points on the right list to the left. Right list is treated as cyclic. If right list is empty, nothing is done.

##### `for(const auto &p : *this)`

**Returns:** ``

Adds a point to each element of the list.

##### `for(auto &p : *this)`

**Returns:** ``

Adds a point to each element of the list.

##### `for(const auto &p : *this)`

**Returns:** ``

Subtracts a point to each element of the list.

##### `for(auto &p : *this)`

**Returns:** ``

Subtracts a point to each element of the list.

##### `for(const auto &p : *this)`

**Returns:** ``

Adds a point to each element of the list.

##### `for(auto &p : *this)`

**Returns:** ``

Adds a point to each element of the list.

##### `for(const auto &p : *this)`

**Returns:** ``

Subtracts a point to each element of the list.

##### `for(auto &p : *this)`

**Returns:** ``

Subtracts a point to each element of the list.

##### `Swap(PointList<P_> &right)`

**Returns:** `void`

Swaps two lists, mainly for move operations.

##### `swap(this->Points, right.Points)`

**Returns:** ``


---

## Functions

### `swap(PointList<P_> &left, PointList<P_> &right)`

**Returns:** `void`


Stored points. You may directly use this class as if it is a point vector. Comparison: this operation is expensive: O(n). Comparison: this operation is expensive: O(n). Comparison: this operation is expensive: O(n). Comparison: this operation is expensive: O(n). Comparison: this operation is expensive: O(n). Comparison: this operation is expensive: O(n).


### `Translate(PointList<P_> &pointlist, O_ x, O_ y)`

**Returns:** `void`


Translation moves the given point *by* the given amount


### `Translate(p, x, y)`

**Returns:** ``



### `Translate(PointList<P_> &pointlist, const P_ &other)`

**Returns:** `void`


Translation moves the given pointlist *by* the given amount


### `Translate(p, other)`

**Returns:** ``



### `Scale(PointList<P_> &pointlist, const O_ &size)`

**Returns:** `void`


Scales the given pointlist by the given factor


### `Scale(p, size)`

**Returns:** ``



### `Scale(PointList<P_> &pointlist, const O_ &sizex, const O_ &sizey)`

**Returns:** `void`


Scales the given pointlist by the given factors for x and y coordinates.


### `Scale(p, sizex, sizey)`

**Returns:** ``



### `Scale(PointList<P_> &pointlist, const O_ &size, const PointList<P_> &origin)`

**Returns:** `void`


Scales the given pointlist by the given factor, considering given pointlist as origin


### `Scale(p, size, origin)`

**Returns:** ``



### `Scale(PointList<P_> &pointlist, const O_ &sizex, const O_ &sizey, const PointList<P_> &origin)`

**Returns:** `void`


Scales the given pointlist by the given factor, considering given pointlist as origin.


### `Scale(p, sizex, sizey, origin)`

**Returns:** ``



### `Rotate(PointList<P_> &pointlist, Float angle)`

**Returns:** `void`


Rotates the given pointlist by the given angle. @param  pointlist the pointlist to rotate @param  angle is the Euler rotation angle in radians


### `Rotate(p, angle)`

**Returns:** ``



### `Rotate(PointList<P_> &pointlist, Float angle, const P_ &origin)`

**Returns:** `void`


Rotates the given pointlist by the given angle around the given origin. @param  pointlist the pointlist to rotate @param  angle is the Euler rotation angle in radians @param  origin is the origin of rotation


### `Rotate(p, angle, origin)`

**Returns:** ``



### `SkewX(PointList<P_> &pointlist, const O_ &rate)`

**Returns:** `void`


Skews the given pointlist with the given rate along X axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewX(p, rate)`

**Returns:** ``



### `SkewY(PointList<P_> &pointlist, const O_ &rate)`

**Returns:** `void`


Skews the given pointlist with the given rate along Y axis. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewY(p, rate)`

**Returns:** ``



### `SkewX(PointList<P_> &pointlist, const O_ &rate, const PointList<P_> &origin)`

**Returns:** `void`


Skews the given pointlist with the given rate along X axis considering given pointlist as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewX(p, rate, origin)`

**Returns:** ``



### `SkewY(PointList<P_> &pointlist, const O_ &rate, const PointList<P_> &origin)`

**Returns:** `void`


Skews the given pointlist with the given rate along Y axis considering given pointlist as the origin. Skew operation transforms objects in a way that it converts a rectangle to a parallelogram.


### `SkewY(p, rate, origin)`

**Returns:** ``



### `ReflectX(PointList<P_> &pointlist)`

**Returns:** `void`


Reflects the given pointlist along the X axis


### `ReflectX(p)`

**Returns:** ``



### `ReflectY(PointList<P_> &pointlist)`

**Returns:** `void`


Reflects the given pointlist along the Y axis


### `ReflectY(p)`

**Returns:** ``



### `HorizontalMirror(PointList<P_> &pointlist)`

**Returns:** `void`


Reflects the given pointlist horizontally


### `ReflectX(pointlist)`

**Returns:** ``



### `VerticalMirror(PointList<P_> &pointlist)`

**Returns:** `void`


Reflects the given pointlist vertically


### `ReflectY(pointlist)`

**Returns:** ``



### `ReflectX(PointList<P_> &pointlist, const PointList<P_> &origin)`

**Returns:** `void`


Reflects the given pointlist along the X axis considering given origin


### `ReflectX(p, origin)`

**Returns:** ``



### `ReflectY(PointList<P_> &pointlist, const PointList<P_> &origin)`

**Returns:** `void`


Reflects the given pointlist along the Y axis considering given origin


### `ReflectY(p, origin)`

**Returns:** ``



### `HorizontalMirror(PointList<P_> &pointlist, const PointList<P_> &origin)`

**Returns:** `void`


Reflects the given pointlist horizontally considering given origin


### `ReflectX(pointlist, origin)`

**Returns:** ``



### `VerticalMirror(PointList<P_> &pointlist, const PointList<P_> &origin)`

**Returns:** `void`


Reflects the given pointlist vertically considering given origin


### `ReflectY(pointlist, origin)`

**Returns:** ``


