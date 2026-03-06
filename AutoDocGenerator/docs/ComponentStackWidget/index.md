# ComponentStackWidget

&gt; Auto-generated documentation for the **ComponentStackWidget** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ComponentStackWidget`

**Namespace:** `Gorgon`

#### Methods

##### `if(!value)`

**Returns:** ``

##### `if(enabled && !state)`

**Returns:** ``

This function is called when the parent's enabled state changes.

##### `if(enabled && state)`

**Returns:** `else`

##### `FocusEvent(—)`

**Returns:** ``

##### `FocusEvent(—)`

**Returns:** ``

##### `SetAutosize(UI::Autosize hor, UI::Autosize ver)`

**Returns:** `void`

Adjusts autosizing of the widget. In autosize mode, set width is used to limit text width so that it will flow to next line.

##### `boundschanged(—)`

**Returns:** ``

##### `SetHorizonalAutosize(UI::Autosize value)`

**Returns:** `void`

Adjusts autosizing of the widget. In autosize mode, set width is used to limit text width so that it will flow to next line.

##### `boundschanged(—)`

**Returns:** ``

##### `SetVerticalAutosize(UI::Autosize value)`

**Returns:** `void`

Adjusts autosizing of the widget. In autosize mode, set width is used to limit text width so that it will flow to next line.

##### `boundschanged(—)`

**Returns:** ``

##### `SetAutosize(bool hor, bool ver)`

**Returns:** `void`

Adjusts autosizing of the widget. Setting autosize to true sets the autosize to automatic to nearest unit size

##### `SetAutosize(hor ? Autosize::Unit : Autosize::None, ver ? Autosize::Automatic : Autosize::None)`

**Returns:** ``

##### `SetHorizonalAutosize(bool value)`

**Returns:** `void`

Adjusts autosizing of the widget. Setting autosize to true sets the autosize to automatic to nearest unit size

##### `SetHorizonalAutosize(value ? Autosize::Unit : Autosize::None)`

**Returns:** ``

##### `SetVerticalAutosize(bool value)`

**Returns:** `void`

Adjusts autosizing of the widget. Setting autosize to true sets the autosize to automatic to nearest unit size

##### `SetVerticalAutosize(value ? Autosize::Automatic : Autosize::None)`

**Returns:** ``

##### `GetHorizontalAutosize(—)`

**Returns:** `UI::Autosize`

Returns the horizontal autosize mode of the widget

##### `GetVerticalAutosize(—)`

**Returns:** `UI::Autosize`

Returns the horizontal autosize mode of the widget

##### `boundschanged(—)`

**Returns:** ``

##### `boundschanged(—)`

**Returns:** ``


---

## Functions

### `SetTextWrap(const bool &value)`

**Returns:** `void`



### `GetTextWrap()`

**Returns:** `bool`



### `PROPERTY_GETSET(cls, Boolean, bool, TextWrap)`

**Returns:** ``


