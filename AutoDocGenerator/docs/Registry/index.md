# Registry

> Auto-generated documentation for the **Registry** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `Registry`

**Namespace:** `Gorgon`

#### Methods

##### `Activate(—)`

**Returns:** ``

Do not use this value Default constructor

##### `for(auto t : templates)`

**Returns:** ``

Destroys all stored templates

##### `Activate(—)`

**Returns:** `void`

Activates this registry to be used to provide templates

##### `Changed(—)`

**Returns:** ``

##### `ASSERT(active, "UI is not initialized.")`

**Returns:** ``

##### `if(templates[type] == nullptr)`

**Returns:** ``

Returns the template for the requested type.

##### `virtual` `Forecolor(Graphics::Color::Designation designation)`

**Returns:** `virtual Graphics::RGBA`

Returns the foreground color for the requested designation.

##### `virtual` `Backcolor(Graphics::Color::Designation designation)`

**Returns:** `virtual Graphics::RGBA`

Returns the background for the requested designation.

##### `virtual` `GetSpacing(—)`

**Returns:** `virtual int`

Returns an printer instance that will render the requested text style Returns an advanced printer instance that will be able to render any text style The spacing should be left between widgets

##### `virtual` `GetEmSize(—)`

**Returns:** `virtual int`

The size of EM space. Roughly the same size as the height of a character.

##### `virtual` `GetUnitSize(—)`

**Returns:** `virtual int`

Returns the unit size for a widget. This size is enough to have a bordered icon. Widgets should be sized according to unit width and spacing. A single unit width would be too small for most widgets. Multiple units can be obtained by GetUnitSize(n)

##### `GetUnitSize(int n)`

**Returns:** `int`

Returns the width for a n-sized widget. Generally, 1 is for icons, 2 is for numberbox, 3 can be used for buttons, labels, short textboxes 4 for textboxes, 6 is for checkboxes. Standard panels can contain 6 units and they are less than 7 units wide.


### `PresetRegistry`

**Namespace:** `Gorgon`

Fired when the active registry is changed. This function should return a template for the given type. Due to being used in constructors you are not allowed to reject template type. If the generator is capable of generating a similar template, simply return that one instead of throwing (ie. return Panel_Regular instead of Panel_Top if Panel_Top is not supported). If that is not possible as well, return a template with a fixed error image/text. Stores the templates. Mutable to allow late loading.

#### Methods

##### `Add(TemplateType type, UI::Template &temp)`

**Returns:** `void`

Add the given template to the registry, transferring ownership. If a template with the same type exists, it will be deleted.

##### `SetSpacing(const int tspacing)`

**Returns:** `void`

##### `SetEmSize(const int size)`

**Returns:** `void`

##### `virtual` `SetColors(Graphics::Color::PairPack colors)`

**Returns:** `virtual void`

Sets the colors that will be provided by this registry

##### `swap(colors, this->colors)`

**Returns:** ``


---

## Enums

### `TemplateType`

**Namespace:** `Gorgon`

This enum lists all possible template types. All registries should be able to provide a template for each time, even if the template is completely empty.

