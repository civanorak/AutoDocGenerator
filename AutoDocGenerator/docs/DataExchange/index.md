# DataExchange

> Auto-generated documentation for the **DataExchange** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `ExchangeData`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `Name(—)`

**Returns:** `virtual std::string`

Should return the name of the data type

##### `virtual` `Type(—)`

**Returns:** `virtual Resource::GID::Type`

Should return the type id of the data

##### `virtual` `Text(—)`

**Returns:** `virtual std::string`

Should return the textual representation of the data. A datatype can simply return its typename

##### `Name(—)`

**Returns:** `return`


### `TextData`

**Namespace:** `Gorgon`

#### Methods

##### `SetText(std::string value)`

**Returns:** `void`

Changes the text in this data

##### `GetText(—)`

**Returns:** `std::string`

Returns the text in this data


### `FileData`

**Namespace:** `Gorgon`

#### Methods

##### `AddFile(std::string value)`

**Returns:** `void`

Adds a new file to the list

##### `RemoveFile(int ind)`

**Returns:** `void`

Removes a file from the list

##### `Clear(—)`

**Returns:** `void`

Clears the file list

##### `GetSize(—)`

**Returns:** `int`

Returns the number of files in the list

##### `begin(—)`

**Returns:** `std::vector<std::string>::const_iterator`

Returns the file at the given index To allow ranged based iteration

##### `end(—)`

**Returns:** `std::vector<std::string>::const_iterator`

To allow ranged based iteration

##### `begin(—)`

**Returns:** `std::vector<std::string>::iterator`

To allow ranged based iteration

##### `end(—)`

**Returns:** `std::vector<std::string>::iterator`

To allow ranged based iteration


---

## Enums

### `ExchangeAction`

**Namespace:** `Gorgon`

