# Struct

&gt; Auto-generated documentation for the **Struct** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `GetElm`

**Namespace:** `Gorgon`


### `Inner`

**Namespace:** `Gorgon`


### `Inner`

**Namespace:** `Gorgon`


### `StructDefiner`

**Namespace:** `Gorgon`


### `Inner`

**Namespace:** `Gorgon`


### `Member`

**Namespace:** `Gorgon`

#### Methods

##### `MemberPointer(—)`

**Returns:** ``


---

## Functions

### `Reflection()`

**Returns:** `static constexpr ReflectionType`


Defines a struct members with the given name. The first parameter is the name of the class. This macro should be called inside the class/struct scope. This reflection is geared towards POD objects. Might not behave as intented on polymorphic objects. After calling this function the class will have ReflectionType and Reflection() that returns reflection object with names.


### `Reflection()`

**Returns:** `static constexpr ReflectionType`


Defines a struct members with the given name. The first parameter is the name of the class. This macro should be called inside the class/struct scope. This reflection is geared towards POD objects. Might not behave as intented on polymorphic objects. After calling this function the class will have ReflectionType and Reflection() that returns reflection object with names.

