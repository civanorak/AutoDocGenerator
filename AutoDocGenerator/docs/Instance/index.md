# Instance

&gt; Auto-generated documentation for the **Instance** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_InstanceInjection`

**Namespace:** `Gorgon`


### `basic_Instance`

**Namespace:** `Gorgon`

#### Methods

##### `Remove(—)`

**Returns:** ``

Empty constructor Filling constructor Copy constructor is disabled for ownership reasons Move constructor Copy assignment Move assignment

##### `Remove(—)`

**Returns:** ``

Move assignment, owns the assigned object as CreateAnimation returns objects that needs to be owned

##### `HasAnimation(—)`

**Returns:** `bool`

Check if this instance has an animation

##### `GetAnimation(—)`

**Returns:** `return`

Returns the animation stored in the object. If there is no animation provider stored, it will throw std::runtime_error Alias for GetAnimation

##### `SetAnimation(A_ &value, bool owner = true)`

**Returns:** `void`

Alias for GetAnimation Sets the animation stored in this container

##### `Remove(—)`

**Returns:** ``

##### `Remove(—)`

**Returns:** `void`

Removes the animation stored in the container, if the container owns the animation, it will be destroyed. Use Release to release resource without destroying it

##### `Remove(—)`

**Returns:** ``

Removes the animation from the storage without destroying it.

##### `IsOwner(—)`

**Returns:** `bool`

Whether the stored animation is owned by this container


---

## Functions

### `AnimationCast(basic_Instance<Original_> &&original)`

**Returns:** `basic_Instance<Target_>`


Moves one type of animation into another.

