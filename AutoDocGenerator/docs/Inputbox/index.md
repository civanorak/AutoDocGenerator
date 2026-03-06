# Inputbox

&gt; Auto-generated documentation for the **Inputbox** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Inputbox_base`

**Namespace:** `internal`

#### Methods

##### `Inputbox_base(const UI::Template &temp)`

**Returns:** ``


### `glyphbyte`

**Namespace:** `internal`


### `validatorextras`

**Namespace:** `internal`

@endcond

#### Methods

##### `transfer(V_ &)`

**Returns:** `void`


### `StringValidator`

**Namespace:** `internal`

#### Methods

##### `SetMaxChars(int value)`

**Returns:** `void`


---

## Functions

### `mousedown(tag, location, button)`

**Returns:** ``



### `if(key == Keycodes::Backspace)`

**Returns:** ``



### `if(sellen.byte == 0)`

**Returns:** ``



### `if(selstart.glyph != 0)`

**Returns:** ``



### `moveselleft()`

**Returns:** ``



### `updatevalue()`

**Returns:** ``



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `eraseselected()`

**Returns:** ``



### `updatevalue()`

**Returns:** ``



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(key == Keycodes::Delete)`

**Returns:** ``



### `if(sellen.byte == 0)`

**Returns:** ``



### `if(selstart.glyph < glyphcount)`

**Returns:** ``



### `updatevalue()`

**Returns:** ``



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `eraseselected()`

**Returns:** ``



### `updatevalue()`

**Returns:** ``



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Modifier::Shift)`

**Returns:** ``



### `if(sellen.byte == allselected)`

**Returns:** ``



### `if(key == Input::Keyboard::Keycodes::Left)`

**Returns:** ``



### `if(sellen.glyph + selstart.glyph > 0)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(key == Input::Keyboard::Keycodes::Right)`

**Returns:** `else`



### `if(sellen.glyph + selstart.glyph < glyphcount)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Modifier::None)`

**Returns:** `else`



### `if(sellen.byte == allselected)`

**Returns:** ``



### `if(key == Keycodes::Left)`

**Returns:** ``



### `if(key == Keycodes::Right)`

**Returns:** `else`



### `updateselection()`

**Returns:** ``



### `if(sellen.byte != 0)`

**Returns:** `else`



### `if(key == Keycodes::Left)`

**Returns:** ``



### `if(sellen.byte < 0)`

**Returns:** ``



### `moveselleft()`

**Returns:** ``



### `if(key == Keycodes::Right)`

**Returns:** `else`



### `if(sellen.byte > 0)`

**Returns:** ``



### `moveselright()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(key == Keycodes::Left)`

**Returns:** ``



### `moveselleft()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(key == Keycodes::Right)`

**Returns:** `else`



### `moveselright()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `updatevaluedisplay()`

**Returns:** ``



### `if(autoselectall)`

**Returns:** ``



### `SelectAll()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `changed()`

**Returns:** ``



### `if(state)`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Modifier::None)`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(!readonly)`

**Returns:** ``



### `Done()`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Modifier::Shift)`

**Returns:** `else`



### `switch(key)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Modifier::Ctrl)`

**Returns:** `else`



### `switch(key)`

**Returns:** ``



### `SelectAll()`

**Returns:** ``



### `eraseselected()`

**Returns:** ``



### `updatevalue()`

**Returns:** ``



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(state && relevant)`

**Returns:** ``



### `if(sellen.byte != 0)`

**Returns:** ``



### `eraseselected()`

**Returns:** ``



### `updatevalue()`

**Returns:** ``



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(selstart.byte < 0)`

**Returns:** ``



### `if(selstart.byte + sellen.byte < 0)`

**Returns:** ``



### `if(viewportidx == -1)`

**Returns:** ``



### `if(targetsize.Width > textsize.Width)`

**Returns:** ``



### `if(display == "")`

**Returns:** ``



### `if(location.X < -scrolloffset)`

**Returns:** ``



### `if(location.X > targetsize.Width - scrolloffset)`

**Returns:** `else`



### `if(display == "")`

**Returns:** ``



### `if(sellen.byte == 0)`

**Returns:** ``



### `if(srclocation.X < location.X)`

**Returns:** ``



### `SelectAll()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(!readonly)`

**Returns:** ``



### `Done()`

**Returns:** ``



### `if(dirty)`

**Returns:** ``



### `changed()`

**Returns:** ``



### `if(button != Input::Mouse::Button::Left)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `while(g)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(!ismousedown)`

**Returns:** ``



### `while(g)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `if(button == Input::Mouse::Button::Left)`

**Returns:** ``



### `if(sellen.byte < 0)`

**Returns:** ``



### `if(sellen.byte > 0)`

