# Validators

&gt; Auto-generated documentation for the **Validators** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ConversionValidator`

**Namespace:** `Gorgon`

#### Methods

##### `IsValid(std::string)`

**Returns:** `bool`

Checks if the given string is valid

##### `AllowInsert(std::string /*start*/, std::string /*insert*/, std::string /*end*/)`

**Returns:** `bool`

Checks if given string can be inserted between start and end

##### `AllowErase(std::string /*before*/, int /*count*/, std::string /*after*/)`

**Returns:** `bool`

Checks if given number of characters can be erased from before.

##### `AllowReplace(std::string /*before*/, int /*count*/, std::string /*insert*/, std::string /*after*/)`

**Returns:** `bool`

Checks if given number of characters can be replace with insert at the end of before.

##### `From(std::string text)`

**Returns:** `Type`

Converts the given string to the type. If input is not valid, return initial value

##### `ToString(const Type &value)`

**Returns:** `std::string`

Converts the given value to string.


---

## Enums

### `DisplayType`

**Namespace:** `Gorgon`


---

## Functions

### `IsValid(std::string)`

**Returns:** `bool`


Checks if the given string is valid


### `AllowInsert(std::string /*start*/, std::string /*insert*/, std::string /*end*/)`

**Returns:** `bool`


Checks if given string can be inserted between start and end


### `AllowErase(std::string /*before*/, int /*count*/, std::string /*after*/)`

**Returns:** `bool`


Checks if given number of characters can be erased from before.


### `AllowReplace(std::string /*before*/, int /*count*/, std::string /*insert*/, std::string /*after*/)`

**Returns:** `bool`


Checks if given number of characters can be replace with insert at the end of before.


### `From(std::string text)`

**Returns:** `Type`


Converts the given string to the type. If input is not valid, return initial value


### `ToString(const Type &value)`

**Returns:** `std::string`


Converts the given value to string.


### `switch(Display)`

**Returns:** ``


