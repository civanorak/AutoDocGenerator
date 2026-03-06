# Dropdown

&gt; Auto-generated documentation for the **Dropdown** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `for(auto it = begin; it != end; ++it)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `Toggle()`

**Returns:** ``



### `Refresh()`

**Returns:** `virtual void`


Refreshes the dropdown. Normally this is not required unless references of the data contained within the list is updated without any modification to the dropdown. This is intended to be overloaded.


### `Open()`

**Returns:** `void`


Opens the list


### `BeforeOpenEvent()`

**Returns:** ``



### `if(below < defaultheight && above > below)`

**Returns:** ``



### `if(!fit)`

**Returns:** ``



### `if(reversed)`

**Returns:** ``



### `if(refresh)`

**Returns:** ``



### `Close()`

**Returns:** `void`


Closes the list


### `Toggle()`

**Returns:** `void`


Toggles open/close state of the dropdown


### `Close()`

**Returns:** ``



### `Open()`

**Returns:** ``



### `IsOpened()`

**Returns:** `bool`


Returns whether the dropdown is opened


### `IsReversed()`

**Returns:** `bool`


Retuns if the list will be opened above the dropdown instead of below. This can happen if there is not enough space below. Currently this function will return false if the dropdown is not open.


### `if(status && key == Input::Keyboard::Keycodes::Space)`

**Returns:** ``



### `Toggle()`

**Returns:** ``



### `parentboundschanged()`

**Returns:** ``



### `Close()`

**Returns:** ``



### `Open()`

**Returns:** ``



### `checkfocus()`

**Returns:** `void`



### `Close()`

**Returns:** ``



### `ChangedEvent(-1)`

**Returns:** ``



### `for(auto it = begin; it != end; ++it)`

**Returns:** ``



### `SetSelectedIndex(long index)`

**Returns:** `void`


Changes selection to the given item. If it is not found this function will throw. Changes the selection to the given index.


### `Get()`

**Returns:** `T_`


Returns the currently selected item. If nothing is selected, this will throw. Returns the currently selected item. Changing the selected item does not update dropdown automatically. If nothing is selected, this will throw. Returns the currently selected item. If nothing is selected, this will throw.


### `if(index == -1)`

**Returns:** `*`



### `if(Coffee == Latte)`

**Returns:** `*`



### `switch(Coffee)`

**Returns:** `*`


