# PetContainer

&gt; Auto-generated documentation for the **PetContainer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `PetContainer`

**Namespace:** `gge`

#### Methods

##### `virtual` `Resize(utils::Size Size)`

**Returns:** `virtual void`

##### `Detach(—)`

**Returns:** `void`

##### `virtual` `IsActive(—)`

**Returns:** `virtual bool`

##### `virtual` `Deactivate(—)`

**Returns:** `virtual void`

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

##### `virtual` `Show(bool setfocus=false)`

**Returns:** `virtual void`

##### `virtual` `Hide(—)`

**Returns:** `virtual void`

##### `virtual` `focus_changed(WidgetBase *newwidget)`

**Returns:** `virtual void`

##### `if(newwidget)`

**Returns:** ``

##### `AttachTo(LayerBase *layer, int order=0)`

**Returns:** `void`

##### `if(layer)`

**Returns:** ``

##### `AttachTo(LayerBase &layer, int order=0)`

**Returns:** `void`

##### `AttachTo(&layer, order)`

**Returns:** ``

##### `InformEnabledChange(bool state)`

**Returns:** `void`

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_containerenabledchanged(*it, state)`

**Returns:** ``

##### `KeyboardEvent(input::keyboard::Event event)`

**Returns:** `bool`

##### `if(Focused)`

**Returns:** ``


### `ExtendedPetContiner`

**Namespace:** `gge`

#### Methods

##### `AttachTo(LayerBase *layer, ExtenderLayer *extender, int order=0)`

**Returns:** `void`

##### `if(layer && extender)`

**Returns:** ``

##### `AttachTo(LayerBase &layer, LayerBase &extender, int order=0)`

**Returns:** `void`

##### `AttachTo(&layer, &extender, order)`

**Returns:** ``

