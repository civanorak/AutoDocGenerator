# Controllers

&gt; Auto-generated documentation for the **Controllers** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Controller`

**Namespace:** `internal`

#### Methods

##### `AudioLoop(—)`

**Returns:** `friend void`

##### `Controller(—)`

**Returns:** ``

Default constructor

##### `virtual` `Type(—)`

**Returns:** `virtual ControllerType`

Returns the type of the controller

##### `RemoveMe(—)`

**Returns:** `void`


### `BasicController`

**Namespace:** `internal`

#### Methods

##### `AudioLoop(—)`

**Returns:** `friend void`

##### `datachanged(—)`

**Returns:** ``

Default constructor Filling constructor

##### `RemoveMe(—)`

**Returns:** ``

##### `HasData(—)`

**Returns:** `bool`

Returns whether this controller has data

##### `ReleaseData(—)`

**Returns:** `void`

Releases the data being played by this controller

##### `SetData(const Source &wavedata)`

**Returns:** `void`

Sets the data to be played by this controller. Timing might be percent based, thus, when an audio data is swapped with another, playback position can be moved. Additionally, if the timing is stored in seconds, swapping wavedata might cause playback to stop or loop to the start immediately.

##### `GetVolume(—)`

**Returns:** `float`

Plays this sound. When called, this function will unset looping flag. If there is no wavedata associated with this controller, nothing happens until the data is set, after data is set, it starts playing immediately. Plays this sound. When called, this function will set looping flag. If there is no wavedata associated with this controller, nothing happens until the data is set, after data is set, it starts playing immediately. Pauses the playback. Next time when a play or loop is called, the playback will continue from where it left off. Use Reset to start over. Resets the playback to the beginning of the buffer. This function will not stop the playback. Changes the point of playback to the given time in seconds. This function will not start or stop the playback Changes the point of playback to the given time in fraction: 1 would be the end of buffer. This function will not start or stop the playback Changes the volume of the playback. 1 would mean the volume is not modified. While its possible to use higher values, it might cause distortion in the sound. Returns the current volume of the playback

##### `GetDuration(—)`

**Returns:** `float`

Returns the duration of the audio buffer in seconds. This function will return 0 if data is not set.

##### `GetCurrentTime(—)`

**Returns:** `float`

Returns the current playback time in seconds

##### `GetCurrentFraction(—)`

**Returns:** `float`

Returns the fraction of the audio that is played

##### `IsFinished(—)`

**Returns:** `bool`

Whether the audio is finished playing

##### `IsPlaying(—)`

**Returns:** `bool`

Whether the audio is being played right now

##### `IsLooping(—)`

**Returns:** `bool`

Whether the audio is being looped

##### `virtual` `datachanged(—)`

**Returns:** `virtual void`

Contains the data for this controller Override this function to detect changes in the wave data. It will be called if the constructor sets wavedata


### `PositionalController`

**Namespace:** `internal`

#### Methods

##### `AudioLoop(—)`

**Returns:** `friend void`

##### `RemoveMe(—)`

**Returns:** ``

Default constructor Filling constructor

##### `Move(const Geometry::Point3D &target)`

**Returns:** `void`

##### `Move(const Geometry::Pointf &target)`

**Returns:** `void`

##### `GetLocation(—)`

**Returns:** `Geometry::Point3D`


---

## Enums

### `ControllerType`

**Namespace:** `internal`


---

## Functions

### `guard(internal::ControllerMtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `RemoveMe()`

**Returns:** ``



### `guard(internal::ControllerMtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `guard(internal::ControllerMtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `datachanged()`

**Returns:** ``



### `guard(internal::ControllerMtx)`

**Returns:** `std::lock_guard<std::mutex>`



### `Seek(0)`

**Returns:** ``



### `datachanged()`

**Returns:** ``



### `if(wavedata)`

**Returns:** ``



### `Seek(0)`

**Returns:** ``



### `Seek(0)`

**Returns:** ``



### `Play()`

**Returns:** ``



### `if(wavedata)`

**Returns:** ``



### `if(ret == Source::Done)`

**Returns:** ``



### `if(wavedata)`

**Returns:** ``



### `Seek(0)`

**Returns:** ``


