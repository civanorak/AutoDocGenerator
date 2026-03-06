# SGuid

&gt; Auto-generated documentation for the **SGuid** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `SGuid`

**Namespace:** `Gorgon`

This class represents a short globally unique identifier. Unlike full guids, this is not guranteed to be really unique. However, its almost impossible to find a duplicate. This object is 8 bytes long.

#### Methods

##### `SGuid(const CreateNewTag&)`

**Returns:** `explicit`

Allows byte-by-byte addressing of the guid Single integer value representing this guid Tag to create a new GUID Constructor for an empty guid Constructor to create a new guid. Use `Gorgon::SGuid guid{Gorgon::SGuid::CreateNew}` to create a new guid

##### `New(—)`

**Returns:** ``

##### `SGuid(const Byte data[8])`

**Returns:** ``

Creates a new GUID from the given data

##### `if(data==nullptr)`

**Returns:** ``

##### `memcpy_s(Bytes, 8, data, 8)`

**Returns:** ``

##### `checknewserial(—)`

**Returns:** ``

##### `SGuid(unsigned long long data)`

**Returns:** ``

Creates a new GUID from the given data

##### `checknewserial(—)`

**Returns:** ``

##### `SGuid(unsigned serial, unsigned random, unsigned time)`

**Returns:** ``

Creates a new GUID from the given data

##### `Set(serial, random, time)`

**Returns:** ``

##### `SGuid(std::istream &in)`

**Returns:** `explicit`

Reads a new GUID from the given stream

##### `Load(in)`

**Returns:** ``

##### `Set(unsigned serial, unsigned random, unsigned time)`

**Returns:** `void`

Compares two GUIDs Compares two GUIDs Compares two GUIDs Sets the GUID to the given components

##### `memcpy(Bytes+0, &time, 2)`

**Returns:** ``

##### `memcpy(Bytes+2, &random, 3)`

**Returns:** ``

##### `memcpy(Bytes+5, &serial, 3)`

**Returns:** ``

##### `checknewserial(—)`

**Returns:** ``

##### `New(—)`

**Returns:** `void`

Generates a new GUID and assign that GUID to this one

##### `for(int i=7;i>=0;i--)`

**Returns:** ``

Converts the GUID to a string

##### `if(i==5 || i==2)`

**Returns:** ``

##### `Load(std::istream &Data)`

**Returns:** `void`

Loads the GUID from a given stream

##### `checknewserial(—)`

**Returns:** ``

##### `LoadLong(std::istream &file)`

**Returns:** `void`

Loads a full length 16bit GUID from the given file. Used for back compatibility

##### `Save(std::ostream &file)`

**Returns:** `void`

Saves this GUID to file

##### `IsEmpty(—)`

**Returns:** `bool`

Returns whether this GUID is empty

##### `bool(—)`

**Returns:** `operator`

Checks if the GUID is set

##### `checknewserial(—)`

**Returns:** `void`

Value for empty GUID


---

## Functions

### `for(int i=15; i>=0; i--)`

**Returns:** ``


Extracts an SGuid from a stream. Allows an optional % at the beginning


### `if(c>='0' && c<='9')`

**Returns:** ``



### `if(c>='a' && c<='f')`

**Returns:** `else`


