# Blob

> Auto-generated documentation for the **Blob** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Blob`

**Namespace:** `Gorgon`

/This is sound resource. It may contain 22kHz or 44kHz mono or stereo wave files. Also supports LZMA compression. No native sound compression is supported.

#### Methods

##### `Blob(—)`

**Returns:** ``

The type information related to the blob Default constructor

##### `GetSize(—)`

**Returns:** `unsigned long`

Destructor 04010000h (Extended, Blob) Size of the blob

##### `GetType(—)`

**Returns:** `Type`

Returns the type of the blob

##### `Destroy(—)`

**Returns:** `void`

Readies the blob for data writing. Erases previous data, sets current size and type. Also marks blob as loaded. Returned vector which can be used to assign data to it. The returned vector should not be resized even though it will work (for now). It also discards any reader connections. Destroys the data stored in the blob

##### `Load(—)`

**Returns:** `bool`

Loads the blob from the disk. If blob is already loaded, this function will return true

##### `IsLoaded(—)`

**Returns:** `bool`

Returns whether the blob data is loaded

##### `ImportFile(const std::string &filename)`

**Returns:** `bool`

Returns the data stored in this blob. It is safe to change its contents, even its size. However, its better to use reset to adjust the size and the type of the blob Imports the given file as data without changing the type of the blob

##### `ImportFile(filename, type)`

**Returns:** `return`

##### `ImportFile(const std::string &filename, Type type)`

**Returns:** `bool`

Imports the given file as data and sets the type

##### `AppendFile(const std::string &filename)`

**Returns:** `bool`

Appends the given file to the end of the blob data

##### `load(std::shared_ptr<Reader> reader, unsigned long size, bool forceload)`

**Returns:** `bool`

This function loads a blob resource from the given file Loads the blob from the data stream


---

## Functions

### `if(reader)`

**Returns:** ``



### `if(ret && isloaded)`

**Returns:** ``



### `while(!target)`

**Returns:** ``



### `if(gid==GID::Blob_Props)`

**Returns:** ``



### `if(!load)`

**Returns:** ``



### `if(gid==GID::Blob_Data)`

**Returns:** `else`



### `if(load)`

**Returns:** ``



### `if(load)`

**Returns:** ``



### `if(size>0)`

**Returns:** ``



### `if(compression==GID::None)`

**Returns:** ``



### `if(compression==GID::LZMA)`

**Returns:** `else`



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `while(true)`

**Returns:** ``



### `if(reader)`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `while(true)`

**Returns:** ``


