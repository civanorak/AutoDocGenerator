# Label

&gt; Auto-generated documentation for the **Label** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Label`

**Namespace:** `Gorgon`

#### Methods

##### `settext(const std::string &value)`

**Returns:** `void`

##### `gettext(—)`

**Returns:** `std::string`

##### `Label(const UI::Template &temp, const std::string &text = "")`

**Returns:** `explicit`

##### `virtual` `SetText(const std::string &value)`

**Returns:** `virtual void`

##### `virtual` `GetText(—)`

**Returns:** `virtual std::string`

##### `SetIcon(const Graphics::Bitmap &value)`

**Returns:** `void`

Changes the icon on the label. The ownership of the bitmap is not transferred. If you wish the bitmap to be destroyed with the label, use OwnIcon instead.

##### `SetIcon(const Graphics::Drawable &value)`

**Returns:** `void`

Changes the icon on the label. The ownership of the animation is not transferred. If you wish the animation to be destroyed with the label, use OwnIcon instead.

##### `SetIconProvider(const Graphics::AnimationProvider &value)`

**Returns:** `void`

Changes the icon on the label. This will create a new animation from the given provider and will own the resultant animation.

##### `SetIconProvider(Graphics::AnimationProvider &&provider)`

**Returns:** `void`

Changes the icon on the label. This will move in the provider, create a new animation and own both the provider and the animation

##### `RemoveIcon(—)`

**Returns:** `void`

Removes the icon on the label

##### `HasIcon(—)`

**Returns:** `bool`

Returns if the label has an icon

##### `SetText(text)`

**Returns:** ``

Returns the icon on the label. If the label does not have an icon, this function will throw To set the text using direct assignment

##### `OwnIcon(—)`

**Returns:** `void`

Allows direct conversion to string Transfers the ownership of the current icon.

##### `OwnIcon(const Graphics::Drawable &value)`

**Returns:** `void`

Sets the icon while transferring the ownership

##### `OwnIcon(Graphics::Bitmap &&value)`

**Returns:** `void`

Moves the given animation to the icon of the label

##### `GORGON_UI_CSW_WRAP_WIDGET(Label, ContentsTag, true)`

**Returns:** ``


### `MarkdownLabel`

**Namespace:** `Gorgon`

#### Methods

##### `MarkdownLabel(const UI::Template &temp, std::string text = "")`

**Returns:** `explicit`

##### `SetUseInfoFont(const bool &value)`

**Returns:** `void`

Sets whether this label should use info font for text. Default value is false.

##### `if(info != value)`

**Returns:** ``

##### `SetText(original)`

**Returns:** ``

##### `GetUseInfoFont(—)`

**Returns:** `bool`

Returns whether this label should use info font for text

##### `PROPERTY_GETSET(MarkdownLabel, Boolean, bool, UseInfoFont)`

**Returns:** ``

Sets a function that will be called if an in page link starting with # is encountered. If this function does not exist, or returns false, application wide page link handler is called.


---

## Functions

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



### `SetText(text)`

**Returns:** ``



### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `for(auto &r : regions)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `for(auto &r : regions)`

**Returns:** ``


