# DataItems

&gt; Auto-generated documentation for the **DataItems** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `DataItem`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `GetGID(—)`

**Returns:** `virtual GID::Type`

Returns the Gorgon ID of this data object

##### `virtual` `Save(Writer &writer)`

**Returns:** `virtual void`

The name of the data item Saves the data item with header information to gorgon file

##### `SaveValue(writer)`

**Returns:** ``

##### `Get(—)`

**Returns:** `T_`

Returns the contents of this data item to the requested type; use GetObject in order to get resource objects

##### `static_assert(std::is_same<T_, int>::value, "Unknown data type.")`

**Returns:** ``

##### `virtual` `ToString(—)`

**Returns:** `virtual std::string`

Converts the contents of this data to string

##### `virtual` `SaveValue(Writer &writer)`

**Returns:** `virtual void`

Saves only the value of the data item to gorgon file. issizewritten controls whether the size of the object should be written for some data types (like blob and string)

##### `static` `InitializeLoaders(—)`

**Returns:** `static void`

This function will initialize data loaders


### `DataImp`

**Namespace:** `internal`

#### Methods

##### `Get(—)`

**Returns:** `T_`

##### `Set(T_ val)`

**Returns:** `void`


### `IntegerData`

**Namespace:** `internal`

#### Methods

##### `IntegerData(—)`

**Returns:** ``


### `FloatData`

**Namespace:** `internal`

#### Methods

##### `FloatData(—)`

**Returns:** ``


### `TextData`

**Namespace:** `internal`

#### Methods

##### `TextData(—)`

**Returns:** ``


### `PointData`

**Namespace:** `internal`

#### Methods

##### `PointData(—)`

**Returns:** ``


### `PointfData`

**Namespace:** `internal`

#### Methods

##### `PointfData(—)`

**Returns:** ``


### `SizeData`

**Namespace:** `internal`

#### Methods

##### `SizeData(—)`

**Returns:** ``


### `RectangleData`

**Namespace:** `internal`

#### Methods

##### `RectangleData(—)`

**Returns:** ``


### `BoundsData`

**Namespace:** `internal`

#### Methods

##### `BoundsData(—)`

**Returns:** ``


### `MarginData`

**Namespace:** `internal`

#### Methods

##### `MarginData(—)`

**Returns:** ``


### `ObjectData`

**Namespace:** `internal`

#### Methods

##### `ObjectData(—)`

**Returns:** ``

##### `if(value)`

**Returns:** ``

##### `Set(Base &v)`

**Returns:** `void`

Changes the object that this data holds. Once set, the data owns the object.

##### `Set(Base *v)`

**Returns:** `void`

Changes the object that this data holds. Once set, the data owns the object.

##### `Unset(—)`

**Returns:** `void`

Removes the object that this data holds

##### `IsSet(—)`

**Returns:** `bool`

Removes the object from this data without destroying it.


---

## Functions

### `IntegerData(name, value)`

**Returns:** `return new`



### `FloatData(name, value)`

**Returns:** `return new`



### `TextData(name, value)`

**Returns:** `return new`



### `PointData(name, value)`

**Returns:** `return new`



### `PointfData(name, value)`

**Returns:** `return new`



### `SizeData(name, value)`

**Returns:** `return new`



### `RectangleData(name, value)`

**Returns:** `return new`



### `BoundsData(name, value)`

**Returns:** `return new`



### `MarginData(name, value)`

**Returns:** `return new`



### `if(!target)`

**Returns:** ``



### `ObjectData(name, value)`

**Returns:** `return new`


