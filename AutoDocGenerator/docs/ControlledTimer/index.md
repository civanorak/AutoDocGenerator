# ControlledTimer

&gt; Auto-generated documentation for the **ControlledTimer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `ControlledTimer`

**Namespace:** `Gorgon`

#### Methods

##### `for(auto &anim : animations)`

**Returns:** ``

##### `int(dur * v)`

**Returns:** `return`

##### `GetProgress(int ind)`

**Returns:** `unsigned int`

Returns the progress of the given animation. If the given index does not exists, this function will return (unsigned)-1.

##### `SetProgress(float value)`

**Returns:** `void`

Sets the progress of this controlled timer. 0 is the start of the animation 1 is the end of it. The value is threated as cyclic and normalized before used while keeping the original value. Negative values are act as if starting from the end. Thus a value of -0.1 is same as 0.9. Use GetProgressRate to obtain the value set in this function. GetProgress can be used to obtain progress of the first or specific animation.

##### `GetProgressRate(—)`

**Returns:** `float`

Returns the progress of this controlled timer.

