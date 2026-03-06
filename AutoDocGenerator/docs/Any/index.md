# Any

&gt; Auto-generated documentation for the **Any** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Any`

**Namespace:** `Gorgon`

This class can hold any other information providing type erasure. It requires the type to be either copy constructible or move constructible. Type safety is ensured during debug using RTTI information.  This class only checks type safety in debug mode. In release it only checks for Any being empty. This check can also be removed if it causes bottleneck. Define GORGON_FAST_ANY to remove these checks.  Currently cannot work with object without copy constructor.

#### Methods

##### `Any(const TMP::RTTS &typeinterface, void *data)`

**Returns:** ``

Default constructor. Initializes and empty Any. Unsafe! Constructs any from give raw data. Both typeinterface and data are duplicated. @warning Using this constructor might be dangerous

##### `Any(void *data, const TMP::RTTS &typeinterface)`

**Returns:** ``

Unsafe! Constructs any from give raw data. typeinterface is duplicated. Ownership of data is taken. @warning Using this constructor might be dangerous

##### `Any(const T_ &data)`

**Returns:** ``

Creates a new Any from the given data. This constructor duplicates the given data. Requires type in the copied Any to be copy constructible.

##### `Any(const Any &any)`

**Returns:** ``

Copy constructor. Requires type in the copied Any to be copy constructible.

##### `if(any.content)`

**Returns:** ``

##### `Swap(any)`

**Returns:** ``

Move constructor. Requires type in the copied Any to be move constructible.

##### `ASSERT(type, "Any is not set")`

**Returns:** ``

Returns TypeInfo used by current data

##### `Clear(—)`

**Returns:** ``

Returns TypeInterface used by this any. Copies the information in the given Any. It requires type in the copied Any to be copy constructible.

##### `if(any.type)`

**Returns:** ``

##### `Clear(—)`

**Returns:** ``

Moves the information in the given Any to this Any. This function directly moves the pointer therefore, no copying or moving performed on the original type.

##### `Swap(any)`

**Returns:** ``

##### `Set(value)`

**Returns:** ``

Set the content of the Any to the given value. The value is duplicated. Requires T_ to be copy constructible.

##### `Swap(Any &other)`

**Returns:** `void`

Swaps the contents of the current any with another. Does not perform copying or moving.

##### `swap(type, other.type)`

**Returns:** ``

##### `swap(content, other.content)`

**Returns:** ``

##### `Set(const T_ &data)`

**Returns:** `void`

Set the content of the Any to the given value. The value is duplicated. Requires T_ to be copy constructible.

##### `Clear(—)`

**Returns:** ``

##### `Set(T_ &&data)`

**Returns:** `void`

Set the content of the Any to the given value. The value is moved. Requires T_ to be move constructible.

##### `Clear(—)`

**Returns:** ``

##### `Clear(—)`

**Returns:** `void`

Clears the content of the any.

##### `if(content)`

**Returns:** ``

##### `SetRaw(void *data)`

**Returns:** `void`

Unsafe! This function returns raw data contained within any. @warning this function is unsafe Unsafe! This function sets the raw data contained within any, without modifying its type data. data is duplicated. @warning this function is unsafe

##### `SetRaw(TMP::RTTS *type, void *data)`

**Returns:** `void`

Unsafe! This function sets the raw data contained within any, while modifying its type data. type and data are duplicated. @warning this function is unsafe

##### `Clear(—)`

**Returns:** ``

##### `Set(const T_ &data, TMP::RTTS *type)`

**Returns:** `void`

Unsafe! This function sets the data contained within any with regular means. However, the type info is user supplied. Its primary aim is to be able to set pointer types from from void pointers. This can also be used as type casting. @warning this function is unsafe

##### `Clear(—)`

**Returns:** ``

##### `AssumeRaw(TMP::RTTS &type, void *data)`

**Returns:** `void`

Unsafe! This function sets the raw data contained within any, while modifying its type data. type is duplicated, whereas data ownership is assumed. @warning this function is unsafe

##### `Clear(—)`

**Returns:** ``

##### `SetType(const TMP::RTTS &type)`

**Returns:** `void`

Unsafe! Disowns the data contained in this any. The data is not freed. This function returns the raw pointer that is disowned Unsafe! This function modifies type information of the data content. type is duplicated @warning this function is extremely unsafe, basically, it performs reinterpret_cast

##### `if(!type || !content)`

**Returns:** ``

Returns the value contained with this any. If this Any is not const, this method could be used to move the object out of Any. It can also be used to modify the value contained within this Any. @throw std::runtime_error if Any is empty @throw std::bad_cast (debug only) if types do not match

##### `GetTypeName(—)`

**Returns:** `std::string`

##### `if(!type || !content)`

**Returns:** ``

Returns the value contained with this any. If this Any is not const, this method could be used to move the object out of Any. It can also be used to modify the value contained within this Any. @throw std::runtime_error if Any is empty @throw std::bad_cast (debug only) if types do not match

##### `UnsafeGet(—)`

**Returns:** `T_`

Unsafe version of Get. Should be used as last resort. Only const version is available. @warning Does not perform type check even in debug mode @throw std::runtime_error if Any is empty

##### `if(!type || !content)`

**Returns:** ``

##### `TypeCheck(—)`

**Returns:** `bool`

Checks whether the Any is the same type with the given type.

##### `IsSameType(const Any &other)`

**Returns:** `bool`

Checks whether the Any is the same type with the given type.

##### `IsPointer(—)`

**Returns:** `bool`

Checks if any contains a pointer

##### `if(!type || !this->content)`

**Returns:** ``

Returns the pointer without type information Compares the contents of this Any to the given value. The value should be the same type as this Any. Even if it is possible, no cross type comparison will be performed. You may use `any.Get<originaltype>() == othertype_variable` @throw std::runtime_error if Any is empty @throw std::bad_cast (debug only) if types do not match

##### `if(!content.content && !this->content)`

**Returns:** ``

Compares two Any variables. @return true if both are empty or have their contents equal. @throw std::bad_cast (debug only) if types do not match

##### `if(!content.content || !this->content)`

**Returns:** `else`

##### `IsSet(—)`

**Returns:** `bool`

Compares the contents of this Any to the given value. The value should be the same type as this Any. Even if it is possible, no cross type comparison will be performed. You may use `any.Get<originaltype>() == othertype_variable` @throw std::runtime_error if Any is empty @throw std::bad_cast (debug only) if types do not match Compares two Any variables. @return true if both are empty or have their contents equal. @throw std::bad_cast if types do not match  Checks whether the Any is set

##### `Clear(—)`

**Returns:** ``

 Destructor


### `CopyFreeAny`

**Namespace:** `Gorgon`

@cond internal


### `CopyFreeAny_impl`

**Namespace:** `Gorgon`

#### Methods

##### `CopyFreeAny_impl(CopyFreeAny_impl &&other)`

**Returns:** ``

