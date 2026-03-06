# Composer

&gt; Auto-generated documentation for the **Composer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Composer`

**Namespace:** `Gorgon`

#### Methods

##### `Resize(size)`

**Returns:** ``

##### `SetWidth(size)`

**Returns:** ``

##### `SetHeight(size)`

**Returns:** ``

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `distributeparentenabled(value)`

**Returns:** ``

##### `Composer(const UI::UnitSize &size)`

**Returns:** ``

This function should be called whenever a key is pressed or released. This function should be called whenever a character is received from operating system.

##### `SetSizes(int spacing, int unitwidth)`

**Returns:** `void`

The spacing should be left between widgets Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Overrides default spacing and unitwidth

##### `UseDefaultSizes(—)`

**Returns:** `void`

Return to use default sizes

##### `distributeparentenabled(state)`

**Returns:** ``

##### `distributeparentenabled(state)`

**Returns:** ``

##### `distributeparentboundschanged(—)`

**Returns:** ``


### `ComponentStackComposer`

**Namespace:** `Gorgon`

#### Methods

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `distributeparentenabled(value)`

**Returns:** ``

##### `Resize(size, {false, false})`

**Returns:** ``

This function should be called whenever a key is pressed or released. This function should be called whenever a character is received from operating system.

##### `Resize(const UI::UnitSize &size, std::pair<bool, bool> interiorsized)`

**Returns:** `void`

##### `distributeparentenabled(state)`

**Returns:** ``

##### `distributeparentenabled(state)`

**Returns:** ``

##### `distributeparentboundschanged(—)`

**Returns:** ``

##### `SetSizes(int spacing, int unitwidth)`

**Returns:** `void`

The spacing should be left between widgets Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Overrides default spacing and unitwidth

##### `UseDefaultSizes(—)`

**Returns:** `void`

Return to use default sizes

##### `distributeparentboundschanged(—)`

**Returns:** ``


---

## Functions

### `Resize(size)`

**Returns:** ``



### `mouseenter()`

**Returns:** ``



### `mouseleave()`

**Returns:** ``



### `FocusFirst()`

**Returns:** ``



### `for(auto &w : widgets)`

**Returns:** ``



### `FocusFirst()`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `boundschanged()`

**Returns:** ``



### `boundschanged()`

**Returns:** ``



### `boundschanged()`

**Returns:** ``



### `boundschanged()`

**Returns:** ``



### `if(ans.Extender)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``



### `FocusFirst()`

**Returns:** ``



### `for(auto &w : widgets)`

**Returns:** ``



### `FocusFirst()`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `RemoveFocus()`

**Returns:** ``



### `if(interiorsized.first || interiorsized.second)`

**Returns:** ``



### `if(ans.Extender)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``


