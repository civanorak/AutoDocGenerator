# ColorPlane

&gt; Auto-generated documentation for the **ColorPlane** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ColorPlane`

**Namespace:** `Gorgon`

#### Methods

##### `ColorPlane(const UI::Template &temp)`

**Returns:** `explicit`

##### `GetValue(—)`

**Returns:** `ColorType`

Returns the current color

##### `SetValue(const ColorType &value)`

**Returns:** `void`

Sets the color. If the color does not match any color exactly, nothing will be shown as selected.

##### `Refresh(—)`

**Returns:** ``

##### `ChangedEvent(value)`

**Returns:** ``

##### `SetValue(value)`

**Returns:** ``

Sets the color. If the color does not match any color exactly, nothing will be shown as selected.

##### `ColorType(—)`

**Returns:** `operator`

Returns the current color

##### `GetValue(—)`

**Returns:** `return`

##### `Focus(—)`

**Returns:** `return`

##### `Refresh(—)`

**Returns:** `void`

##### `PROPERTY_REFRESH_VN(ColorPlane, Density, HueDensity, huedensity)`

**Returns:** ``

Huedensity changes the number of different hue values displayed

##### `PROPERTY_REFRESH_VN(ColorPlane, Density, LCDensity, lcdensity)`

**Returns:** ``

LCDensity changes the number of different luminance chromacity pairs displayed

##### `PROPERTY_REFRESH_VN(ColorPlane, Boolean, bool, Alpha, alpha)`

**Returns:** ``

Controls whether alpha channel will be displayed

##### `click(Geometry::Point location)`

**Returns:** `void`

##### `getinteriorsize(—)`

**Returns:** `Geometry::Size`


---

## Enums

### `Mode`

**Namespace:** `Gorgon`

Color plane modes


### `Density`

**Namespace:** `Gorgon`

Display density constants


---

## Functions

### `Refresh()`

**Returns:** ``



### `if(oldsz != newsz)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `if(location.Y > halftableoffset.Y)`

**Returns:** `else`



### `if(l.Y == 0)`

**Returns:** ``



### `if(l.Y == 1)`

**Returns:** ``



### `if(l.Y == 0)`

**Returns:** `else`



### `switch(halftablerow)`

**Returns:** ``



### `if(location.Y > colortableoffset.Y)`

**Returns:** `else`



### `if(location.Y > grayscaleoffset.Y)`

**Returns:** `else`



### `if(found && color != this->color)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `ChangedEvent(color)`

**Returns:** ``



### `ClickedEvent(alphaclick)`

**Returns:** ``



### `if(alpha)`

**Returns:** ``



### `for(int xx=0; xx<totw; xx++)`

**Returns:** ``



### `if(color == basecolor)`

**Returns:** ``



### `for(int c=0; c<huetable.size()`

**Returns:** ``



### `for(auto p : lctable)`

**Returns:** ``



### `for(auto hue : huetable)`

**Returns:** ``



### `if(alpha)`

**Returns:** ``



### `for(int a=0; a<huetable.size()`

**Returns:** ``



### `if(this->color.A == c.A)`

**Returns:** ``



### `if(selected)`

**Returns:** ``


