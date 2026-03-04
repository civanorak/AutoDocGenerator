# Runtime

> Auto-generated documentation for the **Runtime** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ReferenceCounter`

**Namespace:** `Scripting`

This class allows references to be counted and destroyed properly.

#### Methods

##### `Register(const Data &data)`

**Returns:** `void`

Registers a new object of reference counting, this will set reference count to one. This function ignores register requests for nullptr

##### `Register(void *ptr)`

**Returns:** `void`

Registers a new object of reference counting, this will set reference count to 0. This function ignores register requests for nullptr

##### `Increase(const Data &data)`

**Returns:** `void`

Increases the reference count of the given object. If it is not registered, this request is ignored

##### `Increase(void *ptr)`

**Returns:** `void`

Increases the reference count of the given object. If it is not registered, this request is ignored

##### `Decrease(const Data &data)`

**Returns:** `void`

Decreases the reference count of the given object. If it is not registered, this request is ignored. If reference count of the object reaches 0, it is deleted.

##### `if(v<=0)`

**Returns:** ``

##### `Reset(const Data &data)`

**Returns:** `void`

Resets the reference count to 0

##### `IsRegistered(const Data &data)`

**Returns:** `bool`

##### `Unregister(const Data &data)`

**Returns:** `void`

Unregisters an object from reference counter

##### `GetRidOf(Data &data)`

**Returns:** `void`

Never use without a proper reason. Gets rid of the data without destroying its content. It does decrease reference count. However, if it hits 0 it will not destroy its count.

##### `list(—)`

**Returns:** `void`

##### `for(auto it : references)`

**Returns:** ``


### `Variable`

**Namespace:** `Scripting`

This class represents a variable. It contains the data and the name of the variable.

#### Methods

##### `Set(Any value)`

**Returns:** `void`

Creates an invalid variable Creates an invalid variable Constructor that sets the name, type and value of the variable. Unless this variable is declared inside an executing code, definedin should be left nullptr. Constructor that sets the name, and type of the variable. Default value of the specified type is used as value. Unless this variable is declared inside an executing code, definedin should be left nullptr. Sets the data contained in this variable without changing its type

##### `Set(const Data &value)`

**Returns:** `void`

Sets the data contained in this variable

##### `Set(const Type &type, Any value)`

**Returns:** `void`

Sets the data contained in this variable by modifying its type. Also this function resets the tags unless they are re-specified

##### `SetReferenceable(const Data &value)`

**Returns:** `void`

Sets the data contained in this variable. If it is a reference, the value that is referenced is updated

##### `GetName(—)`

**Returns:** `std::string`

Returns the name of the variable

##### `IsReferenceAssigned(—)`

**Returns:** `bool`


### `ParameterTemplate`

**Namespace:** `Scripting`

This class holds information about a parameter without resolving constructs


---

## Functions

### `if(isconstant)`

**Returns:** ``



### `CastException("Constant", "Non-constant", "While performing assignment")`

**Returns:** `throw`


