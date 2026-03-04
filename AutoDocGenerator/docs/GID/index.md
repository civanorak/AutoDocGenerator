# GID

> Auto-generated documentation for the **GID** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Type`

**Namespace:** `GID`

Type to store GID information. This class is necessary to require explicit cast from and to integer. It also allows String::From and printing to streams. GIDs are not only for Resource, they are also used for data exchange.

#### Methods

##### `AsInteger(—)`

**Returns:** `constexpr uint32_t`

Default constructor creates an empty type Constructor to create a new GID from the given value Returns the value of the GID as an integer

##### `IsEmpty(—)`

**Returns:** `constexpr bool`

Returns the value of the GID as a character array Checks if this type information is empty

##### `Module(—)`

**Returns:** `constexpr Byte`

Compares two GIDs Compares two GIDs For std::less Returns the module identifier

##### `Object(—)`

**Returns:** `constexpr Byte`

Returns the object identifier

##### `Property(—)`

**Returns:** `constexpr Byte`

Returns the property part of the GID

##### `Name(—)`

**Returns:** `std::string`

Return the name of a known GID. If this is an unknown GID, its ID will be returned in hex format.


---

## Functions

### `From(const Resource::GID::Type &value)`

**Returns:** `inline std::string`


Creates a string from a GID


### `for(int i=1;i<=8;i++)`

**Returns:** ``



### `switch(value)`

**Returns:** ``


Inserts a GID to a stream

