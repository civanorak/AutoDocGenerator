# DialogWindow

&gt; Auto-generated documentation for the **DialogWindow** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `DialogWindow`

**Namespace:** `Gorgon`

#### Methods

##### `DialogWindow(const UI::Template &temp, const std::string &title = "", AutoplaceTarget autoplace = DialogLevel)`

**Returns:** `explicit`

##### `DialogWindow(const UI::Template &temp, const std::string &title, const UI::UnitSize size, AutoplaceTarget autoplace = DialogLevel)`

**Returns:** ``

##### `RemoveButton(Widget &w)`

**Returns:** `void`

Returns the organizer that manages buttons area. Adds a new button to the buttons area of the dialog window. DialogWindow owns this button. Removes a widget from the buttons area


### `DialogWindow`

**Namespace:** `gge`

#### Methods

##### `setblueprint(*WR.Panels.DialogWindow)`

**Returns:** ``

##### `AddDialogButton(WidgetBase &item)`

**Returns:** `void`

##### `placedialogbutton(item)`

**Returns:** ``

##### `InsertDialogButton(WidgetBase &item, const WidgetBase &before)`

**Returns:** `void`

##### `placedialogbutton(item)`

**Returns:** ``

##### `RemoveDialogButton(WidgetBase &item)`

**Returns:** `void`

##### `DeleteDialogButton(WidgetBase &item)`

**Returns:** `void`

##### `ClearDialogButtons(—)`

**Returns:** `void`

##### `for(auto i=dialogbuttons.First()`

**Returns:** ``

##### `GetDialogButtonCount(—)`

**Returns:** `int`

##### `virtual` `ForcedRollDown(—)`

**Returns:** `virtual void`

##### `virtual` `ForcedRollUp(—)`

**Returns:** `virtual void`

##### `wr_loaded(—)`

**Returns:** `void`

##### `setblueprint(*WR.Panels.DialogWindow)`

**Returns:** ``


---

## Enums

### `AutoplaceTarget`

**Namespace:** `Gorgon`


---

## Functions

### `if(autoplace != None)`

**Returns:** ``



### `for(auto &w : Gorgon::Window::Windows)`

**Returns:** ``



### `if(!done)`

**Returns:** ``



### `for(auto &w : Gorgon::Window::Windows)`

**Returns:** ``



### `Center()`

**Returns:** ``



### `if(ind != -1)`

**Returns:** ``



### `ResizeInterior(size)`

**Returns:** ``



### `updatescrollvisibility()`

**Returns:** ``



### `Center()`

**Returns:** ``



### `Own(*btn)`

**Returns:** ``


