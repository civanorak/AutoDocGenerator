# Layer

> Auto-generated documentation for the **Layer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Surface`

**Namespace:** `internal`

This class represents a drawable surface.

#### Methods

##### `Surface(Surface &&s)`

**Returns:** ``

##### `IsSet(—)`

**Returns:** `bool`

Sets the source to the given source. This variant uses texture coordinates given by the source. Uses fill shader to fill an area with solid color. Sets the source to the given source. This variant uses supplied texture coordinates. If the source is set.

##### `TextureID(—)`

**Returns:** `GL::Texture`

Returns the GL texture to be drawn

##### `GetVertices(const Geometry::Transform3D &transform)`

**Returns:** `GL::QuadVertices`

Returns the transformed vertex coordinates

##### `GetTextureCoords(—)`

**Returns:** `GL::QuadTextureCoords`

Returns the texture coordinates of this surface

##### `IsPartial(—)`

**Returns:** `bool`

##### `GetMode(—)`

**Returns:** `ColorMode`

Returns the color mode of the texture

##### `GetColor(—)`

**Returns:** `RGBAf`

Returns the tint color for this surface

##### `GetDrawMode(—)`

**Returns:** `TextureTarget::DrawMode`

##### `SetDrawMode(TextureTarget::DrawMode value)`

**Returns:** `void`


### `Layer`

**Namespace:** `internal`

@endcond


### `Operation`

**Namespace:** `internal`


### `Layer`

**Namespace:** `Gorgon`

#### Methods

##### `ResetHitCheck(—)`

**Returns:** `void`

@name Mouse event handling @{ Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Removes hit check handler, default action for hit check is to return true.

##### `GetClick(—)`

**Returns:** `auto`

Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets click handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function.

##### `ResetClick(—)`

**Returns:** `void`

Removes click handler

##### `ResetDown(—)`

**Returns:** `void`

Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Sets mouse down handler. If hit check function is set, this event is only called if hit check returns true. This variant accepts class member function. Removes mouse down handler

##### `ResetUp(—)`

**Returns:** `void`

Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Sets mouse up handler. If hit check function is set, this event is only called if hit check returns true and mouse down is also handled. This variant accepts class member function. Removes mouse up handler

##### `ResetMove(—)`

**Returns:** `void`

Sets mouse move handler. This function will be called every frame when the mouse is over the layer, even if the mouse does not move. Sets mouse move handler. This function will be called every frame when the mouse is over the layer, even if the mouse does not move. Sets mouse move handler. This function will be called every frame when the mouse is over the layer, even if the mouse does not move. Sets mouse move handler. This function will be called every frame when the mouse is over the layer, even if the mouse does not move. Sets mouse move handler. This function will be called every frame when the mouse is over the layer, even if the mouse does not move. Sets mouse move handler. This function will be called every frame when the mouse is over the layer, even if the mouse does not move. Removes mouse move handler

##### `ResetScroll(—)`

**Returns:** `void`

Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Sets scroll handler. Scrolling down will give negative number while scrolling up will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Removes scroll handler

##### `ResetHScroll(—)`

**Returns:** `void`

Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Sets horizontal scroll handler. Scrolling right will give negative number while scrolling left will give a positive number. 1 means one full scroll. If the device supports smooth scrolling, partial values can be obtained. Not all devices support horizontal scrolling. Removes horizontal scroll handler

##### `ResetZoom(—)`

**Returns:** `void`

Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Sets zoom handler. Zoom amount is calculated as a ratio. 2 means, 2x zoom should be performed. Not all devices support zoom gesture. Removes zoom handler

##### `ResetRotate(—)`

**Returns:** `void`

Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Sets rotate handler. Rotate amount is given in radians. Positive values should rotate counter clockwise. Not all devices support rotation gesture. Removes rotate handler.

##### `ResetOver(—)`

**Returns:** `void`

Sets mouse over handler. Mouse over occurs for parent layers of a layer as well. However, If two siblings overlap, only one will receive it. Sets mouse over handler. Mouse over occurs for parent layers of a layer as well. However, If two siblings overlap, only one will receive it. Sets mouse over handler. Mouse over occurs for parent layers of a layer as well. However, If two siblings overlap, only one will receive it. Sets mouse over handler. Mouse over occurs for parent layers of a layer as well. However, If two siblings overlap, only one will receive it. Sets mouse over handler. Mouse over occurs for parent layers of a layer as well. However, If two siblings overlap, only one will receive it. Sets mouse over handler. Mouse over occurs for parent layers of a layer as well. However, If two siblings overlap, only one will receive it. Removes mouse over handler

##### `ResetOut(—)`

**Returns:** `void`

Sets mouse out handler. Sets mouse out handler. Sets mouse out handler. Sets mouse out handler. Sets mouse out handler. Sets mouse out handler. Removes mouse out handler

##### `FireClick(Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`

Fires the click event manually, allowing both mouse up and click events to happen at the same time.

##### `click(*this, location, button)`

**Returns:** ``


### `MouseHandler`

**Namespace:** `Gorgon`

#### Methods

##### `MouseHandler(MouseHandler &&other)`

**Returns:** ``

##### `MouseHandler(Layer *layer = nullptr)`

**Returns:** `explicit`

##### `bool(—)`

**Returns:** `operator`

##### `Clear(—)`

**Returns:** `void`

##### `Add(Layer *l)`

**Returns:** `void`

##### `Swap(MouseHandler &other)`

**Returns:** `void`


### `Layer`

**Namespace:** `Gorgon`

#### Methods

##### `Swap(other)`

**Returns:** ``

Initializing constructor Constructor that sets the layer to cover entire parent, no matter how big it is. The location of the layer is set to be the origin Constructor that places the layer to the given location Copy constructor is disabled. Move constructor

##### `Swap(Layer &other)`

**Returns:** `void`

Copy assignment is deleted Move assignment Destructor Swaps two layers, mostly used for move semantics

##### `virtual` `Add(Layer &layer)`

**Returns:** `virtual void`

@name Children related functions @{ These functions deals with child layers. Adds the given layer as a child. Notice that the newly added layer is drawn on top of others.

##### `Add(Layer *layer)`

**Returns:** `void`

Adds the given layer as a child. Notice that the newly added layer is drawn on top of others.

##### `Add(*layer)`

**Returns:** ``

##### `setname(std::string value)`

**Returns:** `void`

For debugging

##### `virtual` `Insert(Layer &layer, long under)`

**Returns:** `virtual void`

Inserts the given layer before the given index. The newly inserted layer will be drawn *under* the layer in the given index

##### `Insert(Layer *layer, long under)`

**Returns:** `void`

Inserts the given layer before the given index. The newly inserted layer will be drawn *under* the layer in the given index

##### `Insert(*layer, under)`

**Returns:** ``

##### `virtual` `Remove(Layer &layer)`

**Returns:** `virtual void`

Removes the given layer

##### `removed(layer)`

**Returns:** ``

##### `Remove(Layer *layer)`

**Returns:** `void`

Removes the given layer

##### `Remove(*layer)`

**Returns:** ``

##### `virtual` `HasParent(—)`

**Returns:** `virtual bool`

Returns whether this layer has a parent

##### `virtual` `TranslateToTopLevel(Geometry::Point location = {0, 0})`

**Returns:** `virtual Geometry::Point`

Returns the parent of this layer. Throws if no parent is set. Use HasParent to make sure this layer has a parent @throw std::runtime_error if no parent is set Returns the top level layer that contains this layer. Returns the top level layer that contains this layer. Translates the given location to the top level

##### `begin(—)`

**Returns:** `Containers::Collection<Layer>::ConstIterator`

@} @name Iterator related functions @{ These functions return an iterator that allows children to be iterated. An iterator pointing to the start of the children

##### `end(—)`

**Returns:** `Containers::Collection<Layer>::ConstIterator`

An iterator pointing to the end of the children

##### `First(—)`

**Returns:** `Containers::Collection<Layer>::ConstIterator`

An iterator pointing to the start of the children

##### `Last(—)`

**Returns:** `Containers::Collection<Layer>::ConstIterator`

An iterator pointing to the last item of the children

##### `PlaceBefore(int before)`

**Returns:** `void`

@} @name Ordering functions @{ This layer should be a in another layer for these methods to work. Places this layer before the given index. This layer will be drawn above the given index.

##### `if(parent)`

**Returns:** ``

##### `PlaceToTop(—)`

**Returns:** `void`

Places this layer to the top of the layer stack its in. This makes sure that its not being covered by other layers apart from its own children

##### `PlaceToBottom(—)`

**Returns:** `void`

Places this layer to the bottom of the layer stack.

##### `GetOrder(—)`

**Returns:** `int`

Gets the current order of the stack. 0 means the layer is the bottommost layer in the stack

##### `virtual` `Move(const Geometry::Point &location)`

**Returns:** `virtual void`

@} @name Geometry related functions @{ These functions modify or return the boundaries of this layer Moves this layer to the given location

##### `virtual` `Move(int x, int y)`

**Returns:** `virtual void`

Moves this layer to the given location

##### `virtual` `Resize(const Geometry::Size &size)`

**Returns:** `virtual void`

Resizes the layer to the given size

##### `Resize(int width, int height)`

**Returns:** `void`

Resizes the layer to the given size

##### `Resize({width, height})`

**Returns:** ``

##### `SetWidth(int width)`

**Returns:** `void`

Resizes the layer to the given size

##### `SetHeight(int height)`

**Returns:** `void`

Resizes the layer to the given size

##### `virtual` `SetBounds(const Geometry::Bounds &bounds)`

**Returns:** `virtual void`

Sets the boundaries of this layer.

##### `GetSize(—)`

**Returns:** `Geometry::Size`

Returns the size of the layer

##### `GetCalculatedSize(—)`

**Returns:** `Geometry::Size`

Returns the size of the layer. If any dimension size is 0, it means the layer will span its parent, this function will perform necessary calculation to get parent size.

##### `GetWidth(—)`

**Returns:** `int`

Returns the width of the layer

##### `GetHeight(—)`

**Returns:** `int`

Returns the height of the layer

##### `GetLocation(—)`

**Returns:** `Geometry::Point`

Returns the current location of the layer

##### `GetLeft(—)`

**Returns:** `int`

Returns the current location of the layer

##### `GetTop(—)`

**Returns:** `int`

Returns the current location of the layer

##### `virtual` `GetBounds(—)`

**Returns:** `virtual Geometry::Bounds`

Returns the boundaries of the layer

##### `GetEffectiveBounds(—)`

**Returns:** `Geometry::Bounds`

Returns the effective boundaries of the layer

##### `virtual` `Show(—)`

**Returns:** `virtual void`

@} Displays this layer

##### `virtual` `Hide(—)`

**Returns:** `virtual void`

Hides this layer

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

Returns whether this layer is effectively visible

##### `virtual` `propagate_mouseevent(Input::Mouse::EventType evet, Geometry::Point location, Input::Mouse::Button button, float amount, MouseHandler &handlers)`

**Returns:** `virtual bool`

Propagates a mouse event. Some events will be called directly. Do not use this function. Direct calls should never touch handlers. Input layers should cache perform transformations on direct calls. Direct calls should not be clipped. button is set only for Click/Down/Up events, amount will be set for Scroll/Zoom events. Mouse event system is not thread safe.

##### `virtual` `Render(—)`

**Returns:** `virtual void`

Renders the current layer, default handling is to pass the request to the sub-layers. Rendering is not thread safe.

##### `virtual` `added(Layer &layer)`

**Returns:** `virtual void`

Sub-layers that this layer holds, all the sub-layers are considered to be above current layer When used as layer bounds, represents the entire region its placed in. Will be called when a layer is added. This function will even be called when the given layer was already in the children.

##### `virtual` `removed(Layer &layer)`

**Returns:** `virtual void`

Will be called when a layer is removed. This function will be called even if the given layer is not a child of this layer.

##### `virtual` `located(Layer *parent)`

**Returns:** `virtual void`

Will be called when this layer is added to another.

##### `dotransformandclip(bool inverse = false)`

**Returns:** `void`

Performs transformation and clipping. Use inverse for reverse mapping for mouse events

##### `reverttransformandclip(—)`

**Returns:** `void`

Reverts previously done transformation


---

## Functions

### `if(tiling==Tiling::None)`

**Returns:** ``



### `if(tiling == Tiling::Both)`

**Returns:** ``



### `if(tiling == Tiling::Horizontal)`

**Returns:** `else`



### `dotransformandclip()`

**Returns:** ``



### `if(clippingenabled)`

**Returns:** ``



### `glEnable(GL_SCISSOR_TEST)`

**Returns:** ``



### `glScissor(cliprectangle.X, cliprectangle.Y, cliprectangle.Width, cliprectangle.Height)`

**Returns:** ``



### `ActivateQuadVertices()`

**Returns:** ``



### `for(auto &surface : surfaces)`

**Returns:** ``



### `while(ind == nextopind)`

**Returns:** ``



### `switch(nextop->type)`

**Returns:** ``



### `glClearColor(1.0f, 0, 0, 0)`

**Returns:** ``



### `glBlendFuncSeparate(GL_DST_COLOR, GL_ZERO, GL_ONE, GL_ZERO)`

**Returns:** ``



### `DrawQuadVertices()`

**Returns:** ``



### `if(current == ToMask)`

**Returns:** ``



### `for(auto &l : children)`

**Returns:** ``



### `if(clippingenabled)`

**Returns:** ``



### `glDisable(GL_SCISSOR_TEST)`

**Returns:** ``



### `glScissor(cliprectangle.X, cliprectangle.Y, cliprectangle.Width, cliprectangle.Height)`

**Returns:** ``



### `reverttransformandclip()`

**Returns:** ``



### `Initialize()`

**Returns:** `friend void`



### `Layer(Layer &&other)`

**Returns:** ``


Initializing constructor Constructor that sets the layer to cover entire parent, no matter how big it is. The location of the layer is set to be the origin Constructor that places the layer to the given location Copy constructor is disabled. Move constructor


### `Swap(other)`

**Returns:** ``



### `Swap(Layer &other)`

**Returns:** `void`



### `swap(bounds, other.bounds)`

**Returns:** ``



### `swap(isvisible, other.isvisible)`

**Returns:** ``



### `swap(children, other.children)`

**Returns:** ``



### `swap(color, other.color)`

**Returns:** ``



### `swap(tint, other.tint)`

**Returns:** ``



### `swap(mode, other.mode)`

**Returns:** ``



### `swap(surfaces, other.surfaces)`

**Returns:** ``



### `if(myparent)`

**Returns:** ``



### `if(otherparent)`

**Returns:** ``



### `if(myparent)`

**Returns:** ``



### `if(otherparent)`

**Returns:** ``



### `SetTintColor(RGBAf value)`

**Returns:** `virtual void`


Prefer using Draw functions of image or animations Prefer using Draw functions of image or animations Prefer using Draw functions of image or animations Prefer using Draw functions of image or animations Render this layer to the GL. This function is used internally and not necessary to be called Get current drawing mode. See Layer page to see available drawing modes Change current drawing mode. See Layer page to see available drawing modes Queues the start of a new mask. Only one mask buffer exists and it will be cleared and reused. Changes the tint color of the layer, every image pixel will be multiplied by this color


### `GetTintColor()`

**Returns:** `virtual RGBAf`


Returns the tint color of the layer, every image pixel will be multiplied by this color


### `SetColor(RGBAf value)`

**Returns:** `virtual void`


Changes the tint color of the layer, every image pixel will be multiplied by this color. This value effects only the images drawn after it is set.


### `GetColor()`

**Returns:** `virtual RGBAf`


Changes the tint color of the layer, every image pixel will be multiplied by this color


### `EnableClipping()`

**Returns:** `void`


Enables graphics clipping from the visible borders of the layer


### `DisableClipping()`

**Returns:** `void`


Disables graphics clipping


### `IsClippingEnabled()`

**Returns:** `bool`


Returns if the clipping is enabled


### `needsclip(Input::Mouse::EventType event)`

**Returns:** `bool`



### `switch(event)`

**Returns:** ``



### `needsforward(Input::Mouse::EventType event)`

**Returns:** `bool`



### `switch(event)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::HitCheck)`

**Returns:** ``



### `dotransformandclip(true)`

**Returns:** ``



### `reverttransformandclip()`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Over)`

