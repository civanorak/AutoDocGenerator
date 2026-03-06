# Rectangle

&gt; Auto-generated documentation for the **Rectangle** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `basic_Rectangle`

**Namespace:** `Gorgon`

Represents a rectangle in a 2D space. Top left corner and the size is stored.

#### Methods

##### `basic_Rectangle(—)`

**Returns:** ``

Base type of the rectangle elements. Default constructor, does not initialize stored values

##### `basic_Rectangle(const std::string &str)`

**Returns:** `explicit`

Filling constructor using values for top left corner and size Filling constructor using values for top left corner and size Filling constructor using values for top left corner and size Filling constructor using values for top left corner and size Filling constructor using values for top left and bottom right corners Converting constructor from a different typed rectangle Converting constructor from bounds Conversion from string

##### `static` `Parse(std::string s)`

**Returns:** `static basic_Rectangle`

Properly parses a rectangle, throwing errors when necessary.

##### `is(s)`

**Returns:** `std::istringstream`

##### `Right(—)`

**Returns:** `T_`

Conversion to bounds Conversion to string Calculates and returns the rightmost coordinate

##### `Bottom(—)`

**Returns:** `T_`

Calculates and returns the bottommost coordinate

##### `SetRight(const T_ &right)`

**Returns:** `void`

Moves the rectangle by changing its rightmost coordinate

##### `SetBottom(const T_ &bottom)`

**Returns:** `void`

Moves the rectangle by changing its bottommost coordinate

##### `Resize(const T_ &w, const T_ &h)`

**Returns:** `void`

Resizes the rectangle

##### `Resize(const basic_Size<T_> &s)`

**Returns:** `void`

Resizes the rectangle

##### `Move(const basic_Point<T_> &p)`

**Returns:** `void`

Changes the position of the rectangle

##### `Move(const T_ &x, const T_ &y)`

**Returns:** `void`

Changes the position of the rectangle

##### `Center(—)`

**Returns:** `basic_Point<T_>`

Returns the center point of the rectangle

##### `TopLeft(—)`

**Returns:** `basic_Point<T_>`

Returns the top left coordinates of the rectangle

##### `TopRight(—)`

**Returns:** `basic_Point<T_>`

Returns the top right coordinates of the rectangle

##### `BottomLeft(—)`

**Returns:** `basic_Point<T_>`

Returns the bottom left coordinates of the rectangle

##### `BottomRight(—)`

**Returns:** `basic_Point<T_>`

Returns the bottom right coordinates of the rectangle

##### `GetSize(—)`

**Returns:** `basic_Size<T_>`

Returns the size of the rectangle


### `IRectangleProvider`

**Namespace:** `Gorgon`

Interface for RectangleProviders

#### Methods

##### `IRectangleProvider(—)`

**Returns:** ``

##### `virtual` `SetCenterTiling(bool value)`

**Returns:** `virtual void`

Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Creates an animation without controller. This function should always return an animation Sets whether the middle part would be tiled. If set to false it will be stretched to fit the given area. Instances will require redrawing before this change is reflected. This effects both dimensions. Tiling is recommended for all applications.

##### `virtual` `GetCenterTiling(—)`

**Returns:** `virtual bool`

Returns if the middle part will be tiled.

##### `virtual` `SetSideTiling(bool value)`

**Returns:** `virtual void`

Sets whether the side parts (tm, ml, mr, bm) would be tiled. If set to false it will be stretched to fit the given area. Instances will require redrawing before this change is reflected. Tiling is recommended for all applications.

##### `virtual` `GetSideTiling(—)`

**Returns:** `virtual bool`

Returns if the middle part will be tiled.


### `Rectangle`

**Namespace:** `Gorgon`

#### Methods

##### `Rectangle(const IRectangleProvider &prov, Gorgon::Animation::ControllerBase &timer)`

**Returns:** ``

##### `Rectangle(const IRectangleProvider &prov, bool create = true)`

**Returns:** ``


### `basic_RectangleProvider`

**Namespace:** `Gorgon`

#### Methods

##### `if(own)`

**Returns:** ``

