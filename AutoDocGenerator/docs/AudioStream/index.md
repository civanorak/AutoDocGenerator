# AudioStream

> Auto-generated documentation for the **AudioStream** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `WavStreamStreamer`

**Namespace:** `internal`

#### Methods

##### `for(auto sample : target)`

**Returns:** ``

Creates a wave stream streamer. Stream location should be at the start of the data.

##### `for(int c=0; c<channels; c++)`

**Returns:** ``

##### `if(samplesize == 8)`

**Returns:** ``


### `DecoderStreamer`

**Namespace:** `internal`


### `AudioStreamer`

**Namespace:** `internal`

This class is the interface for all audiostreamers

#### Methods

##### `virtual` `Init(Containers::Wave &target)`

**Returns:** `virtual unsigned long`

This functions loads all necessary information to wave container without actually loading any data. Returns the total number of samples in the stream source.

##### `virtual` `LoadData(unsigned long samplestart, Containers::Wave &target)`

**Returns:** `virtual unsigned long`

This function should check if there is data to be loaded. If there is, streamer should decode and pass data to audiostream. If there is any extra data that is decoded, it should stay with the streamer.


### `AudioStream`

**Namespace:** `internal`

Currently active streamers Performs stream loading @endcond

#### Methods

##### `AudioStream(AudioStream &&other)`

**Returns:** ``

Constructor

##### `Stream(const std::string &filename)`

**Returns:** `bool`

Starts streaming the given file. File type will be determined automatically from the extension. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `Stream(std::istream &stream, bool ownstream = false)`

**Returns:** `bool`

Starts streaming the given file. File type will be determined automatically from the extension. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `Stream(Resource::Sound &source)`

**Returns:** `bool`

Starts streaming the given resource. Only a portion of the resource will be loaded immediately and it will be loaded automatically as necessary. Returns false if the resource cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `StreamWav(const std::string &filename)`

**Returns:** `bool`

Starts streaming the given wav file. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `StreamWav(std::istream &stream, bool ownstream = false)`

**Returns:** `bool`

Starts streaming the given wav file. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `StreamFLAC(const std::string &filename)`

**Returns:** `bool`

Starts streaming the given FLAC file. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `StreamFLAC(std::istream &stream, bool ownstream = false)`

**Returns:** `bool`

Starts streaming the given FLAC file. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `StreamVorbis(const std::string &filename)`

**Returns:** `bool`

Starts streaming the given Vorbis file. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.

##### `StreamVorbis(std::istream &stream, bool ownstream = false)`

**Returns:** `bool`

Starts streaming the given Vorbis file. Only a portion of the file will be loaded immediately and it will be loaded automatically as necessary. Returns false if the file cannot be read.  @warning  Streaming works if this object is only used by a single controller. Multiple controllers will cause stream to switch back and forth causing issues.


### `bufferdata`

**Namespace:** `internal`

This function will fill the buffer of the stream. This function should only be called from stream thread. Returns the length of the wave data in seconds Returns the number of channels that this wave data has. Returns the type of the channel at the given index Returns the index of the given channel. If the given channel does not exists, this function returns -1 Returns the number of samples per second Starts seeking the stream to the given point. Only one buffer will start loading. The other two buffers will continue playing from the old point. Once the data is started streaming from this new location, other buffers will be loaded as well.


---

## Functions

### `if(dotpos != -1)`

**Returns:** ``


Creates a wave stream streamer. Stream location should be at the start of the data.


### `StreamWav(filename)`

**Returns:** `return`



### `StreamFLAC(filename)`

**Returns:** `return`



### `StreamVorbis(filename)`

**Returns:** `return`



### `Stream(file, true)`

**Returns:** `return`



### `if(sig == wavsig)`

**Returns:** ``



### `StreamWav(file, ownstream)`

**Returns:** `return`



### `if(sig == flacsig)`

**Returns:** `else`



### `StreamFLAC(file)`

**Returns:** `return`



### `if(sig == oggsig)`

**Returns:** `else`



### `StreamVorbis(file)`

**Returns:** `return`



### `StreamWav(file, true)`

**Returns:** `return`



### `g(guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `catch(...)`

**Returns:** ``



### `for(int i=1; i<buffers.size()`

**Returns:** ``


load metadata


### `for(int i=0; i<buffers.size()`

**Returns:** ``



### `StreamFLAC(file, true)`

**Returns:** `return`



### `g(guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `catch(...)`

**Returns:** ``



### `for(int i=1; i<buffers.size()`

**Returns:** ``


load metadata


### `for(int i=0; i<buffers.size()`

**Returns:** ``



### `StreamVorbis(file, true)`

**Returns:** `return`



### `g(guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `catch(...)`

**Returns:** ``



### `for(int i=1; i<buffers.size()`

**Returns:** ``


load metadata


### `for(int i=0; i<buffers.size()`

**Returns:** ``



### `g(guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `if(isseeking && !seekcomplete)`

**Returns:** ``



### `for(int i=0; i<buffers.size()`

**Returns:** ``



### `if(seektarget >= buffers[i].beg  && seektarget < buffers[i].end)`

**Returns:** ``



### `for(int i=0; i<buffers.size()`

**Returns:** ``



### `if(lastsample >= buffers[i].beg  && lastsample < buffers[i].end)`

**Returns:** ``



### `if(sampleind != -1)`

**Returns:** ``



### `for(int i=0; i<buffers.size()`

**Returns:** ``



### `if(sampleind == -1)`

**Returns:** ``



### `for(int i=1; i<buffers.size()`

**Returns:** ``



### `if(p != buffers[cur].beg)`

**Returns:** ``



### `g(Audio::internal::ControllerMtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `if(loaded == 0)`

**Returns:** ``



### `g(guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `g1(guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `g2(other.guard)`

**Returns:** `std::lock_guard<std::mutex>`



### `loadbuffer(bufferdata &buffer, unsigned long startoff)`

**Returns:** `void`