**Returns:** ``



### `over(*this)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Out)`

**Returns:** `else`



### `out(*this)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Up)`

**Returns:** `else`



### `up(*this, curlocation, button)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::MovePressed)`

**Returns:** `else`



### `move(*this, curlocation)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::DownPressed)`

**Returns:** `else`



### `if(down)`

**Returns:** ``



### `down(*this, curlocation, button)`

**Returns:** ``



### `if(down || click || up)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::HitCheck)`

**Returns:** `else`



### `if(event == Input::Mouse::EventType::Click && click)`

**Returns:** ``



### `click(*this, curlocation, button)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Down)`

**Returns:** ``



### `if(down)`

**Returns:** ``



### `down(*this, curlocation, button)`

**Returns:** ``



### `if(down || click || up)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Scroll_Vert && vscroll)`

**Returns:** `else`



### `if(event == Input::Mouse::EventType::Scroll_Hor && hscroll)`

**Returns:** `else`



### `if(event == Input::Mouse::EventType::Zoom && zoom)`

**Returns:** `else`



### `if(event == Input::Mouse::EventType::Rotate && rotate)`

**Returns:** `else`



### `if(event == Input::Mouse::EventType::Move && move)`

**Returns:** `else`



### `move(*this, curlocation)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::HitCheck && over)`

