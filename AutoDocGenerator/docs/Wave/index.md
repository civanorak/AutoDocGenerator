# Wave

> Auto-generated documentation for the **Wave** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Wave`

**Namespace:** `Containers`

This class is a container for wave data. It supports different color modes and access to the underlying data through () operator. This object implements move semantics. Since copy constructor is expensive, it is deleted against accidental use. If a copy of the object is required, use Duplicate function.


### `Sample`

**Namespace:** `Containers`

#### Methods

##### `Sample(—)`

**Returns:** ``

##### `ASSERT(channel < channels, "Index out of bounds")`

**Returns:** ``

##### `Channel(unsigned channel)`

**Returns:** `float`

##### `ASSERT(channel < channels, "Index out of bounds")`

**Returns:** ``

##### `Channel(channel)`

**Returns:** `return`

##### `Channel(channel)`

**Returns:** `return`


### `Iterator`

**Namespace:** `Containers`


### `Wave`

**Namespace:** `Multimedia`

#### Methods

##### `Wave(Containers::Wave &data, bool own = false)`

**Returns:** ``

Empty constructor Constructor assigns or assumes given data

##### `Destroy(—)`

**Returns:** ``

Copy constructor is disabled for accidental copying. Use Duplicate. Move is allowed Destructor

##### `Duplicate(—)`

**Returns:** `Wave`

Duplicates this object along with its data

##### `HasData(—)`

**Returns:** `bool`

Returns if this object has a wave container. Even if this function returns true, the container could be empty.

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the container stored in this object. If this object does not have a wave container, this function will cause a crash.

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the container stored in this object. If this object does not have a wave container, this function will cause a crash.

##### `Destroy(—)`

**Returns:** `void`

Destroys the container in this object.

##### `Get(unsigned long p, unsigned ch)`

**Returns:** `float`

Releases the container data without destroying it Allows access to individual members

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

##### `GetBytes(—)`

**Returns:** `unsigned long`

Returns the size of the wave in bytes

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the length of the wave data in seconds

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the number of channels that this wave data has.

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the type of the channel at the given index

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the index of the given channel. If the given channel does not exists, this function returns -1

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

Returns the number of samples per second

##### `SetSampleRate(unsigned rate)`

**Returns:** `void`

Sets the number samples per second

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

##### `Assign(Containers::Wave &wave)`

**Returns:** `void`

Assigns the given wave container as the data for this object. Ownership of the wave container is not transferred. Data is not copied, thus it should be alive as long as this object is alive.

##### `Assign(float *data, unsigned long size)`

**Returns:** `void`

Uses the supplied data for this object. Ownership of the wave data is not transferred.

##### `Assign(float *data, unsigned long size, std::vector<Audio::Channel> channels)`

**Returns:** `void`

Uses the supplied data for this object. Ownership of the wave data is not transferred.

##### `Assume(Containers::Wave &wave)`

**Returns:** `void`

Assumes the ownership of the given wave container as the data for this object.

##### `Assume(Containers::Wave &&wave)`

**Returns:** `void`

Assumes the ownership of the given wave container as the data for this object.

##### `Assume(float *data, unsigned long size)`

**Returns:** `void`

Assumes the ownership of the given wave data as the data for this object.

##### `Assume(float *data, unsigned long size, std::vector<Audio::Channel> channels)`

**Returns:** `void`

Assumes the ownership of the given wave data as the data for this object.

##### `Import(const std::string &filename)`

**Returns:** `bool`

Imports the given file. File type will be determined automatically from the extension or from the file content. Returns false if the file cannot be imported. This function might throw if there is a problem with the file.

##### `Import(std::istream &stream)`

**Returns:** `bool`

Imports the given file. File type will be determined automatically from the extension or from the file content. Returns false if the file cannot be imported. This function might throw if there is a problem with the file.

##### `Export(const std::string &filename)`

**Returns:** `bool`

Export the data to the given file. File type will be determined automatically from the extension. Returns false if the file cannot be saved.

##### `ImportWav(std::istream &stream)`

**Returns:** `bool`

Imports the given wav file. Returns false if the file cannot be imported.

##### `ImportWav(const std::string &filename)`

**Returns:** `bool`

Imports the given wav file. Returns false if the file cannot be imported.

##### `ExportWav(const std::string &filename)`

**Returns:** `bool`

Export the data to the given wav file. Returns false if the file cannot be saved.

##### `ImportFLAC(const std::string &filename)`

**Returns:** `bool`

Imports the given FLAC file. Returns false if the file cannot be imported.

##### `ImportFLAC(std::istream &stream)`

**Returns:** `bool`

Imports the given FLAC file. Returns false if the file cannot be imported.

##### `ExportFLAC(const std::string &filename, int bps = 16)`

**Returns:** `bool`

Export the data to the given FLAC file. Returns false if the file cannot be saved.

##### `begin(—)`

**Returns:** `auto`

For iteration

##### `ASSERT(data, "Data is not set")`

**Returns:** ``

##### `end(—)`

**Returns:** `auto`

For iteration

##### `ASSERT(data, "Data is not set")`

**Returns:** ``


---

## Functions

### `Wave()`

**Returns:** ``


Constructs an empty wave data


### `Swap(data)`

**Returns:** ``


Constructs a new wave data with the given number of samples and channels. This constructor does not initialize data inside the wave Copy constructor is disabled Move constructor


### `Destroy()`

**Returns:** ``


Copy assignment is disabled Move assignment


### `Swap(other)`

**Returns:** ``



### `Destroy()`

**Returns:** ``


Destructor


### `Duplicate()`

**Returns:** `Wave`


Duplicates this wave, essentially performing the work of copy constructor


### `Resize(unsigned long size, std::vector<Audio::Channel> channels)`

**Returns:** `void`


Resizes the wave to the given size and channels. This function discards the contents of the wave and does not perform any initialization.


### `if(data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `Resize(unsigned long size)`

**Returns:** `void`


Resizes the wave to the given size. This function discards the contents of the wave and does not perform any initialization. Previously set number of channels is used


### `if(data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `Assign(float *newdata, unsigned long size)`

**Returns:** `void`


Copies the given data assigns the new data to this object, size is the number of samples. Assumes number of channels stays the same. newdata should have size*channels number of entries


### `if(data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `if(size > 0)`

**Returns:** ``



### `Assign(float *newdata, unsigned long size, std::vector<Audio::Channel> channels)`

**Returns:** `void`


Copies the given data assigns the new data to this object, size is the number of samples. newdata should have size*channels number of entries


### `if(data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `if(size > 0)`

**Returns:** ``



### `Assign(float *newdata)`

**Returns:** `void`


Copies the given data assigns the new data to this object, size is the number of samples. Assumes number of channels and samples stays the same. newdata should have size*channels number of entries


### `Assume(float *newdata, unsigned long size)`

**Returns:** `void`


Assumes the ownership of the data.


### `if(data && newdata!=data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `Assume(float *newdata, unsigned long size, std::vector<Audio::Channel> channels)`

**Returns:** `void`


Assumes the ownership of the given data. This variant changes the size and channels of the wave. The given data should have the size of size*channels. This function does not perform any checks for the data size while assuming it. newdata could be nullptr however, in this case size should be 0.


### `if(data && newdata!=data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `Assume(float *newdata)`

**Returns:** `void`



### `if(data && newdata!=data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `Destroy()`

**Returns:** ``


Returns and disowns the current data buffer. If wave is empty, this method will return a nullptr.


### `Clear()`

**Returns:** `void`


Cleans the contents of the buffer by setting every byte it contains to 0.


### `Destroy()`

**Returns:** `void`


Destroys this wave by setting its size to 0 and freeing the memory used by its data.


### `if(data)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `Swap(Wave &other)`

**Returns:** `void`


Swaps this wave with another. This function is used to implement move semantics.


### `swap(size, other.size)`

**Returns:** ``



### `swap(channels, other.channels)`

**Returns:** ``



### `swap(data, other.data)`

**Returns:** ``



### `swap(samplerate, other.samplerate)`

**Returns:** ``



### `Get(unsigned long p, unsigned ch)`

**Returns:** `float`


Returns the raw data pointer Returns the raw data pointer Allows access to individual members Allows access to individual members Allows access to individual members


### `GetSize()`

**Returns:** `unsigned long`


Returns the size of the wave in number of samples


### `GetBytes()`

**Returns:** `unsigned long`


Returns the size of the wave in bytes


### `GetLength()`

**Returns:** `float`


Returns the length of the wave data in seconds


### `GetChannelCount()`

**Returns:** `unsigned`


Returns the number of channels that this wave data has.


### `GetChannelType(int channel)`

**Returns:** `Audio::Channel`


Returns the type of the channel at the given index


### `SetChannels(std::vector<Audio::Channel> channels)`

**Returns:** `void`


Sets the channel assignment to this wave data. This function should not change the number of channels, failing that would throw std::runtime_error


### `FindChannel(Audio::Channel channel)`

**Returns:** `int`


Returns the index of the given channel. If the given channel does not exists, this function returns -1


### `GetSampleRate()`

**Returns:** `unsigned`


Returns the number of samples per second


### `SetSampleRate(unsigned rate)`

**Returns:** `void`


Sets the number samples per second


### `ImportWav(const std::string &filename, std::vector<Audio::Channel> channels = {})`

**Returns:** `bool`


Imports a PCM based wav file. Leave channels empty to determine them automatically.


### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `ImportWav(const std::string &filename, bool loaddata, unsigned long &size, int &samplesize, int &blocksize, std::vector<Audio::Channel> channels = {})`

**Returns:** `bool`


Imports a PCM based wav file. Leave channels empty to determine them automatically.


### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `ImportWav(std::istream &file, std::vector<Audio::Channel> channels = {})`

**Returns:** `bool`



### `ImportWav(std::istream &file, bool loaddata, unsigned long &size, int &samplesize, int &blocksize, std::vector<Audio::Channel> channels = {})`

**Returns:** `bool`



### `if(!loaddata)`

**Returns:** ``



### `Resize(size, channels)`

**Returns:** ``



### `for(int c = 0; c<channelcnt; c++)`

**Returns:** ``



### `if(samplesize == 8)`

**Returns:** ``



### `ExportWav(const std::string &filename, int bits = 16)`

**Returns:** `bool`


Exports a PCM based wav file. Bits can be 8 or 16


### `file(filename, std::ios::binary)`

**Returns:** `std::ofstream`



### `ExportWav(file, bits)`

**Returns:** `return`



### `ExportWav(std::ostream &file, int bits = 16)`

**Returns:** `bool`


Exports a PCM based wav file. Bits can be 8 or 16


### `if(bits == 8)`

**Returns:** ``



### `if(bits == 16)`

**Returns:** `else`



### `WriteString(file, "RIFF")`

**Returns:** ``



### `WriteInt32(file, hs+ds-8)`

**Returns:** ``



### `WriteString(file, "WAVEfmt ")`

**Returns:** ``



### `WriteInt32(file, 16)`

**Returns:** ``



### `WriteInt16(file, 1)`

**Returns:** ``



### `WriteInt16(file, bits)`

**Returns:** ``



### `WriteString(file, "data")`

**Returns:** ``



### `WriteInt32(file, ds)`

**Returns:** ``



### `if(bits == 8)`

**Returns:** ``



### `while(ptr<end)`

**Returns:** ``



### `while(ptr<end)`

**Returns:** ``



### `begin()`

**Returns:** `Iterator`



### `end()`

**Returns:** `Iterator`



### `swap(Wave &l, Wave &r)`

**Returns:** `inline void`


Data that stores pixels of the wave Number of samples in the wave Number of channels Sampling rate of the wave Swaps two waves. Should be used unqualified for ADL.


### `Assume(data)`

**Returns:** ``



### `Assign(data)`

**Returns:** ``



### `if(own)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `if(!data)`

**Returns:** ``



### `if(!data)`

**Returns:** ``



### `Destroy()`

**Returns:** ``



### `if(!data)`

**Returns:** ``



### `if(!data)`

**Returns:** ``



### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `if(dotpos != -1)`

**Returns:** ``



### `ImportWav(filename)`

**Returns:** `return`



### `ImportFLAC(filename)`

**Returns:** `return`



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `Import(file)`

**Returns:** `return`



### `if(sig == wavsig)`

**Returns:** ``



### `ImportWav(file)`

**Returns:** `return`



### `if(sig == flacsig)`

**Returns:** `else`



### `ImportFLAC(file)`

**Returns:** `return`



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `ImportWav(file)`

**Returns:** `return`



### `if(!data)`

**Returns:** ``



### `if(dotpos != -1)`

**Returns:** ``



### `ImportWav(filename)`

**Returns:** `return`



### `ImportFLAC(filename)`

**Returns:** `return`



### `ASSERT(data, "Data is not set")`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `ImportFLAC(file)`

**Returns:** `return`



### `if(!data)`

**Returns:** ``



### `if(!data)`

**Returns:** ``



### `file(filename, std::ios::binary)`

**Returns:** `std::ofstream`


