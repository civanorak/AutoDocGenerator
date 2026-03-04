# Property

> Auto-generated documentation for the **Property** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Property`

**Namespace:** `Gorgon`

This is generic property that can be set and retrieved good for enums mostly, its ok to use with POD structs for direct assignment but better not to use it with complex data types.

#### Methods

##### `T_(—)`

**Returns:** `operator`

##### `T_(—)`

**Returns:** `operator const`

##### `Get(—)`

**Returns:** `T_`

##### `Set(const T_ &value)`

**Returns:** `void`


### `NumericProperty`

**Namespace:** `Gorgon`

Supports arithmetic operators including +, * ..., +=, ... ==, <, > but not &, && float, int, double, math/Complex


### `BooleanProperty`

**Namespace:** `Gorgon`

Supports logic operators. Mostly designed to be used with bool &&, ||, !, and equalities ==, !=


### `BinaryProperty`

**Namespace:** `Gorgon`

Supports all operators that the numeric property supports. Additionally supports and |, &, ~, ... Use with unsigned int, Gorgon::Byte


### `ObjectProperty`

**Namespace:** `Gorgon`

Object property allows the consumers of the property to be able to access object's member functions and data members in a const manner


### `MutableObjectProperty`

**Namespace:** `internal`

Object property allows the consumers of the property to be able to access objects member functions and variables. This alternative calls Setter anytime a member of the object is accessed, even if it is not changed. However, usage of dereferencing operator cannot be tracked.


### `ReferenceProperty`

**Namespace:** `internal`

Reference property allows clients to access a reference object within the class. This property does not have a setter, but instead it uses update function that is called whenever reference object is accessed by using -> operator. The client can call update function manually.

#### Methods

##### `Update(—)`

**Returns:** `void`

Compares two objects, this performs reference comparison, not lexical. Compares two objects, this performs reference comparison, not lexical. Compares two objects, this performs reference comparison, not lexical. Compares two objects, this performs reference comparison, not lexical.


### `ReferencePropertyWatch`

**Namespace:** `internal`


### `ObjectPropertyWatch`

**Namespace:** `internal`


### `TextualProperty`

**Namespace:** `internal`

Supports everything that string class supports including +, +=, length()

#### Methods

##### `length(—)`

**Returns:** `typename T_::size_type`

##### `substr(typename T_::size_type off=0U, typename T_::size_type len=T_::npos)`

**Returns:** `T_`

##### `find(const T_& str, typename T_::size_type pos = 0)`

**Returns:** `typename T_::size_type`

##### `find(const char* s, typename T_::size_type pos, typename T_::size_type n)`

**Returns:** `typename T_::size_type`

##### `find(const char* s, typename T_::size_type pos = 0)`

**Returns:** `typename T_::size_type`

##### `find(char c, typename T_::size_type pos = 0)`

**Returns:** `typename T_::size_type`

##### `rfind(const T_& str, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `rfind(const char* s, typename T_::size_type pos, typename T_::size_type n)`

**Returns:** `typename T_::size_type`

##### `rfind(const char* s, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `rfind(char c, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_first_of(const T_& str, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_first_of(const char* s, typename T_::size_type pos, typename T_::size_type n)`

**Returns:** `typename T_::size_type`

##### `find_first_of(const char* s, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_first_of(char c, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_last_of(const T_& str, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_last_of(const char* s, typename T_::size_type pos, typename T_::size_type n)`

**Returns:** `typename T_::size_type`

##### `find_last_of(const char* s, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_last_of(char c, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_first_not_of(const T_& str, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_first_not_of(const char* s, typename T_::size_type pos, typename T_::size_type n)`

**Returns:** `typename T_::size_type`

##### `find_first_not_of(const char* s, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_first_not_of(char c, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_last_not_of(const T_& str, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_last_not_of(const char* s, typename T_::size_type pos, typename T_::size_type n)`

**Returns:** `typename T_::size_type`

##### `find_last_not_of(const char* s, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `find_last_not_of(char c, typename T_::size_type pos = T_::npos)`

**Returns:** `typename T_::size_type`

##### `clear(—)`

**Returns:** `void`

##### `append(InputIterator first, InputIterator last)`

**Returns:** `TextualProperty&`

##### `T_(—)`

**Returns:** `operator`

##### `T_(—)`

**Returns:** `operator const`

