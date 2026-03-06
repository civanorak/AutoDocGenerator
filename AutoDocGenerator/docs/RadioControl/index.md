# RadioControl

&gt; Auto-generated documentation for the **RadioControl** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `RadioControl`

**Namespace:** `Gorgon`

#### Methods

##### `for(auto p : elements)`

**Returns:** ``

Default constructor. Use filling constructor if possible. No copying. Filling constructor that prepares RadioControl from the start. This variant will not own its children.

##### `for(auto p : elements)`

**Returns:** ``

##### `for(auto p : elements)`

**Returns:** ``

Filling constructor that prepares RadioControl from the start. This variant will own its children.

##### `for(auto p : elements)`

**Returns:** ``

##### `Set(value)`

**Returns:** ``

Assigns a new value to the radio control. If the specified value exists in the, it will be selected, if not, nothing will be selected.

##### `T_(—)`

**Returns:** `operator`

Returns the current value

##### `Set(const T_ value)`

**Returns:** `bool`

Assigns a new value to the radio control. If the specified value exists in the, it will be selected, if not, nothing will be selected and this function will return false.

##### `clearall(—)`

**Returns:** ``

##### `ChangedEvent(current)`

**Returns:** ``

##### `Get(—)`

**Returns:** `T_`

Returns the current value

##### `Exists(const T_ value)`

**Returns:** `bool`

Returns if the given element exists

##### `Add(const T_ value, CT_ &control)`

**Returns:** `void`

Adds the given element to this controller

##### `ChangeValue(const T_ &before, const T_ &after)`

**Returns:** `void`

Changes the value of the given element

##### `PlaceIn(C_ &container, Geometry::Point start, int spacing)`

**Returns:** `void`

This function will add all widgets in this controller to the given container. If any member is not a widget, it will be ignored.

##### `for(auto p : elements)`

**Returns:** ``

##### `if(col%columns == 0)`

**Returns:** ``

##### `begin(—)`

**Returns:** `auto`

Allows access to controllers Allows access to controllers For iteration

##### `end(—)`

**Returns:** `auto`

For iteration

##### `begin(—)`

**Returns:** `auto`

For iteration

##### `end(—)`

**Returns:** `auto`

For iteration

##### `SetColumns(int value)`

**Returns:** `void`

Changes the number of columns when placing the widgets

##### `GetColumns(—)`

**Returns:** `int`

Returns the number of columns when placing the widgets

##### `changing(TwoStateControl &control, bool state, bool &allow)`

**Returns:** `void`

##### `if(!state)`

**Returns:** ``

##### `clearall(—)`

**Returns:** ``

##### `ChangedEvent(current)`

**Returns:** ``

##### `clearall(—)`

**Returns:** `void`

##### `for(auto p : elements)`

**Returns:** ``

##### `virtual` `elementadded(const T_ &index)`

**Returns:** `virtual void`

