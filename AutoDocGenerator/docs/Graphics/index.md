# Graphics

&gt; Auto-generated documentation for the **Graphics** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `SizeController`

**Namespace:** `Graphics`

This class allows control over a sizable object

#### Methods

##### `CalculateSize(Geometry::Size objectsize, const Geometry::Size &area)`

**Returns:** `Geometry::Size`

The drawing is drawn only once with its original size. The placement of this single drawing will be determined by the alignment. The drawing is stretched along this axis to cover the given size. If the given drawing object is truly scalable, this value acts same as Tile. The drawing is tiled along this axis to cover the given size. If the area is smaller, drawing will be cut from the given size. If the area is larger, drawing will be repeated as necessary. While repeating, it is possible for drawing not to cover the area exactly, In this case, alignment determines which side will be incomplete. If center alignment is selected, both sides will have same amount of incomplete drawing. The drawing is tiled along this axis to cover the given size. In this mode, the drawing will never placed incomplete. Instead, it will be repeated to cover as much area as possible without exceeding the given size. Any area that is left will be distributed to the edges according to the selected alignment. The drawing is tiled along this axis to cover the given size. In this mode, the drawing will never placed incomplete. Instead, it will be repeated to cover entire area. Excess drawing will be aligned depending on the selected alignment. The drawing is tiled along this axis to cover the given size. In this mode, the drawing will never placed incomplete. Instead, it will be repeated to cover entire area. If the last drawing that will be partial is more than 50% of the size of the original drawing, it will be drawn. Excess drawing or the area left empty is distributed according to the selected alignment. Creates a default size controller which tiles the object from top-left Creates a size controller that places a single object to the given placement. This is an implicit conversion constructor. Creates a new size controller with the given tiling options and placement Creates a new size controller with the given tiling options and placement Calculates the size of the object according to the tiling rules

##### `switch(Horizontal)`

**Returns:** ``

##### `switch(Vertical)`

**Returns:** ``

##### `CalculateSize(Geometry::Sizef objectsize, const Geometry::Sizef &area)`

**Returns:** `Geometry::Sizef`

Calculates the size of the object according to the tiling rules

##### `switch(Horizontal)`

**Returns:** ``

##### `switch(Vertical)`

**Returns:** ``

##### `CalculateOffset(const Geometry::Size &objectsize, const Geometry::Size &area)`

**Returns:** `Geometry::Point`

Calculates the size of the object according to the tiling and placement rules

##### `CalculateOffset(const Geometry::Sizef &objectsize, const Geometry::Sizef &area)`

**Returns:** `Geometry::Pointf`

Calculates the size of the object according to the tiling and placement rules

##### `CalculateArea(const Geometry::Size &objectsize, const Geometry::Size &area)`

**Returns:** `Geometry::Rectangle`

Calculates the drawing area of the object according to the tiling and placement rules

##### `CalculateArea(const Geometry::Sizef &objectsize, const Geometry::Sizef &area)`

**Returns:** `Geometry::Rectanglef`

Calculates the drawing area of the object according to the tiling and placement rules

##### `CalculateSize(Geometry::Size repeatingsize, const Geometry::Size &fixedsize, const Geometry::Size &area)`

**Returns:** `Geometry::Size`

Calculates the size of the object according to the tiling rules

##### `switch(Horizontal)`

**Returns:** ``

##### `switch(Vertical)`

**Returns:** ``

##### `CalculateSize(Geometry::Sizef repeatingsize, const Geometry::Sizef &fixedsize, const Geometry::Sizef &area)`

**Returns:** `Geometry::Sizef`

Calculates the size of the object according to the tiling rules

##### `switch(Horizontal)`

**Returns:** ``

##### `switch(Vertical)`

**Returns:** ``

##### `CalculateOffset(const Geometry::Size &repeatingsize, const Geometry::Size &fixedsize, const Geometry::Size &area)`

**Returns:** `Geometry::Point`

Calculates the size of the object according to the tiling and placement rules

##### `CalculateOffset(const Geometry::Sizef &repeatingsize, const Geometry::Sizef &fixedsize, const Geometry::Sizef &area)`

**Returns:** `Geometry::Pointf`

Calculates the size of the object according to the tiling and placement rules

##### `CalculateArea(const Geometry::Size &repeatingsize, const Geometry::Size &fixedsize, const Geometry::Size &area)`

**Returns:** `Geometry::Rectangle`

Calculates the drawing area of the object according to the tiling and placement rules

##### `CalculateArea(const Geometry::Sizef &repeatingsize, const Geometry::Sizef &fixedsize, const Geometry::Sizef &area)`

