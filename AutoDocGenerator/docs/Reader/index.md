# Reader

&gt; Auto-generated documentation for the **Reader** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `LoadError`

**Namespace:** `Gorgon`

This class represents a loading error


### `Reader`

**Namespace:** `Gorgon`

An unknown error occurred Cannot find the given file File does not contain correct signature and is probably not a Gorgon resource Version in the file is not recognized There is no containing root folder There is an unknown node in the file. This is never thrown in release mode. Cannot open the given file There is no file object associated with the resource. Generally thrown during late loading If the compression type in the file is not supported. Regular constructor, creates error text from error number A constructor to allow custom text for the error The type of loading error occurred Strings for error codes


### `Mark`

**Namespace:** `Gorgon`

Marks a target position in file. Can be checked if it is reached. Asserts to make sure target is not passed.

#### Methods

##### `bool(—)`

**Returns:** `explicit operator`

Constructs a target using a reader and absolute file position. Prefer using Reader::Target function to create a target. Copy constructor Checks if the target is reached

##### `ASSERT(pos==target, "Reading operation passed the target.")`

**Returns:** ``

##### `Tell(—)`

**Returns:** `unsigned long`

Tells the position of this mark


### `FileReader`

**Namespace:** `Gorgon`

This is the stream that will be used to read data from. Underlying readers can have specialized copies of this member. This is a file reader. Allows a Gorgon Resource to be loaded from a file

#### Methods

##### `catch(...)`

**Returns:** ``

Constructor requires a file to be opened later.

##### `if(thrw)`

**Returns:** ``

##### `LoadError(LoadError::FileNotFound, "Cannot open file: "+filename)`

**Returns:** `throw`


---

## Enums

### `ErrorType`

**Namespace:** `Gorgon`

Error types


---

## Functions

### `Reader()`

**Returns:** ``



### `KeepOpen()`

**Returns:** `void`


Request reader to keep reading stream open. There is an internal counter that makes sure that the reader is closed when it is no longer needed.


### `NoLongerNeeded()`

**Returns:** `void`


Marks that this reader is no longer needed. This action will decrement requests made to keep the stream open. If no object requires this reader, it is closed. Note that some readers cannot be reopened.


### `if(--keepopenrequests)`

**Returns:** ``



### `close()`

**Returns:** ``



### `Open()`

**Returns:** `void`


Opens the reader. If this operation fails, it will throw LoadError.


### `if(!stream)`

**Returns:** ``



### `open(true)`

**Returns:** ``



### `ASSERT(stream, "Reader did not set the stream.")`

**Returns:** ``



### `IsOpen()`

**Returns:** `bool`


Checks if the stream is open


### `IsGood()`

**Returns:** `bool`


Checks if the stream is open and it can be read from


### `IsFailed()`

**Returns:** `bool`


Checks if the stream is open and it can be read from


### `TryOpen()`

**Returns:** `bool`


Tries to open the stream, if it fails, this function returns false. If this function returns true, read operations can be carried.


### `if(!stream)`

**Returns:** ``



### `open(false)`

**Returns:** `return`



### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``


This should be last resort, use if the actual stream is needed.


### `Tell()`

**Returns:** `unsigned long`


Tells the current position


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `Seek(unsigned long pos)`

**Returns:** `void`


Seeks to the given position


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `Seek(const Mark &pos)`

**Returns:** `void`


Seeks to the given position


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `Target(unsigned long delta)`

**Returns:** `Mark`


Creates mark to the the target that is delta distance from current point in file


### `ReadCommonChunk(Base &self, GID::Type gid, unsigned long size)`

**Returns:** `bool`



### `ReadEnum32()`

**Returns:** `E_`


@name Platform independent data readers @{ These functions allow platform independent data reading capability. In worst case, where the platform cannot be supported, they stop compilation instead of generating incorrectly working system. These functions might differ in encoding depending on the file version. Make sure a file is open before invoking these functions no runtime checks will be performed during release. Reads an enumeration as 32-bit integer from the stream.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadInt32()`

**Returns:** `long`


Reads a 32-bit integer from the stream. A long is at least 32 bits, could be more however, only 4 bytes will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadUInt32()`

**Returns:** `unsigned long`


Reads a 32-bit unsigned integer from the stream. An unsigned long is at least 32 bits, could be more however, only 4 bytes will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadInt16()`

**Returns:** `int`


Reads a 16-bit integer from the stream. An int is at least 16 bits, could be more however, only 2 bytes will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadUInt16()`

**Returns:** `unsigned`


Reads a 16-bit unsigned integer from the stream. An unsigned int is at least 32 bits, could be more however, only 2 bytes will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadInt8()`

**Returns:** `char`


Reads an 8-bit integer from the stream. A char is at least 8 bits, could be more however, only 1 byte will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadUInt8()`

**Returns:** `Byte`


Reads an 8-bit unsigned integer from the stream. A char is at least 8 bits, could be more however, only 1 byte will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadFloat()`

**Returns:** `float`


Reads a 32 bit IEEE floating point number from the file. This function only works on systems that that have native 32 bit floats.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadDouble()`

**Returns:** `double`


Reads a 64 bit IEEE double precision floating point number from the file. This function only works on systems that have native 64 bit doubles.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadBool()`

**Returns:** `bool`


Reads a boolean value. In resource 1.0, booleans are stored as 32bit integers


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadRGBA()`

**Returns:** `Graphics::RGBA`


Reads a RGBA color, R will be read first


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadRGBAf()`

**Returns:** `Graphics::RGBAf`


Reads a RGBAf color, R will be read first


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadString()`

**Returns:** `std::string`


Reads a string from a given stream. Assumes the size of the string is appended before the string as 32-bit unsigned value.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadString(unsigned long size)`

**Returns:** `std::string`


Reads a string with the given size.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadArray(T_ *data, unsigned long size)`

**Returns:** `void`


Reads an array from the file. Array type should be given a fixed size construct, otherwise a mismatch between binary formats will cause trouble. @param  data is the data to be read from the file @param  size is the number of elements to be read


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadGID()`

**Returns:** `GID::Type`


Reads a GID from the given stream.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadGuid()`

**Returns:** `SGuid`


Reads a GUID from the given stream.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadPoint()`

**Returns:** `Geometry::Point`


Reads a Point from the given stream.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadPointf()`

**Returns:** `Geometry::Point`


Reads a Pointf from the given stream.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadSize()`

**Returns:** `Geometry::Size`


Reads a Size from the given stream.


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadChunkSize()`

**Returns:** `unsigned long`


Reads chunk size from a stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `ReadUInt32()`

**Returns:** `return`



### `EatChunk(long size)`

**Returns:** `void`


Removes a chunk of data with the given size from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `EatChunk()`

**Returns:** `void`


Removes a chunk of data from the stream, the size will be read from the stream


### `ASSERT(stream, "Reader is not opened.")`

**Returns:** ``



### `close()`

**Returns:** `virtual void`


@} This function should close the stream. The pointer will be unset by Reader class


### `open(bool thrw)`

**Returns:** `virtual bool`


This function should open the stream and set stream member. If thrw is set to true and stream cannot be opened, a LoadError should be thrown. Otherwise this function is not allowed to throw.

