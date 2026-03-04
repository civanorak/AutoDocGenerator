# TabPanel

> Auto-generated documentation for the **TabPanel** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `Tab`

**Namespace:** `Gorgon`

#### Methods

##### `GetKey(—)`

**Returns:** `Key_`

##### `SetKey(const Key_ &value)`

**Returns:** `void`

##### `GetTitle(—)`

**Returns:** `std::string`

##### `SetTitle(const std::string &value)`

**Returns:** `void`

##### `PROPERTY_GETSET(Tab, Key_, Key)`

**Returns:** ``

##### `PROPERTY_GETSET(Tab, std::string, Title)`

**Returns:** ``


### `basic_TabPanel`

**Namespace:** `Gorgon`

#### Methods

##### `Focus(—)`

**Returns:** ``

Any excess buttons will be hidden Buttons can be scrolled vertically Buttons can be scrolled horizontally Buttons are shown in multiple lines Buttons are forced to a scale that will fit the bar Excess buttons are grouped in a list Construct a new panel

##### `if(!updating)`

**Returns:** ``

##### `Activate(key)`

**Returns:** ``

##### `Refresh(—)`

**Returns:** ``

##### `switch(sizing)`

**Returns:** ``

Construct a new panel Create a new tab with the given key and title

##### `Activate(key)`

**Returns:** ``

##### `Refresh(—)`

**Returns:** ``

##### `New(const std::string &title)`

**Returns:** ``

Create a new tab with the given key, title will be determined from the key Create a new tab with the given title, key will be determined from the title

##### `Remove(const Key_ &key)`

**Returns:** `void`

Create a new tab with the given key and title. The tab will be inserted before the given key. If the key does not exist, new tab will be appended to the end. Create a new tab with the given key, title will be determined from the title. The tab will be inserted before the given key. If the key does not exist, new tab will be appended to the end. Create a new tab with the given title, key will be determined from the title. The tab will be inserted before the given key. If the key does not exist, new tab will be appended to the end. Remove the tab at the given key

##### `MoveBefore(const Key_ &tab, const Key_ &before)`

**Returns:** `void`

Moves the tab at the given key before another tab. If the before tab does not exit, the tab will be moved to the end.

##### `Exists(const Key_ &key)`

**Returns:** `bool`

Return the tab with the supplied key Return the tab with the supplied key Returns true if the tab with the given key exist

##### `Activate(const Key_ &key)`

**Returns:** `void`

Activates the tab with the key. If key does not exist nothing is done.

##### `Clear(—)`

**Returns:** ``

##### `Add(mapping[key])`

**Returns:** ``

##### `Deactivate(—)`

**Returns:** `void`

Deactivate the currently active tab.

##### `ActivateNext(—)`

**Returns:** `void`

Activates the next tab

##### `if(rollover)`

**Returns:** ``

##### `ActivatePrevious(—)`

**Returns:** `void`

Activates the previous tab

##### `if(ind == 0)`

**Returns:** ``

##### `if(rollover)`

**Returns:** ``

##### `HasActiveTab(—)`

**Returns:** `bool`

Returns if there is an active tab.

##### `SetButtonSizing(ButtonSizing value)`

**Returns:** `void`

Returns the currently active tab. Throws is there is no active tab. Returns the currently active tab. Throws is there is no active tab. Set how the tab buttons will be resized. Default is AutoUnit

##### `for(auto &button : buttons)`

**Returns:** ``

##### `switch(sizing)`

**Returns:** ``

##### `Refresh(—)`

**Returns:** ``

##### `GetButtonSizing(—)`

**Returns:** `ButtonSizing`

Returns how the tab buttons will be resized

##### `SetButtonTextWrap(bool value)`

**Returns:** `void`

Sets if the button text would be wrapped. If true, current tab size will be used to determine wrap width. Default value is false.

##### `Refresh(—)`

**Returns:** ``

##### `GetButtonTextWrap(—)`

**Returns:** `bool`

Returns if the button text would wrapped.

##### `SetButtonOverflow(ButtonOverflow value)`

**Returns:** `void`

Sets how the overflowing tab buttons are managed. Default is Scale. Some options are not implemented yet and will default to Scale.

##### `Refresh(—)`

**Returns:** ``

##### `GetButtonOverflow(—)`

**Returns:** `ButtonOverflow`

Returns how the overflowing tab buttons are managed.

##### `SetButtonSize(int w, int h)`

**Returns:** `void`

Sets the size of the tab buttons. The size will be used according to ButtonSizing.

##### `SetButtonSize({w, h})`

**Returns:** ``

##### `SetButtonSize(const Geometry::Size &value)`

**Returns:** `void`

Sets the size of the tab buttons. The size will be used according to ButtonSizing.

##### `Refresh(—)`

**Returns:** ``

##### `SetButtonWidth(int size)`

**Returns:** `void`

##### `SetButtonSize(size, buttonsize.Height)`

**Returns:** ``

##### `SetButtonHeight(int size)`

**Returns:** `void`

##### `SetButtonSize(buttonsize.Width, size)`

**Returns:** ``

##### `GetButtonSize(—)`

**Returns:** `Geometry::Size`

Returns the size of the buttons

##### `SetTabRollover(bool value)`

**Returns:** `void`

Sets if next or previous tab switches will rollover. Default is false

##### `GetTabRollover(—)`

**Returns:** `bool`

Returns if next or previous tab switches will rollover.

##### `Refresh(—)`

**Returns:** `void`

Refreshes the tab buttons and their locations. This function is called automatically.

##### `for(int i=0; i<tabs.GetCount()`

**Returns:** ``

##### `if(buttonspnl)`

**Returns:** ``

##### `for(auto &tab : tabs)`

**Returns:** ``

##### `begin(—)`

**Returns:** `auto`

Used to enumerate tabs

##### `begin(—)`

**Returns:** `auto`

Used to enumerate tabs

##### `end(—)`

**Returns:** `auto`

Used to enumerate tabs

##### `end(—)`

**Returns:** `auto`

Used to enumerate tabs

##### `if(key == Keycodes::Tab)`

**Returns:** ``

##### `if(Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::Ctrl)`

**Returns:** ``

##### `ActivateNext(—)`

**Returns:** ``

##### `if(Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::ShiftCtrl)`

**Returns:** `else`

##### `ActivatePrevious(—)`

**Returns:** ``

##### `getbtns(const UI::Template& temp)`

**Returns:** `UI::Widget*`


---

## Enums

### `ButtonSizing`

**Namespace:** `Gorgon`

Enumeration that controls how tab buttons are sized


### `ButtonOverflow`

**Namespace:** `Gorgon`

Size is automatic depending on the title length Size is the smallest integer unit size that the title will fit into Only the given size is used Fills the full width of the tab bar Fills the full width of the container but will the given size is used as maximum Enumeration that controls how the overflow in buttons is treated

