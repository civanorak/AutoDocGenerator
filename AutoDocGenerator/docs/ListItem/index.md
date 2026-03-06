# ListItem

&gt; Auto-generated documentation for the **ListItem** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ListItem`

**Namespace:** `Gorgon`

#### Methods

##### `ListItem(const UI::Template &temp)`

**Returns:** ``

Constructor requires template. ListItem

##### `SetText(const std::string &value)`

**Returns:** `void`

Changes the text displayed. Depending on the template, text might be overwritten by icon.

##### `GetText(—)`

**Returns:** `std::string`

Returns the currently displayed text.

##### `SetIndex(long value)`

**Returns:** `void`

Sets the index of the ListItem in the Listbox

##### `GetIndex(—)`

**Returns:** `int`

Returns the index of the Item in the Listbox

##### `SetIcon(const Graphics::Bitmap &value)`

**Returns:** `void`

Changes the icon on the label. The ownership of the bitmap is not transferred. If you wish the bitmap to be destroyed with the label, use OwnIcon instead.

##### `SetIcon(const Graphics::Animation &value)`

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

##### `OwnIcon(—)`

**Returns:** `void`

Returns the icon on the label. If the label does not have an icon, this function will throw Transfers the ownership of the current icon.

##### `OwnIcon(const Graphics::Animation &value)`

**Returns:** `void`

Sets the icon while transferring the ownership

##### `OwnIcon(Graphics::Bitmap &&value)`

**Returns:** `void`

Moves the given animation to the icon of the label

##### `SetSelected(bool value)`

**Returns:** `void`

Sets selection status of the widget. Depending on the template, selected status might invert colors or display checkbox, radiobutton or similar indication that the item is selected.

##### `GetSelected(—)`

**Returns:** `bool`

Return selection status.

##### `SetParity(Parity value)`

**Returns:** `void`

Set odd/even parity of the widget. Depending on the template this might not have any effect at all.

##### `GetParity(—)`

**Returns:** `Parity`

Returns the odd/even parity.

##### `SetOpened(YesNoUnset value)`

**Returns:** `void`

Sets whether the item is opened and displaying subitems. This will not actually display any subitems, but only an indication. Depending on the template No might display + icon, Yes might display - icon. Setting this value to Unset will ensure no indication will be displayed.

##### `GetOpened(—)`

**Returns:** `YesNoUnset`

Returns whether the item is opened and displaying subitems.

##### `SetPosition(ItemPosition value)`

**Returns:** `void`

Sets the position of this item in the list. Depending on the template this might display visual cues or used as a way to connect treeview items to their parent.

##### `GetPosition(—)`

**Returns:** `ItemPosition`

Returns the position of this item in the list. This is not automated


### `ListItem`

**Namespace:** `gge`

#### Methods

##### `virtual` `MouseHandler(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `virtual bool`

##### `Focus(—)`

**Returns:** ``

##### `switch(event)`

**Returns:** ``

##### `Trigger(—)`

**Returns:** ``

##### `DragNotify(*this, Index, mdownlocation)`

**Returns:** ``

##### `if(event==Event::Out)`

**Returns:** `else`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `Trigger(—)`

**Returns:** ``

##### `Trigger(—)`

**Returns:** ``

##### `virtual` `Accessed(—)`

**Returns:** `virtual bool`

##### `Trigger(—)`

**Returns:** ``

##### `SetIcon(graphics::RectangularGraphic2D *icon)`

**Returns:** `void`

##### `Select(—)`

**Returns:** `void`

##### `Deselect(—)`

**Returns:** `void`

##### `SetText(const std::string &text)`

**Returns:** `void`

##### `settext(text)`

**Returns:** ``

##### `ListItem(const ListItem &li)`

**Returns:** ``


---

## Functions

### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `ClickEvent()`

**Returns:** ``



### `ToggleEvent()`

**Returns:** ``



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



### `ToggleEvent()`

**Returns:** ``



### `if(value)`

**Returns:** ``



### `if(parity == Parity::Odd)`

**Returns:** ``



### `if(parity == Parity::Even)`

**Returns:** `else`



### `if(value == Parity::Odd)`

**Returns:** ``



### `if(value == Parity::Even)`

**Returns:** `else`



### `if(opened == YesNoUnset::Yes)`

**Returns:** ``



### `if(opened == YesNoUnset::No)`

**Returns:** `else`



### `if(value == YesNoUnset::Yes)`

**Returns:** ``



### `if(value == YesNoUnset::No)`

**Returns:** `else`



### `switch(position)`

**Returns:** ``



### `switch(value)`

**Returns:** ``


