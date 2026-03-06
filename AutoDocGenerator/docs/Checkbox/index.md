# Checkbox

&gt; Auto-generated documentation for the **Checkbox** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Checkbox`

**Namespace:** `Gorgon`

#### Methods

##### `Checkbox(const UI::Template &temp, std::string text, bool state)`

**Returns:** ``

##### `SetText(const std::string &value)`

**Returns:** `void`

##### `GetText(—)`

**Returns:** `std::string`

##### `SetIcon(const Graphics::Bitmap &value)`

**Returns:** `void`

Returns the state of the checkbox Changes the state of the checkbox Changes the icon on the checkbox. The ownership of the bitmap is not transferred. If you wish the bitmap to be destroyed with the checkbox, use OwnIcon instead. Not every checkbox template supports icons.

##### `SetIcon(const Graphics::Drawable &value)`

**Returns:** `void`

Changes the icon on the checkbox. The ownership of the animation is not transferred. If you wish the animation to be destroyed with the checkbox, use OwnIcon instead. Not every checkbox template supports icons.

##### `SetIconProvider(const Graphics::AnimationProvider &value)`

**Returns:** `void`

Changes the icon on the checkbox. This will create a new animation from the given provider and will own the resultant animation. Not every checkbox template supports icons.

##### `SetIconProvider(Graphics::AnimationProvider &&provider)`

**Returns:** `void`

Changes the icon on the checkbox. This will move in the provider, create a new animation and own both the provider and the animation. Not every checkbox template supports icons.

##### `RemoveIcon(—)`

**Returns:** `void`

Removes the icon on the checkbox

##### `HasIcon(—)`

**Returns:** `bool`

Returns if the checkbox has an icon

##### `OwnIcon(—)`

**Returns:** `void`

Returns the icon on the checkbox. If the checkbox does not have an icon, this function will throw Transfers the ownership of the current icon.

##### `OwnIcon(const Graphics::Drawable &value)`

**Returns:** `void`

Sets the icon while transferring the ownership

##### `OwnIcon(Graphics::Bitmap &&value)`

**Returns:** `void`

Moves the given animation to the icon of the checkbox

##### `GORGON_UI_CSW_WRAP_WIDGET(Checkbox, TextTag, true)`

**Returns:** ``


---

## Functions

### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(key == Keycodes::Space)`

**Returns:** ``



### `if(state == 1)`

**Returns:** ``



### `if(spacedown)`

**Returns:** `else`



### `if(state == 1)`

**Returns:** `else`



### `if(key == Keycodes::Numpad_Plus)`

**Returns:** ``



### `if(key == Keycodes::Numpad_Minus)`

**Returns:** `else`



### `if(value != state)`

**Returns:** ``



### `if(!force)`

**Returns:** ``



### `StateChangingEvent(value, allow)`

**Returns:** ``



### `if(value)`

**Returns:** ``



### `RemoveIcon()`

**Returns:** ``



### `OwnIcon(anim)`

**Returns:** ``



### `OwnIcon(anim)`

**Returns:** ``



### `if(ownicon)`

**Returns:** ``



### `SetIcon(value)`

**Returns:** ``


