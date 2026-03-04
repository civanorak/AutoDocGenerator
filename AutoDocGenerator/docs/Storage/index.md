# Storage

> Auto-generated documentation for the **Storage** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_StorageInjection`

**Namespace:** `Gorgon`


### `basic_Storage`

**Namespace:** `Gorgon`

#### Methods

##### `Remove(—)`

**Returns:** ``

Empty constructor Filling constructor Copy constructor is disabled for ownership reasons Move constructor Copy assignment Move assignment

##### `HasAnimation(—)`

**Returns:** `bool`

Check if this storage has an animation

##### `GetAnimation(—)`

**Returns:** `return`

Returns the animation stored in the object. If there is no animation provider stored, it will throw std::runtime_error Alias for GetAnimation

##### `SetAnimation(A_ &value, bool owner = false)`

**Returns:** `void`

Alias for GetAnimation Sets the animation stored in this container

##### `Remove(—)`

**Returns:** ``

##### `SetAnimation(A_ &&value)`

**Returns:** `void`

Sets the animation stored in this container

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

### `AnimationCast(basic_Storage<Original_> &&original)`

**Returns:** `basic_Storage<Target_>`


This function creates a new animation from the stored animation provider. If there is no animation provider stored, it will throw std::runtime_error This function creates a new animation from the stored animation provider. If there is no animation provider stored, it will throw std::runtime_error Moves one type of animation into another.

