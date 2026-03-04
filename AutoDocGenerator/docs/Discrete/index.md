# Discrete

> Auto-generated documentation for the **Discrete** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `DiscreteAnimation`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `CurrentFrame(—)`

**Returns:** `virtual unsigned`

Returns the current frame. This function might return NoFrame to denote that the animation does not contain a frame.


### `Frame`

**Namespace:** `Gorgon`

This variable denotes that this animation has no frame at the moment. This is the base class for a single frame in a discreet animation

#### Methods

##### `virtual` `GetDuration(—)`

**Returns:** `virtual unsigned`

Returns the duration of this frame

##### `virtual` `GetStart(—)`

**Returns:** `virtual unsigned`

Returns the starting time of this frame

##### `virtual` `GetEnd(—)`

**Returns:** `virtual unsigned`

Returns the ending time of this frame

##### `virtual` `IsIn(unsigned time)`

**Returns:** `virtual bool`

Returns if the given time is within this frame


### `DiscreteProvider`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `Add(const Frame &frame)`

**Returns:** `virtual void`

Adds a frame to the end of the animation. Frames are designed to be copied, thus they should be lightweight object.

##### `virtual` `Insert(const Frame &frame, int before)`

**Returns:** `virtual void`

Adds a frame to the specified point the animation. Frames are designed to be copied, thus they should be lightweight object. Before is the index of the frame that this frame will be placed before. If it is greater or equal to the number of frames, this function will act like add. Additionally, before could be negative, denoting it will start from the end. -1 is before the last item.

##### `virtual` `MoveBefore(unsigned index, int before)`

**Returns:** `virtual void`

Moves the frame with the given index to the specified point the animation. Before is the index of the frame that this frame will be placed before. If it is greater or equal to the number of frames, this function will move the item to the end. Additionally, before could be negative, denoting it will start from the end. -1 is before the last item.

##### `virtual` `Remove(unsigned index)`

**Returns:** `virtual void`

Removes the given frame.

##### `virtual` `StartOf(unsigned frame)`

**Returns:** `virtual unsigned`

Returns the frame at specific point Returns the frame at specific point Returns the starting time of the given frame

##### `virtual` `GetDuration(—)`

**Returns:** `virtual unsigned`

Returns the duration of the animation

##### `virtual` `GetDuration(unsigned frame)`

**Returns:** `virtual unsigned`

Returns the duration of the given frame

##### `virtual` `Clear(—)`

**Returns:** `virtual void`

Clears all frames from this animation

##### `virtual` `GetCount(—)`

**Returns:** `virtual int`

Returns number of frames

