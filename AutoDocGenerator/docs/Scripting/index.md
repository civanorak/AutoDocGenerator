# Scripting

&gt; Auto-generated documentation for the **Scripting** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `InitializeScripting()`

**Returns:** `void`



### `temp(0, 0)`

**Returns:** `Point`



### `init_builtin()`

**Returns:** `void`


@cond INTERNAL


### `Initialize()`

**Returns:** `inline void`


@endcond Prints out a data Initializes the scripting system


### `init_builtin()`

**Returns:** ``



### `DEFTYPE(Variant)`

**Returns:** ``


Variant is a special data type. Variant is useful as function parameters or return type. When a value is passed to variant parameter or returned as a variant return type, it is automatically converted to the type passed or returned only aim of the variant type in these uses is to allow any type to be passed or returned. Its internal data type is Data


### `DEFTYPE(String)`

**Returns:** ``


Regular std::string


### `DEFTYPE(Int)`

**Returns:** ``


int data type


### `DEFTYPE(Float)`

**Returns:** ``


float data type


### `DEFTYPE(Bool)`

**Returns:** ``


bool data type


### `DEFTYPE(Double)`

**Returns:** ``


double data type


### `DEFTYPE(Char)`

**Returns:** ``


char data type


### `DEFTYPE(Byte)`

**Returns:** ``


Gorgon::Byte (unsigned char) data type


### `DEFTYPE(Unsigned)`

**Returns:** ``


unsigned int


### `DEFTYPE(Array)`

**Returns:** ``


This type contains array, however, its not a simple std::vector. Builtin array of %Gorgon script allows any type however, once a type is set, it cannot be changed, allowing type checking


### `DEFTYPE(Type)`

**Returns:** ``



### `DEFTYPE(InstanceMember)`

**Returns:** ``



### `DEFTYPE(StaticDataMember)`

**Returns:** ``



### `DEFTYPE(Namespace)`

**Returns:** ``



### `DEFTYPE(Function)`

**Returns:** ``



### `DEFTYPE(Constant)`

**Returns:** ``



### `DEFTYPE(EnumType)`

**Returns:** ``



### `DEFTYPE(EventType)`

**Returns:** ``



### `DEFTYPE(Library)`

**Returns:** ``


