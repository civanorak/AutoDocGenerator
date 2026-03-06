# Writer

&gt; Auto-generated documentation for the **Writer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `WriteError`

**Namespace:** `Gorgon`

This error is fired to a write operations


### `Writer`

**Namespace:** `Gorgon`

The cause of the error cannot be determined The given file cannot be opened, probably its path does not exists or the operation is denied. There is no data to save Regular constructor, creates error text to error number A constructor to allow custom text for the error The type of loading error occurred Strings for error codes


### `Marker`

**Namespace:** `Gorgon`

#### Methods

##### `Marker(Marker &&other)`

**Returns:** ``


### `FileWriter`

**Namespace:** `Gorgon`

This is the stream that will be used to write data to. Underlying writers can have specialized copies of this member. Allows data to be written to a file

#### Methods

##### `catch(...)`

**Returns:** ``

Constructs a new object with the given filename

##### `if(thrw)`

**Returns:** ``

##### `WriteError(WriteError::CannotOpenFile, "Cannot open file: "+filename+" either target path does not exist or access denied.")`

**Returns:** `throw`


---

## Enums

### `ErrorType`

**Namespace:** `Gorgon`

Error types


---

## Functions

### `ASSERT(stream==nullptr, "Stream is not closed by the opener")`

**Returns:** ``


Any writer implementation should close and set the stream to nullptr in destructor


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``


This should be last resort, use if the actual stream is needed.


### `IsGood()`

**Returns:** `bool`


Checks if the stream is open and it can be written to


### `Close()`

**Returns:** `void`



### `close()`

**Returns:** ``



### `Tell()`

**Returns:** `unsigned long`


Tells the current position


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `Seek(unsigned long pos)`

**Returns:** `void`


Seeks to the given position


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteEnum32(E_ value)`

**Returns:** `void`


@name Platform independent data readers @{ These functions allow platform independent data reading capability. In worst case, where the platform cannot be supported, they stop compilation instead of generating incorrectly working system. These functions might differ in encoding depending on the file version. Make sure a file is open before invoking these functions no runtime checks will be performed during release. Writes an enumeration as 32-bit integer to the stream.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteInt32(long value)`

**Returns:** `void`


Writes a 32-bit integer to the stream. A long is at least 32 bits, could be more however, only 4 bytes will be written to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteUInt32(unsigned long value)`

**Returns:** `void`


Writes a 32-bit unsigned integer to the stream. An unsigned long is at least 32 bits, could be more however, only 4 bytes will be written to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteInt16(int value)`

**Returns:** `void`


Writes a 16-bit integer to the stream. An int is at least 16 bits, could be more however, only 2 bytes will be written to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteUInt16(unsigned value)`

**Returns:** `void`


Writes a 16-bit unsigned integer to the stream. An unsigned int is at least 32 bits, could be more however, only 2 bytes will be written to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteInt8(char value)`

**Returns:** `void`


Writes an 8-bit integer to the stream. A char is at least 8 bits, could be more however, only 1 byte will be written to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteUInt8(Byte value)`

**Returns:** `void`


Writes an 8-bit unsigned integer to the stream. A char is at least 8 bits, could be more however, only 1 byte will be written to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteFloat(float value)`

**Returns:** `void`


Writes a 32 bit IEEE floating point number to the file. This function only works on systems that that have native 32 bit floats.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteDouble(double value)`

**Returns:** `void`


Writes a 64 bit IEEE double precision floating point number to the file. This function only works on systems that have native 64 bit doubles.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteBool(bool value)`

**Returns:** `void`


Writes a boolean value. In resource 1.0, booleans are stored as 32bit integers


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteRGBA(Graphics::RGBA value)`

**Returns:** `void`


Writes a RGBA color, R will be saved first. RGBA takes 4 x 1 bytes


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteRGBAf(Graphics::RGBAf value)`

**Returns:** `void`


