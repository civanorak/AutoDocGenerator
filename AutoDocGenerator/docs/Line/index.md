# Line

&gt; Auto-generated documentation for the **Line** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `StrokeSettings`

**Namespace:** `Gorgon`


### `Line`

**Namespace:** `Gorgon`

#### Methods

##### `Slope(—)`

**Returns:** `Float`

Empty constructor Returns the slope of the line. Assumes the line is 2D.

##### `Offset(—)`

**Returns:** `Float`

Returns the offset of the line. Assumes the line is 2D.

##### `SlopeInv(—)`

**Returns:** `Float`

Returns the inverse slope of the line, where the line formula is now x = a * y + b

##### `OffsetInv(—)`

**Returns:** `Float`

Returns the inverse offset of the line, where the line formula is now x = a * y + b

##### `MinY(—)`

**Returns:** `typename P_::BaseType`

Returns minimum Y point

##### `MaxY(—)`

**Returns:** `typename P_::BaseType`

Returns maximum Y point

##### `MinX(—)`

**Returns:** `typename P_::BaseType`

Returns minimum X point

##### `MaxX(—)`

**Returns:** `typename P_::BaseType`

Returns maximum X point

##### `PointAtMinY(—)`

**Returns:** `P_`

Returns minimum Y point

##### `PointAtMaxY(—)`

**Returns:** `P_`

Returns maximum Y point

##### `PointAtMinX(—)`

**Returns:** `P_`

Returns minimum X point

##### `PointAtMaxX(—)`

**Returns:** `P_`

Returns maximum X point

##### `XatY(typename P_::BaseType y)`

**Returns:** `typename P_::BaseType`

Returns the X value at a given Y coordinate. This function does not check if Y is in range and may give invalid values if it doesn't.

##### `YatX(typename P_::BaseType x)`

**Returns:** `typename P_::BaseType`

Returns the Y value at a given X coordinate. This function does not check if X is in range and may give invalid values if it doesn't.

##### `YDirection(—)`

**Returns:** `int`

Returns whether the line is moving up or down. Up movement is -1 down movement is 1 and if line is horizontal this function will return 0

##### `Sign(End.Y - Start.Y)`

**Returns:** `return`

##### `XDirection(—)`

**Returns:** `int`

Returns whether the line is moving left or right. Left movement is -1 right movement is 1 and if line is vertical this function will return 0

##### `Sign(End.X - Start.X)`

**Returns:** `return`

##### `Length(—)`

**Returns:** `Float`

Returns the length of the line

##### `Distance(const P_ &target)`

**Returns:** `Float`

Returns the distance from the target point to the line

##### `sqrt(dx*dx + dy*dy)`

**Returns:** ``

##### `DistanceSquare(const P_ &target)`

**Returns:** `Float`

Returns the squared distance from the target point to the line. This can be calculated faster than the regular distance.


### `ILineProvider`

**Namespace:** `Gorgon`

Interface for LineProviders

#### Methods

##### `virtual` `SetOrientation(Orientation value)`

**Returns:** `virtual void`

Creates a start animation without controller. This function should always return an animation Creates a start animation without controller. This function should always return an animation Creates a start animation without controller. This function should always return an animation Changes the orientation of the provider. Instances will require redrawing before this change is reflected.

##### `virtual` `GetOrientation(—)`

**Returns:** `virtual Orientation`

Returns the orientation of the line provider

##### `virtual` `SetTiling(bool value)`

**Returns:** `virtual void`

Sets whether the middle part would be tiled. If set to false it will be stretched to fit the given area. Instances will require redrawing before this change is reflected. Tiling is recommended for all applications.

##### `virtual` `GetTiling(—)`

**Returns:** `virtual bool`

Returns if the middle part will be tiled.


### `Line`

**Namespace:** `Gorgon`

#### Methods

##### `Line(const ILineProvider &prov, Gorgon::Animation::ControllerBase &timer)`

**Returns:** ``

##### `Line(const ILineProvider &prov, bool create = true)`

**Returns:** ``

##### `getfixedsize(—)`

**Returns:** `int`

Returns the largest size in the non-scalable direction


### `basic_LineProvider`

**Namespace:** `Gorgon`

#### Methods

##### `if(own)`

**Returns:** ``

Empty constructor, line can be instanced even if it is completely empty Filling constructor Filling constructor. This variant will move in the animations, freeing them with this item. Filling constructor, nullptr is acceptable, however, it is not advised to use only one side, that is a waste of resources, a regular image can also be tiled or stretched to fit to an area. Move constructor

##### `Line(*this, timer)`

**Returns:** `return *new`

##### `Line(*this, create)`

**Returns:** `return *new`

##### `SetStart(A_ *value)`