Empty constructor, rectangle can be instanced even if it is completely empty Filling constructor Filling constructor using move semantics, rectangle will create and own new objects. The given objects will be moved to these new objects. Filling constructor. The given object will be used for the borders. Center will be empty Filling constructor using move semantics, rectangle will create and own new object. The given object will be moved to this new object. The given object will be used for the borders Filling constructor. The first given object will be used for the borders. The second will be used for the center Filling constructor using move semantics, rectangle will create and own new objects. The given objects will be moved to these new objects. The first object will be used for the borders, the second will be used for center Filling constructor, nullptr is acceptable Move constructor

##### `for(auto ptr : ptrs)`

**Returns:** ``

##### `Rectangle(*this, timer)`

**Returns:** `return *new`

##### `Rectangle(*this, create)`

**Returns:** `return *new`

##### `SetTL(A_ *value)`

**Returns:** `void`

Returns TL provider, may return nullptr. Returns TM provider, may return nullptr. Returns TR provider, may return nullptr. Returns ML provider, may return nullptr. Returns MM provider, may return nullptr. Returns MR provider, may return nullptr. Returns BL provider, may return nullptr. Returns BM provider, may return nullptr. Returns BR provider, may return nullptr. Changes the TL animation, ownership semantics will not change

##### `SetTM(A_ *value)`

**Returns:** `void`

Changes the TM animation, ownership semantics will not change

##### `SetTR(A_ *value)`

**Returns:** `void`

Changes the TR animation, ownership semantics will not change

##### `SetML(A_ *value)`

**Returns:** `void`

Changes the ML animation, ownership semantics will not change

##### `SetMM(A_ *value)`

**Returns:** `void`

Changes the MM animation, ownership semantics will not change

##### `SetMR(A_ *value)`

**Returns:** `void`

Changes the MR animation, ownership semantics will not change

##### `SetBL(A_ *value)`

**Returns:** `void`

Changes the BL animation, ownership semantics will not change

##### `SetBM(A_ *value)`

**Returns:** `void`

Changes the BM animation, ownership semantics will not change

##### `SetBR(A_ *value)`

**Returns:** `void`

Changes the BR animation, ownership semantics will not change

##### `Prepare(—)`

**Returns:** `void`

Prepares all animation providers if the they support Prepare function.

##### `OwnProviders(—)`

**Returns:** `void`

Issuing this function will make this rectangle to own its providers, destroying them along with itself.


### `Rectangle`

**Namespace:** `Gorgon`

#### Methods

##### `Rectangle(Graphics::BitmapRectangleProvider &prov)`

**Returns:** `explicit`

Creates a new rectangle using another rectangle provider

##### `Rectangle(Graphics::AnimatedBitmapRectangleProvider &prov)`

**Returns:** `explicit`

Creates a new rectangle using another rectangle provider

##### `Rectangle(Graphics::RectangleProvider &prov)`

**Returns:** `explicit`

Creates a new rectangle using another rectangle provider

##### `SetProvider(Graphics::BitmapRectangleProvider &value)`

**Returns:** `void`

Creates a new rectangle using another rectangle provider Creates a new rectangle using another rectangle provider Creates a new rectangle using another rectangle provider Creates an empty rectangle Changes provider to the given provider, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::AnimatedBitmapRectangleProvider &value)`

**Returns:** `void`

Changes provider to the given provider, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::RectangleProvider &value)`

**Returns:** `void`

Changes provider to the given provider, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::BitmapRectangleProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::AnimatedBitmapRectangleProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::RectangleProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `RemoveProvider(—)`

**Returns:** `void`

Removes the provider, if it is own by this resource it will be deleted.

##### `static` `SaveThis(Writer &writer, const Graphics::IRectangleProvider &provider)`

**Returns:** `static void`

This function loads a rectangle resource from the file


### `Rectangle`

**Namespace:** `gge`

#### Methods

##### `Rectangle(RectangleResource &parent, animation::Timer &controller, bool owner=false)`

**Returns:** ``

##### `Rectangle(RectangleResource &parent, bool create=false)`

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


### `MaskedRectangle`

**Namespace:** `gge`

#### Methods

##### `MaskedRectangle(RectangleResource &parent, animation::Timer &controller, RectangleResource *mask, bool owner=false)`

**Returns:** ``

##### `MaskedRectangle(RectangleResource &parent, RectangleResource *mask, bool create=false)`

**Returns:** ``

##### `virtual` `drawin(graphics::ImageTarget2D& Target, int X, int Y, int W, int H)`