**Returns:** `else`



### `updatevaluedisplay(false)`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `Length()`

**Returns:** `int`


Returns the length of the text in this inputbox. This value is in glyphs.


### `GetText()`

**Returns:** `std::string`


Returns the current text in the inputbox. Use Get() to obtain the value of the inputbox, this function exists for special uses.


### `GetSelectedText()`

**Returns:** `std::string`



### `SelectAll()`

**Returns:** `void`


@name Selection @{ Selects the entire contents of this inputbox


### `updateselection()`

**Returns:** ``



### `SelectNone()`

**Returns:** `void`


Removes any selection, does not move the start of the cursor.


### `updateselection()`

**Returns:** ``



### `SelectionStart()`

**Returns:** `int`


Returns the start of the selection in glyphs.


### `SelectionLength()`

**Returns:** `int`


Returns the length of the selection in glyphs. Selection length could be negative denoting the selection is backwards.


### `CaretLocation()`

**Returns:** `int`


Returns the location of the caret. It is always at the end of the selection.


### `Focus()`

**Returns:** `return`


@}


### `if(readonly)`

**Returns:** ``



### `if(!value)`

**Returns:** ``



### `SetAutoSelectAll(const bool &value)`

**Returns:** `void`


Controls if the inputbox will be auto selected recieving focus or right after the user is done with editing. Default is false.


### `SelectAll()`

**Returns:** ``



### `GetAutoSelectAll()`

**Returns:** `bool`


Controls if the inputbox will be auto selected recieving focus or right after the user is done with editing. Default is false.


### `SetBlockEnterKey(const bool &value)`

**Returns:** `void`


When set to true, pressing enter on this widget will block default button to recieve it. Default is false.


### `GetBlockEnterKey()`

**Returns:** `bool`


When set to true, pressing enter on this widget will block default button to recieve it. Default is false.


### `SetReadonly(const bool &value)`

**Returns:** `void`


When set to true, the value contained in the inputbox cannot be edited by the user. Default is false.


### `GetReadonly()`

**Returns:** `bool`


When set to true, the value contained in the inputbox cannot be edited by the user. Default is false.


### `updateselection()`

**Returns:** `void`


Controls if the inputbox will be auto selected recieving focus or right after the user is done with editing. Default is false. When set to true, pressing enter on this widget will block default button to recieve it. Default is false. When set to true, the value contained in the inputbox cannot be edited by the user. Default is false. updates the selection display


### `updatevalue()`

**Returns:** `virtual void`


updates the value display


### `updatevaluedisplay(bool updatedisplay = true)`

**Returns:** `virtual void`


updates the value display


### `changed()`

**Returns:** `virtual void`



### `moveselleft()`

**Returns:** `void`



### `if(selstart.glyph > 0)`

**Returns:** ``



### `moveselright()`

**Returns:** `void`



### `if(selstart.glyph < glyphcount)`

**Returns:** ``



### `eraseselected()`

**Returns:** `void`



### `mousedown(UI::ComponentTemplate::Tag tag, Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`



### `mouseup(UI::ComponentTemplate::Tag tag, Geometry::Point location, Input::Mouse::Button button)`

**Returns:** `void`



### `mousemove(UI::ComponentTemplate::Tag tag, Geometry::Point location)`

**Returns:** `void`



### `SetMaxChars(int value)`

**Returns:** `void`



### `GetMaxChars()`

**Returns:** `int`



### `transfer(V_ &validator)`

**Returns:** `void`



### `updatevaluedisplay()`

**Returns:** ``


Initializes the inputbox


### `updateselection()`

**Returns:** ``



### `set(value)`

**Returns:** ``


Initializes the inputbox Initializes the inputbox Initializes the inputbox Initializes the inputbox Initializes the inputbox Assignment to the value type


### `T_()`

**Returns:** `operator`


Copy assignment will only copy the value Returns the value in the box.


### `T_()`

**Returns:** `operator const`


Returns the value in the box.


### `get()`

**Returns:** `T_`


Fired after the value of the inputbox is changed. Parameter is the previous value before the change. If the user is typing, this event will be fired after the user hits enter or if enabled, after a set amount of time. This function will be called even if the value is not actually changed since the the last call. Fired after the value of in the inputbox is edited. This event will be called even if the user not done with editing. The value is updated before this event is called. Returns the value in the box


### `set(const T_ &val)`

**Returns:** `void`


Changes the value in the box


### `updatevaluedisplay()`

**Returns:** ``



### `updateselection()`

**Returns:** ``



### `EditedEvent()`

**Returns:** ``



### `ChangedEvent(value)`

**Returns:** ``



### `if(updatedisplay)`

**Returns:** ``


updates the value display

