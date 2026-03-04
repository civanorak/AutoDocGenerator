# Texture

> Auto-generated documentation for the **Texture** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Texture`

**Namespace:** `Gorgon`

This class represents an image depends on a GL texture. Fulfills the requirements of Graphics::TextureSource. Unless GL::Texture created by this object, it is not destroyed by constructor. This is because a GL::Texture could be shared between multiple Graphics::Textures.

#### Methods

##### `Texture(—)`

**Returns:** ``

Default constructor, creates an empty texture

##### `Set(0, ColorMode::Invalid, {0, 0})`

**Returns:** ``

##### `Texture(GL::Texture id, ColorMode mode, const Geometry::Size &size)`

**Returns:** ``

Regular, full texture constructor

##### `Set(id, mode, size)`

**Returns:** ``

##### `Texture(GL::Texture id, ColorMode mode, const Geometry::Size &size, const Geometry::Bounds &location)`

**Returns:** ``

Atlas constructor, specifies a region of the texture

##### `Set(id, mode, size, location)`

**Returns:** ``

##### `Swap(Texture &other)`

**Returns:** `void`

This constructor creates a new texture from the given Image Copies a texture. This newly created texture will not assume ownership Moves a texture. This newly created texture object will own the texture if the other object owns it Swaps two textures

##### `swap(id, other.id)`

**Returns:** ``

##### `swap(size, other.size)`

**Returns:** ``

##### `swap(mode, other.mode)`

**Returns:** ``

##### `swap(coordinates, other.coordinates)`

**Returns:** ``

##### `swap(owner, other.owner)`

**Returns:** ``

##### `Destroy(—)`

**Returns:** ``

##### `Set(const Containers::Image &image)`

**Returns:** `void`

Sets the texture to the given id with the given size. Resets the coordinates to cover entire GL texture

##### `Destroy(—)`

**Returns:** ``

##### `Set(GL::Texture id)`

**Returns:** `void`

Sets the texture to the given id without any modification to size or color mode. Use this function to change atlas base.

##### `if(owner)`

**Returns:** ``

##### `Set(GL::Texture id, ColorMode mode, const Geometry::Size &size)`

**Returns:** `void`

Sets the texture to the given id with the given size. Resets the coordinates to cover entire GL texture

##### `Destroy(—)`

**Returns:** ``

##### `Set(GL::Texture id, ColorMode mode, const Geometry::Size &size, const Geometry::Bounds &location)`

**Returns:** `void`

Sets the texture to the given id with the given size. Calculates the texture coordinates for the specified location in pixels @param   id id of the texture, reported by the underlying GL framework @param   size of the GL texture in pixels @param   location is the location of this texture over GL texture in pixels.

##### `Destroy(—)`

**Returns:** ``

##### `Assume(GL::Texture id, ColorMode mode, const Geometry::Size &size)`

**Returns:** `void`

Sets the texture to the given id with the given size. Resets the coordinates to cover entire GL texture. Transfers the ownership of the texture.

##### `Set(id, mode, size)`

**Returns:** ``

##### `Assume(GL::Texture id, ColorMode mode, const Geometry::Size &size, const Geometry::Bounds &location)`

**Returns:** `void`

Sets the texture to the given id with the given size. Calculates the texture coordinates for the specified location in pixels. Transfers the ownership of the texture @param   id id of the texture, reported by the underlying GL framework @param   size of the GL texture in pixels @param   location is the location of this texture over GL texture in pixels.

##### `Set(id, mode, size, location)`

**Returns:** ``

##### `CreateEmpty(const Geometry::Size &size, ColorMode mode)`

**Returns:** `void`

Create an empty texture.

##### `Destroy(—)`

**Returns:** `void`

Returns GL::Texture to be drawn. Declared final to allow inlining. Returns the size of the texture in pixels. Declared final to allow inlining. Returns the coordinates of the texture to be used. Declared final to allow inlining. Remove the texture from this object. If this object is the owner of the texture, then it is destroyed.

##### `if(owner)`

**Returns:** ``

##### `Release(—)`

**Returns:** `GL::Texture`

Releases the texture id that might be owned by this object without destroying it


### `TextureImage`

**Namespace:** `Gorgon`

GL texture id Size of the texture Color mode of the texture, necessary to choose correct texture Whether this object owns this texture Readily calculated texture coordinates of the image. Normally spans entire GL texture, however, could be changed to create texture atlas. These coordinates are kept in floating point u,v representation for quick consumption by the GL This is a solid texture based image class.

#### Methods

##### `TextureImage(—)`

**Returns:** ``

Default constructor, creates an empty texture

##### `TextureImage(TextureImage &&other)`

**Returns:** ``

Copy constructor Move constructor


### `TextureProvider`

**Namespace:** `Gorgon`

Regular, full texture constructor Atlas constructor, specifies a region of the texture, size is for the entirity of the texture This constructor creates a new texture from the given Image

#### Methods

##### `TextureProvider(—)`

**Returns:** ``

Default constructor, creates an empty texture

##### `GetSize(—)`

**Returns:** `return`

Copy constructor Move constructor Regular, full texture constructor Atlas constructor, specifies a region of the texture, size is for the entirity of the texture This constructor creates a new texture from the given Image

