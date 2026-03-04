# Window

> Auto-generated documentation for the **Window** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Window`

**Namespace:** `Gorgon`

#### Methods

##### `init(—)`

**Returns:** ``

Creates a new window @param  rect the position and the **interior** size of the window unless use outer metrics is set to true @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window @param  rect the position and the **interior** size of the window unless use outer metrics is set to true @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  title of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  title of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window at the center of the screen @param  monitor that the window will be centered on @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a new window at the center of the screen @param  monitor that the window will be centered on @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `init(—)`

**Returns:** ``

Creates a fullscreen window. Fullscreen windows do not have chrome and covers entire screen, including any panels it contains.

##### `init(—)`

**Returns:** ``

Creates a fullscreen window. Fullscreen windows do not have chrome and covers entire screen, including any panels it contains.

##### `Window(Window &&other)`

**Returns:** ``

Copy constructor is not allowed

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `ResizeInterior({size, interiorsize.Height})`

**Returns:** `return`

##### `ResizeInterior({interiorsize.Width, size})`

**Returns:** `return`

##### `while(!quiting)`

**Returns:** ``

Closes the window, returning the execution to the point where Run function is called. It allows current frame to be completed before quiting.

##### `SetSizes(int spacing, int unitwidth)`

**Returns:** `void`

Window does not do any scrolling, thus cannot ensure visibility The spacing should be left between widgets Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Overrides default spacing and unitwidth

##### `UseDefaultSizes(—)`

**Returns:** `void`

Return to use default sizes

##### `updateregistry(—)`

**Returns:** `void`

Returns a container that can be used to place windows Returns a container that can be used to place dialog windows. Dialog windows stays above bars (status, menu, etc...) Returns a container that can be used to place bars like statusbar, menubar, or taskbar. Bar container stays above windows Returns a container that can be used to place widgets under the graphical contents of the window.

##### `init(—)`

**Returns:** `void`

##### `focuschangedin(LayerAdapter &cont)`

**Returns:** `void`


### `Window`

**Namespace:** `gge`

#### Methods

##### `setallowmove(true)`

**Returns:** ``

##### `setallownofocus(true)`

**Returns:** ``

##### `setshowtitle(true)`

**Returns:** ``

##### `setupvscroll(true, true, true)`

**Returns:** ``

##### `placetitlebutton(rollbtn)`

**Returns:** ``

##### `placetitlebutton(closebtn)`

**Returns:** ``

##### `SetContainer(TopLevel)`

**Returns:** ``

##### `setblueprint(*WR.Window)`

**Returns:** ``

##### `Close(—)`

**Returns:** `void`

##### `ClosingEvent(allow)`

**Returns:** ``

##### `ForcedClose(—)`

**Returns:** ``

##### `virtual` `ForcedClose(—)`

**Returns:** `virtual void`

##### `Hide(—)`

**Returns:** ``

##### `RollUp(—)`

**Returns:** `void`

##### `RollUpEvent(allow)`

**Returns:** ``

##### `ForcedRollUp(—)`

**Returns:** ``

##### `virtual` `ForcedRollUp(—)`

**Returns:** `virtual void`

##### `SetHeight(h)`

**Returns:** ``

##### `setupvscroll(false, false, false)`

**Returns:** ``

##### `RollDown(—)`

**Returns:** `void`

##### `RollDownEvent(allow)`

**Returns:** ``

##### `ForcedRollDown(—)`

**Returns:** ``

##### `virtual` `ForcedRollDown(—)`

**Returns:** `virtual void`

##### `SetHeight(prevh)`

**Returns:** ``

##### `setupvscroll(true, true, true)`

**Returns:** ``

##### `ToggleRoll(—)`

**Returns:** `void`

##### `SetRoll(bool rolled)`

**Returns:** `void`

##### `IsRolledUp(—)`

**Returns:** `bool`

##### `virtual` `MoveToCenter(—)`

**Returns:** `virtual void`

##### `if(Container)`

**Returns:** ``

##### `Move(sz.Width, sz.Height)`

**Returns:** ``

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `gotfocus(—)`

**Returns:** `void`

##### `FocusOrderToTop(—)`

**Returns:** ``

##### `setPadding(const utils::Margins &value)`

**Returns:** `void`

##### `getPadding(—)`

**Returns:** `utils::Margins`

##### `setTitle(const std::string &value)`

**Returns:** `void`

##### `getTitle(—)`

**Returns:** `std::string`

##### `setIcon(graphics::RectangularGraphic2D *icon)`

**Returns:** `void`

##### `setCloseButton(const bool &value)`

**Returns:** `void`

##### `adjustcontrols(—)`

**Returns:** ``

##### `getCloseButton(—)`

**Returns:** `bool`

##### `setRollButton(const bool &value)`

**Returns:** `void`

##### `adjustcontrols(—)`

**Returns:** ``

##### `getRollButton(—)`

**Returns:** `bool`

##### `wr_loaded(—)`

**Returns:** `void`

##### `setblueprint(*WR.Window)`

**Returns:** ``


### `Window`

**Namespace:** `Gorgon`

#### Methods

##### `Window(const UI::Template &temp, const std::string &title = "", bool autoplace = true)`

**Returns:** `explicit`

##### `Window(const UI::Template &temp, const std::string &title, const UI::UnitSize size, bool autoplace = true)`

**Returns:** ``

##### `SetTitle(const std::string &value)`

**Returns:** `void`

Sets the window title to the given string. Title placement is controlled by the template and might not be visible.

##### `GetTitle(—)`

**Returns:** `std::string`

Returns the window title. Title placement is controlled by the template and might not be visible.

##### `SetIcon(const Graphics::Bitmap &value)`

**Returns:** `void`

Changes the icon on the label. The ownership of the bitmap is not transferred. If you wish the bitmap to be destroyed with the label, use OwnIcon instead.

##### `SetIcon(const Graphics::Animation &value)`

**Returns:** `void`

Changes the icon on the label. The ownership of the animation is not transferred. If you wish the animation to be destroyed with the label, use OwnIcon instead.

##### `SetIconProvider(const Graphics::AnimationProvider &value)`

**Returns:** `void`

Changes the icon on the label. This will create a new animation from the given provider and will own the resultant animation.

##### `SetIconProvider(Graphics::AnimationProvider &&provider)`

**Returns:** `void`

Changes the icon on the label. This will move in the provider, create a new animation and own both the provider and the animation

##### `RemoveIcon(—)`

**Returns:** `void`

Removes the icon on the label

##### `HasIcon(—)`

**Returns:** `bool`

Returns if the label has an icon

##### `OwnIcon(—)`

**Returns:** `void`

Returns the icon on the label. If the label does not have an icon, this function will throw Transfers the ownership of the current icon.

##### `OwnIcon(const Graphics::Animation &value)`

**Returns:** `void`

Sets the icon while transferring the ownership

##### `OwnIcon(Graphics::Bitmap &&value)`

**Returns:** `void`

Moves the given animation to the icon of the label

##### `LockMovement(—)`

**Returns:** `void`

Locks the movement of the window.

##### `AllowMovement(false)`

**Returns:** ``

##### `AllowMovement(bool allow = true)`

**Returns:** `void`

Allows movement of the window.

##### `CanBeMoved(—)`

**Returns:** `bool`

Returns whether the window can be moved.

##### `LockSize(—)`

**Returns:** `void`

Prevents user from resizing the window. Windows are not resizable by default.

##### `AllowResize(false)`

**Returns:** ``

##### `AllowResize(bool allow = true)`

**Returns:** `void`

Allows user to resize the window. Windows are not resizable by default.

##### `CanBeResized(—)`

**Returns:** `bool`

Returns whether the window can be resized by the user.

##### `HideCloseButton(—)`

**Returns:** `void`

Hides the close button. Close button is visible by default.

##### `SetCloseButtonVisibility(false)`

**Returns:** ``

##### `ShowCloseButton(—)`

**Returns:** `void`

Shows the close button. Close button is visible by default.

##### `SetCloseButtonVisibility(true)`

**Returns:** ``

##### `SetCloseButtonVisibility(bool value)`

**Returns:** `void`

Sets close button visibility. Close button is visible by default.

##### `IsCloseButtonVisible(—)`

**Returns:** `bool`

Returns if the close button is visible

##### `DisableCloseButton(—)`

**Returns:** `void`

Disables the close button. Close button is enabled by default.

##### `SetCloseButtonEnabled(false)`

**Returns:** ``

##### `EnableCloseButton(—)`

**Returns:** `void`

Enables the close button. Close button is enabled by default.

##### `SetCloseButtonEnabled(true)`

**Returns:** ``

##### `SetCloseButtonEnabled(bool value)`

**Returns:** `void`

Sets whether close button is enabled. Close button is enabled by default.

##### `IsCloseButtonEnabled(—)`

**Returns:** `bool`

Returns if the close button is enabled

##### `Close(—)`

**Returns:** `void`

Hides the window if it is not canceled. Calling hide will cause the window to become hidden without any chance of preventing it.

##### `ClosingEvent(allow)`

**Returns:** ``

##### `if(allow)`

**Returns:** ``

##### `Hide(—)`

**Returns:** ``

##### `ClosedEvent(—)`

**Returns:** ``

##### `KeyEvent(key, state)`

**Returns:** `return`

##### `Focus(—)`

**Returns:** ``

##### `Center(—)`

**Returns:** `void`

Centers the window to its container. After resizing the window or changing its parent you need to recenter it. All windows open centered to the first UI::Window that is opened.

##### `SetMinSize(const UI::UnitSize &value)`

**Returns:** `void`

Sets minimum internal size of the widget, default value is 2x1 units.

##### `GetMinSize(—)`

**Returns:** `UI::UnitSize`

Returns minimum internal size of the widget

##### `SetMaxSize(const UI::UnitSize &value)`

**Returns:** `void`

Sets maximum external size of the widget, default value is 100%, 100%

##### `GetMaxSize(—)`

**Returns:** `UI::UnitSize`

Sets maximum external size of the widget

##### `updatescrollvisibility(—)`

**Returns:** `void`

Window title Icon that will be displayed on the window. Availability of icon depends on the theme. This event is called after the window is closed. In Gorgon, close button only hides the window. It is the owner's task to cleanup. Set the bool parameter to false to prevent window from closing. This event is called after the window is closed. In Gorgon, close button only hides the window. It is the owner's task to cleanup. This event is called when a key is pressed in this window before any widgets receive it. This event is called when a key is pressed and focused widget is not consumed it.

##### `mouse_down(UI::ComponentTemplate::Tag tag, Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`

##### `mouse_up(UI::ComponentTemplate::Tag tag, Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`

##### `mouse_move(UI::ComponentTemplate::Tag tag, Geometry::Point location)`

**Returns:** `void`

##### `mouse_click(UI::ComponentTemplate::Tag tag, Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`


### `Window`

**Namespace:** `Graphics`

This class represents a window. @nosubgrouping

#### Methods

##### `Window(—)`

**Returns:** ``

Fullscreen tag Empty constructor creates a non-initialized window. This constructor is there support move semantics. Any action on non-initialized window may result in a crash.

##### `Window(monitor, {automaticplacement, size}, name, name, allowresize, visible)`

**Returns:** ``

Creates a new window @param  rect the position and the **interior** size of the window unless use outer metrics is set to true @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value. Creates a new window @param  rect the position and the **interior** size of the window unless use outer metrics is set to true @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value. Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  title of the window @param  visible after creation, window will be visible or invisible depending on this value. Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  title of the window @param  visible after creation, window will be visible or invisible depending on this value. Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value. Creates a new window at the center of the screen @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value. Creates a new window at the center of the screen @param  monitor that the window will be centered on @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `Window(monitor, {automaticplacement, size}, name, name, allowresize, visible)`

**Returns:** ``

Creates a new window at the center of the screen @param  monitor that the window will be centered on @param  size of the window @param  name of the window @param  visible after creation, window will be visible or invisible depending on this value.

##### `Window(const FullscreenTag &, const WindowManager::Monitor &monitor, const std::string &name, const std::string &title="", bool visible = true)`

**Returns:** ``

Creates a fullscreen window. Fullscreen windows do not have chrome and covers entire screen, including any panels it contains.

##### `Window(Window &&other)`

**Returns:** ``

Creates a fullscreen window. Fullscreen windows do not have chrome and covers entire screen, including any panels it contains. Copy constructor is not allowed Move constructor

##### `Swap(other)`

**Returns:** ``

##### `virtual` `Destroy(—)`

**Returns:** `virtual void`

Destroys this window Returns the OS specific data of the window. This data is used internally and should not be used unless necessary. Destroys this window

##### `Swap(other)`

**Returns:** ``

Moves another window into this one

##### `Swap(Window &other)`

**Returns:** `void`

Used for move semantics

##### `processmessages(—)`

**Returns:** `void`

This method is automatically called by the system.Unless its necessary, do not use it.  @warning Notice that it is a window manager defined behavior to handle tasks in Window classes differently or for all of them at the same time. Therefore, OS::processmessage should be used.

##### `activatecontext(—)`

**Returns:** `void`

Activates the GL context of the window. This function is used internally and should not be called unless necessary.

##### `Move({x, y})`

**Returns:** ``

Moves the window to the given position Moves the window to the given position

##### `GetExteriorBounds(—)`

**Returns:** `Geometry::Bounds`

Resizes the window to the given size. The given size is considered as the interior region of the window. The restrictions for the smallest sized window might change depending on the window manager or theme. Largest window size can be obtained using UsableScreenRegion however, this size does not exclude window chrome. This function resizes all window sized layers. Returns the exterior bounding box of the window. May throw or return invalid values if the window is not visible

##### `GetPosition(—)`

**Returns:** `Geometry::Point`

Returns the current position of the window. This value is measured from the (0,0) of the virtual screen to the top-left of the window chrome.

##### `Minimize(—)`

**Returns:** `void`

Minimizes the window. Use Restore function to return it to its previous state.

##### `IsMinimized(—)`

**Returns:** `bool`

Returns if the window is minimized

##### `Maximize(—)`

**Returns:** `void`

Maximizes the window to cover the usable area of the screen. Use Restore function to return the window to its previous size and position. Maximize might take time.

##### `IsMaximized(—)`

**Returns:** `bool`

Returns if the window is maximized

##### `Restore(—)`

**Returns:** `void`

Restores a minimized or maximized window

##### `Focus(—)`

**Returns:** `void`

Returns the monitor that the window is currently on. May throw if the window is not visible, will throw if the window is not on any currently known monitors. If this case occurs consider refreshing monitor list. Displays this window, may generate Activated event Hides this window, may generate Deactivated event Returns whether this layer is effectively visible Focuses this window

##### `IsFocused(—)`

**Returns:** `bool`

Returns if this window has the focus

##### `Close(—)`

**Returns:** `void`

Closes the window. After this function, any use of this object might fail.

##### `SetTitle(const std::string &title)`

**Returns:** `void`

Changes the title of the window to the specified string

##### `GetTitle(—)`

**Returns:** `std::string`

Returns the current title of the window.

##### `GetName(—)`

**Returns:** `std::string`

Returns the name of the window that is set at creation time

##### `IsClosed(—)`

**Returns:** `bool`

Whether the window is currently closed and cannot be acted on.

##### `ShowPointer(—)`

**Returns:** `void`

Displays the pointer. If local pointers are activated, this function will show local pointer, otherwise it will show window manager pointer

##### `HidePointer(—)`

**Returns:** `void`

Hides the pointer. If local pointers are activated, this function will hide local pointer, otherwise it will hide window manager pointer. In both cases, after calling to this function, there will be no visible pointer on the screen.

##### `IsPointerVisible(—)`

**Returns:** `bool`

Returns whether the pointer is visible

##### `SwitchToLocalPointers(—)`

**Returns:** `void`

Removes the operating system pointer and starts using Locally defined pointers. If there are no pointers added to the Pointers object, this function will throw. After switching, ShowPointer and HidePointer will show and hide local pointers not OS pointers. Calling this function will show the local pointer.

##### `SwitchToWMPointers(—)`

**Returns:** `void`

Stops showing local pointers and makes window manager pointer visible.

##### `IsLocalPointer(—)`

**Returns:** `bool`

Returns whether the current pointer is a local pointer

##### `Center(—)`

**Returns:** `void`

Centers the window to the default monitor

##### `Center(const WindowManager::Monitor &monitor)`

**Returns:** `void`

Centers the window to the given monitor

##### `SetIcon(const WindowManager::Icon &icon)`

**Returns:** `void`

Changes the icon of the window.

##### `GetMouseLocation(—)`

**Returns:** `Geometry::Point`

Renders the contents of the window Returns the mouse location on the window. If the cursor is outside the window and its position cannot be determined (-1, -1) is returned. This function can return coordinates outside the bounds of the window.

##### `PressedButtons(—)`

**Returns:** `Input::Mouse::Button`

Returns currently pressed buttons.

##### `IsLeftButtonPressed(—)`

**Returns:** `bool`

Query whether the left mouse button is pressed

##### `IsRightButtonPressed(—)`

**Returns:** `bool`

Query whether the right mouse button is pressed

##### `IsMiddleButtonPressed(—)`

**Returns:** `bool`

Query whether the middle mouse button is pressed

##### `IsX1ButtonPressed(—)`

**Returns:** `bool`

Query whether the X1 mouse button is pressed

##### `IsX2ButtonPressed(—)`

**Returns:** `bool`

Query whether the X2 mouse button is pressed

##### `SetBackground(const Graphics::RGBAf &color)`

**Returns:** `void`

Sets the background color of the window.

##### `SetBackground(const Graphics::Bitmap &bg)`

**Returns:** `void`

Sets the background of the window. This background image will be scaled with the window automatically.

##### `SetBackground(const Graphics::RectangularAnimationProvider &bg)`

**Returns:** `void`

Sets the background of the window. This background image will be scaled with the window automatically.

##### `virtual` `SetBackground(const Graphics::RectangularAnimation &bg)`

**Returns:** `virtual void`

Sets the background of the window. This background image will be scaled with the window automatically.

##### `OwnBackground(const Graphics::RectangularAnimation &bg)`

**Returns:** `void`

Sets the background of the window. This background image will be scaled with the window automatically.

##### `OwnBackground(const Graphics::Bitmap &bg)`

**Returns:** `void`

Sets the background of the window. This background image will be scaled with the window automatically.

##### `virtual` `RemoveBackground(—)`

**Returns:** `virtual void`

Removes the background of the window.

##### `HasBackground(—)`

**Returns:** `bool`

Returns if the window has a background image

##### `AllowResize(—)`

**Returns:** `void`

Returns the background image of the window. If window has no background image, this function throws. Allows window to be resized by the user

##### `PreventResize(—)`

**Returns:** `void`

Prevents window to be resized by the user

##### `UpdatePointer(—)`

**Returns:** `void`

Updates current mouse pointer if OS pointer is shown. This is called automatically.

##### `static` `GetMinimumRequiredSize(—)`

**Returns:** `static Geometry::Size`

Returns the minimum size required to fit any window inside.

##### `mouse_down(Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`

Pointer system to be used within the window @name Events @{ Called when this window is focused Called when this window is deactivated Called when this window is destroyed. Note that at this point, any reference to this object may fail. Called when user tries to close the window. Will not be called if window is closed using Destructor or Close function ### Parameters: ### **allow** `(bool &)`: setting this value to false will stop window being closed. Called after the window is moved, either by the user or programmatically Called after the window is resized, either by the user or programmatically Called after the window is minimized, either by the user or programmatically Called after the window is restored from minimized state, either by the user or programmatically Called when a key is pressed or released. This key could be a keyboard key or any other controller key including mouse. In case of mouse, this method will be triggered if mouse call is not handled by layers.  If the input device is keyboard, key down event (amount=1) is repeated if the first event is handled. The repeats will only be sent to the handler of the event. Additionally, Key up event (amount=0) is sent only to handler, if key down is handled otherwise it will be sent to all listeners.  ### Parameters: ### **Key** `(Input::Key)`: The key that is pressed or released **Amount** `(float)`: Depending on the device this can be a boolean 0 and 1, number of successive key strokes or amount of pressure (0 to 1) in analog controllers Called when a character is received. This event is raised for regular characters that can be printed. If a key is handled in keypress event, this event will not be fired. This event will be called multiple times when the key repeats. @} List of currently created windows These functions are used internally

##### `mouse_up(Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`

These functions are used internally

##### `mouse_event(Input::Mouse::EventType event, Geometry::Point location, Input::Mouse::Button button, float amount)`

**Returns:** `void`

These functions are used internally

##### `mouse_location(—)`

**Returns:** `void`

These functions are used internally

##### `Window(const WindowManager::Monitor &monitor, Geometry::Rectangle rect, const std::string &name, const std::string &title, bool allowresize, bool visible)`

**Returns:** ``

##### `deleting(Layer *layer)`

**Returns:** `void`

A window cannot be placed in another layer. This function always fails.

##### `init(—)`

**Returns:** `void`

##### `virtual` `osdestroy(—)`

**Returns:** `virtual void`

##### `redrawbg(—)`

**Returns:** `void`

##### `virtual` `resized(—)`

**Returns:** `virtual void`

##### `createglcontext(—)`

**Returns:** `void`

##### `updatedataowner(—)`

**Returns:** `void`


---

## Enums

### `resizedir`

**Namespace:** `Gorgon`


---

## Functions

### `if(issizesset)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``



### `focuschangedin(dialogadapter)`

**Returns:** ``



### `focuschangedin(baradapter)`

**Returns:** ``



### `focuschangedin(windowadapter)`

**Returns:** ``



### `focuschangedin(underadapter)`

**Returns:** ``



### `if(autobg)`

**Returns:** ``



### `if(focusedadapter == nullptr)`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `focuschangedin(dialogadapter)`

**Returns:** ``



### `focuschangedin(baradapter)`

**Returns:** ``



### `focuschangedin(windowadapter)`

**Returns:** ``



### `focuschangedin(underadapter)`

**Returns:** ``



### `focuschangedin(dialogadapter)`

**Returns:** ``



### `focuschangedin(baradapter)`

**Returns:** ``



### `focuschangedin(windowadapter)`

**Returns:** ``



### `focuschangedin(underadapter)`

**Returns:** ``



### `distributeparentboundschanged()`

**Returns:** ``



### `updatescrollvisibility()`

**Returns:** ``



### `if(autoplace)`

**Returns:** ``



### `for(auto &w : Gorgon::Window::Windows)`

**Returns:** ``



### `if(!done)`

**Returns:** ``



### `for(auto &w : Gorgon::Window::Windows)`

**Returns:** ``



### `Center()`

**Returns:** ``



### `ResizeInterior(size)`

**Returns:** ``



### `updatescrollvisibility()`

**Returns:** ``



### `Center()`

**Returns:** ``



### `if(ownicon)`

**Returns:** ``



### `OwnIcon(anim)`

**Returns:** ``



### `OwnIcon(anim)`

**Returns:** ``



### `if(ownicon)`

**Returns:** ``



### `SetIcon(value)`

**Returns:** ``



### `updatescrollvisibility()`

**Returns:** ``



### `updatescrollvisibility()`

**Returns:** ``



### `updatescrollvisibility()`

**Returns:** ``



### `if(val[2] == 1 || val[2] == 0 || !hscroll)`

**Returns:** ``



### `if(hscrollon)`

**Returns:** ``



### `if(!hscrollon)`

**Returns:** ``



### `if(val[3] == 1 || val[3] == 0 || !vscroll)`

**Returns:** ``



### `if(vscrollon)`

**Returns:** ``



### `if(!vscrollon)`

**Returns:** ``



### `if(changed)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(button == Input::Mouse::Button::Left)`

**Returns:** ``



### `if(allowmove && tag == UI::ComponentTemplate::DragTag)`

**Returns:** ``



### `if(allowresize && tag == UI::ComponentTemplate::ResizeTag)`

**Returns:** `else`



### `if(leftdist < rightdist)`

**Returns:** ``



### `if(leftdist <= maxdist)`

**Returns:** ``



### `if(rightdist <= maxdist)`

**Returns:** ``



### `if(topdist < bottomdist)`

**Returns:** ``



### `if(topdist <= maxdist)`

**Returns:** ``



### `if(bottomdist <= maxdist)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(button == Input::Mouse::Button::Left)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(moving)`

**Returns:** ``



### `if(resizing != none)`

**Returns:** `else`



### `switch(resizing)`

**Returns:** ``



### `if(allowresize && tag == UI::ComponentTemplate::ResizeTag)`

**Returns:** `else`



### `if(leftdist < rightdist)`

**Returns:** ``



### `if(leftdist <= maxdist)`

**Returns:** ``



### `if(rightdist <= maxdist)`

**Returns:** ``



### `if(topdist < bottomdist)`

**Returns:** ``



### `if(topdist <= maxdist)`

**Returns:** ``



### `if(bottomdist <= maxdist)`

**Returns:** ``



### `switch(r)`

**Returns:** ``



### `if(ptrtype == Graphics::PointerType::None)`

**Returns:** ``



### `if(moving)`

**Returns:** ``



### `switch(resizing)`

**Returns:** ``



### `switch(resizing)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(button == Input::Mouse::Button::Left && tag == UI::ComponentTemplate::CloseTag)`

**Returns:** ``



### `Close()`

**Returns:** ``



### `mouse_up(UI::ComponentTemplate::NoTag, {0, 0}, Input::Mouse::Button::Left)`

**Returns:** ``



### `mouse_up(UI::ComponentTemplate::NoTag, {0, 0}, Input::Mouse::Button::Left)`

**Returns:** ``



### `if(closebutton)`

**Returns:** ``



### `if(closebutton)`

**Returns:** ``



### `if(!updatingminmax)`

**Returns:** ``



### `if(sz.Width < minsizepx.Width && sz.Height < minsizepx.Height)`

**Returns:** ``



### `ResizeInterior(minsize)`

**Returns:** ``



### `if(sz.Width < minsizepx.Width)`

**Returns:** `else`



### `SetInteriorWidth(minsize.Width)`

**Returns:** ``



### `if(sz.Height < minsizepx.Height)`

**Returns:** `else`



### `SetInteriorHeight(minsize.Height)`

**Returns:** ``



### `if(sz.Width > maxsizepx.Width && sz.Height > maxsizepx.Height)`

**Returns:** ``



### `Resize(maxsize)`

**Returns:** ``



### `if(sz.Width > maxsizepx.Width)`

**Returns:** `else`



### `SetWidth(maxsize.Width)`

**Returns:** ``



### `if(sz.Height > maxsizepx.Height)`

**Returns:** `else`



### `SetHeight(maxsize.Height)`

**Returns:** ``



### `swap(data, other.data)`

**Returns:** ``



### `swap(pressed, other.pressed)`

**Returns:** ``



### `swap(allowresize, other.allowresize)`

**Returns:** ``



### `swap(cursorover, other.cursorover)`

**Returns:** ``



### `swap(mousedownlocation, other.mousedownlocation)`

**Returns:** ``



### `swap(mouselocation, other.mouselocation)`

**Returns:** ``



### `swap(pointerlayer, other.pointerlayer)`

**Returns:** ``



### `swap(contentslayer, other.contentslayer)`

**Returns:** ``



### `swap(bglayer, other.bglayer)`

**Returns:** ``



### `if(other.pointerlayer)`

**Returns:** ``



### `swap(iswmpointer, other.iswmpointer)`

**Returns:** ``



### `swap(showptr, other.showptr)`

**Returns:** ``



### `swap(switchbacktolocalptr, other.switchbacktolocalptr)`

**Returns:** ``



### `swap(glsize, other.glsize)`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `if(other.data)`

**Returns:** ``



### `updatedataowner()`

**Returns:** ``



### `activatecontext()`

**Returns:** ``



### `if(down)`

**Returns:** ``



### `if(down)`

**Returns:** ``



### `if(down)`

**Returns:** ``



### `for(auto &l : over.layers)`

**Returns:** ``



### `for(auto &l : newover.layers)`

**Returns:** ``



### `HidePointer()`

**Returns:** ``



### `ShowPointer()`

**Returns:** ``



### `HidePointer()`

**Returns:** ``



### `ShowPointer()`

**Returns:** ``



### `osdestroy()`

**Returns:** ``



### `redrawbg()`

**Returns:** ``



### `SetBackground(value)`

**Returns:** ``



### `redrawbg()`

**Returns:** ``



### `WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)`

**Returns:** `LRESULT __stdcall`



### `DefWindowProc(hWnd, message, wParam, lParam)`

**Returns:** `return`



### `DefWindowProc(hWnd, message, wParam, lParam)`

**Returns:** `return`



### `switch(message)`

**Returns:** ``



### `DefWindowProc(handle, message, wParam, lParam)`

**Returns:** `return`



### `if(wParam == SC_MINIMIZE)`

**Returns:** ``



### `if(wParam == SC_RESTORE && min)`

**Returns:** `else`



### `GetClientRect(parent->data->handle, &rect)`

**Returns:** ``



### `DefWindowProc(handle, message, wParam, lParam)`

**Returns:** `return`



### `if(ret == 0)`

**Returns:** ``



### `if(allowresize)`

**Returns:** ``



### `if(hwnd==INVALID_HANDLE_VALUE)`

**Returns:** ``



### `GetWindowInfo(hwnd, &wi)`

**Returns:** ``



### `SetWindowPos(hwnd, 0, rect.X, rect.Y, rect.Width, rect.Height, 0)`

**Returns:** ``



### `UpdateWindow(hwnd)`

**Returns:** ``



### `PostMessage(hwnd, WM_ACTIVATE, -1, -1)`

**Returns:** ``



### `createglcontext()`

**Returns:** ``



### `OleInitialize(NULL)`

**Returns:** ``



### `RegisterDragDrop(hwnd, &data->target)`

**Returns:** ``



### `init()`

**Returns:** ``



### `RegisterClassEx(&windclass)`

**Returns:** ``



### `if(hwnd == INVALID_HANDLE_VALUE)`

**Returns:** ``



### `UpdateWindow(hwnd)`

**Returns:** ``



### `PostMessage(hwnd, WM_ACTIVATE, -1, -1)`

**Returns:** ``



### `createglcontext()`

**Returns:** ``



### `OleInitialize(NULL)`

**Returns:** ``



### `RegisterDragDrop(hwnd, &data->target)`

**Returns:** ``



### `init()`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `DestroyWindow(data->handle)`

**Returns:** ``



### `ShowWindow(data->handle, SW_SHOW)`

**Returns:** ``



### `SetActiveWindow(data->handle)`

**Returns:** ``



### `ShowWindow(data->handle, SW_SHOW)`

**Returns:** ``



### `ShowWindow(data->handle, SW_HIDE)`

**Returns:** ``



### `if(iswmpointer)`

**Returns:** ``



### `if(data->pointerdisplayed)`

**Returns:** ``



### `SetCursor(NULL)`

**Returns:** ``



### `ShowCursor(false)`

**Returns:** ``



### `SetCursor(NULL)`

**Returns:** ``



### `ShowCursor(false)`

**Returns:** ``



### `if(iswmpointer)`

**Returns:** ``



### `if(!data->pointerdisplayed)`

**Returns:** ``



### `ShowCursor(true)`

**Returns:** ``



### `ShowCursor(true)`

**Returns:** ``



### `GetWindowInfo(data->handle, &wi)`

**Returns:** ``



### `GetClientRect(data->handle, &rect)`

**Returns:** ``



### `activatecontext()`

**Returns:** ``



### `redrawbg()`

**Returns:** ``



### `resized()`

**Returns:** ``



### `SetWindowPos(data->handle, 0, location.X, location.Y, 0, 0, SWP_NOSIZE | SWP_NOZORDER)`

**Returns:** ``



### `GetCursorPos(&p)`

**Returns:** ``



### `mouse_location()`

**Returns:** ``



### `SetPixelFormat(data->device_context, PixelFormat, &pfd)`

**Returns:** ``



### `if(data->context==NULL)`

**Returns:** ``



### `exit(0)`

**Returns:** ``



### `DestroyWindow(data->handle)`

**Returns:** ``



### `UnicodeToMByte(ret)`

**Returns:** `return`



### `GetWindowRect(data->handle, &rect)`

**Returns:** ``



### `SetFocus(data->handle)`

**Returns:** ``



### `ShowWindow(data->handle, SW_MINIMIZE)`

**Returns:** ``



### `MinimizedEvent()`

**Returns:** ``



### `ShowWindow(data->handle, SW_MAXIMIZE)`

**Returns:** ``



### `GetClientRect(data->handle, &rect)`

**Returns:** ``



### `activatecontext()`

**Returns:** ``



### `redrawbg()`

**Returns:** ``



### `ShowWindow(data->handle, SW_RESTORE)`

**Returns:** ``



### `if(data->min)`

**Returns:** ``



### `RestoredEvent()`

**Returns:** ``



### `GetClientRect(data->handle, &rect)`

**Returns:** ``



### `activatecontext()`

**Returns:** ``



### `redrawbg()`

**Returns:** ``



### `GetWindowPlacement(data->handle, &p)`

**Returns:** ``



### `SetWindowLong(data->handle, GWL_STYLE, s)`

**Returns:** ``



### `SetWindowLong(data->handle, GWL_STYLE, s)`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `SetPointer(Window &wind, Graphics::PointerType type)`

**Returns:** `void`



### `switch(type)`

**Returns:** ``



### `SetCursor(c)`

**Returns:** ``



### `getanywindow()`

**Returns:** `::Window`



### `for(auto &w : Window::Windows)`

**Returns:** ``



### `if(data && data->handle)`

**Returns:** ``



### `if(windowhandle==0)`

**Returns:** ``



### `data(new internal::windowdata)`

**Returns:** ``



### `ASSERT(WindowManager::display, "Window manager system is not initialized.")`

**Returns:** ``



### `XSetClassHint(WindowManager::display, data->handle, classhint)`

**Returns:** ``



### `XFree(classhint)`

**Returns:** ``



### `if(!allowresize)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XSetWMProtocols(WindowManager::display, data->handle, &WindowManager::WM_DELETE_WINDOW, 1)`

**Returns:** ``



### `if(visible)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XMapWindow(WindowManager::display, data->handle)`

**Returns:** ``



### `XMoveWindow(WindowManager::display, data->handle, rect.X, rect.Y)`

**Returns:** ``



### `if(autoplaced)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XMoveWindow(WindowManager::display, data->handle, rect.X, rect.Y)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `createglcontext()`

**Returns:** ``



### `init()`

**Returns:** ``



### `ASSERT(WindowManager::display, "Window manager system is not initialized.")`

**Returns:** ``



### `XSetClassHint(WindowManager::display, data->handle, classhint)`

**Returns:** ``



### `XFree(classhint)`

**Returns:** ``



### `XSetWMProtocols(WindowManager::display, data->handle, &WindowManager::WM_DELETE_WINDOW, 1)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `if(isvisible)`

**Returns:** ``



### `XMapWindow(WindowManager::display, data->handle)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `createglcontext()`

**Returns:** ``



### `init()`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `Close()`

**Returns:** ``



### `XMapWindow(WindowManager::display, data->handle)`

**Returns:** ``



### `XRaiseWindow(WindowManager::display, data->handle)`

**Returns:** ``



### `if(data->move)`

**Returns:** ``



### `XMoveWindow(WindowManager::display, data->handle, data->moveto.X, data->moveto.Y)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XUnmapWindow(WindowManager::display, data->handle)`

**Returns:** ``



### `if(iswmpointer)`

**Returns:** ``



### `if(data->pointerdisplayed)`

**Returns:** ``



### `XDefineCursor(WindowManager::display, data->handle, WindowManager::blank_cursor)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `if(iswmpointer)`

**Returns:** ``



### `if(!data->pointerdisplayed)`

**Returns:** ``



### `XDefineCursor(WindowManager::display, data->handle, 0)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `if(data->ismapped)`

**Returns:** ``



### `XMoveWindow(WindowManager::display, data->handle, location.X+borders.Left, location.Y+borders.Top)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `if(!allowresize)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XResizeWindow(WindowManager::display, data->handle, size.Width, size.Height)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XDestroyWindow(WindowManager::display, data->handle)`

**Returns:** ``



### `DestroyedEvent()`

**Returns:** ``



### `for(auto &w : windows)`

**Returns:** ``



### `if(w.data->context!=0)`

**Returns:** ``



### `if(data->context==0)`

**Returns:** ``



### `exit(1)`

**Returns:** ``



### `glXSwapBuffers(WindowManager::display, data->handle)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `if(!prop)`

**Returns:** ``



### `XFree(prop)`

**Returns:** ``



### `XGetGeometry(WindowManager::display, data->handle, &r, &x, &y, &w, &h, &bw, &d)`

**Returns:** ``



### `XTranslateCoordinates(WindowManager::display, data->handle, r, 0, 0, &x, &y, &c)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XGetInputFocus(WindowManager::display, &focused, &r)`

**Returns:** ``



### `XIconifyWindow(WindowManager::display, data->handle, 0)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `if(!allowresize)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XGetGeometry(WindowManager::display, data->handle, &r, &x, &y, &w, &h, &bw, &d)`

**Returns:** ``



### `if(!allowresize)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `for(int i=0; i<count; i++)`

**Returns:** ``



### `if(min)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(max)`

**Returns:** `else`



### `if(!allowresize)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XGetGeometry(WindowManager::display, data->handle, &r, &x, &y, &w, &h, &bw, &d)`

**Returns:** ``



### `if(!allowresize)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XFree(properties)`

**Returns:** ``



### `for(int i=0; i<count; i++)`

**Returns:** ``



### `XFree(properties)`

**Returns:** ``



### `for(int i=0; i<count; i++)`

**Returns:** ``



### `XFree(properties)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XSync(WindowManager::display, False)`

**Returns:** ``



### `XSetWMNormalHints(WindowManager::display, data->handle, sizehints)`

**Returns:** ``



### `XFlush(WindowManager::display)`

**Returns:** ``



### `XSync(WindowManager::display, False)`

**Returns:** ``



### `XFree(sizehints)`

**Returns:** ``



### `XChangeProperty(WindowManager::display, data->handle, WindowManager::XA_NET_WM_ICON, WindowManager::XA_CARDINAL, 32, PropModeReplace, icon.data->data, icon.data->w*icon.data->h+2)`

**Returns:** ``



### `XSync(WindowManager::display, 1)`

**Returns:** ``



### `mouse_location()`

**Returns:** ``



### `XNextEvent(WindowManager::display, &event)`

**Returns:** ``



### `switch(event.type)`

**Returns:** ``



### `ClosingEvent(allow)`

**Returns:** ``



### `if(allow)`

**Returns:** ``



### `Close()`

**Returns:** ``



### `if(event.xclient.message_type==WindowManager::XdndEnter)`

**Returns:** `else`



### `if(event.xclient.message_type==WindowManager::XdndPosition)`

**Returns:** `else`



### `if(event.xclient.message_type == WindowManager::XdndLeave)`

**Returns:** `else`



### `if(event.xclient.message_type == WindowManager::XdndDrop)`

**Returns:** `else`



### `activatecontext()`

**Returns:** ``



### `ResizedEvent()`

**Returns:** ``



### `redrawbg()`

**Returns:** ``



### `resized()`

**Returns:** ``



### `if(data->ppoint.X != x || data->ppoint.Y != y)`

**Returns:** ``



### `MovedEvent()`

**Returns:** ``



### `if(event.xfocus.mode == NotifyNormal)`

**Returns:** ``



### `if(!data->focused)`

**Returns:** ``



### `FocusedEvent()`

**Returns:** ``



### `if(data->focused)`

**Returns:** ``



### `LostFocusEvent()`

**Returns:** ``



### `if(event.xproperty.atom == WindowManager::XA_NET_WM_STATE)`

**Returns:** ``



### `if(minstate && !data->min)`

**Returns:** ``



### `MinimizedEvent()`

**Returns:** ``



### `if(!minstate && data->min)`

**Returns:** `else`



### `RestoredEvent()`

**Returns:** ``



### `SetPointer(Window &wind, Graphics::PointerType type)`

**Returns:** `void`



### `switch(type)`

**Returns:** ``


