# ComboboxBase

> Auto-generated documentation for the **ComboboxBase** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ComboboxType`

**Namespace:** `gge`


### `Base`

**Namespace:** `combobox`

#### Methods

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `virtual` `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `setblueprint(bp)`

**Returns:** ``

##### `virtual` `Resize(utils::Size Size)`

**Returns:** `virtual void`

##### `virtual` `Move(utils::Point Location)`

**Returns:** `virtual void`

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key key)`

**Returns:** `virtual bool`

##### `shrink(—)`

**Returns:** ``

##### `if(!isextended && key==KeyCodes::Enter)`

**Returns:** ``

##### `extend(—)`

**Returns:** ``

##### `if(key==KeyCodes::Down)`

**Returns:** ``

##### `if(key==KeyCodes::Up)`

**Returns:** ``

##### `if(key==KeyCodes::PageDown)`

**Returns:** ``

##### `if(key==KeyCodes::PageUp)`

**Returns:** ``

##### `if(target<0)`

**Returns:** ``

##### `if(key==KeyCodes::Home)`

**Returns:** ``

##### `if(key==KeyCodes::End)`

**Returns:** ``

##### `virtual` `IsExtended(—)`

**Returns:** `virtual bool`

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`

##### `virtual` `add(typename A_::paramtype item)`

**Returns:** `virtual void`

##### `virtual` `insert(typename A_::paramtype item, unsigned before)`

**Returns:** `virtual void`

##### `virtual` `remove(unsigned before)`

**Returns:** `virtual void`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `shrink(—)`

**Returns:** ``

##### `if(force)`

**Returns:** ``

##### `virtual` `detach(ContainerBase *container)`

**Returns:** `virtual bool`

##### `textbox_mouse(input::mouse::Event event)`

**Returns:** `bool`

##### `dropbutton_focus(—)`

**Returns:** `void`

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `virtual` `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `if(container)`

**Returns:** ``

##### `virtual` `extend(—)`

**Returns:** `virtual void`

##### `if(!isextended)`

**Returns:** ``

##### `virtual` `shrink(—)`

**Returns:** `virtual void`

##### `if(isextended)`

**Returns:** ``

##### `virtual` `valuechanged(—)`

**Returns:** `virtual void`

##### `setvalue(typename A_::paramtype &value)`

**Returns:** `void`

##### `if(this->value!=value)`

**Returns:** ``

##### `if(isextended)`

**Returns:** ``

##### `CS_(value, str)`

**Returns:** ``

##### `valuechanged(—)`

**Returns:** ``

##### `getvalue(—)`

**Returns:** `T_`

##### `container_scrolling(bool &allow)`

**Returns:** `void`

##### `setAutoUpdate(const bool &value)`

**Returns:** `void`

##### `getAutoUpdate(—)`

**Returns:** `bool`


---

## Functions

### `CastToString(const T_ &v, std::string &str)`

**Returns:** `void`



### `CastFromString(T_ &v, const std::string &str)`

**Returns:** `void`



### `if(this->bp->Listbox)`

**Returns:** ``



### `Resize(size)`

**Returns:** ``


