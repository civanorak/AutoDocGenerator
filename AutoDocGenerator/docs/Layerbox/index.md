# Layerbox

&gt; Auto-generated documentation for the **Layerbox** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Layerbox`

**Namespace:** `Gorgon`

#### Methods

##### `Layerbox(const UI::Template &temp, std::string text = "")`

**Returns:** `explicit`

##### `SetText(const std::string &value)`

**Returns:** `void`

Changes the displayed text which is generally shown on top

##### `GetText(—)`

**Returns:** `std::string`

Returns the displayed text which is generally shown on top

##### `SetIcon(const Graphics::Bitmap &value)`

**Returns:** `void`

Changes the icon of the layer. The ownership of the bitmap is not transferred. If you wish the bitmap to be destroyed with the layerbox, use OwnIcon instead.

##### `SetIcon(const Graphics::Animation &value)`

**Returns:** `void`

Changes the icon of the layer. The ownership of the animation is not transferred. If you wish the animation to be destroyed with the layerbox, use OwnIcon instead.

##### `SetIconProvider(const Graphics::AnimationProvider &value)`

**Returns:** `void`

Changes the icon of the layer. This will create a new animation from the given provider and will own the resultant animation.

##### `SetIconProvider(Graphics::AnimationProvider &&provider)`

**Returns:** `void`

Changes the icon of the layer. This will move in the provider, create a new animation and own both the provider and the animation

##### `RemoveIcon(—)`

**Returns:** `void`

Removes the icon of the layer

##### `HasIcon(—)`

**Returns:** `bool`

Returns if the layerbox has an icon

##### `OwnIcon(—)`

**Returns:** `void`

Returns the icon of the layer. If the layerbox does not have an icon, this function will throw Transfers the ownership of the current icon.

##### `OwnIcon(const Graphics::Animation &value)`

**Returns:** `void`

Sets the icon while transferring the ownership

##### `OwnIcon(Graphics::Bitmap &&value)`

**Returns:** `void`

Moves the given animation to the icon of the layerbox

##### `Refresh(—)`

**Returns:** `void`

Returns the layer of this layerbox Forces layerbox to be refreshed, ensuring contained layers are properly resized.


---

## Functions

### `if(ownicon)`

**Returns:** ``



### `OwnIcon(anim)`

**Returns:** ``



### `OwnIcon(anim)`

**Returns:** ``



### `if(ownicon)`

**Returns:** ``



### `SetIcon(value)`

**Returns:** ``