Writes a RGBAf color, R will be saved first. RGBAf takes 4 x 4 bytes


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WritePoint(Geometry::Point value)`

**Returns:** `void`


Writes a point to the stream, point takes 2 x 4 bytes


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WritePointf(Geometry::Pointf value)`

**Returns:** `void`


Writes a point to the stream, point takes 2 x 4 bytes


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteSize(Geometry::Size value)`

**Returns:** `void`


Writes a size to the stream, size takes 2 x 4 bytes


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteStringWithSize(const std::string &value)`

**Returns:** `void`


Writes a string from a given stream. The size of the string is appended before the string as 32-bit unsigned value.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteString(const std::string &value)`

**Returns:** `void`


Writes a string without its size.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteArray(const T_ *data, unsigned long size)`

**Returns:** `void`


Writes an array to the file. Array type should be given a fixed size construct, otherwise a mismatch between binary formats will cause trouble. @param  data is the data to be written to the file @param  size is the number of elements to be read


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteVector(const std::vector<T_> &data)`

**Returns:** `inline void`


Writes a vector to the stream. Type of vector elements should be given a fixed size construct, otherwise a mismatch between binary formats will cause trouble.


### `WriteGID(GID::Type value)`

**Returns:** `void`


Writes a GID to the given stream.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteGuid(const SGuid &value)`

**Returns:** `void`


Writes a GUID to the given stream.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteChunkSize(unsigned long value)`

**Returns:** `void`


Writes chunk size to the stream


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteUInt32(value)`

**Returns:** ``



### `WriteObjectStart(const Base &base)`

**Returns:** `Marker`


@} Writes the start of an object. Should have a matching WriteEnd with the returned marker.


### `WriteObjectStart(const Base *base)`

**Returns:** `Marker`


Writes the start of an object. Should have a matching WriteEnd with the returned marker.


### `ASSERT(base, "Object cannot be nullptr")`

**Returns:** ``



### `WriteObjectStart(*base)`

**Returns:** `return`



### `WriteObjectStart(const Base &base, GID::Type type)`

**Returns:** `Marker`


Writes the start of an object. Should have a matching WriteEnd with the returned marker. This variant allows a replacement GID.


### `WriteObjectStart(const Base *base, GID::Type type)`

**Returns:** `Marker`


Writes the start of an object. Should have a matching WriteEnd with the returned marker. This variant allows a replacement GID.


### `ASSERT(base, "Object cannot be nullptr")`

**Returns:** ``



### `WriteObjectStart(*base, type)`

**Returns:** `return`



### `WriteChunkStart(GID::Type type)`

**Returns:** `Marker`


Writes the start of a chunk. Should have a matching WriteEnd


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteGID(type)`

**Returns:** ``



### `WriteChunkSize(-1)`

**Returns:** ``



### `WriteChunkHeader(GID::Type type, unsigned long size)`

**Returns:** `void`


Writes the header of a chunk. If the size of the chunk is hard to compute, it is possible to use WriteChunkStart


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `WriteGID(type)`

**Returns:** ``



### `WriteChunkSize(size)`

**Returns:** ``



### `WriteEnd(Marker &marker)`

**Returns:** `void`


This function performs writes necessary to end a chunk that is represented by the marker.


### `ASSERT(stream, "Writer is not opened.")`

**Returns:** ``



### `ASSERT(pos>=marker.pos+4, "Seeking before the start of the file.")`

**Returns:** ``



### `ASSERT(marker.pos<=pos, "Marker is after the current position.")`

**Returns:** ``



### `Seek(marker.pos)`

**Returns:** ``



### `WriteChunkSize(size)`

**Returns:** ``



### `Seek(pos)`

**Returns:** ``



### `close()`

**Returns:** `virtual void`


This function should close the stream. The pointer will be unset by Writeer class


### `open(bool thrw)`

**Returns:** `virtual bool`


This function should open the stream and set stream member. If thrw is set to true and stream cannot be opened, a WriteError should be thrown. Otherwise this function is not allowed to throw.

