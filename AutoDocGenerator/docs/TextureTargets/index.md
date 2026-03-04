# TextureTargets

> Auto-generated documentation for the **TextureTargets** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `TextureTarget`

**Namespace:** `Gorgon`

This interface defines a class that can be used as a common target for texture based drawing

#### Methods

##### `Draw({x, y, size}, color)`

**Returns:** ``

Draws a simple texture to the screen. This variant allows every corner on the target to be specified. The texture target should be cleared before the texture drawn on it is destroyed Draws a textureless solid colored rectangle on the screen. Draws a textureless solid colored rectangle on the screen.

##### `Draw({location, w, h}, color)`

**Returns:** ``

Draws a textureless solid colored rectangle on the screen.

##### `Draw({x, y, w, h}, color)`

**Returns:** ``

Draws a textureless solid colored rectangle on the screen.

##### `Draw({location, size}, color)`

**Returns:** ``

Draws a textureless solid colored rectangle on the screen. Draws a textureless solid colored rectangle on the screen.

##### `virtual` `Draw(const TextureSource &image, const Geometry::Pointf &location, RGBAf color)`

**Returns:** `virtual void`

Draws a textureless solid colored rectangle on the screen. Draws a textureless solid colored rectangle to cover the texture target. Draws a simple texture to the screen. This variant allows every corner on the target and on the texture be specified. The texture target should be cleared before the texture drawn on it is destroyed Draws a simple image to the screen to the given position

##### `virtual` `Clear(—)`

**Returns:** `virtual void`

Draws a simple image to the screen to the given position with the given size. Draws a simple image to the screen using the given tiling method, coordinates and size Clears drawing buffer, in layer architecture this request only affects the layer itself, not its children

##### `virtual` `GetTargetSize(—)`

**Returns:** `virtual Geometry::Size`

Get size of the target

##### `virtual` `GetDrawMode(—)`

**Returns:** `virtual DrawMode`

Returns current draw mode

##### `virtual` `SetDrawMode(DrawMode mode)`

**Returns:** `virtual void`

Sets current draw mode

##### `virtual` `NewMask(—)`

**Returns:** `virtual void`

Should queue the start of a new mask. Only one mask buffer exists and it will be cleared and reused.


---

## Enums

### `DrawMode`

**Namespace:** `Gorgon`

