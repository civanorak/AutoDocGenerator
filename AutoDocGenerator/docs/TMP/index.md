# TMP

&gt; Auto-generated documentation for the **TMP** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Arguments`

**Namespace:** `TMP`

Return type of the function Number of arguments of the function Whether this function is a member function This struct allow access to types of individual arguments. Do not forget to use template keyword before arguments.


### `RTTI`

**Namespace:** `TMP`

@endcond This acts like ? operator between two types @cond @endcond This class contains information about a runtime type

#### Methods

##### `virtual` `IsPointer(—)`

**Returns:** `virtual bool`

Returns if this type is pointer

##### `virtual` `IsReference(—)`

**Returns:** `virtual bool`

Returns if this type is a reference

##### `virtual` `IsConstant(—)`

**Returns:** `virtual bool`

Returns if this type is a constant

##### `virtual` `IsSameType(const std::type_info &)`

**Returns:** `virtual bool`

Compares the type stored with this service to the given type info

##### `IsSameType(—)`

**Returns:** `bool`

Compares the type stored with this service to the given type

##### `IsSameType(info)`

**Returns:** `return`

##### `IsSameType(info)`

**Returns:** `return`

##### `TypeInfo(—)`

**Returns:** `return`

##### `virtual` `GetSize(—)`

**Returns:** `virtual long`

Returns the size of the object

##### `Name(—)`

**Returns:** `std::string`

@name TypeInfo @{ @} Returns human readable name of the type


### `RTTS`

**Namespace:** `TMP`

This class contains runtime type services that allows dealing with unknown type. RTTS should be constructed for RTT class. This class is not designed to work with array types.

#### Methods

##### `virtual` `Clone(void* const dest, const void* const obj)`

**Returns:** `virtual void`

Duplicates this service Clones the given object Clones the given object

##### `virtual` `Delete(void* obj)`

**Returns:** `virtual void`

Deletes the given object


### `RTT`

**Namespace:** `TMP`

Destructor Runtime Type. This class implements both RTTS and RTTI

#### Methods

##### `typeid(T_)`

**Returns:** `return`


### `AbstractRTT`

**Namespace:** `TMP`

Runtime Type. This class implements both RTTS and RTTI

#### Methods

##### `typeid(T_)`

**Returns:** `return`


### `RTTH`

**Namespace:** `TMP`

Runtime Type Hierarchy


### `RTTC`

**Namespace:** `TMP`

Runtime type class, implements RTTH


### `AbstractRTTC`

**Namespace:** `TMP`

Runtime type class, implements RTTH


### `RemoveRValueReference`

**Namespace:** `TMP`


### `two`

**Namespace:** `TMP`


### `MakeIndices`

**Namespace:** `TMP`

Solution by Peter Dimov-5: http://std.2283326.n4.nabble.com/bind-Possible-to-use-variadic-templates-with-bind-td2557818.html


### `HasParanthesisOperator`

**Namespace:** `TMP`


### `no`

**Namespace:** `TMP`

#### Methods

##### `static` `impl(T*)`

**Returns:** `static yes`

##### `static` `impl(...)`

**Returns:** `static no`


---

## Functions

### `static_strequal_helper(const char * a, const char * b, unsigned len)`

**Returns:** `constexpr bool`


A sequence element, can be used to represent a sequence of integer numbers Generates a sequence from 0 to the given value. @cond @endcond


### `MembersOnly(F_ fn)`

**Returns:** `* typename std::enable_if<FunctionTraits<F_>::IsMember>::type`



### `static_assert(N<Arity, "Argument index out of bounds")`

**Returns:** ``


Type of the argument. @cond


### `clonetype_wnull(const void* const obj)`

**Returns:** ``



### `copytype_wnull(void* const dest, const void* const obj)`

**Returns:** ``



### `typeid(void)`

**Returns:** `return`


Runtime Type. This class implements both RTTS and RTTI


### `test(...)`

**Returns:** `static two`


