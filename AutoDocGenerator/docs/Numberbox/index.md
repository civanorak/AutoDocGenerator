# Numberbox

> Auto-generated documentation for the **Numberbox** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Numberbox`

**Namespace:** `gge`

#### Methods

##### `setupvscroll(false, false, false)`

**Returns:** ``

##### `setblueprint(*WR.Textboxes.Numberbox)`

**Returns:** ``

##### `SelectAll(—)`

**Returns:** `void`

##### `Select(int start, int end)`

**Returns:** `void`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `SelectAll(—)`

**Returns:** ``

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `virtual` `textchanged(—)`

**Returns:** `virtual void`

##### `settext(s)`

**Returns:** ``

##### `ChangeEvent(—)`

**Returns:** ``

##### `virtual` `setValue(const T_ &value)`

**Returns:** `virtual void`

##### `ChangeEvent(—)`

**Returns:** ``

##### `virtual` `getValue(—)`

**Returns:** `virtual T_`

##### `setCaretLocation(const int &value)`

**Returns:** `void`

##### `getCaretLocation(—)`

**Returns:** `int`

##### `setUseHex(const bool &value)`

**Returns:** `void`

##### `if(UseHex!=value)`

**Returns:** ``

##### `setValue(this->value)`

**Returns:** ``

##### `getUseHex(—)`

**Returns:** `bool`

##### `setPrefix(const std::string &value)`

**Returns:** `void`

##### `setprefix(value)`

**Returns:** ``

##### `getPrefix(—)`

**Returns:** `std::string`

##### `getprefix(—)`

**Returns:** `return`

##### `setSuffix(const std::string &value)`

**Returns:** `void`

##### `setsuffix(value)`

**Returns:** ``

##### `getSuffix(—)`

**Returns:** `std::string`

##### `getsuffix(—)`

**Returns:** `return`

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`

##### `setblueprint(*WR.Textboxes.Numberbox)`

**Returns:** ``


---

## Functions

### `FixStdNumberString(std::string &number, int location, int &removedbefore, int base, bool2type<false> floattype)`

**Returns:** `void`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`



### `FixStdNumberString(std::string &number, int location, int &removedbefore, int base, bool2type<true> floattype)`

**Returns:** `inline void`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c=='.')`

**Returns:** `else`



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`



### `FixNumberString(std::string &number, int location, int &removedbefore, int base)`

**Returns:** `inline void`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c==', ')`

**Returns:** `else`



### `if(c=='.')`

**Returns:** `else`



### `if(passedfirst && c==' ' && !passedcomma)`

**Returns:** `else`



### `if(c=='(')`

**Returns:** `else`



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c=='x')`

**Returns:** `else`



### `if(c=='.')`

**Returns:** `else`



### `if(passedfirst && c==' ' && !passedcomma)`

**Returns:** `else`



### `if(c=='(')`

**Returns:** `else`



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c=='.')`

**Returns:** `else`



### `if(passedfirst && c==' ' && passedcomma<3)`

**Returns:** `else`



### `if(c=='<')`

**Returns:** `else`



### `if(c=='>')`

**Returns:** `else`



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c=='.')`

**Returns:** `else`



### `if(passedfirst && c==' ' && passedcomma<3)`

**Returns:** `else`



### `if(c=='<')`

**Returns:** `else`



### `if(c=='>')`

**Returns:** `else`



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`



### `for(std::string::size_type i=0;i<number.length()`

**Returns:** ``



### `if(c==', ')`

**Returns:** `else`



### `if(c=='.')`

**Returns:** `else`



### `if(passedfirst && c==' ' && passedcomma<3)`

**Returns:** `else`



### `if(c=='(')`

**Returns:** `else`



### `if(c!=' ' && c!='-' && c!='+')`

**Returns:** `else`


