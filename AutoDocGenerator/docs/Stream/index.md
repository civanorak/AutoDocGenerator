# Stream

> Auto-generated documentation for the **Stream** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Stream`

**Namespace:** `Gorgon`

#### Methods

##### `StreamThread(—)`

**Returns:** `friend void`

##### `Stream(—)`

**Returns:** ``

##### `virtual` `FillBuffer(—)`

**Returns:** `virtual void`

This function is called to allow stream to fill its buffer. It is used internally and should only be called from the stream thread.


---

## Functions

### `ReadEnum32(std::istream &stream)`

**Returns:** `inline E_`


Reads an enumeration that is saved as 32bit integer


### `E_(r)`

**Returns:** `return`



### `ReadInt32(std::istream &stream)`

**Returns:** `inline long`


Reads a 32-bit integer from the stream. A long is at least 32 bits, could be more however, only 4 bytes will be read from the stream


### `ReadUInt32(std::istream &stream)`

**Returns:** `inline unsigned long`


Reads a 32-bit unsigned integer from the stream. An unsigned long is at least 32 bits, could be more however, only 4 bytes will be read from the stream


### `ReadInt16(std::istream &stream)`

**Returns:** `inline int`


Reads a 16-bit integer from the stream. An int is at least 16 bits, could be more however, only 2 bytes will be read from the stream


### `ReadUInt16(std::istream &stream)`

**Returns:** `inline unsigned`


Reads a 16-bit unsigned integer from the stream. An unsigned int is at least 16 bits, could be more however, only 2 bytes will be read from the stream


### `ReadInt8(std::istream &stream)`

**Returns:** `inline char`


Reads an 8-bit integer from the stream. A char is at least 8 bits, could be more however, only 1 byte will be read from the stream


### `ReadUInt8(std::istream &stream)`

**Returns:** `inline Byte`


Reads an 8-bit unsigned integer from the stream. A char is at least 8 bits, could be more however, only 1 byte will be read from the stream


### `ReadFloat(std::istream &stream)`

**Returns:** `inline float`


Reads a 32 bit IEEE floating point number from the stream. This function only works on systems that that have native 32 bit floats.


### `ReadDouble(std::istream &stream)`

**Returns:** `inline double`


Reads a 64 bit IEEE double precision floating point number from the stream. This function only works on systems that have native 64 bit doubles.


### `ReadBool(std::istream &stream)`

**Returns:** `inline bool`


Reads a boolean value. In resource 1.0, booleans are stored as 32bit integers


### `ReadRGBA(std::istream &stream)`

**Returns:** `inline Graphics::RGBA`


Reads a RGBA color, R will be read first


### `ReadRGBAf(std::istream &stream)`

**Returns:** `inline Graphics::RGBAf`


Reads a RGBAf color, R will be read first


### `ReadString(std::istream &stream)`

**Returns:** `inline std::string`


Reads a string from a given stream. Assumes the size of the string is appended before the string as 32-bit unsigned value.


### `ReadString(std::istream &stream, unsigned long size)`

**Returns:** `inline std::string`


Reads a string with the given size.


### `ReadArray(std::istream &stream, T_ *data, unsigned long size)`

**Returns:** `inline void`


Reads an array from the stream. Array type should be a fixed size construct (ie. a byte, int32_t), otherwise a mismatch between binary formats will cause trouble. @param  data is the data to be read from the stream @param  size is the number of elements to be read


### `ReadGuid(std::istream &stream)`

**Returns:** `inline SGuid`


Reads a GUID from the given stream.


### `SGuid(stream)`

**Returns:** `return`



### `ReadPoint(std::istream &stream)`

**Returns:** `inline Geometry::Point`



### `ReadPointf(std::istream &stream)`

**Returns:** `inline Geometry::Pointf`



### `ReadSize(std::istream &stream)`

**Returns:** `inline Geometry::Size`



### `WriteEnum32(std::ostream &stream, E_ v)`

**Returns:** `inline void`


Writes an enumeration as a 32-bit integer


### `WriteInt32(std::ostream &stream, long value)`

**Returns:** `inline void`


Writes a 32-bit integer to the stream.


### `WriteUInt32(std::ostream &stream, unsigned long value)`

**Returns:** `inline void`


Writes a 32-bit unsigned integer from the stream. An unsigned long is at least 32 bits, could be more however, only 4 bytes will be written to the stream


### `WriteInt16(std::ostream &stream, int value)`

**Returns:** `inline void`


Writes a 16-bit integer from the stream. An int is at least 16 bits, could be more however, only 2 bytes will be written to the stream


### `WriteUInt16(std::ostream &stream, unsigned value)`

**Returns:** `inline void`


Writes a 16-bit unsigned integer from the stream. An unsigned int is at least 16 bits, could be more however, only 2 bytes will be written to the stream


### `WriteInt8(std::ostream &stream, char value)`

**Returns:** `inline void`


Writes an 8-bit integer from the stream. A char is at least 8 bits, could be more however, only 1 byte will be written to the stream


### `WriteUInt8(std::ostream &stream, Byte value)`

**Returns:** `inline void`


Writes an 8-bit unsigned integer from the stream. A char is at least 8 bits, could be more however, only 1 byte will be written to the stream


### `WriteFloat(std::ostream &stream, float value)`

**Returns:** `inline void`


Writes a 32 bit IEEE floating point number from the stream. This function only works on systems that that have native 32 bit floats.


### `WriteDouble(std::ostream &stream, double value)`

**Returns:** `inline void`


Writes a 64 bit IEEE double precision floating point number from the stream. This function only works on systems that have native 64 bit doubles.


### `WriteBool(std::ostream &stream, bool value)`

**Returns:** `inline void`


Writes a boolean value. In resource 1.0, booleans are stored as 32bit integers


### `WriteInt32(stream, value)`

**Returns:** ``



### `WriteRGBA(std::ostream &stream, Graphics::RGBA value)`

**Returns:** `inline void`


Writes a RGBA color, R will be saved first


### `WriteUInt8(stream, value.R)`

**Returns:** ``



### `WriteUInt8(stream, value.G)`

**Returns:** ``



### `WriteUInt8(stream, value.B)`

**Returns:** ``



### `WriteUInt8(stream, value.A)`

**Returns:** ``



### `WriteRGBAf(std::ostream &stream, Graphics::RGBAf value)`

**Returns:** `inline void`


Writes a RGBAf color, R will be saved first


### `WriteFloat(stream, value.R)`

**Returns:** ``



### `WriteFloat(stream, value.G)`

**Returns:** ``



### `WriteFloat(stream, value.B)`

**Returns:** ``



### `WriteFloat(stream, value.A)`

**Returns:** ``



### `WriteStringWithSize(std::ostream &stream, const std::string &value)`

**Returns:** `inline void`


Writes a string from a given stream. The size of the string is appended before the string as 32-bit unsigned value.


### `WriteString(std::ostream &stream, const std::string &value)`

**Returns:** `inline void`


Writes a string without its size.


### `WriteArray(std::ostream &stream, const T_ *data, unsigned long size)`

**Returns:** `inline void`


Writes an array to the stream. Array type should be a fixed size construct (ie. a byte, int32_t), otherwise a mismatch between binary formats will cause trouble. @param  data is the data to be written to the stream @param  size is the number of elements to be write


### `WriteVector(std::ostream &stream, const std::vector<T_> &data)`

**Returns:** `inline void`


Writes a vector to the stream. Type of vector elements should be given a fixed size construct, otherwise a mismatch between binary formats will cause trouble.


### `WriteGuid(std::ostream &stream, const SGuid &value)`

**Returns:** `inline void`


Writes a GUID from the given stream.


### `WriteArray(stream, value.Bytes, 8)`

**Returns:** ``



### `WritePoint(std::ostream &stream, Geometry::Point p)`

**Returns:** `inline void`


Saves the point as two consecutive 32bit integers


### `WriteInt32(stream, p.X)`

**Returns:** ``



### `WriteInt32(stream, p.Y)`

**Returns:** ``



### `WritePointf(std::ostream &stream, Geometry::Pointf p)`

**Returns:** ``


Saves the point as two consecutive floats. This function will not work if float type is double


### `WriteFloat(stream, p.X)`

**Returns:** ``



### `WriteFloat(stream, p.Y)`

**Returns:** ``



### `WriteSize(std::ostream &stream, Geometry::Size s)`

**Returns:** `inline void`


Saves the size as two consecutive 32bit integers


### `WriteInt32(stream, s.Width)`

**Returns:** ``



### `WriteInt32(stream, s.Height)`

**Returns:** ``


