# Transform3D

&gt; Auto-generated documentation for the **Transform3D** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_Transform3D`

**Namespace:** `Gorgon`

#### Methods

##### `basic_Transform3D(—)`

**Returns:** ``

##### `LoadIdentity(—)`

**Returns:** ``

##### `basic_Transform3D(std::initializer_list<std::array<T_, 4>> init)`

**Returns:** ``

##### `for(auto r : init)`

**Returns:** ``

##### `for(int j=0; j<4; j++)`

**Returns:** ``

##### `LoadIdentity(—)`

**Returns:** `void`

##### `for(int i=0; i<4; i++)`

**Returns:** ``

##### `Get(int row, int col)`

**Returns:** `T_`

##### `Translate(const basic_Point3D<T_> &p)`

**Returns:** `void`

##### `Translate(T_ x, T_ y, T_ z = 0)`

**Returns:** `void`

##### `Scale(T_ x, T_ y, T_ z = 1)`

**Returns:** `void`

##### `Scale(T_ f)`

**Returns:** `void`

##### `Rotate(T_ x, T_ y, T_ z)`

**Returns:** `void`

##### `Rotate(const basic_Point3D<T_> &vec, T_ ang)`

**Returns:** `void`

Rotates around the given plane, vec should be a unit vector

##### `Transpose(—)`

**Returns:** `void`

This function transposes only 3x3 portion of the matrix


---

## Functions

### `for(int i=0; i<4; i++)`

**Returns:** ``



### `for(int j=0; j<4; j++)`

**Returns:** ``


