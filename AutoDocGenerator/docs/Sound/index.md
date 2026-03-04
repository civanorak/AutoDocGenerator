# Sound

> Auto-generated documentation for the **Sound** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Sound`

**Namespace:** `Resource`

This is sound resource. Supports

#### Methods

##### `Sound(—)`

**Returns:** ``

Default constructor

##### `Destroy(—)`

**Returns:** `void`

Destructor 04010000h (Extended, Sound) Destroys the data stored in the sound

##### `Load(—)`

**Returns:** `bool`

Loads the sound from the disk. If sound is already loaded, this function will return true

##### `IsLoaded(—)`

**Returns:** `bool`

Returns whether the sound data is loaded

##### `Assign(const Containers::Wave &wave)`

**Returns:** `void`

This function loads a sound resource from the given file Assigns the sound to the copy of the given data. Ownership of the given data is not transferred. If the given data is not required elsewhere, consider using Assume function. Also sets IsLoaded.

##### `Assume(Containers::Wave &wave)`

**Returns:** `void`

Assumes the contents of the given wave as wave data. The given parameter is moved from and will become empty. Also sets IsLoaded.

##### `GetBits(—)`

**Returns:** `int`

##### `SetBits(int bits)`

**Returns:** `void`

Sets the number of bits per sample. Only effects saving, in memory format is non-PCM 32bit float. Currently this does not have effect if data is saved non-PCM fashion.

##### `checkfmt(—)`

**Returns:** ``

##### `IsPCM(—)`

**Returns:** `bool`

Returns if the wave data will be saved as PCM data.

##### `SetPCM(bool pcm)`

**Returns:** `void`

Set whether the wave data should be saved in PCM format. FLAC supports only PCM while internal saving mechanism can save wave non-PCM mode as 32bit float.

##### `checkfmt(—)`

**Returns:** ``

##### `GetCompression(—)`

**Returns:** `GID::Type`

Returns the compression type of this resource.

##### `SetCompression(GID::Type compression)`

**Returns:** `void`

Changes the compression type of this resource. Currently GID::None and GID::FLAC is supported. If Flac support is disabled, GID::FLAC will cause a runtime_error during save.

##### `checkfmt(—)`

**Returns:** ``

##### `load(std::shared_ptr<Reader> reader, unsigned long size, bool forceload)`

**Returns:** `bool`

Loads the sound from the data stream

##### `checkfmt(—)`

**Returns:** `void`

Checks if the format of the file is well-formed


---

## Functions

### `if(ret && isloaded)`

**Returns:** ``



### `while(!target)`

**Returns:** ``



### `if(gid==GID::Sound_Fmt)`

**Returns:** ``



### `if(!load)`

**Returns:** ``



### `checkfmt()`

**Returns:** ``



### `if(gid==GID::Sound_Props)`

**Returns:** `else`



### `checkfmt()`

**Returns:** ``



### `if(gid==GID::Sound_Channels)`

**Returns:** `else`



### `if(gid==GID::Sound_Wave)`

**Returns:** `else`



### `if(load)`

**Returns:** ``



### `if(!pcm)`

**Returns:** ``



### `for(unsigned long i=0; i<uncompressed; i++)`

**Returns:** ``



### `for(unsigned c = 0; c<data.GetChannelCount()`

**Returns:** ``



### `if(bits == 8)`

**Returns:** ``



### `if(gid==GID::Sound_Cmp_Wave)`

**Returns:** `else`



### `if(load)`

**Returns:** ``



### `if(size>0)`

**Returns:** ``



### `if(compression == GID::None)`

**Returns:** ``



### `if(compression == GID::FLAC)`

**Returns:** `else`



### `for(unsigned i=0; i<data.GetChannelCount()`

**Returns:** ``



### `if(compression==GID::None)`

**Returns:** ``



### `if(pcm)`

**Returns:** ``



### `if(bits == 8)`

**Returns:** ``



### `for(unsigned long i=0; i<data.GetSize()`

**Returns:** ``



### `for(unsigned c=0; c<data.GetChannelCount()`

**Returns:** ``



### `if(bits == 16)`

**Returns:** `else`



### `for(unsigned long i=0; i<data.GetSize()`

**Returns:** ``



### `for(unsigned c=0; c<data.GetChannelCount()`

**Returns:** ``



### `if(compression==GID::FLAC)`

**Returns:** `else`



### `if(compression == GID::FLAC)`

**Returns:** ``



### `if(compression == GID::None)`

**Returns:** `else`


