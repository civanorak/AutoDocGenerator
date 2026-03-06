# Button

&gt; Auto-generated documentation for the **Button** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Button`

**Namespace:** `Gorgon`

#### Methods

##### `Button(const UI::Template &temp, std::string text = "")`

**Returns:** `explicit`

##### `SetText(const std::string &value)`

**Returns:** `void`

Changes the text displayed on the button

##### `GetText(—)`

**Returns:** `std::string`

Returns the text displayed on the button

##### `SetIcon(const Graphics::Bitmap &value)`

**Returns:** `void`

Changes the icon on the button. The ownership of the bitmap is not transferred. If you wish the bitmap to be destroyed with the button, use OwnIcon instead.

##### `SetIcon(const Graphics::Drawable &value)`

**Returns:** `void`

Changes the icon on the button. The ownership of the animation is not transferred. If you wish the animation to be destroyed with the button, use OwnIcon instead.

##### `SetIconProvider(const Graphics::AnimationProvider &value)`

**Returns:** `void`

Changes the icon on the button. This will create a new animation from the given provider and will own the resultant animation.

##### `SetIconProvider(Graphics::AnimationProvider &&provider)`

**Returns:** `void`

Changes the icon on the button. This will move in the provider, create a new animation and own both the provider and the animation

##### `RemoveIcon(—)`

**Returns:** `void`

Removes the icon on the button

##### `HasIcon(—)`

**Returns:** `bool`

Returns if the button has an icon

##### `OwnIcon(—)`

**Returns:** `void`

Returns the icon on the button. If the button does not have an icon, this function will throw Transfers the ownership of the current icon.

##### `OwnIcon(const Graphics::Animation &value)`

**Returns:** `void`

Sets the icon while transferring the ownership

##### `OwnIcon(Graphics::Bitmap &&value)`

**Returns:** `void`

Moves the given animation to the icon of the button

##### `ActivateClickRepeat(int delay = 500, int repeat = 400, int accelerationtime = 2000, int minrepeat = 200)`

**Returns:** `void`

Activates click repeat. All parameters are in milliseconds. delay is the time before first repeat. repeat is the initial time between repeats. accelerationtime is time to reach minimum repeat interval. maxrepeat is the minimum time between the repeats.

##### `DeactivateClickRepeat(—)`

**Returns:** `void`

Deactivates click repeat.

##### `GORGON_UI_CSW_WRAP_WIDGET(Button, TextTag, true)`

**Returns:** ``

##### `repeattick(—)`

**Returns:** `void`


---

## Enums

### `repeatstate`

**Namespace:** `Gorgon`


---

## Functions

### `ClickEvent()`

**Returns:** ``



### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `PressEvent()`

**Returns:** ``



### `if(repeaten == repeatstandby)`

**Returns:** ``



### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `ReleaseEvent()`

**Returns:** ``



### `if(repeaten != repeatdisabled)`

**Returns:** ``



### `RemoveIcon()`

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



### `ClickEvent()`

**Returns:** ``



### `PressEvent()`

**Returns:** ``



### `ClickEvent()`

**Returns:** ``



### `ReleaseEvent()`

**Returns:** ``



### `if(key == Keycodes::Space)`

**Returns:** `else`



### `if(state == 1)`

**Returns:** ``



### `PressEvent()`

**Returns:** ``



### `if(repeaten == repeatstandby)`

**Returns:** ``



### `if(spacedown)`

**Returns:** `else`



### `if(!mousedown)`

**Returns:** ``



### `ClickEvent()`

**Returns:** ``



### `ReleaseEvent()`

**Returns:** ``



### `if(repeaten != repeatdisabled)`

**Returns:** ``



### `ClickEvent()`

**Returns:** ``



### `if(repeaten == repeatondelay)`

**Returns:** ``


