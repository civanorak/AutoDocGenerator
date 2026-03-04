# Drawables

> Auto-generated documentation for the **Drawables** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Drawable`

**Namespace:** `Gorgon`

Represents a drawable object, that can be drawn to the given point. Size of the object is assumed to be fixed. Drawing a single drawable can cause many texture to be added to the given texture target

#### Methods

##### `draw(target, {x, y}, color)`

**Returns:** ``

Draw to the given coordinates Draw to the given coordinates Draw to the given coordinates

##### `draw(target, p, color)`

**Returns:** ``

Draw to the given coordinates

##### `virtual` `draw(TextureTarget &target, const Geometry::Pointf &p, RGBAf color)`

**Returns:** `virtual void`

This is the only function that needs to implemented for a drawable


### `SizelessDrawable`

**Namespace:** `Gorgon`

A drawable object that does not have a size and requires a region to draw.

#### Methods

##### `virtual` `drawin(TextureTarget &target, const Geometry::Rectanglef &r, RGBAf color)`

**Returns:** `virtual void`

This function should draw this drawable inside the given rectangle

##### `virtual` `drawin(TextureTarget &target, const SizeController &controller, const Geometry::Rectanglef &r, RGBAf color)`

**Returns:** `virtual void`

This function should draw this drawable inside the given rectangle according to the given controller. If this object already have a size controller, this given controller should be given priority.

##### `virtual` `calculatesize(const Geometry::Size &area)`

**Returns:** `virtual Geometry::Size`

This function should return the size of the object when it is requested to be drawn in the given area. If size contains is a negative value, this function should try to return native size of the object. If no such size exists, a logical size should be returned.

##### `virtual` `calculatesize(const SizeController &controller, const Geometry::Size &s)`

**Returns:** `virtual Geometry::Size`

This function should return the size of the object when it is requested to be drawn in the given area. This variant should use the given size controller. If the object already has a controller, given controller should be given priority. If h parameter is a negative value, this function should try to return native size of the object. If no such size exists, a logical size should be returned.


### `RectangularDrawable`

**Namespace:** `Gorgon`

/This is a basic drawing object

#### Methods

##### `drawstretched(target, {x, y, w, h}, color)`

**Returns:** ``

Draw to the given area by stretching object to fit Draw to the given area by stretching object to fit Draw to the given area by stretching object to fit Draw to the given area by stretching object to fit Draw to the given area by stretching object to fit Draw to the given area by stretching object to fit

##### `drawstretched(target, {p, w, h}, color)`

**Returns:** ``

Draw to the given area by stretching object to fit

##### `drawstretched(target, {x, y, size}, color)`

**Returns:** ``

Draw to the given area by stretching object to fit

##### `drawstretched(target, {p, size}, color)`

**Returns:** ``

Draw to the given area by stretching object to fit

##### `drawstretched(target, r, color)`

**Returns:** ``

Draw to the given area by stretching object to fit

##### `DrawShrinked(TextureTarget &target, Placement align = Placement::MiddleCenter)`

**Returns:** `void`

Draw to the given area by fitting the bitmap down to the size of the area

##### `DrawShrinked(TextureTarget &target, float x, float y, const Geometry::Sizef &size, Placement align = Placement::MiddleCenter)`

**Returns:** `void`

Draw to the given area by fitting the bitmap down to the size of the area

##### `DrawShrinked(target, {x, y}, size, align)`

**Returns:** ``

##### `DrawShrinked(TextureTarget &target, const Geometry::Point &p, float w, float h, Placement align = Placement::MiddleCenter)`

**Returns:** `void`

Draw to the given area by fitting the bitmap down to the size of the area

##### `DrawShrinked(target, p, {w, h}, align)`

**Returns:** ``

##### `DrawShrinked(TextureTarget &target, float x, float y, float w, float h, Placement align = Placement::MiddleCenter)`

**Returns:** `void`

Draw to the given area by fitting the bitmap down to the size of the area

##### `DrawShrinked(target, {x, y}, {w, h}, align)`

**Returns:** ``

##### `DrawShrinked(TextureTarget &target, const Geometry::Pointf &p, const Geometry::Sizef &size, Placement align = Placement::MiddleCenter)`

**Returns:** `void`

Draw to the given area by fitting the bitmap down to the size of the area

##### `draw(target, {x1, y1}, {x2, y2}, {x3, y3}, {x4, y4}, color)`

**Returns:** ``

Draw the object to the target by specifying coordinates for four corners

##### `draw(target, p1, p2, p3, p4, color)`

**Returns:** ``

Draw the object to the target by specifying coordinates for four corners

##### `DrawRotated(TextureTarget &target, const Geometry::Point &p, float angle, RGBAf color)`

**Returns:** `void`

Draw the object rotated to the given angle in radians, full C++11 support will enable the use of 90deg like qualifiers Draw the object rotated to the given angle in radians, full C++11 support will enable the use of 90deg like qualifiers

##### `DrawRotated(target, {x, y}, angle, {oX, oY}, color)`

**Returns:** ``

Draw the object rotated to the given angle in radians, full C++11 support will enable the use of 90deg like qualifiers

##### `drawin(target, tiling, {x, y, w, h}, color)`

**Returns:** ``

Draws the object to the target using the given tiling information Draws the object to the target using the given tiling information Draws the object to the target using the given tiling information Draws the object to the target using the given tiling information Draws the object to the target using the given tiling information Draws the object to the target using the given tiling information

##### `drawin(target, tiling, {p, w, h}, color)`

**Returns:** ``

Draws the object to the target using the given tiling information

##### `drawin(target, tiling, {x, y, size}, color)`

**Returns:** ``

Draws the object to the target using the given tiling information

##### `drawin(target, tiling, {p, size}, color)`

**Returns:** ``

Draws the object to the target using the given tiling information

##### `drawin(target, tiling, r, color)`

**Returns:** ``

Draws the object to the target using the given tiling information

##### `drawin(target, {x, y, w, h}, color)`

**Returns:** ``

Draw to the given area Draw to the given area Draw to the given area Draw to the given area Draw in the given area Draw to fill the given target Draw to the given coordinates with the given size according to the given controller Draw to the given area according to the given controller Draw to the given area the given size according to the given controller Draw to the given area with the given size according to the given controller Draw in the given area according to the given controller Draw to fill the given target according to the given controller Draw to the given area

##### `drawin(target, {p, w, h}, color)`

**Returns:** ``

Draw to the given area

##### `drawin(target, {x, y, size}, color)`

**Returns:** ``

Draw to the given area

##### `drawin(target, {p, size}, color)`

**Returns:** ``

Draw to the given area

##### `drawin(target, r, color)`

**Returns:** ``

Draw in the given area

##### `drawin(target, controller, {x, y, w, h}, color)`

**Returns:** ``

Draw to the given coordinates with the given size according to the given controller

##### `drawin(target, controller, {p, w, h}, color)`

**Returns:** ``

Draw to the given area according to the given controller

##### `drawin(target, controller, {x, y, size}, color)`

**Returns:** ``

Draw to the given area the given size according to the given controller

##### `drawin(target, controller, {p, size}, color)`

**Returns:** ``

Draw to the given area with the given size according to the given controller

##### `drawin(target, controller, r, color)`

**Returns:** ``

Draw in the given area according to the given controller

##### `CalculateSize(const Geometry::Size &area)`

**Returns:** `const Geometry::Size`

Calculates the adjusted size of this drawable depending on the given area. This function calculates actual the size of the drawable when it is drawn in an area that has the given size. When a size parameter is set to -1, the object returns its native size. Native size might not be available for some objects however, they will try to return a logical value.

##### `calculatesize(area)`

**Returns:** `return`

##### `CalculateSize(int w=-1, int h=-1)`

**Returns:** `const Geometry::Size`

Calculates the adjusted size of this drawable depending on the given area. This function calculates actual the size of the drawable when it is drawn in an area that has the given size. When a size parameter is set to -1, the object returns its native size. Native size might not be available for some objects however, they will try to return a logical value.

##### `calculatesize({w, h})`

**Returns:** `return`

##### `CalculateSize(const SizeController &controller, const Geometry::Size &area)`

**Returns:** `const Geometry::Size`

Calculates the adjusted size of this drawable depending on the given area and controller. This function calculates actual the size of the drawable when it is drawn in an area that has the given size. When a size parameter is set to -1, the object returns its native size. Native size might not be available for some objects however, they will try to return a logical value.

##### `calculatesize(controller, area)`

**Returns:** `return`

##### `CalculateSize(const SizeController &controller, int w=-1, int h=-1)`

**Returns:** `const Geometry::Size`

Calculates the adjusted size of this drawable depending on the given area and controller. This function calculates actual the size of the drawable when it is drawn in an area that has the given size. When a size parameter is set to -1, the object returns its native size. Native size might not be available for some objects however, they will try to return a logical value.

##### `calculatesize(controller, {w, h})`

**Returns:** `return`

##### `draw(target, {x1, y1}, {x2, y2}, {x3, y3}, {x4, y4}, {u1, v1}, {u2, v2}, {u3, v3}, {u4, v4}, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `draw(target, p1, p2, p3, p4, {u1, v1}, {u2, v2}, {u3, v3}, {u4, v4}, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `draw(target, {x1, y1}, {x2, y2}, {x3, y3}, {x4, y4}, t1, t2, t3, t4, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `draw(target, p1, p2, p3, p4, t1, t2, t3, t4, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `draw(target, {x, y}, {x+w, y}, {x+w, y+h}, {x, y+h}, {u1, v1}, {u2, v2}, {u3, v3}, {u4, v4}, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `draw(target, {x, y}, {x+w, y}, {x+w, y+h}, {x, y+h}, t1, t2, t3, t4, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `Draw(target, p.X, p.Y, w, h, {u1, v1}, {u2, v2}, {u3, v3}, {u4, v4}, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `Draw(target, p.X, p.Y, w, h, t1, t2, t3, t4, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `Draw(target, x, y, size.Width, size.Height, {u1, v1}, {u2, v2}, {u3, v3}, {u4, v4}, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `Draw(target, x, y, size.Width, size.Height, t1, t2, t3, t4, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated

##### `Draw(target, p.X, p.Y, size.Width, size.Height, {u1, v1}, {u2, v2}, {u3, v3}, {u4, v4}, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `Draw(target, p.X, p.Y, size.Width, size.Height, t1, t2, t3, t4, color)`

**Returns:** ``

Draws the object with the given screen and texture coordinates. Texture coordinates are given between 0 and 1. If the coordinates are out of bounds the texture is repeated. This function is not guaranteed to be implemented and can be directed the draw call where texture coordinates are not specified. This function can be removed in the future.

##### `GetSize(—)`

**Returns:** `const Geometry::Size`

Returns the size of this object

##### `getsize(—)`

**Returns:** `return`

##### `GetWidth(—)`

**Returns:** `int`

Returns the width of the drawable

##### `GetHeight(—)`

**Returns:** `int`

Returns the height of the drawable

##### `virtual` `drawstretched(TextureTarget &target, const Geometry::Rectanglef &r, RGBAf color)`

**Returns:** `virtual void`

This function should draw the object to the given point. This method should draw to object inside the given quad with the given texture coordinates. The texture should be considered repeating and any values outside 0-1 range should be treated as such This function should draw the object inside the given quad. The object should be stretched as necessary This function should draw the object to the target area. The object should be stretched along both dimensions to fit into the given area. It might be logical to override this as it is possible to avoid additional function calls and if statements

##### `drawin(target, Tiling::None, r, color)`

**Returns:** ``

##### `virtual` `drawin(TextureTarget &target, const Geometry::Rectanglef &r, RGBAf color)`

**Returns:** `virtual void`

This function should draw the object to the target area. The object should be tiled or cut to fit the given area It might be logical to override this as it is possible to avoid additional function calls and if statements

##### `drawin(target, Tiling::Both, r, color)`

**Returns:** ``

##### `virtual` `drawin(TextureTarget &target, const SizeController &controller, const Geometry::Rectanglef &r, RGBAf color)`

**Returns:** `virtual void`

This function should draw this drawable inside the given rectangle according to the given controller. If this object already have a size controller, this given controller should be given priority.

##### `virtual` `calculatesize(const Geometry::Size &area)`

**Returns:** `virtual Geometry::Size`

This function should return the size of the object when it is requested to be drawn in the given area. If size contains is a negative value, this function should try to return native size of the object. If no such size exists, a logical size should be returned.

##### `virtual` `calculatesize(const SizeController &controller, const Geometry::Size &s)`

**Returns:** `virtual Geometry::Size`

This function should return the size of the object when it is requested to be drawn in the given area. This variant should use the given size controller. If the object already has a controller, given controller should be given priority. If h parameter is a negative value, this function should try to return native size of the object. If no such size exists, a logical size should be returned.

##### `virtual` `getsize(—)`

**Returns:** `virtual Geometry::Size`

Should return the exact size of this object


### `Image`

**Namespace:** `Gorgon`

This is an interface for solid texture based image. It handles the drawing automatically. Does not supply implementation for Texture.

#### Methods

##### `GetImageSize(—)`

**Returns:** `return`

##### `GetImageSize(—)`

**Returns:** `return`

