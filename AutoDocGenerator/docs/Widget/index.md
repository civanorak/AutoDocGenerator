# Widget

> Auto-generated documentation for the **Widget** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Widget`

**Namespace:** `Gorgon`

#### Methods

##### `resize_(const UnitSize &size)`

**Returns:** `void`

##### `Resize(size)`

**Returns:** ``

##### `Move(UnitDimension x, UnitDimension y)`

**Returns:** `void`

Moves this widget to the given position. Widget might be moved by organizers.

##### `Move(const UnitPoint &value)`

**Returns:** `void`

Moves this widget to the given position.

##### `GetLocation(—)`

**Returns:** `UnitPoint`

Returns the location of the widget. This is the assigned location and may not reflect actual position. Widget might be moved by organizers.

##### `virtual` `GetCurrentLocation(—)`

**Returns:** `virtual Geometry::Point`

Returns the current location of the widget in pixels. This might be different than location that is set.

##### `GetCalculatedLocation(Dimension::Unit units = Dimension::MilliUnitSize)`

**Returns:** `UnitPoint`

Returns the current location converted to requested units

##### `Resize(UnitDimension w, UnitDimension h)`

**Returns:** `void`

Changes the size of the widget.

##### `virtual` `Resize(const UnitSize &size)`

**Returns:** `virtual void`

Changes the size of the widget.

##### `GetSize(—)`

**Returns:** `UnitSize`

Returns the size of the widget

##### `virtual` `GetCurrentSize(—)`

**Returns:** `virtual Geometry::Size`

Returns the current size of the widget in pixels. This might be different than the size that is set.

##### `GetCalculatedSize(Dimension::Unit units = Dimension::MilliUnitSize)`

**Returns:** `UnitSize`

Returns the current size converted to requested units

##### `GetBounds(—)`

**Returns:** `Geometry::Bounds`

Returns the bounds of the widget in pixels.

##### `GetWidth(—)`

**Returns:** `UnitDimension`

Returns the width of the widget

##### `GetHeight(—)`

**Returns:** `UnitDimension`

Returns the height of the widget

##### `GetCurrentWidth(—)`

**Returns:** `int`

Returns the width of the widget in pixels.

##### `GetCurrentHeight(—)`

**Returns:** `int`

Returns the height of the widget in pixels.

##### `virtual` `SetWidth(UnitDimension width)`

**Returns:** `virtual void`

Sets the width of the widget

##### `virtual` `SetHeight(UnitDimension height)`

**Returns:** `virtual void`

Sets the height of the widget

##### `virtual` `Activate(—)`

**Returns:** `virtual bool`

Activates the widget. This might perform the action if the widget is a button, forward the focus if it is a label or focus if it is an input field.

##### `Remove(—)`

**Returns:** `bool`

Removes the widget from its parent. Returns true if the widget has no parent after the operation.

##### `AllowFocus(—)`

**Returns:** `bool`

If this widget can be focused currently

##### `Focus(—)`

**Returns:** `bool`

Transfers the focus to this widget. Returns true if the focus is actually transferred to this widget

##### `Defocus(—)`

**Returns:** `bool`

Removes the focus from this widget if this widget is focused. This function will not transfer the focus to another widget.

##### `IsFocused(—)`

**Returns:** `bool`

Returns if this widget is focused.

##### `virtual` `Show(—)`

**Returns:** `virtual void`

Shows this widget, widgets are visible by default.

##### `virtual` `Hide(—)`

**Returns:** `virtual void`

Hides this widget, when hidden, widgets cannot gain focus

##### `ToggleVisible(—)`

**Returns:** `void`

Toggles the visibility state of the widget.

##### `virtual` `SetVisible(bool value)`

**Returns:** `virtual void`

Changes the visibility of the widget

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

Returns if the widget is visible

##### `EnsureVisible(—)`

**Returns:** `bool`

Ensures this widget is visible in its container by scrolling it into view. This function will not change visibility of the widget and will return false if the widget is not visible. This function cannot be expected to take outside factors into account, such as occlusion.

##### `Enable(—)`

**Returns:** `void`

Enables the widget so that the user can interact with it

##### `Disable(—)`

**Returns:** `void`

Disables the widget so that the user cannot interact with it

##### `ToggleEnabled(—)`

**Returns:** `void`

Toggles enabled state of the widget

##### `virtual` `SetEnabled(bool value)`

**Returns:** `virtual void`

Sets the enabled state of the widget

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

Returns whether the widget is enabled.

##### `HasParent(—)`

**Returns:** `bool`

Returns if this widget has a parent

##### `virtual` `SetFloating(bool value)`

**Returns:** `virtual void`

Returns the parent of this widget, throws if it does not have a parent. Sets floating status of this widget. Floating widgets will not be moved or resized by organizers.

##### `boundschanged(—)`

**Returns:** ``

##### `IsFloating(—)`

**Returns:** `bool`

Returns floating status of this widget. Floating widgets will not be moved or resized by organizers.

##### `virtual` `KeyPressed(Input::Key, float)`

**Returns:** `virtual bool`

This function should be called whenever a key is pressed or released.

##### `virtual` `CharacterPressed(Char)`

**Returns:** `virtual bool`

This function should be called whenever a character is received from operating system.

##### `virtual` `Done(—)`

**Returns:** `virtual bool`

For widgets that supports it, this will trigger finalization the user interaction. This may cause widget fire change event or reorganize itself.

##### `SetTooltip(const std::string &value)`

**Returns:** `void`

Sets the tooltip to the given value. This will immediately update the display if it is currently displayed.

##### `if(tooltip != value)`

**Returns:** ``

##### `TooltipChangedEvent(—)`

**Returns:** ``

##### `RemoveTooltip(—)`

**Returns:** `void`

Removes the tooltip from this widget

##### `SetTooltip("")`

**Returns:** ``

##### `GetTooltip(—)`

**Returns:** `std::string`

Returns the tooltip of this widget.

##### `Convert(const UnitDimension &val, bool isvertical, bool issize = false)`

**Returns:** `int`

Converts the given size in units to pixels

##### `Convert(const UnitSize &size)`

**Returns:** `Geometry::Size`

Converts the given size in units to pixels

##### `Convert(const UnitPoint &location)`

**Returns:** `Geometry::Point`

Converts the given location in units to pixels

##### `Convert(Dimension::Unit target, const UnitDimension &val, bool isvertical, bool issize = false)`

**Returns:** `UnitDimension`

Converts the given size in units to requested units.

##### `Convert(Dimension::Unit target, const UnitSize &size)`

**Returns:** `UnitSize`

Converts the given size in units to requested units.

##### `Convert(Dimension::Unit target, const UnitPoint &location)`

**Returns:** `UnitPoint`

Converts the given location in units to requested units.

##### `setname(std::string value)`

**Returns:** `void`

This event will be fired when the widget receives or looses focus. This event will be fired when the area that the widget occupies on its container is changed. It will be fired when the widget is hidden or shown or its parent is changed. Movement, resize and parent change will not trigger this event if the widget is not visible. Similarly, if the object does not have a parent movement and resize will not trigger this event. Organizers use this event to rearrange widgets, thus it is not advisable to remove all handlers from this event. This event will be fired when the mouse enters the widget area. This event will be fired when the mouse exits the widget area. This event will be fired when the tooltip of the widget is changed This event will be fired before the widget is destroyed. This event is fired in the middle of the destruction. It is not safe to access the widget at this point. Only the aliases to this widget should be invalidated in the event handlers registered to this function. This is a debug feature

##### `setwidthperfraction(float value)`

**Returns:** `void`

Is designed to be used by organizers

##### `calculatebounds(—)`

**Returns:** ``

##### `virtual` `resize(const Geometry::Size &size)`

**Returns:** `virtual void`

Should resize the widget in pixels

##### `virtual` `move(const Geometry::Point &value)`

**Returns:** `virtual void`

Should move the widget in pixels

##### `virtual` `addingto(WidgetContainer &)`

**Returns:** `virtual bool`

Called when it is about to be added to the given container

##### `virtual` `addto(Layer &layer)`

**Returns:** `virtual void`

When called, widget should locate itself on to this layer.

##### `virtual` `addedto(WidgetContainer &container)`

**Returns:** `virtual void`

Called when this widget added to the given container

##### `virtual` `removefrom(Layer &layer)`

**Returns:** `virtual void`

When called, widget should remove itself from the given layer

##### `virtual` `removingfrom(—)`

**Returns:** `virtual bool`

Called before this widget is removed from its parent.

##### `virtual` `removed(—)`

**Returns:** `virtual void`

Called after this widget is removed from its parent.

##### `virtual` `setlayerorder(Layer &layer, int order)`

**Returns:** `virtual void`

When called, widget should reorder itself in layer hierarchy

##### `virtual` `allowfocus(—)`

**Returns:** `virtual bool`

Should return true if the widget can be focused

##### `virtual` `focused(—)`

**Returns:** `virtual void`

This is called after the focus is transferred to this widget.

##### `virtual` `canloosefocus(—)`

**Returns:** `virtual bool`

Should return true if the widget can loose the focus right now. Even if you return false, you still might be forced to loose focus, even without this function getting called.

##### `virtual` `focuslost(—)`

**Returns:** `virtual void`

This is called after the focus is lost. This is called even if focus removal is forced.

##### `virtual` `boundschanged(—)`

**Returns:** `virtual void`

Call this function when the widget bounds is changed

##### `virtual` `parentboundschanged(—)`

**Returns:** `virtual void`

Call this function when the bounds of the parent is changed

##### `virtual` `parentenabledchanged(bool /*state*/)`

**Returns:** `virtual void`

This function is called when the parent's enabled state changes.

##### `virtual` `setdefaultstate(bool /*default*/)`

**Returns:** `virtual void`

This function is called when this widget is made or unmade default.

##### `virtual` `setcancelstate(bool /*cancel*/)`

**Returns:** `virtual void`

This function is called when this widget is made or unmade cancel.

##### `virtual` `mouseenter(—)`

**Returns:** `virtual void`

##### `virtual` `mouseleave(—)`

**Returns:** `virtual void`

##### `calculatebounds(—)`

**Returns:** `void`

This function will recalculate location and the size of the widget and if there is a change it will call necessary functions.

##### `virtual` `hide(—)`

**Returns:** `virtual void`

last set location in pixels, used to determine if move is necessary last set size in pixels, used to determine if resize is necessary currently set location, used to determine if move is necessary currently set size, used to determine if resize is necessary Never call this function

##### `virtual` `show(—)`

**Returns:** `virtual void`

Never call this function


### `WidgetBase`

**Namespace:** `gge`

#### Methods

##### `Draw_Signal(IntervalObject &interval)`

**Returns:** `friend void`

##### `virtual` `SetBlueprint(const Blueprint &bp)`

**Returns:** `virtual void`

##### `virtual` `SetBlueprint(const Blueprint *bp)`

**Returns:** `virtual void`

##### `SetBlueprint(*bp)`

**Returns:** ``

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

##### `IsHidden(—)`

**Returns:** `inline bool`

##### `virtual` `Show(bool setfocus=false)`

**Returns:** `virtual void`

##### `if(!isvisible)`

**Returns:** ``

##### `call_container_widget_visibility_change(true)`

**Returns:** ``

##### `Focus(—)`

**Returns:** ``

##### `virtual` `Hide(—)`

**Returns:** `virtual void`

##### `if(isvisible)`

**Returns:** ``

##### `call_container_widget_visibility_change(false)`

**Returns:** ``

##### `ToggleVisibility(—)`

**Returns:** `void`

##### `Hide(—)`

**Returns:** `else`

##### `SetVisibility(bool visible)`

**Returns:** `void`

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

##### `IsDisabled(—)`

**Returns:** `inline bool`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `ToggleEnabled(—)`

**Returns:** `void`

##### `Disable(—)`

**Returns:** `else`

##### `SetEnabled(bool enabled)`

**Returns:** `void`

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `GetWidth(—)`

**Returns:** `int`

##### `GetHeight(—)`

**Returns:** `int`

##### `virtual` `Resize(utils::Size Size)`

**Returns:** `virtual void`

##### `Resize(int W, int H)`

**Returns:** `void`

##### `SetWidth(int W)`

**Returns:** `void`

##### `SetHeight(int H)`

**Returns:** `void`

##### `virtual` `GetLocation(—)`

**Returns:** `virtual utils::Point`

##### `GetX(—)`

**Returns:** `int`

##### `GetY(—)`

**Returns:** `int`

##### `GetLeft(—)`

**Returns:** `int`

##### `GetTop(—)`

**Returns:** `int`

##### `virtual` `Move(utils::Point Location)`

**Returns:** `virtual void`

##### `Move(int X, int Y)`

**Returns:** `void`

##### `SetX(int X)`

**Returns:** `void`

##### `SetY(int Y)`

**Returns:** `void`

##### `SetLeft(int X)`

**Returns:** `void`

##### `SetTop(int Y)`

**Returns:** `void`

##### `virtual` `GetBounds(—)`

**Returns:** `virtual utils::Bounds`

##### `virtual` `GetRectangle(—)`

**Returns:** `virtual utils::Rectangle`

##### `virtual` `SetBounds(utils::Bounds b)`

**Returns:** `virtual void`

##### `virtual` `SetRectangle(utils::Rectangle r)`

**Returns:** `virtual void`

##### `virtual` `IsFocused(—)`

**Returns:** `virtual bool`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `call_container_setfocus(—)`

**Returns:** ``

##### `GotFocus(—)`

**Returns:** ``

##### `SetFocus(bool focus)`

**Returns:** `bool`

##### `call_container_setfocus(—)`

**Returns:** ``

##### `RemoveFocus(—)`

**Returns:** `return`

##### `virtual` `RemoveFocus(—)`

**Returns:** `virtual bool`

##### `call_container_removefocus(—)`

**Returns:** ``

##### `virtual` `ForceRemoveFocus(—)`

**Returns:** `virtual void`

##### `call_container_forceremovefocus(—)`

**Returns:** ``

##### `virtual` `GetZOrder(—)`

**Returns:** `virtual int`

##### `virtual` `SetZOrder(int Order)`

**Returns:** `virtual void`

##### `virtual` `ToTop(—)`

**Returns:** `virtual void`

##### `virtual` `ToBottom(—)`

**Returns:** `virtual void`

##### `virtual` `GetFocusOrder(—)`

**Returns:** `virtual int`

##### `virtual` `SetFocusOrder(int Order)`

**Returns:** `virtual void`

##### `FocusOrderToTop(—)`

**Returns:** `void`

##### `FocusOrderToBottom(—)`

**Returns:** `void`

##### `virtual` `HasContainer(—)`

**Returns:** `virtual bool`

##### `SetContainer(ContainerBase &container)`

**Returns:** `void`

##### `SetContainer(ContainerBase *container)`

**Returns:** `void`

##### `virtual` `Detach(—)`

**Returns:** `virtual void`

##### `virtual` `GetPointer(—)`

**Returns:** `virtual Pointer::PointerType`

##### `virtual` `SetPointer(Pointer::PointerType Pointer)`

**Returns:** `virtual void`

##### `virtual` `ResetPointer(—)`

**Returns:** `virtual void`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `virtual` `MouseHandler(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `virtual bool`

##### `Focus(—)`

**Returns:** ``

##### `if(event==input::mouse::Event::Out)`

**Returns:** `else`

##### `virtual` `Draw(—)`

**Returns:** `virtual void`

##### `virtual` `Accessed(—)`

**Returns:** `virtual bool`

##### `Focus(—)`

**Returns:** `return`

##### `virtual` `SetIsExtender(bool value)`

**Returns:** `virtual void`

##### `if(value!=targetextender)`

**Returns:** ``

##### `SetContainer(Container)`

**Returns:** ``

##### `MakeExtender(—)`

**Returns:** `void`

##### `SetIsExtender(true)`

**Returns:** ``

##### `GetIsExtender(—)`

**Returns:** `bool`

##### `Detach(—)`

**Returns:** ``

##### `playsound(resource::Sound *snd)`

**Returns:** `void`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `virtual` `locating(ContainerBase *container, int Order)`

**Returns:** `virtual bool`

##### `virtual` `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `virtual` `accesskeystatechanged(—)`

**Returns:** `virtual void`

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `locateto(ContainerBase* container, int Order, utils::SortedCollection<WidgetBase>::Wrapper * w)`

**Returns:** `void`

##### `virtual` `detach(ContainerBase *container)`

**Returns:** `virtual bool`

##### `call_container_setfocus(—)`

**Returns:** `bool`

##### `call_container_widget_visibility_change(bool state)`

**Returns:** `void`

##### `call_container_removefocus(—)`

**Returns:** `void`

##### `call_container_forceremovefocus(—)`

**Returns:** `void`

##### `WidgetBase(const WidgetBase &wb)`

**Returns:** ``


---

## Functions

### `if(visible != value)`

**Returns:** ``



### `show()`

**Returns:** ``



### `Defocus()`

**Returns:** ``



### `hide()`

**Returns:** ``



### `BoundsChangedEvent()`

**Returns:** ``



### `calculatebounds()`

**Returns:** ``


Called when this widget added to the given container


### `boundschanged()`

**Returns:** ``



### `boundschanged()`

**Returns:** ``



### `FocusEvent()`

**Returns:** ``



### `FocusEvent()`

**Returns:** ``



### `DestroyedEvent()`

**Returns:** ``



### `MouseEnterEvent()`

**Returns:** ``



### `MouseLeaveEvent()`

**Returns:** ``



### `if(llocation != l)`

**Returns:** ``



### `move(l)`

**Returns:** ``



### `if(lsize != s)`

**Returns:** ``



### `resize(s)`

**Returns:** ``



### `boundschanged()`

**Returns:** ``



### `calculatebounds()`

**Returns:** ``



### `calculatebounds()`

**Returns:** ``



### `switch(target)`

**Returns:** ``



### `Pixels(px)`

**Returns:** `return`



### `switch(target)`

**Returns:** ``



### `Pixels(px)`

**Returns:** `return`



### `if(widthperfraction != -1)`

**Returns:** ``



### `switch(target)`

**Returns:** ``



### `Pixels(px)`

**Returns:** `return`



### `calculatebounds()`

**Returns:** ``



### `Detach()`

**Returns:** ``



### `locateto(container, Order, w)`

**Returns:** ``



### `BoundsChanged()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(BaseLayer)`

**Returns:** ``



### `if(input::mouse::PressedObject==BaseLayer->MouseCallback.object)`

**Returns:** ``



### `BoundsChanged()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `BoundsChanged()`

**Returns:** ``



### `if(Container)`

**Returns:** ``


