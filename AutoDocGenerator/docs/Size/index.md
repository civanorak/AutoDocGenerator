# Size

> Auto-generated documentation for the **Size** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_Size`

**Namespace:** `Gorgon`

This class represents a 2D geometric size. Although negative size is meaningless, this class allows all operations over negative sizes.

#### Methods

##### `basic_Size(—)`

**Returns:** ``

Base type of the size elements. Default constructor. This constructor does **not** zero initialize the object.

##### `basic_Size(const std::string &str)`

**Returns:** `explicit`

Filling constructor. This variant assigns the given value to both dimensions, effectively creating a square. Filling constructor Converting constructor. Converts a different typed size object to this type. Converts a point to size object. The size a point represents is the size of the rectangle that starts from origin to the given point. Conversion from string

##### `static` `Parse(const std::string &str)`

**Returns:** `static basic_Size`

Converts this object to string. Properly parses given string into a size. Throws errors if the size is not well formed. Works only on types that can be parsed using strtod. Following error codes are reported by this parse function:  * *IllegalTokenError* **121001**: Illegal token while reading Width * *IllegalTokenError* **121002**: Illegal token while looking for width/height separator * *IllegalTokenError* **121003**: Illegal token while reading Height * *IllegalTokenError* **121004**: Illegal token(s) at the end

##### `if(endptr==&*s)`

**Returns:** ``

##### `if(*s!='x')`

**Returns:** ``

##### `if(endptr==&*s)`

**Returns:** ``

##### `basic_Size(size.Width+Width, size.Height+Height)`

**Returns:** `return`

Converting assignment operator. Converting assignment operator. The size a point represents is the size of the rectangle that starts from origin to the given point. Compares two size objects Compares two size objects Adds two size objects

##### `basic_Size(Width-size.Width, Height-size.Height)`

**Returns:** `return`

Subtracts two size objects

##### `Cells(—)`

**Returns:** `T_`

Negation operator Adds the given size object to this size Subtracts the given size object from this size Multiplies this size object with the given factor Divides this size object to the given factor Converts this size object to a point. Conversion is performed in a manner that the resultant point is the far corner of a rectangle that is placed at origin and the size of this object. Returns the number of fully encompassed cells. For instance, a 3.2x2.2 size object has 6 cells.

##### `Area(—)`

**Returns:** `T_`

Returns the exact area of the rectangle has the size of this object

##### `IsValid(—)`

**Returns:** `bool`

Returns whether the size is valid, i.e. both dimensions are positive.

##### `static` `Max(—)`

**Returns:** `static basic_Size`

Returns the maximum representable size. This function requires T_ to be standard arithmetic type


---

## Functions

### `Scale(basic_Point<T_> &point, const basic_Size<O_> &size)`

**Returns:** `void`


Width of this size object Height of this size object Multiplies a size with a scalar, effectively resizing it. Multiplies a size with a scalar, effectively resizing it. Multiplies a size with a scalar, effectively resizing it. Divides a size with a scalar, effectively resizing it. Divides a size with a scalar, effectively resizing it. Multiplies a size with a scalar, effectively resizing it. Writes the given size object to the stream. Width and Height components of size objects are separated by an x Reads a size object from a stream. Width and Height components should be separated by an x. Allows multiplication of point with a size object Allows division of point with a size object Scales the given point by the given factor


### `Scale(basic_Size<T_> &l, const O_ &size)`

**Returns:** `void`


Scales the given size by the given factor


### `Scale(basic_Size<T_> &l, const O1_ &sizex, const O2_ &sizey)`

**Returns:** `void`


Scales the given size by the given factors for x and y coordinates.


### `Scale(basic_Size<T_> &l, const basic_Size<O_> &size)`

**Returns:** `void`


Scales the given l by the given factor


### `Union(const basic_Size<T_> &l, const basic_Size<T_> &r)`

**Returns:** `basic_Size<T_>`


Returns the maximum size that can fit into both size objects


### `Combine(const basic_Size<T_> &l, const basic_Size<T_> &r)`

**Returns:** `basic_Size<T_>`


Returns the minimum required size that can hold both size objects

