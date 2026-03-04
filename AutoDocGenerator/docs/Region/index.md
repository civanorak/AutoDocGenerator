# Region

> Auto-generated documentation for the **Region** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Region`

**Namespace:** `gge`

#### Methods

##### `Region(RegionResource &parent, animation::Timer &controller, bool owner=false)`

**Returns:** ``

##### `Region(RegionResource &parent, bool create=false)`

**Returns:** ``

##### `BorderWidth(—)`

**Returns:** `utils::Margins`

##### `virtual` `SetController(animation::Timer &controller, bool owner=false)`

**Returns:** `virtual void`

##### `virtual` `Progress(—)`

**Returns:** `virtual animation::ProgressResult::Type`

##### `virtual` `drawin(graphics::ImageTarget2D& Target, int X, int Y, int W, int H)`

**Returns:** `virtual void`

##### `virtual` `drawin(graphics::ImageTarget2D& Target, const graphics::SizeController2D &controller, int X, int Y, int W, int H)`

**Returns:** `virtual void`

##### `virtual` `calculatewidth(int w=-1)`

**Returns:** `virtual int`

##### `virtual` `calculateheight(int h=-1)`

**Returns:** `virtual int`

##### `virtual` `calculatewidth(const graphics::SizeController2D &controller, int w=-1)`

**Returns:** `virtual int`

##### `virtual` `calculateheight(const graphics::SizeController2D &controller, int h=-1)`

**Returns:** `virtual int`


### `MaskedRegion`

**Namespace:** `gge`

#### Methods

##### `MaskedRegion(RegionResource &parent, animation::Timer &controller, RegionResource *mask, bool owner=false)`

**Returns:** ``

##### `MaskedRegion(RegionResource &parent, RegionResource *mask, bool create=false)`

**Returns:** ``

##### `virtual` `drawin(graphics::ImageTarget2D& Target, int X, int Y, int W, int H)`

**Returns:** `virtual void`

##### `virtual` `drawin(graphics::ImageTarget2D& Target, const graphics::SizeController2D &controller, int X, int Y, int W, int H)`

**Returns:** `virtual void`


### `TilingInfo`

**Namespace:** `gge`


---

## Functions

### `setregionprovider(vector<Animation *> &anims, RectangularGraphic2DSequenceProvider *&obj, int id)`

**Returns:** `void`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Region_Props)`

**Returns:** `else`



### `EatChunk(Data, size-32)`

**Returns:** ``



### `if(gid==resource::GID::Animation)`

**Returns:** `else`



### `EatChunk(Data, size)`

**Returns:** ``



### `for(auto i=anims.begin()`

**Returns:** ``



### `drawin(Target, X, Y, W, H)`

**Returns:** ``



### `drawin(Target, X, Y, W, H)`

**Returns:** ``



### `GetGID()`

**Returns:** `virtual GID::Type`



### `CreateResizableObject(controller, owner)`

**Returns:** `return`



### `CreateResizableObject(create)`

**Returns:** `return`



### `Region(*this, controller, owner)`

**Returns:** `return *new`



### `MaskedRegion(*this, controller, Mask, owner)`

**Returns:** `return *new`



### `Region(*this, create)`

**Returns:** `return *new`



### `MaskedRegion(*this, Mask, create)`

**Returns:** `return *new`



### `BorderWidth()`

**Returns:** `utils::Margins`



### `GetDuration()`

**Returns:** `virtual int`



### `GetDuration(unsigned Frame)`

**Returns:** `virtual int`



### `GetNumberofFrames()`

**Returns:** `virtual int`



### `FrameAt(unsigned Time)`

**Returns:** `virtual int`



### `StartOf(unsigned Frame)`

**Returns:** `virtual int`



### `EndOf(unsigned Frame)`

**Returns:** `virtual int`



### `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`



### `if(Controller)`

**Returns:** ``


