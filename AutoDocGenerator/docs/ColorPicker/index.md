# ColorPicker

> Auto-generated documentation for the **ColorPicker** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ColorPicker`

**Namespace:** `Gorgon`

#### Methods

##### `ColorPicker(const UI::Template &temp)`

**Returns:** `explicit`

##### `Open(—)`

**Returns:** `void`

Opens the color panel

##### `Close(—)`

**Returns:** `void`

Closes the color panel

##### `Toggle(—)`

**Returns:** `void`

Toggles open/close state of the dropdown

##### `IsOpened(—)`

**Returns:** `bool`

Returns whether the color plane is open

##### `Refresh(—)`

**Returns:** `void`

Refreshes the contents of the color plane

##### `SetDisplay(const DisplayType &value)`

**Returns:** `void`

Changes how the color is displayed

##### `GetDisplay(—)`

**Returns:** `DisplayType`

Returns how the color is displayed

##### `PROPERTY_REFRESH_VN(ColorPicker, Density, HueDensity, huedensity)`

**Returns:** ``

Huedensity changes the number of different hue values displayed

##### `PROPERTY_REFRESH_VN(ColorPicker, Density, LCDensity, lcdensity)`

**Returns:** ``

LCDensity changes the number of different luminance chromacity pairs displayed

##### `PROPERTY_REFRESH_VN(ColorPicker, Boolean, bool, Alpha, alpha)`

**Returns:** ``

Controls whether alpha channel will be displayed

##### `PROPERTY_REFRESH_VN(ColorPicker, Geometry::basic_Size, Geometry::Size, PlaneSize, defaultsize)`

**Returns:** ``

Changes the size of the plane

##### `PROPERTY_GETSET(ColorPicker, DisplayType, Display)`

**Returns:** ``

##### `parentboundschanged(—)`

**Returns:** ``

##### `Close(—)`

**Returns:** ``

##### `Open(—)`

**Returns:** ``

##### `checkfocus(—)`

**Returns:** `void`


### `ColorPicker`

**Namespace:** `gge`

#### Methods

##### `Draw(—)`

**Returns:** ``

##### `ChangeEvent(—)`

**Returns:** ``

##### `if(event==gge::input::mouse::Event::Move)`

**Returns:** ``

##### `if(location.x>=64)`

**Returns:** ``

##### `draw(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `if(event==gge::input::mouse::Event::Left_Click)`

**Returns:** `else`

##### `if(location.x<64)`

**Returns:** ``

##### `ChangeEvent(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `if(event==gge::input::mouse::Event::Out)`

**Returns:** `else`

##### `Draw(—)`

**Returns:** ``

##### `Resize(160, 40)`

**Returns:** ``

##### `virtual` `SetBlueprint(const gge::widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `virtual` `Resize(gge::utils::Size Size)`

**Returns:** `virtual void`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `drawpixel(int row, int col, graphics::RGBint color)`

**Returns:** `void`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `for(int i=0;i<16;i++)`

**Returns:** ``

##### `for(int i=0;i<8;i++)`

**Returns:** ``

##### `for(int h=0;h<16;h++)`

**Returns:** ``

##### `for(int i=0;i<9;i++)`

**Returns:** ``

##### `drawpixel(i, 20, tempcolor)`

**Returns:** ``

##### `for(int i=0;i<9;i++)`

**Returns:** ``

##### `drawpixel(i, 17, tempcolor)`

**Returns:** ``

##### `drawpixel(i, 18, tempcolor)`

**Returns:** ``

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `virtual` `detach(gge::widgets::ContainerBase *container)`

**Returns:** `virtual bool`

##### `virtual` `located(gge::widgets::ContainerBase* container, gge::utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `if(container)`

**Returns:** ``

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `if(force)`

**Returns:** ``

##### `lch_rgb(float l, float c, float h)`

**Returns:** `graphics::RGBint`

##### `setValue(const graphics::RGBint &value)`

**Returns:** `void`

##### `draw(—)`

**Returns:** ``

##### `getValue(—)`

**Returns:** `graphics::RGBint`


---

## Functions

### `updatevaluedisplay(false)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::ButtonTag)`

**Returns:** ``



### `Toggle()`

**Returns:** ``



### `mouseup(tag, location, btn)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::ButtonTag)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `mousedown(tag, location, btn)`

**Returns:** ``



### `ChangedEvent(*this)`

**Returns:** ``



### `Close()`

**Returns:** ``



### `SelectAll()`

**Returns:** ``



### `updatevaluedisplay(true)`

**Returns:** ``



### `Close()`

**Returns:** ``



### `Open()`

**Returns:** ``



### `if(below < defaultsize.Height && above > below)`

**Returns:** ``



### `if(targetx < 0)`

**Returns:** ``



### `if(reversed)`

**Returns:** ``



### `Close()`

**Returns:** ``


