# Source

> Auto-generated documentation for the **Source** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `Source`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `GetSize(—)`

**Returns:** `virtual unsigned long`

Returns the size of the wave in number of samples

##### `virtual` `GetLength(—)`

**Returns:** `virtual float`

Returns the length of the wave data in seconds

##### `virtual` `GetChannelCount(—)`

**Returns:** `virtual unsigned`

Returns the number of channels that this wave data has.

##### `virtual` `GetChannelType(int channel)`

**Returns:** `virtual Audio::Channel`

Returns the type of the channel at the given index

##### `virtual` `FindChannel(Audio::Channel channel)`

**Returns:** `virtual int`

Returns the index of the given channel. If the given channel does not exists, this function returns -1

##### `virtual` `GetSampleRate(—)`

**Returns:** `virtual unsigned`

Returns the number of samples per second

##### `virtual` `StartSeeking(unsigned long target)`

**Returns:** `virtual SeekResult`

In order to fully support multithreaded streaming, seeking is requested and then checked by the audio loop if it is completed. If the location is not accessible, this function should return Failed. If the operation is completed immediately, it should return Done. If return value is pending, IsSeeking and IsSeekComplete will be used to complete seek operation. Seeking to a new location while seeking could be allowed depending on the source. If not supported, Failed should be returned.

##### `virtual` `IsSeeking(—)`

**Returns:** `virtual bool`

Returns if source is currently seeking. Even if the seek operation is completed, this function should return true from StartSeeking to SeekingDone. However, if seek operation fails, then this function should return false before IsSeekComplete ever returns true. Even if seek operation is immediately Done, this function could return false permanently.

##### `virtual` `IsSeekComplete(—)`

**Returns:** `virtual bool`

If the current seek operation is completed. Should return true if not seeking or seeking is immediate.

##### `virtual` `SeekTarget(—)`

**Returns:** `virtual unsigned long`

Should return current target that the stream is seeking towards. Should return 0 if not seeking or seeking is immediate.

##### `virtual` `SeekingDone(—)`

**Returns:** `virtual void`

Marks seeking operation as finished. After this call, IsSeeking should be false.


---

## Enums

### `SeekResult`

**Namespace:** `Gorgon`

Denotes the out come of a seek operation

