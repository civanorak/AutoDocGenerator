# GL

> Auto-generated documentation for the **GL** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `GenerateTexture(const Containers::Image &data)`

**Returns:** `Texture`


This is a GLTexture descriptor. This may change depending on the GL used. It will always be copy constructible/assignable and comparable. This function generates a texture from the given image data.


### `GenerateEmptyTexture(const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `Texture`


This function generates a texture from the given image data.


### `ResizeTexture(Texture texture, const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`


Resizes the given texture to the specified size. The data in the texture cannot be trusted after this call.


### `UpdateTexture(Texture texture, const Containers::Image &data)`

**Returns:** `void`


Updates the given texture to contain the given data


### `CopyToTexture(Texture texture, const Containers::Image &data, Geometry::Point target)`

**Returns:** `void`


Copies the data from the given image to the texture starting from the given target


### `CopyToTexture(Texture texture, const Containers::Image &data, Geometry::Bounds source, Geometry::Point target)`

**Returns:** `void`


Copies the data from the given image to the texture starting from specified boundary of the given target


### `DestroyTexture(Texture texture)`

**Returns:** `void`


Destroys the given texture


### `RenderToTexture(FrameBuffer &buffer)`

**Returns:** `void`


Begins using the given frame buffer.


### `RenderToScreen()`

**Returns:** `void`


Stops rendering to a texture and start rendering to a buffer


### `SetupContext(const Geometry::Size &size)`

**Returns:** `void`


Performs first time initialization on GL context


### `Resize(const Geometry::Size &size)`

**Returns:** `void`


Resizes the active context


### `Clear()`

**Returns:** `void`


Clears the window pointed by the active context


### `SetDefaultClear()`

**Returns:** `void`


Sets default clear parameters as current.


### `SetDefaultBlending()`

**Returns:** `void`


Sets default blending parameters as current.