**Returns:** `void`

Returns the start animation, might return nullptr Returns the middle animation, might return nullptr Returns the end animation, might return nullptr Changes the start animation, ownership semantics will not change

##### `SetMiddle(A_ *value)`

**Returns:** `void`

Changes the middle animation, ownership semantics will not change

##### `SetEnd(A_ *value)`

**Returns:** `void`

Changes the end animation, ownership semantics will not change

##### `Prepare(—)`

**Returns:** `void`

Prepares all animation providers if the they support Prepare function.

##### `OwnProviders(—)`

**Returns:** `void`

Issuing this function will make this line to own its providers destroying them along with itself

##### `ReleaseProviders(—)`

**Returns:** `void`

Issuing this function will make this line to disown its providers and set them to nullptr

##### `if(start)`

**Returns:** ``

##### `if(middle)`

**Returns:** ``

##### `if(end)`

**Returns:** ``

##### `if(start)`

**Returns:** ``

##### `if(middle)`

**Returns:** ``

##### `if(end)`

**Returns:** ``


### `Line`

**Namespace:** `Gorgon`

#### Methods

##### `Line(Graphics::BitmapLineProvider &prov)`

**Returns:** `explicit`

Creates a new line using another line provider.

##### `Line(Graphics::AnimatedBitmapLineProvider &prov)`

**Returns:** `explicit`

Creates a new line using another line provider.

##### `Line(Graphics::LineProvider &prov)`

**Returns:** `explicit`

Creates a new line using another line provider.

##### `SetProvider(Graphics::BitmapLineProvider &value)`

**Returns:** `void`

