# LayerAdapter

&gt; Auto-generated documentation for the **LayerAdapter** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `LayerAdapter`

**Namespace:** `Gorgon`

#### Methods

##### `LayerAdapter(—)`

**Returns:** ``

This constructor will leave the LayerAdapter in an invalid state. You must use SetLayer before calling any other functions.

##### `SetFocusStrategy(Deny)`

**Returns:** ``

Constructor requires the base layer

##### `ResizeInterior({size, interiorsize.Height})`

**Returns:** `return`

##### `ResizeInterior({interiorsize.Width, size})`

**Returns:** `return`

##### `IsReady(—)`

**Returns:** `bool`

Returns true if this adapter can be used.

##### `SetLayer(Gorgon::Layer &value)`

**Returns:** `void`

Sets the base layer

##### `SetSizes(int spacing, int unitwidth)`

**Returns:** `void`

Returns the base layer The spacing should be left between widgets Returns the unit width for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Overrides default spacing and unitwidth

##### `UseDefaultSizes(—)`

**Returns:** `void`

Return to use default sizes

##### `focushandler(—)`

**Returns:** ``


---

## Functions

### `if(issizesset)`

**Returns:** ``



### `if(issizesset)`

**Returns:** ``



### `if(base)`

**Returns:** ``


