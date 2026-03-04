# Keyboard

> Auto-generated documentation for the **Keyboard** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Modifier`

**Namespace:** `Keycodes`

@} A Unicode character, use String::Append to append this character to an std::string. MOVETO -> Window? This class represents a modifier key. These keys can be

#### Methods

##### `IsModified(—)`

**Returns:** `bool`

No modifier is pressed Only shift modifier is pressed Only control modifier is pressed Only alt modifier is pressed Only meta/super/window modifier is pressed Shift and control Shift and alt Control and alt Shift control alt together Modifier mask to check if the key is modified Modifier mask to check if the key is modified Constructs a new modifier from the given modifier key Assignment operator Checks if this modifier really modifies the key state so that no printable characters can be formed

##### `Remove(Type key)`

**Returns:** `void`

Removes the modifier key

##### `Add(Type key)`

**Returns:** `void`

Adds the given modifier key

##### `Add(Key key)`

**Returns:** `void`

Adds the given keyboard key to modifiers

##### `if(key == Keycodes::Shift || key == Keycodes::RShift)`

**Returns:** ``

##### `if(key == Keycodes::Control || key == Keycodes::RControl)`

**Returns:** `else`

##### `if(key == Keycodes::Alt || key == Keycodes::RAlt)`

**Returns:** `else`

##### `if(key == Keycodes::Meta || key == Keycodes::RMeta)`

**Returns:** `else`

##### `Remove(Key key)`

**Returns:** `void`

Removes the given keyboard key from modifiers

##### `if(key == Keycodes::Shift || key == Keycodes::RShift)`

**Returns:** ``

##### `if(key == Keycodes::Control || key == Keycodes::RControl)`

**Returns:** `else`

##### `if(key == Keycodes::Alt || key == Keycodes::RAlt)`

**Returns:** `else`

##### `if(key == Keycodes::Meta || key == Keycodes::RMeta)`

**Returns:** `else`

##### `bool(—)`

**Returns:** `explicit operator`

Or assignment And assignment Or operator And operator Check modifier


---

## Enums

### `Type`

**Namespace:** `Keycodes`

A type to represent modifier keys


---

## Functions

### `osgetkeyname(Input::Keyboard::Key key)`

**Returns:** `std::string`



### `GetName(Key key)`

**Returns:** `std::string`



### `switch(key)`

**Returns:** ``



### `IsEnter(Key key)`

**Returns:** `inline constexpr bool`


Keycodes that are transported from OS. Returns if the key is an enter key


### `IsModifier(Key key)`

**Returns:** `inline constexpr bool`


Returns if the given key is a known modifier


### `GetName(Key key)`

**Returns:** `std::string`


Returns the name of the key. This function returns capital letters for printable letter keys, names of known keys and OS dependent names for other keys.