**Returns:** `Geometry::Rectangle`

Calculates the drawing area of the object according to the tiling and placement rules

##### `GetTiling(—)`

**Returns:** `Graphics::Tiling`


### `TextureSource`

**Namespace:** `Graphics`

Horizontal tiling mode Vertical tiling mode Placement method This interface represents a GL texture source.

#### Methods

##### `virtual` `GetID(—)`

**Returns:** `virtual GL::Texture`

Should return GL::Texture to be drawn. This could be 0 to denote no texture is to be used.

##### `virtual` `GetMode(—)`

**Returns:** `virtual ColorMode`

##### `virtual` `GetImageSize(—)`

**Returns:** `virtual Geometry::Size`

Should return the size of the image stored in texture. Not the whole texture size.

##### `IsPartial(—)`

**Returns:** `bool`

Should return the coordinates of the texture to be used Returns whether this texture uses only a part of the GL::Texture. This indicates that the tiling operations should be performed without texture repeating method.


---

## Enums

### `Tiling`

**Namespace:** `Graphics`

Details which directions a texture should tile. If its not tiled for that direction, it will be stretched. If the target size is smaller, tiling causes partial draw instead of shrinking. @todo Should be fitted to String::Enum


### `Orientation`

**Namespace:** `Graphics`

2D orientation constants


### `Alignment`

**Namespace:** `Graphics`

Defines how an object is aligned


### `TextAlignment`

**Namespace:** `Graphics`

Placed at the start of the axis Centered along the axis Placed at the end of the axis Defines how a text is aligned. Justification should be used as an independent flag as a text could both be justified and centered (for partial lines).


### `Placement`

**Namespace:** `Graphics`

Text is aligned to left Text is aligned to center Text is aligned to right Defines how an object is placed in a 2D axis system


### `Tiling`

**Namespace:** `Graphics`

Controls how a direction is tiled


---

## Functions

### `ActivateQuadVertices()`

**Returns:** `void`



### `DrawQuadVertices()`

**Returns:** `void`



### `glDrawArrays(GL_TRIANGLES, 0, 6)`

**Returns:** ``



### `Initialize()`

**Returns:** `void`



### `if(!initialized)`

**Returns:** ``



### `glGenBuffers(1, &quadvbo)`

**Returns:** ``



### `glBindBuffer(GL_ARRAY_BUFFER, quadvbo)`

**Returns:** ``



### `glGenVertexArrays(1, &vaos[ctx])`

**Returns:** ``



### `glBindVertexArray(vaos[ctx])`

**Returns:** ``



### `glEnableVertexAttribArray(0)`

**Returns:** ``



### `for(int i=0;i<sz;i++)`

**Returns:** ``



### `ResizeGL(int Width, int Height)`

**Returns:** `void`



### `glViewport(0, 0, Width, Height)`

**Returns:** ``


*Adjusting Matrices


### `glFrontFace(GL_CCW)`

**Returns:** ``



### `PostRender(os::DeviceHandle hDC, os::WindowHandle win)`

**Returns:** `void`



### `glFlush()`

**Returns:** ``



### `glFinish()`

**Returns:** ``



### `Initialize()`

**Returns:** `void`


Initializes Graphics module, should be performed after an OpenGL context is created. There is a mechanism to ensure initialization is performed once.


### `Tile(bool horizontal, bool vertical)`

**Returns:** `inline Tiling`


Creates a Tiling class from the given horizontal, vertical tiling info.


### `GetHorizontal(Placement placement)`

**Returns:** `inline Alignment`


Placed at top left Placed at top center Placed at top right Placed at middle left Placed at the center Placed at middle right Placed at bottom Placed at bottom center Placed at bottom right Returns horizontal alignment from a placement


### `GetVertical(Placement placement)`

**Returns:** `inline Alignment`


Returns vertical alignment from a placement


### `CalculateOffset(Placement place, Geometry::basic_Size<T_> remainder)`

**Returns:** `Geometry::basic_Point<T_>`


Returns the offset of the object according to the given placement rule when there is the given remainder between object size and the area its being drawn on. Typical usage: `CalculateOffset(Placement::MiddleCenter, areasize - objectsize)`


### `ShrinkFit(Placement place, const Geometry::Size &obj, const Geometry::Size &target)`

**Returns:** `inline Geometry::Rectangle`



### `if(target.Width < obj.Width || target.Height < obj.Height)`

**Returns:** ``



### `ActivateQuadVertices()`

**Returns:** `void`



### `DrawQuadVertices()`

**Returns:** `void`