**Returns:** `else`



### `needsclip(Input::Mouse::EventType event)`

**Returns:** `bool`



### `ASSERT(&layer != this, "Layer cannot be placed inside itself")`

**Returns:** ``



### `added(layer)`

**Returns:** ``



### `ASSERT(&layer != this, "Layer cannot be placed inside itself")`

**Returns:** ``



### `added(layer)`

**Returns:** ``



### `dotransformandclip()`

**Returns:** ``



### `for(auto &l : children)`

**Returns:** ``



### `reverttransformandclip()`

**Returns:** ``



### `dotransformandclip(true)`

**Returns:** ``



### `if(out)`

**Returns:** ``



### `reverttransformandclip()`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Out)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Up)`

**Returns:** `else`



### `reverttransformandclip()`

**Returns:** ``



### `if(parent)`

**Returns:** ``



### `swap(bounds, other.bounds)`

**Returns:** ``



### `swap(isvisible, other.isvisible)`

**Returns:** ``



### `swap(children, other.children)`

**Returns:** ``



### `if(myparent)`

**Returns:** ``



### `if(otherparent)`

**Returns:** ``



### `if(myparent)`

**Returns:** ``



### `if(otherparent)`

**Returns:** ``



### `Swap(other)`

**Returns:** ``



### `if(s.Width == 0)`

**Returns:** ``



### `if(s.Height == 0)`

**Returns:** ``



### `ResetTransform(const Geometry::Size &size)`

**Returns:** `inline void`


This should be called by the windows to reset transformation stack.

