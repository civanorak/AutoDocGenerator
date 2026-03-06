# TextureAnimation

&gt; Auto-generated documentation for the **TextureAnimation** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_TextureAnimationInjection`

**Namespace:** `Gorgon`


### `basic_AnimationFrame`

**Namespace:** `Gorgon`


### `basic_TextureAnimation`

**Namespace:** `Gorgon`

Returns the duration of this frame Returns the starting time of this frame Returns the ending time of this frame Returns if the given time is within this frame Returns the image for this frame


### `basic_TextureAnimationProvider`

**Namespace:** `Gorgon`

Creates a new image animation from the given parent Creates a new image animation from the given parent Deletes this animation object

#### Methods

##### `basic_TextureAnimationProvider(C_ &&other)`

**Returns:** ``

##### `swapout(other)`

**Returns:** ``

##### `swapout(other)`

**Returns:** ``

##### `Duplicate(—)`

**Returns:** `basic_TextureAnimationProvider`

##### `GetWidth(—)`

**Returns:** `int`

Returns the size of the first image

##### `GetHeight(—)`

**Returns:** `int`

Returns the size of the first image

##### `AnimationType(*this, controller)`

**Returns:** `return *new`

Returns the size of the first image Returns number of frames Creates a new animation from this resource

##### `AnimationType(*this, create)`

**Returns:** `return *new`

Creates a new animation from this resource

##### `FrameIndexAt(unsigned time)`

**Returns:** `unsigned`

Returns the image that is to be shown at the given time. If the given time is larger than the animation duration, animation is assumed to be looping. Returns the image at the given frame Returns which frame is at the given time. If the given time is larger than the animation duration, last frame is returned.

##### `for(auto f : frames)`

**Returns:** ``

##### `Add(T_ &image, unsigned duration = 42, bool own = false)`

**Returns:** `void`

Returns the frame at specific point Returns the starting time of the given frame Returns the duration of the animation Returns the duration of the given frame Adds the given image to the end of the animation

##### `Add(T_ &&image, unsigned duration = 42)`

**Returns:** `void`

Adds the given image to the end of the animation. This version owns the given image by moving it in the ownership list

##### `Add(const F_ &frame)`

**Returns:** `void`

##### `Insert(T_ &image, int before, unsigned duration = 42)`

**Returns:** `void`

Inserts the given image before the given frame

##### `for(unsigned i=before+1; i<frames.size()`

**Returns:** ``

##### `Insert(T_ &&img, int before, unsigned duration = 42)`

**Returns:** `void`

Inserts the given image before the given frame

##### `for(unsigned i=before+1; i<frames.size()`

**Returns:** ``

##### `Insert(const F_ &frm, int before)`

**Returns:** `void`

Inserts the given image before the given frame

##### `for(unsigned i=before+1; i<frames.size()`

**Returns:** ``

##### `Own(T_ &image)`

**Returns:** `void`

Inserts the given image before the given frame Moves a frame that has the index before the given position. Owns the given image so that it would be destroyed with this animation

##### `ReleaseAll(—)`

**Returns:** `void`

Removes an image from the animation Removes all images from the animation Releases ownership of all images in the animation without destroying them

##### `Remove(ConstIterator it)`

**Returns:** `void`

Removes an image from the animation

##### `frames(it)`

**Returns:** ``

##### `begin(—)`

**Returns:** `Iterator`

Returns an iterator to the beginning of the animation frames

##### `begin(—)`

**Returns:** `ConstIterator`

Returns an iterator to the beginning of the animation frames

##### `end(—)`

**Returns:** `Iterator`

Returns an iterator to the end of the animation frames

##### `end(—)`

**Returns:** `ConstIterator`

Returns an iterator to the end of the animation frames

##### `swapout(basic_TextureAnimationProvider &other)`

**Returns:** `void`

##### `swap(frames, other.frames)`

**Returns:** ``

##### `swap(duration, other.duration)`

**Returns:** ``

##### `swap(destroylist, other.destroylist)`

**Returns:** ``

##### `swapout(basic_TextureAnimationProvider<typename std::remove_const<T_>::type, A_, N_> &other)`

**Returns:** ``

##### `for(auto &frame : other)`

**Returns:** ``


---

## Functions

### `Prepare()`

**Returns:** `void`



### `for(int i=0; i<c; i++)`

**Returns:** ``