**Returns:** `virtual void`

##### `virtual` `drawin(graphics::ImageTarget2D& Target, const graphics::SizeController2D &controller, int X, int Y, int W, int H)`

**Returns:** `virtual void`


### `TilingInfo`

**Namespace:** `gge`


---

## Functions

### `IsInside(const basic_Rectangle<T_> &r, const basic_Point<T_> &p)`

**Returns:** `bool`


Compares two rectangles Compares two rectangles Adds a point to this rectangle, effectively translating it Adds a size to this rectangle, resizing it Subtracts a point from this rectangle, effectively translating it Subtracts a size from this rectangle, resizing it Scales this rectangle with the given size. Origin of this operation is top left point of the rectangle. Scales this rectangle with the given size. Origin of this operation is top left point of the rectangle. Scales this rectangle with the given value. Origin of this operation is top left point of the rectangle. Scales this rectangle with the given value. Origin of this operation is top left point of the rectangle. Adds a point to this rectangle, effectively translating it Adds a size to this rectangle, resizing it Subtracts a point to this rectangle, effectively translating it Subtracts a size from this rectangle, resizing it Scales this rectangle with the given size. Origin of this operation is top left point of the rectangle. Scales this rectangle with the given size. Origin of this operation is top left point of the rectangle. Scales this rectangle with the given value. Origin of this operation is top left point of the rectangle. Scales this rectangle with the given value. Origin of this operation is top left point of the rectangle. X coordinate of the top left corner of this rectangle Y coordinate of the top left corner of this rectangle Width of the rectangle Height of the rectangle Allows streaming of Rectangle Allows reading a rectangle from a stream TODO requires more work Checks whether a given point is inside the given rectangle.


### `if(r.Height < maxt+maxb)`

**Returns:** ``



### `drawin(target, newr, color)`

**Returns:** ``



### `draw(target, p1, p2, p3, p4, color)`

**Returns:** ``



### `SliceHorizontal(const Bitmap &source, int t, int b, int tl, int tr, int l, int r, int bl, int br)`

**Returns:** `BitmapRectangleProvider`



### `SliceVertical(const Bitmap &source, int l, int r, int tl, int bl, int t, int b, int tr, int br)`

**Returns:** `BitmapRectangleProvider`



### `SliceHorizontal(const Bitmap &source, int t, int b, int tl, int tr, int l, int r, int bl, int br)`

**Returns:** `BitmapRectangleProvider`


Horizontally slices the given image. t and b slices the image to 3 parts then each part is further sliced by X offset pairs (tl, tr), (l, r), and (bl, br). Currently this works only with bitmaps. This function will create an atlas out of the given image, thus, the source should be kept alive. Currently atlas functionality does not work.


### `SliceVertical(const Bitmap &source, int l, int r, int tl, int bl, int t, int b, int tr, int br)`

**Returns:** `BitmapRectangleProvider`


Vertically slices the given image. l and r slices the image to 3 parts then each part is further sliced by Y offset pairs (tl, bl), (t, b), and (tr, br). Currently this works only with bitmaps. This function will create an atlas out of the given image, thus, the source should be kept alive. Currently atlas functionality does not work.


### `Slice(const Bitmap &source, Geometry::Bounds center)`

**Returns:** `inline BitmapRectangleProvider`


