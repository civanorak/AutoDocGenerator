# AnimationStorage

> Auto-generated documentation for the **AnimationStorage** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `AnimationStorage`

**Namespace:** `Gorgon`

This class denotes the resource is an image animation storage. Unlike graphics based storages, this interface only allows a rectangular animation storage to be moved out.

#### Methods

##### `MoveOut(—)`

**Returns:** `Graphics::RectangularAnimationStorage`

Moves this animation out as a generic value type animation

##### `animmoveout(—)`

**Returns:** `return`

##### `virtual` `animmoveout(—)`

**Returns:** `virtual Graphics::RectangularAnimationStorage`


---

## Functions

### `SaveAnimation(Writer &writer, const Graphics::RectangularAnimationProvider &object)`

**Returns:** `void`


Saves a given generic rectangular animation as resource. Only known animation types can be saved.


### `SaveAnimation(Writer &writer, const Graphics::RectangularAnimationProvider *object)`

**Returns:** `void`


Saves a given generic rectangular animation as resource. Only known animation types can be saved. In this version, if the object is null, it will be saved as Null object.

