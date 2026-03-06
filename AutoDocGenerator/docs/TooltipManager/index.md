# TooltipManager

&gt; Auto-generated documentation for the **TooltipManager** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `TooltipManager`

**Namespace:** `UI`

#### Methods

##### `TooltipManager(WidgetContainer &container)`

**Returns:** ``

Tooltip manager requires a widget container to work.

##### `SetDelay(int value)`

**Returns:** `void`

Destructor Sets the delay in milliseconds before the tooltip is shown. Default value is 1000.

##### `GetDelay(—)`

**Returns:** `int`

Returns the delay in milliseconds before the tooltip is shown.

##### `SetLinger(int value)`

**Returns:** `void`

Sets the duration in milliseconds tooltip will stay on after the mouse leaves a widget. If the mouse enters a widget with tooltip before this duration is expended, tooltip will be updated immediately without waiting for delay or linger. Default is 1000.

##### `GetLinger(—)`

**Returns:** `int`

Returns the delay in milliseconds the tooltip will be displayed after the mouse leaves a widget.

##### `RemoveDelay(—)`

**Returns:** `void`

Removes all the delays in the tooltip including linger.

##### `SetTolerence(int value)`

**Returns:** `void`

Sets the mouse movement tolerance. If the mouse is moved more than this amount, tooltip delay is reset. Default value is 5.

##### `GetTolerence(—)`

**Returns:** `int`

Returns the mouse movement tolerance before the tooltip delay is reset.

##### `SetMode(Mode value)`

**Returns:** `void`

Sets the current mode. Static only calls SetText while dynamic will display, hide and move the target widget. If the target widget is not set, dynamic mode will not work. Default value is Dynamic.

##### `GetMode(—)`

**Returns:** `Mode`

Returns the current operation mode.

##### `SetFollow(Follow value)`

**Returns:** `void`

Sets the current follow mode. Follow modes are only functional if tooltip is operating in Dynamic mode. In Pointer mode, tooltip is placed under the pointer but will not move with it. In FollowPointer mode, tooltip is placed under the pointer and will follow it. In UnderWidget, tooltip will be placed under the widget if there is space, over it if not. In NextToWidget mode, tooltip is placed on the right side of the widget if there is space, if not, first left side, then bottom and finally above is tried. Default is Pointer. Currently only Pointer mode is implemented.

##### `GetFollow(—)`

**Returns:** `Follow`

Returns the current follow mode.

##### `Enable(—)`

**Returns:** `void`

Enables tooltips. Manager starts enabled.

##### `Disable(—)`

**Returns:** `void`

Disables tooltips. Manager starts enabled.

##### `Hide(—)`

**Returns:** `void`

Hides currently displayed tooltip. The tooltip will only shown if mouse moves to another widget or tooltip text is changed.

##### `Show(const std::string &text)`

**Returns:** `void`

Shows the given text until hovered widget is changed or tooltip of the currently hovered widget is changed. Tooltip will not be displayed if the text is empty.

##### `SetEnabled(bool value)`

**Returns:** `void`

Sets the enabled state of the tooltip manager.

##### `Disable(—)`

**Returns:** `else`

##### `IsEnabled(—)`

**Returns:** `bool`

Returns if the manager is enabled

##### `IsDisplayed(—)`

**Returns:** `bool`

Returns if a tooltip is displayed

##### `GetTooltip(—)`

**Returns:** `std::string`

If a tooltip is displayed returns it, if not this function returns empty string.

##### `SetTarget(Widget &target, bool own = false)`

**Returns:** `void`

Returns the widget that will be managed by this manager. Throws if no target is set. You may use CreateTarget or SetTarget functions to create a target. If a widget registry available, constructor will create a target. If not, it will wait until a registry is created and then it creates the target automatically if it is not set already. Sets the target that will be used in dynamic mode. If own is true, ownership is transferred to this manager

##### `CreateTarget(—)`

**Returns:** `void`

Changes the set text function that will be used to set the tooltip text. CreateTarget overwrites this value. If there is a tooltip displayed, this function will be called immediately. Creates a target automatically. Replaces both target and SetText function. This function creates a label with Tooltip template.

##### `RecreateTarget(—)`

**Returns:** `void`

If this manager has a target, destroys it and recreates the target. If it has no target this function has no effect.

##### `Tick(—)`

**Returns:** `void`

This function is called automatically to detect current mouse location, adjust and display tooltip

##### `SetContainer(WidgetContainer &value)`

**Returns:** `void`

Changes the the container that this manager uses. Does not automatically update if the tooltip is already displayed.

##### `destroyed(—)`

**Returns:** `void`

##### `changed(—)`

**Returns:** `void`

##### `place(—)`

**Returns:** `void`

##### `setmytargettext(const std::string &text)`

**Returns:** `void`


---

## Enums

### `Mode`

**Namespace:** `UI`


### `Follow`

**Namespace:** `UI`


---

## Functions

### `Enable()`

**Returns:** ``



### `Disable()`

**Returns:** ``



### `if(value != follow)`

**Returns:** ``



### `place()`

**Returns:** ``



### `if(token)`

**Returns:** ``



### `settext("")`

**Returns:** ``



### `if(mode == Dynamic && target)`

**Returns:** ``



### `settext(tooltip)`

**Returns:** ``



### `Hide()`

**Returns:** ``



### `if(owntarget)`

**Returns:** ``



### `if(mode == Dynamic)`

**Returns:** ``



### `if(displayed)`

**Returns:** ``



### `place()`

**Returns:** ``



### `settext(tooltip)`

**Returns:** ``



### `if(mode == Dynamic)`

**Returns:** ``



### `place()`

**Returns:** ``



### `if(!toplevel)`

**Returns:** ``



### `if(!target && !settext)`

**Returns:** ``



### `CreateTarget()`

**Returns:** ``



### `if(wgt != current)`

**Returns:** ``



### `if(current && changetoken)`

**Returns:** ``



### `if(!wgt)`

**Returns:** ``



### `if(displayed)`

**Returns:** ``



### `if(toplevel)`

**Returns:** ``



### `if(delayleft != -1)`

**Returns:** ``



### `if(toplevel)`

**Returns:** ``



### `if(toleranceleft < movement)`

**Returns:** ``



### `if(current)`

**Returns:** ``



### `place()`

**Returns:** ``



### `if(lingerleft != -1)`

**Returns:** ``



### `Hide()`

**Returns:** ``



### `if(!mytarget)`

**Returns:** ``



### `if(target)`

**Returns:** ``



### `if(owntarget)`

**Returns:** ``



### `CreateTarget()`

**Returns:** ``



### `if(res.Extender)`

**Returns:** ``



### `if(offset.X + size.Width > csize.Width)`

**Returns:** ``



### `if(offset.Y + size.Height > csize.Height)`

**Returns:** ``



### `while(wgt)`

**Returns:** ``



### `if(wgt == target)`

**Returns:** ``



### `if(current && changetoken)`

**Returns:** ``



### `Hide()`

**Returns:** ``