Slices an image to create a rectangle. Imagine a pound sign (#) slicing the image, center parameter is the central region of the pound sign. Currently this works only with bitmaps. This function will create an atlas out of the given image, thus, the source should be kept alive. Currently atlas functionality does not work.


### `SliceHorizontal(source, center.Top, center.Bottom, center.Left, center.Right, center.Left, center.Right, center.Left, center.Right)`

**Returns:** `return`



### `while(!target)`

**Returns:** ``



### `if(gid == GID::Rectangle_Props)`

**Returns:** ``



### `if(gid == GID::Rectangle_Props_II)`

**Returns:** `else`



### `if(resource)`

**Returns:** ``



### `if(++c > 9)`

**Returns:** ``



### `if(type == anim)`

**Returns:** ``



### `if(type == img)`

**Returns:** `else`



### `if(type == mixed)`

**Returns:** `else`



### `if(type != unknown)`

**Returns:** ``



### `savethis(Writer &writer, const Graphics::basic_RectangleProvider<T_> &provider)`

**Returns:** `static void`



### `if(tm && ml && mr && bm && !tl && !tr && !bl && !br)`

**Returns:** ``



### `SaveAnimation(writer, tm)`

**Returns:** ``



### `SaveAnimation(writer, ml)`

**Returns:** ``



### `SaveAnimation(writer, mm)`

**Returns:** ``



### `SaveAnimation(writer, mr)`

**Returns:** ``



### `SaveAnimation(writer, bm)`

**Returns:** ``



### `if(tm && ml && mr && bm && tl && tr && bl && br)`

**Returns:** `else`



### `SaveAnimation(writer, tl)`

**Returns:** ``



### `SaveAnimation(writer, tm)`

**Returns:** ``



### `SaveAnimation(writer, tr)`

**Returns:** ``



### `SaveAnimation(writer, ml)`

**Returns:** ``



### `SaveAnimation(writer, mm)`

**Returns:** ``



### `SaveAnimation(writer, mr)`

**Returns:** ``



### `SaveAnimation(writer, bl)`

**Returns:** ``



### `SaveAnimation(writer, bm)`

**Returns:** ``



### `SaveAnimation(writer, br)`

**Returns:** ``



### `if(!tr && !tm && !tr && !ml && !mr && !bl && !bm && !br)`

**Returns:** `else`



### `SaveAnimation(writer, mm)`

**Returns:** ``



### `SaveAnimation(writer, tl)`

**Returns:** ``



### `SaveAnimation(writer, tm)`

**Returns:** ``



### `SaveAnimation(writer, tr)`

**Returns:** ``



### `SaveAnimation(writer, ml)`

**Returns:** ``



### `SaveAnimation(writer, mm)`

**Returns:** ``



### `SaveAnimation(writer, mr)`

**Returns:** ``



### `SaveAnimation(writer, bl)`

**Returns:** ``



### `SaveAnimation(writer, bm)`

**Returns:** ``



### `SaveAnimation(writer, br)`

**Returns:** ``



### `if(prov != nullptr)`

**Returns:** `else`



### `setthis(F_, Graphics::basic_RectangleProvider<T_> *, T_ *)`

**Returns:** `static void`



### `setthis(F_ f, Graphics::BitmapRectangleProvider *provider, Graphics::Bitmap *o)`

**Returns:** `static void`



### `CallBitmapAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::AnimatedBitmapRectangleProvider *provider, Graphics::BitmapAnimationProvider *o)`

**Returns:** `static void`



### `CallBitmapAnimationAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::RectangleProvider *provider, Graphics::RectangularAnimationProvider *o)`

**Returns:** `static void`



### `CallGenericAnimationSetter(f, provider, o)`

**Returns:** ``



### `moveout(Graphics::basic_RectangleProvider<T_> *provider, Graphics::IRectangleProvider *&p)`

**Returns:** `static void`



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetTL, bp, tl)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetTM, bp, tm)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetTR, bp, tr)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetML, bp, ml)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetMM, bp, mm)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetMR, bp, mr)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetBL, bp, bl)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetBM, bp, bm)`

**Returns:** ``



### `setthis(&Graphics::basic_RectangleProvider<T_>::SetBR, bp, br)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``



### `setrectangleprovider(vector<Animation *> &anims, RectangularGraphic2DSequenceProvider *&obj, int id)`

**Returns:** `void`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Rectangle_Props)`

**Returns:** `else`



### `EatChunk(Data, size-32)`

**Returns:** ``



### `if(gid==resource::GID::Animation)`

**Returns:** `else`



### `EatChunk(Data, size)`

**Returns:** ``



### `for(auto i=anims.begin()`

**Returns:** ``



### `if(Mask->c)`

**Returns:** ``



### `drawin(Target, X, Y, W, H)`

**Returns:** ``



### `GetGID()`

**Returns:** `virtual GID::Type`



### `CreateResizableObject(controller, owner)`

**Returns:** `return`



### `CreateResizableObject(create)`

**Returns:** `return`



### `Rectangle(*this, controller, owner)`

**Returns:** `return *new`



### `MaskedRectangle(*this, controller, Mask, owner)`

**Returns:** `return *new`



### `Rectangle(*this, create)`

**Returns:** `return *new`



### `MaskedRectangle(*this, Mask, create)`

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


