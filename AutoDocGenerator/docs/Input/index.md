# Input

> Auto-generated documentation for the **Input** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `InputProvider`

**Namespace:** `Gorgon`

#### Methods

##### `GetDialect(—)`

**Returns:** `Dialect`

Returns the current dialect of the input

##### `SetDialect(Dialect dialect)`

**Returns:** `void`

Changes the current dialect of the input

##### `checkdialect(—)`

**Returns:** ``

##### `GetName(—)`

**Returns:** `std::string`

##### `virtual` `ReadLine(std::string &, bool newline)`

**Returns:** `virtual bool`

This method should read a single physical line from the source. Logical line separation is handled by InputSource. Return of false means no input is fetched as it is finished. If there is a read error, rather than returning false, this function should throw. newline parameter denotes that this line is a new line, not continuation of another.

##### `virtual` `IsInteractive(—)`

**Returns:** `virtual bool`

Returns if this input provider allows interaction

##### `virtual` `Reset(—)`

**Returns:** `virtual void`

Resets the input to the beginning

##### `virtual` `checkdialect(—)`

**Returns:** `virtual void`


### `ConsoleInput`

**Namespace:** `Gorgon`

Reads lines from the console

#### Methods

##### `prompt(prompt)`

**Returns:** ``

Initializes console input. line number will be appended at the start of the prompt

##### `SetPrompt(const std::string &prompt)`

**Returns:** `void`

##### `if(dialect==InputProvider::Binary)`

**Returns:** ``

##### `SetDialect(InputProvider::Console)`

**Returns:** ``


### `StreamInput`

**Namespace:** `Gorgon`

Reads lines from a stream


### `FileInput`

**Namespace:** `Gorgon`

Reads lines from a file


### `windaccess`

**Namespace:** `Gorgon`


---

## Enums

### `Dialect`

**Namespace:** `Gorgon`


---

## Functions

### `ishandled(HWND hwnd, Input::Key key)`

**Returns:** `bool`



### `osgetkeyname(Input::Keyboard::Key key)`

**Returns:** `std::string`



### `UnicodeToMByte(strupper)`

**Returns:** `return`



### `maposkey(WPARAM wParam, LPARAM lParam)`

**Returns:** `Input::Keyboard::Key`



### `switch(wParam)`

**Returns:** ``



### `clearkeys(Gorgon::internal::windowdata *data)`

**Returns:** `void`



### `for(auto key : data->pressedkeys)`

**Returns:** ``



### `handlekeydown(Gorgon::internal::windowdata *data, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `switch(wParam)`

**Returns:** ``



### `if(token!=ConsumableEvent<Window, Input::Key, bool>::EmptyToken && !Input::AllowCharEvent)`

**Returns:** ``



### `handlekeyup(Gorgon::internal::windowdata *data, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `switch(wParam)`

**Returns:** ``



### `handlechar(Gorgon::internal::windowdata *data, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `handlemousedown(Gorgon::internal::windowdata *data, UINT message, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `switch(message)`

**Returns:** ``



### `handlemouseup(Gorgon::internal::windowdata *data, UINT message, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `switch(message)`

**Returns:** ``



### `handleinputevent(Gorgon::internal::windowdata *data, UINT message, WPARAM wParam, LPARAM lParam)`

**Returns:** `void`



### `windp(*data->parent)`

**Returns:** `windaccess`



### `switch(message)`

**Returns:** ``



### `handlemousedown(data, message, wParam, lParam)`

**Returns:** ``



### `handlemouseup(data, message, wParam, lParam)`

**Returns:** ``



### `if(gi.dwID == GID_ZOOM)`

**Returns:** ``



### `if(gi.dwID == GID_ROTATE)`

**Returns:** `else`



### `handlekeydown(data, wParam, lParam)`

**Returns:** ``



### `handlekeyup(data, wParam, lParam)`

**Returns:** ``



### `handlechar(data, wParam, lParam)`

**Returns:** ``



### `if(keysym == 13 || keysym == 10)`

**Returns:** ``



### `while(max >= min)`

**Returns:** ``



### `osgetkeyname(Input::Keyboard::Key key)`

**Returns:** `std::string`



### `XFree(keys)`

**Returns:** ``



### `buttonfromx11(unsigned btn)`

**Returns:** `Input::Mouse::Button`



### `switch(btn)`

**Returns:** ``



### `mapx11key(KeySym key, unsigned int keycode)`

**Returns:** `Input::Keyboard::Key`



### `if(key == 'i')`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `assertkeys(Window &wind, Gorgon::internal::windowdata *data)`

**Returns:** `void`



### `XQueryKeymap(WindowManager::display, keys)`

**Returns:** ``



### `for(auto it=data->pressed.begin()`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `handlekeypressevent(XEvent event, Window &wind)`

**Returns:** `void`



### `switch(key)`

**Returns:** ``



### `if(token != wind.KeyEvent.EmptyToken && !Input::AllowCharEvent)`

**Returns:** ``



### `XLookupString(&event.xkey, nullptr, 0, &key, nullptr)`

**Returns:** ``



### `if(c != 0xfffd)`

**Returns:** ``



### `handlekeyreleaseevent(XEvent event, Window &wind)`

**Returns:** `void`



### `XPeekEvent(WindowManager::display, &nextevent)`

**Returns:** ``



### `XLookupString(&event.xkey, nullptr, 0, &key, nullptr)`

**Returns:** ``



### `if(c != 0xfffd)`

**Returns:** ``



### `XNextEvent(WindowManager::display, &nextevent)`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `handlebuttonpressevent(XEvent event, Window &wind)`

**Returns:** `void`



### `if(event.xbutton.button==4)`

**Returns:** ``



### `if(event.xbutton.button==5)`

**Returns:** `else`



### `handlebuttonreleaseevent(XEvent event, Window &wind)`

**Returns:** `void`



### `if(event.xbutton.button!=4 && event.xbutton.button!=5)`

**Returns:** ``



### `handleinputevent(XEvent event, Window &wind)`

**Returns:** `void`



### `switch(event.type)`

**Returns:** ``



### `handlekeypressevent(event, wind)`

**Returns:** ``



### `handlekeyreleaseevent(event, wind)`

**Returns:** ``



### `handlebuttonpressevent(event, wind)`

**Returns:** ``



### `handlebuttonreleaseevent(event, wind)`

**Returns:** ``