Creates a new line using another line provider. Creates a new line using another line provider. Creates a new line using another line provider. Creates a new empty line Changes the provider stored in this line, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::AnimatedBitmapLineProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `SetProvider(Graphics::LineProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will not be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::BitmapLineProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::AnimatedBitmapLineProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `AssumeProvider(Graphics::LineProvider &value)`

**Returns:** `void`

Changes the provider stored in this line, ownership will be transferred

##### `RemoveProvider(—)`

**Returns:** ``

##### `RemoveProvider(—)`

**Returns:** `void`

Removes the provider, if it is owned by this resource it will be deleted.

##### `static` `SaveThis(Writer &writer, const Graphics::ILineProvider &provider)`

**Returns:** `static void`

This function loads a line resource from the file


### `Line`

**Namespace:** `gge`

#### Methods

##### `Line(LineResource &parent, animation::Timer &controller, bool owner=false)`

**Returns:** ``

##### `Line(LineResource &parent, bool create=false)`

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


### `MaskedLine`

**Namespace:** `gge`

#### Methods

##### `MaskedLine(LineResource &parent, animation::Timer &controller, LineResource *mask, bool owner=false)`

**Returns:** ``

##### `MaskedLine(LineResource &parent, LineResource *mask, bool create=false)`

**Returns:** ``

##### `virtual` `drawin(graphics::ImageTarget2D& Target, int X, int Y, int W, int H)`

**Returns:** `virtual void`

##### `virtual` `drawin(graphics::ImageTarget2D& Target, const graphics::SizeController2D &controller, int X, int Y, int W, int H)`

**Returns:** `virtual void`


---

## Enums

### `OrientationType`

**Namespace:** `gge`


---

## Functions

### `LinesToPolygons(const Geometry::PointList<P_> &p, StrokeSettings settings = 1.0)`

**Returns:** `std::vector<Geometry::PointList<P_>>`



### `if(dotp > 0)`

**Returns:** ``



### `if(dotp != 0)`

**Returns:** `else`



### `if(dotp < 0)`

**Returns:** ``



### `if(dotp != 0)`

**Returns:** `else`



### `if(dotp > 0)`

**Returns:** ``



### `if(dotp != 0)`

**Returns:** `else`



### `if(dotp < 0)`

**Returns:** ``



### `if(dotp != 0)`

**Returns:** `else`



### `for(auto it=points[1].rbegin()`

**Returns:** ``



### `DrawLines(Containers::Image &target, const Geometry::PointList<P_> &p, StrokeSettings settings = 1.0, F_ stroke = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `DrawLines(Graphics::Bitmap &target, const Geometry::PointList<P_> &p, StrokeSettings settings = 1.0, F_ stroke = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `DrawLines(Containers::Image &target, const std::vector<Geometry::PointList<P_>> &pnts, StrokeSettings settings = 1.0, F_ stroke = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `for(auto &p : pnts)`

**Returns:** ``



### `for(auto &p : np)`

**Returns:** ``



### `DrawLines(Graphics::Bitmap &target, const std::vector<Geometry::PointList<P_>> &pnts, StrokeSettings settings = 1.0, F_ stroke = SolidFill<>{Graphics::Color::Black})`

**Returns:** `void`



### `for(auto &p : pnts)`

**Returns:** ``



### `draw(target, p1, p2, p3, p4, color)`

**Returns:** ``



### `while(!target)`

**Returns:** ``



### `if(gid == GID::Line_Props)`

**Returns:** ``



### `if(gid == GID::Line_Props_II)`

**Returns:** `else`



### `if(resource)`

**Returns:** ``



### `if(++c > 3)`

**Returns:** ``



### `if(type == anim)`

**Returns:** ``



### `if(type == img)`

**Returns:** `else`



### `if(type == mixed)`

**Returns:** `else`



### `savethis(Writer &writer, const Graphics::basic_LineProvider<T_> &provider)`

**Returns:** `static void`



### `if(s && e)`

**Returns:** ``



### `SaveAnimation(writer, s)`

**Returns:** ``



### `SaveAnimation(writer, m)`

**Returns:** ``



### `SaveAnimation(writer, e)`

**Returns:** ``



### `if(!s && !e)`

**Returns:** `else`



### `SaveAnimation(writer, m)`

**Returns:** ``



### `SaveAnimation(writer, s)`

**Returns:** ``



### `SaveAnimation(writer, m)`

**Returns:** ``



### `SaveAnimation(writer, e)`

**Returns:** ``



### `if(prov != nullptr)`

**Returns:** `else`



### `setthis(F_ f, Graphics::basic_LineProvider<T_> *provider, T_ *o)`

**Returns:** `static void`



### `setthis(F_ f, Graphics::BitmapLineProvider *provider, Graphics::Bitmap *o)`

**Returns:** `static void`



### `CallBitmapAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::AnimatedBitmapLineProvider *provider, Graphics::BitmapAnimationProvider *o)`

**Returns:** `static void`



### `CallBitmapAnimationAnimationSetter(f, provider, o)`

**Returns:** ``



### `setthis(F_ f, Graphics::LineProvider *provider, Graphics::RectangularAnimationProvider *o)`

**Returns:** `static void`



### `CallGenericAnimationSetter(f, provider, o)`

**Returns:** ``



### `moveout(Graphics::basic_LineProvider<T_> *provider, Graphics::ILineProvider *&p)`

**Returns:** `static void`



### `setthis(&Graphics::basic_LineProvider<T_>::SetStart, bp, s)`

**Returns:** ``



### `setthis(&Graphics::basic_LineProvider<T_>::SetMiddle, bp, m)`

**Returns:** ``



### `setthis(&Graphics::basic_LineProvider<T_>::SetEnd, bp, e)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `moveout(provider, p)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``



### `setlineprovider(vector<Animation *> &anims, RectangularGraphic2DSequenceProvider *&obj, int id)`

**Returns:** `void`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Line_Props)`

**Returns:** `else`



### `EatChunk(Data, size-16)`

**Returns:** ``



### `if(gid==resource::GID::Animation)`

**Returns:** `else`



### `EatChunk(Data, size)`

**Returns:** ``



### `for(auto i=anims.begin()`

**Returns:** ``



### `if(parent.Orientation==LineResource::Horizontal)`

**Returns:** ``



### `if(parent.Orientation==LineResource::Horizontal)`

**Returns:** ``



### `if(parent.Orientation==LineResource::Horizontal)`

**Returns:** ``



### `if(parent.Orientation==LineResource::Horizontal)`

**Returns:** ``



### `if(parent.Orientation==LineResource::Horizontal)`

**Returns:** ``



### `GetGID()`

**Returns:** `virtual GID::Type`



### `Line(*this, controller, owner)`

**Returns:** `return *new`



### `MaskedLine(*this, controller, Mask, owner)`

**Returns:** `return *new`



### `Line(*this, create)`

**Returns:** `return *new`



### `MaskedLine(*this, Mask, create)`

**Returns:** `return *new`



### `IsVertical()`

**Returns:** `bool`



### `IsHorizontal()`

**Returns:** `bool`



### `SetStart(animation::RectangularGraphic2DSequenceProvider &val)`

**Returns:** `void`



### `SetLoop(animation::RectangularGraphic2DSequenceProvider &val)`

**Returns:** `void`



### `SetEnd(animation::RectangularGraphic2DSequenceProvider &val)`

**Returns:** `void`



### `SetSources(animation::RectangularGraphic2DSequenceProvider &Start, animation::RectangularGraphic2DSequenceProvider &Loop, animation::RectangularGraphic2DSequenceProvider &End)`

**Returns:** `virtual void`



### `SetMask(LineResource *mask)`

**Returns:** `virtual void`



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


