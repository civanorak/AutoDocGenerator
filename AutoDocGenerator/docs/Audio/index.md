# Audio

&gt; Auto-generated documentation for the **Audio** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Loop`

**Namespace:** `internal`

#### Methods

##### `Loop(—)`

**Returns:** ``

##### `g(internal::ControllerMtx)`

**Returns:** `std::lock_guard<std::mutex>`

##### `for(auto &controller : internal::Controllers)`

**Returns:** ``

##### `perform(basic, wave)`

**Returns:** ``

##### `perform(basic, stream)`

**Returns:** ``

##### `perform(positional, wave)`

**Returns:** ``

##### `perform(positional, stream)`

**Returns:** ``

##### `GetSize(—)`

**Returns:** `int`

##### `GetChannelCount(—)`

**Returns:** `int`

##### `checkseek(BasicController &basic)`

**Returns:** `void`

##### `seekandcheck(BasicController &basic)`

**Returns:** `bool`

##### `checkseek(basic)`

**Returns:** ``

##### `outofbounds(BasicController &basic)`

**Returns:** `bool`

##### `if(basic.looping)`

**Returns:** ``

##### `perform(BasicController &basic, S_ *src)`

**Returns:** `void`

##### `for(unsigned ch = 0; ch <wavedata->GetChannelCount()`

**Returns:** ``

##### `if(channel == Channel::Mono)`

**Returns:** ``

##### `distributetoall(basic, src, org, ch)`

**Returns:** ``

##### `if(channel == Channel::FrontLeft)`

**Returns:** ``

##### `if(channel == Channel::FrontRight)`

**Returns:** `else`

##### `if(channel == Channel::Center)`

**Returns:** `else`

##### `if(ind!=-1)`

**Returns:** ``

##### `sendto(basic, src, org, ch, ind)`

**Returns:** ``

##### `if(channel == Channel::BackLeft)`

**Returns:** `else`

##### `if(ind!=-1)`

**Returns:** ``

##### `sendto(basic, src, org, ch, ind)`

**Returns:** ``

##### `if(channel == Channel::BackRight)`

**Returns:** `else`

##### `if(ind!=-1)`

**Returns:** ``

##### `sendto(basic, src, org, ch, ind)`

**Returns:** ``

##### `if(channel == Channel::LowFreq)`

**Returns:** `else`

##### `if(ind!=-1)`

**Returns:** ``

##### `sendto(basic, src, org, ch, ind)`

**Returns:** ``

##### `distributetoall(basic, src, org, ch)`

**Returns:** ``

##### `perform(PositionalController &positional, S_ *src)`

**Returns:** `void`

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `get(const Multimedia::Wave *src, unsigned long int sample, int ch)`

**Returns:** `float`

##### `get(const Multimedia::AudioStream *src, unsigned long int sample, int ch)`

**Returns:** `float`

##### `for(int i=0; i<src->buffers.size()`

**Returns:** ``

##### `if(sample >= cur.beg && sample < cur.end)`

**Returns:** ``

##### `if(bufferind == -1)`

**Returns:** ``

##### `interpolate(BasicController &basic, S_ *source, int ch)`

**Returns:** `float`

##### `distributetoall(BasicController &basic, S_ *src, double org, int ch)`

**Returns:** `void`

##### `for(int s=0; s<size; s++)`

**Returns:** ``

##### `for(int c = 0; c<channels; c++)`

**Returns:** ``

##### `sendto(BasicController &basic, S_ *src, double org, int src_ch, int dest_ch, float vol = 1.f)`

**Returns:** `void`

##### `for(int s=0; s<size; s++)`

**Returns:** ``


### `Device`

**Namespace:** `Audio`

Represents an audio device.

#### Methods

##### `GetID(—)`

**Returns:** `std::string`

Returns the ID of this device

##### `GetName(—)`

**Returns:** `std::string`

Returns the readable name of this device

##### `GetSampleRate(—)`

**Returns:** `int`

Returns number of samples per second

##### `GetFormat(—)`

**Returns:** `Format`

Returns the format of this device. In some cases, this format might be different than the actual device format.

##### `GetChannelCount(—)`

**Returns:** `int`

Returns the number of channels available

##### `GetChannel(int index)`

**Returns:** `Channel`

Returns the channel type with the given index

##### `FindChannel(Channel type)`

**Returns:** `int`

Returns the index of the given type of channel. If that channel type does not exists, -1 is returned.

##### `IsValid(—)`

**Returns:** `bool`

Returns if this is a valid device

##### `IsHeadphones(—)`

**Returns:** `bool`

Returns if this device is connected to headphones

##### `static` `Default(—)`

**Returns:** `static Device`

Returns the devices in the current system Returns the default device of the current system

##### `static` `Refresh(—)`

**Returns:** `static void`

Refreshes the list of audio devices. Calling this function triggers ChangedEvent.

##### `static` `Find(const std::string &id)`

**Returns:** `static Device`

Name based device lookup. Fires std::runtime_error if the given device cannot be found.

##### `for(auto &dev : devices)`

**Returns:** ``


---

## Functions

### `Log("Audio")`

**Returns:** `Utils::Logger`



### `exitfn()`

**Returns:** `void`



### `SetVolume(float volume)`

**Returns:** `void`



### `SetVolume(Channel channel, float volume)`

**Returns:** `void`



### `for(int i=0;i<Current.GetChannelCount()`

**Returns:** ``



### `if(channel == Channel::Mono)`

**Returns:** ``



### `for(int i=0;i<Current.GetChannelCount()`

**Returns:** ``



### `GetVolume()`

**Returns:** `float`



### `GetVolume(Channel channel)`

**Returns:** `float`



### `for(int i=0;i<Current.GetChannelCount()`

**Returns:** ``



### `AudioLoop()`

**Returns:** `void`



### `while(!exiting)`

**Returns:** ``



### `SkipFrame()`

**Returns:** `else`



### `if(Delay > 0)`

**Returns:** ``



### `Initialize()`

**Returns:** `void`


Starts audio subsystem with the default device


### `IsAvailable()`

**Returns:** `bool`


Whether the audio is available


### `SetVolume(float volume)`

**Returns:** `void`


Changes the master volume


### `SetVolume(Channel channel, float volume)`

**Returns:** `void`


Changes the volume of a channel. If the channel is not found, nothing is done except if the channel is mono. In that case all channel's volume is changed.


### `GetVolume()`

**Returns:** `float`


Returns the master volume


### `GetVolume(Channel channel)`

**Returns:** `float`


Returns the volume of a channel. If the channel does not exists, this function will return 0.

