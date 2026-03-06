# Animations

&gt; Auto-generated documentation for the **Animations** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Animation`

**Namespace:** `Gorgon`

A regular drawable animation


### `RectangularAnimation`

**Namespace:** `Gorgon`

Rectangular drawable animation


### `DiscreteAnimation`

**Namespace:** `Gorgon`

A discrete rectangular animation, this is most suitable for bitmap or texture animations


### `AnimationProvider`

**Namespace:** `Gorgon`

A regular drawable animation provider


### `RectangularAnimationProvider`

**Namespace:** `Gorgon`

This function moves this animation provider into a new provider. Ownership of this new object belongs to the caller and this object could be destroyed safely using DeleteAnimation. This function should create a new animation with the given controller and if owner parameter is set to true, it should assume ownership of the controller This function should create and animation and depending on the create parameter, it should create its own timer. This class provides rectangular animations

#### Methods

##### `virtual` `GetSize(—)`

**Returns:** `virtual Geometry::Size`

This function moves this animation provider into a new provider. Ownership of this new object belongs to the caller and this object could be destroyed safely. This function should create a new animation with the given controller and if owner parameter is set to true, it should assume ownership of the controller This function should create and animation and depending on the create parameter, it should create its own timer.

##### `GetWidth(—)`

**Returns:** `int`

##### `GetHeight(—)`

**Returns:** `int`


### `DiscreteAnimationProvider`

**Namespace:** `Gorgon`

This class provides discrete and rectangular animation which is suitable for bitmap and texture animations


### `ImageProvider`

**Namespace:** `Gorgon`

This function should create a new animation with the given controller and if owner parameter is set to true, it should assume ownership of the controller This function should create and animation and depending on the create parameter, it should create its own timer.


---

## Functions

### `GetWidth()`

**Returns:** `int`


Injects additional functionality for AnimationProviders Injects additional functionality for RectangularAnimationProviders


### `GetHeight()`

**Returns:** `int`


