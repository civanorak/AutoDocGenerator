# Compiler

&gt; Auto-generated documentation for the **Compiler** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `demangle(const std::string &)`

**Returns:** `std::string`


@cond INTERNAL


### `GetTypeName()`

**Returns:** `std::string`


@endcond Returns the human readable form of the typename. By the standard typeid::name is not required to be the same as declared type. This function uses compiler facilities to obtain readable name.


### `GetTypeName(const std::type_info &inf)`

**Returns:** `inline std::string`


Returns the human readable form of the typename. By the standard typeid::name is not required to be the same as declared type. This function uses compiler facilities to obtain readable name.

