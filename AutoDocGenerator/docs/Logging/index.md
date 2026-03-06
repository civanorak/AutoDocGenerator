# Logging

&gt; Auto-generated documentation for the **Logging** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Logger`

**Namespace:** `Gorgon`


### `helper`

**Namespace:** `Gorgon`

#### Methods

##### `helper(helper &&h)`

**Returns:** ``


---

## Enums

### `State`

**Namespace:** `Gorgon`


---

## Functions

### `CleanUp()`

**Returns:** ``


Default constructor. Allows you to specify a section Default constructor. Allows you to specify a section


### `InitializeConsole()`

**Returns:** `void`



### `CleanUp()`

**Returns:** ``



### `InitializeStream(std::ostream &stream)`

**Returns:** `void`


Initializes the logger to direct its input to the given stream. Ownership is not transferred


### `CleanUp()`

**Returns:** ``



### `InitializeFile(const std::string &filename, bool append = false)`

**Returns:** `void`


Opens and initializer the logger using the given filename. The file will automatically be closed when CleanUp is performed.


### `CleanUp()`

**Returns:** ``



### `CleanUp()`

**Returns:** `void`


Cleans the stream. If it is built by this object, it will be destroyed. After this point nothing will be logged.


### `if(owner)`

**Returns:** ``



### `SetWidth(int width)`

**Returns:** `void`


Sets the width to break lines from. Set to 0 to disable.


### `Log(v, Message)`

**Returns:** `return`


Streams out the given value to the underlying stream. This function will automatically add requested information in front. Always cascade entries. Every time a new `logger << ...` is called, header information will be printed out. You may use std::endl in your logs, but a new line will be added for all entries. An extra empty line will be inserted for multiline entries. Do not use "\n" as it will not be detected. Message state is used for this case.


### `Log(const T_ &v, State state = Error)`

**Returns:** `helper`


Streams out the given value to the underlying stream. This function will automatically add requested information in front. Always cascade entries. Every time a new `logger << ...` is called, header information will be printed out. You may use std::endl in your logs, but a new line will be added for all entries. An extra empty line will be inserted for multiline entries. Do not use "\n" as it will not be detected. , @code logger.Log("Unexpected error: ", Utils::Logger::Error)&lt;&lt;ex.what(); @endcode


### `if(width && headw*1.25 >= width)`

**Returns:** ``



### `if(headw)`

**Returns:** `else`



### `if(marktime || markdate)`

**Returns:** ``



### `if(markdate)`

**Returns:** ``



### `if(marktime)`

**Returns:** ``



### `reset(stream)`

**Returns:** ``



### `colorize(state)`

**Returns:** ``



### `reset(stream)`

**Returns:** ``



### `if(state != Message)`

**Returns:** ``



### `colorize(state)`

**Returns:** ``



### `SetSection(const std::string &value)`

**Returns:** `void`


Sets the section of this logger.


### `GetSection()`

**Returns:** `std::string`


Returns the current section of this logger.


### `SetMarkTime(bool value)`

**Returns:** `void`


Sets whether to mark the time on log output


### `GetMarkTime()`

**Returns:** `bool`


Returns whether time is being marked


### `SetMarkDate(bool value)`

**Returns:** `void`


Sets whether to mark the date on log output


### `GetMarkDate()`

**Returns:** `bool`


Returns whether date is being marked


### `EnableColor()`

**Returns:** `void`


Enables color support, however, if the underlying stream does not allow coloring this will not have any effect. You may use ForceColor to output color coding to a device that does not support color.


### `DisableColor()`

**Returns:** `void`


Disable color output


### `SetColorEnabled(bool value)`

**Returns:** `void`


Sets color enabled state. If color is enabled and the underlying stream does not allow coloring setting coloring to true will not have any effect. You may use ForceColor to output color coding to a device that does not support color.


### `IsColorEnabled()`

**Returns:** `bool`


Whether color is enabled, a value of true is not a warranty that color output is working, use IsColorFunctional to make sure.


### `IsColorFunctional()`

**Returns:** `bool`


Returns whether the color output is currently working.


### `reset(std::ostream &stream)`

**Returns:** `void`



### `colorize(State state)`

**Returns:** `void`



### `switch(state)`

**Returns:** ``


