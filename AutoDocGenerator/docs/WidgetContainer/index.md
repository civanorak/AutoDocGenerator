# WidgetContainer

> Auto-generated documentation for the **WidgetContainer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ExtenderRequestResponse`

**Namespace:** `UI`

This structure is used to transfer extender request response


### `WidgetContainer`

**Namespace:** `UI`

If the coordinates are properly translated. This is internally used to perform step by step transformation If the extender is provided by the request Coordinates of the given point in the extender container Total size of the container. -1 means infinite

#### Methods

##### `Add(Widget &widget)`

**Returns:** `bool`

Inherit from the parent. If this container is top level then it will be AllowAll All widgets that can be focused are allowed to receive focus, including buttons but not labels. Widgets that require input to work or benefit from input greatly are allowed to receive focus. Button, listbox, and select will loose the ability to receive focus. However, sliders and input boxes will receive the focus Only the widget that will not work without input will receive focus. This includes input boxes. This will also disable tab switching. No widget is allowed focus and this container will not handle any keys. Virtual destructor Adds the given widget to this container. Widget will be placed to the top of the z-order, to the end of the focus order. If the given widget cannot be added, this function will return false.

##### `AddUnder(Widget &widget)`

**Returns:** `bool`

Adds a new label with the given text. Ownership of this newly created widget lies with the container. This function enables horizontal autosizing. Adds a new label with the given text. Ownership of this newly created widget lies with the container. This function enables horizontal autosizing. Adds a new label with the given text. Ownership of this newly created widget lies with the container. This function enables horizontal autosizing. Adds a new label with the given text. Ownership of this newly created widget lies with the container. This function enables horizontal autosizing. Adds a new label with the given text. Ownership of this newly created widget lies with the container. This function enables horizontal autosizing. Adds the given widget to this container and locates it under the last widget at the start of the next line. If container is empty, the widget will be located at the top left. Note that this does not create a bond between widgets thus if target widget is moved or resized, added widget will not move.

##### `AddUnder(Widget &widget, const Widget &other)`

**Returns:** `bool`

Adds the given widget to this container and locates it under the given widget at the start of the next line. Note that this does not create a bond between widgets thus if target widget is moved or resized, added widget will not move.

##### `AddNextTo(Widget &widget)`

**Returns:** `bool`

Adds the given widget to this container and locates it next to the given widget. If container is empty, the widget will be located at the top left. Note that this does not create a bond between widgets thus if target widget is moved or resized, added widget will not move.

##### `AddNextTo(Widget &widget, const Widget &other)`

**Returns:** `bool`

Adds the given widget to this container and locates it next to the given widget. Note that this does not create a bond between widgets thus if target widget is moved or resized, added widget will not move.

##### `Insert(Widget &widget, int index)`

**Returns:** `bool`

Add the given widget to this container. Widget will be placed to the top of the z-order, and to the specified focus order. If the given widget cannot be added, this function will return false. If the index is out of bounds the widget will be added at the end.

##### `Remove(Widget &widget)`

**Returns:** `bool`

Removes the given widget from this container. If the widget does not exits, this function will return true without taking any additional action. If the widget cannot be removed from the container, this function will return false.

##### `Clear(—)`

**Returns:** `bool`

Removes all widgets from this container. Returns true if all widgets are removed successfully.

##### `ForceRemove(Widget &widget)`

**Returns:** `void`

Forcefully removes the given widget from this container.

##### `ChangeFocusOrder(Widget &widget, int order)`

**Returns:** `void`

Changes the focus order of the given widget. If the order is out of bounds, the widget will be moved to the end. You may use the functions in the widget to manage focus order.

##### `GetFocusOrder(const Widget &widget)`

**Returns:** `int`

##### `ChangeZorder(Widget &widget, int order)`

**Returns:** `void`

Changes the z-order of the widget. If the order is out of bounds, the widget will be drawn on top. You may use the functions in the widget to manage z-order.

##### `FocusFirst(—)`

**Returns:** `bool`

Focuses the first widget that accepts focus. If none of the widgets accept focus or if the currently focused widget blocks focus transfer then this function will return false.

##### `FocusNext(—)`

**Returns:** `bool`

Focuses the next widget that accepts focus. If no widget other than the currently focused widget accept focus then this function will return false. Additionally, if the currently focused widget blocks focus transfer, this function will return false.

##### `FocusNext(int after)`

**Returns:** `bool`

Focuses the next widget that accepts focus starting from the given focus index. If no widget other than the currently focused widget accept focus then this function will return false. Additionally, if the currently focused widget blocks focus transfer, this function will return false.

##### `FocusNext(const Widget &widget)`

**Returns:** `bool`

Focuses the next widget that accepts focus starting from the given focus index. If no widget other than the currently focused widget accept focus then this function will return false. Additionally, if the currently focused widget blocks focus transfer, this function will return false.

##### `FocusLast(—)`

**Returns:** `bool`

Focuses the last widget in the container. If none of the widgets accept focus or if the currently focused widget blocks focus transfer then this function will return false.

##### `FocusPrevious(—)`

**Returns:** `bool`

Focuses the previous widget that accepts focus. If no widget other than the currently focused widget accept focus then this function will return false. Additionally, if the currently focused widget blocks focus transfer, this function will return false.

##### `FocusPrevious(const Widget& widget)`

**Returns:** `bool`

Focuses the previous widget that accepts focus. If no widget other than the currently focused widget accept focus then this function will return false. Additionally, if the currently focused widget blocks focus transfer, this function will return false.

##### `FocusPrevious(int before)`

**Returns:** `bool`

Focuses the previous widget that accepts focus. If no widget other than the currently focused widget accept focus then this function will return false. Additionally, if the currently focused widget blocks focus transfer, this function will return false.

##### `SetFocusTo(Widget &widget)`

**Returns:** `bool`

Sets the focus to the given widget

##### `RemoveFocus(—)`

**Returns:** `bool`

Removes the focus from the focused widget

##### `ForceRemoveFocus(—)`

**Returns:** `void`

Forcefully removes the focus from the focused widget

##### `HasFocusedWidget(—)`

**Returns:** `bool`

Returns if this container has a focused widget

##### `virtual` `EnsureVisible(const Widget &widget)`

**Returns:** `virtual bool`

Returns the focused widget. If no widget is focused, this function will throw. Ensures the widget is visible. Returns true if the container can be scroll to make sure the given widget is visible. This function cannot be expected to take outside factors into account, such as occlusion. This function does not change the visibility of the widget and will return false if the widget is not visible.

##### `virtual` `IsDisplayed(—)`

**Returns:** `virtual bool`

Should return whether the container is visible. Due to different container designs and capabilities, setting visibility depends on the particular container

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

Returns whether container is enabled.

##### `Enable(—)`

**Returns:** `void`

Enables the container, allowing interaction with the widgets in it.

##### `SetEnabled(true)`

**Returns:** ``

##### `Disable(—)`

**Returns:** `void`

Disables the container, disallowing interactions of all widgets in it.

##### `SetEnabled(false)`

**Returns:** ``

##### `ToggleEnabled(—)`

**Returns:** `void`

Toggles the enabled state of this container. If the state is toggled after the call, this function will return true.

##### `virtual` `SetEnabled(bool value)`

**Returns:** `virtual void`

Sets the enabled state of this container. This function will return true if the container is enabled at the end of the call.

##### `if(value != isenabled)`

**Returns:** ``

##### `distributeparentenabled(value)`

**Returns:** ``

##### `virtual` `GetInteriorSize(—)`

**Returns:** `virtual Geometry::Size`

Should return the interior (usable) size of the container. This value is calculated and might differ from the value set by ResizeInterior

##### `virtual` `ResizeInterior(const UI::UnitSize &size)`

**Returns:** `virtual bool`

Should resize the interior (usable) size of the container. If resize operation cannot set the size exactly to the requested size, this function returns false.

##### `virtual` `SetInteriorWidth(const UnitDimension &size)`

**Returns:** `virtual bool`

Should resize the interior (usable) size of the container. If resize operation cannot set the size exactly to the requested size, this function returns false.

##### `virtual` `SetInteriorHeight(const UnitDimension &size)`

**Returns:** `virtual bool`

Should resize the interior (usable) size of the container. If resize operation cannot set the size exactly to the requested size, this function returns false.

##### `virtual` `IsTabSwitchEnabled(—)`

**Returns:** `virtual bool`

Check if tab switch is enabled. Tab switch allows user to change focus to the next widget using tab key. Default is enabled.

##### `EnableTabSwitch(—)`

**Returns:** `void`

Enable tab switching. Tab switch allows user to change focus to the next widget using tab key

##### `DisableTabSwitch(—)`

**Returns:** `void`

Disable tab switching. Tab switch allows user to change focus to the next widget using tab key

##### `ToggleTabSwitchEnabledState(—)`

**Returns:** `void`

Toggles the state of tab switching. Tab switch allows user to change focus to the next widget using tab key

##### `virtual` `SetTabSwitchEnabledState(bool state)`

**Returns:** `virtual void`

Sets the state of tab switching. Tab switch allows user to change focus to the next widget using tab key

##### `begin(—)`

**Returns:** `auto`

Returns the begin iterator for the contained widgets

##### `begin(—)`

**Returns:** `auto`

Returns the begin iterator for the contained widgets

##### `end(—)`

**Returns:** `auto`

Returns the end iterator for the contained widgets

##### `end(—)`

**Returns:** `auto`

Returns the end iterator for the contained widgets

##### `GetCount(—)`

**Returns:** `int`

Returns the number of widgets in this container

##### `virtual` `HasDefault(—)`

**Returns:** `virtual bool`

Returns the widget at the given index Returns the widget at the given index Returns the default element of the container. Default widget is activated when the user presses enter and the focused widget does not consume the key or if the user presses ctrl+enter. Default elements are generally buttons, however, any widget can be designated as default widget. If there is no default object, this function will throw. Use HasDefault to check if this container has a default widget. Returns if this container has a default object.

##### `virtual` `SetDefault(Widget &widget)`

**Returns:** `virtual void`

Sets the default object of the container. Ideally this should be a button or a similar widget.

##### `virtual` `RemoveDefault(—)`

**Returns:** `virtual void`

Removes the default widget of this container.

##### `virtual` `HasCancel(—)`

**Returns:** `virtual bool`

Returns the cancel element of the container which is called when the use presses escape key. It also might be activated programmatically. Cancel elements are generally buttons, however, any widget can be cancel widget. If there is no cancel object set, this function will throw. Use HasCancel to check if this container has a cancel widget. Returns if this container has a cancel widget.

##### `virtual` `SetCancel(Widget &widget)`

**Returns:** `virtual void`

Sets the cancel widget of the container. Ideally this should be a button or a similar widget.

##### `virtual` `RemoveCancel(—)`

**Returns:** `virtual void`

Removes the cancel widget of this container.

##### `SetFocusStrategy(FocusStrategy value)`

**Returns:** `void`

Sets the focus strategy, see FocusStrategy

##### `GetFocusStrategy(—)`

**Returns:** `FocusStrategy`

Returns the focus strategy set to this container. Do not use this to determine current strategy, use CurrentFocusStrategy instead.

##### `CurrentFocusStrategy(—)`

**Returns:** `FocusStrategy`

Returns the active focus strategy. This function will not return Inherit.

##### `getparentfocusstrategy(—)`

**Returns:** `return`

##### `AttachOrganizer(org)`

**Returns:** ``

Creates a new organizer that lives with this container

##### `AttachOrganizer(Organizers::Base &organizer)`

**Returns:** `void`

Attaches an organizer to this container. Ownership is not transferred

##### `RemoveOrganizer(—)`

**Returns:** `void`

Removes the organizer from this container

##### `HasOrganizer(—)`

**Returns:** `bool`

Returns if this container has an organizer

##### `if(organizer == nullptr)`

**Returns:** ``

Returns the organizer controlling this container. If this container does not have an organizer this function will throw

##### `Own(const Widget &widget)`

**Returns:** `void`

This container will own the given widget.

##### `Disown(const Widget &widget)`

**Returns:** `void`

Removes the ownership of the given widget, if it is not owned nothing happens.

##### `Displaced(—)`

**Returns:** `void`

Call this function if this container is moved without its knowledge

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `virtual` `KeyPressed(Input::Key key, float state)`

**Returns:** `virtual bool`

This function should be called whenever a key is pressed or released.

##### `virtual` `CharacterPressed(Char c)`

**Returns:** `virtual bool`

This function should be called whenever a character is received from operating system.

##### `virtual` `IsInFullView(const Widget &widget)`

**Returns:** `virtual bool`

Returns if the given widget is in view. Returns false if the widget is not on the container. This should be overloaded by scrollable containers.

##### `virtual` `IsInPartialView(const Widget &widget)`

**Returns:** `virtual bool`

Returns if the given widget is in view. Returns false if the widget is not on the container. This should be overloaded by scrollable containers.

##### `virtual` `IsWidget(—)`

**Returns:** `virtual bool`

Returns if this container is a widget. If it is, it can be converted using AsWidget function

##### `virtual` `SetHoveredWidget(Widget *widget)`

**Returns:** `virtual void`

If this container is a widget, this function will return it; if not, it will throw. This system allows container widgets that have multiple indirection levels. Returns the currently hovered widget. Returns nullptr if no widget is hovered. Set the currently hovered widget. Setting it to nullptr is supported. A widget that is became invisible, or removed from its container should unset the hovered if it is the hovered widget.

##### `getlayer(—)`

**Returns:** `return`

Returns the layer of this container

##### `virtual` `RequestExtender(const Gorgon::Layer &self)`

**Returns:** `virtual ExtenderRequestResponse`

Returns the toplevel layer of this container This function will return a container that will act as an extender.

##### `virtual` `GetSpacing(—)`

**Returns:** `virtual int`

The spacing should be left between widgets

##### `virtual` `GetUnitSize(—)`

**Returns:** `virtual int`

Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Multiple units can be obtained by GetUnitSize(n)

##### `GetUnitSize(int n)`

**Returns:** `int`

Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Multiple units can be obtained by GetUnitSize(n)

##### `SetFractionCount(int value)`

**Returns:** `void`

Number of fractions that this container have. This value can be ignored and the used value can be calculated by the organizers. Default value is 6.

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `GetFractionCount(—)`

**Returns:** `int`

Number of fractions that this container have. This value can be ignored and the used value can be calculated by the organizers. Default value is 6.

##### `virtual` `addingwidget(Widget &)`

**Returns:** `virtual bool`

This container is sorted by the focus order This is the currently hovered widget This function can return false to prevent the given widget from getting added to the container.

##### `virtual` `widgetadded(Widget &)`

**Returns:** `virtual void`

This function is called after a widget is added.

##### `virtual` `removingwidget(Widget &)`

**Returns:** `virtual bool`

This function is called before removing a widget. Return false to prevent that widget from getting removed. This widget is guaranteed to be in this container

##### `virtual` `widgetremoved(Widget &)`

**Returns:** `virtual void`

This function is called after a widget is removed

##### `virtual` `getparentfocusstrategy(—)`

**Returns:** `virtual FocusStrategy`

If this widget is not top level, return the current strategy used by the parent. Never return Inherit from this function.

##### `virtual` `focuschanged(—)`

**Returns:** `virtual void`

Returns the layer that will be used to place the contained widgets. This function is called when the focus is changed

##### `handlestandardkey(Input::Key key)`

**Returns:** `bool`

Performs the standard operations (tab/enter/escape)

##### `distributekeyevent(Input::Key key, float state, bool handlestandard)`

**Returns:** `bool`

Distributes the pressed key to the focused widget. If action not handled and and handlestandard is true, this function will also perform standard action.

##### `distributecharevent(Char c)`

**Returns:** `bool`

Distributes a pressed character to the focused widget.

##### `distributeparentenabled(bool state)`

**Returns:** `void`

Distributes a enabled state to children

##### `distributeparentboundschanged(—)`

**Returns:** `void`

Distributes bounds changed event to children

##### `virtual` `childboundschanged(Widget *source)`

**Returns:** `virtual void`

The boundary of any of the children is changed. Source could be nullptr

##### `virtual` `deleted(Widget *widget)`

**Returns:** `virtual void`

This widget that is owned by the container is being deleted.


---

## Enums

### `FocusStrategy`

**Namespace:** `UI`

Defines focus strategy for the container. Default is Inherit


---

## Functions

### `widgetadded(widget)`

**Returns:** ``



### `ChangeFocusOrder(widget, index)`

**Returns:** ``



### `ChangeZorder(widget, index)`

**Returns:** ``



### `widgetadded(widget)`

**Returns:** ``



### `for(int i=0; i<widgets.GetSize()`

**Returns:** ``



### `ForceRemove(widget)`

**Returns:** ``



### `FocusNext()`

**Returns:** ``



### `widgetremoved(widget)`

**Returns:** ``



### `SetHoveredWidget(nullptr)`

**Returns:** ``



### `SetHoveredWidget(nullptr)`

**Returns:** ``



### `SetHoveredWidget(nullptr)`

**Returns:** ``



### `SetHoveredWidget(nullptr)`

**Returns:** ``



### `FocusNext()`

**Returns:** ``



### `RemoveDefault()`

**Returns:** ``



### `RemoveCancel()`

**Returns:** ``



### `widgetremoved(*widget)`

**Returns:** ``



### `FocusNext(-1)`

**Returns:** `return`



### `FocusNext(focusindex)`

**Returns:** `return`



### `for(int i=after+1; i<widgets.GetSize()`

**Returns:** ``



### `focuschanged()`

**Returns:** ``



### `EnsureVisible(widgets[i])`

**Returns:** ``



### `for(int i=0; i<after; i++)`

**Returns:** ``



### `focuschanged()`

**Returns:** ``



### `EnsureVisible(widgets[i])`

**Returns:** ``



### `for(int i=before-1; i>=0; i--)`

**Returns:** ``



### `focuschanged()`

**Returns:** ``



### `EnsureVisible(widgets[i])`

**Returns:** ``



### `focuschanged()`

**Returns:** ``



### `EnsureVisible(widgets[i])`

**Returns:** ``



### `focuschanged()`

**Returns:** ``



### `EnsureVisible(widget)`

**Returns:** ``



### `ForceRemoveFocus()`

**Returns:** ``



### `focuschanged()`

**Returns:** ``



### `if(key == Keycodes::Escape && Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::None)`

**Returns:** `else`



### `if(key == Keycodes::Tab)`

**Returns:** `else`



### `if(Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::Shift)`

**Returns:** ``



### `FocusPrevious()`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::None)`

**Returns:** ``



### `FocusNext()`

**Returns:** ``



### `handlestandardkey(key)`

**Returns:** `return`



### `if(organizer)`

**Returns:** ``



### `Add(l)`

**Returns:** ``



### `AddUnder(l)`

**Returns:** ``



### `AddUnder(l, other)`

**Returns:** ``



### `AddNextTo(l)`

**Returns:** ``



### `AddNextTo(l, other)`

**Returns:** ``



### `if(res)`

**Returns:** ``



### `if(res)`

**Returns:** ``


