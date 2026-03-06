# RefCounter

&gt; Auto-generated documentation for the **RefCounter** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `RefCounter`

**Namespace:** `Gorgon`

RefCounter helps implementing reference counted objects. Suitable for shared implicit heap management and flyweight objects. RefCounter requires destroy method to be implemented by client classes.  Copy constructor should increment counter, assignment should call refassign, destructor should decrement counter. Add/subtract is not called automatically.

#### Methods

##### `refassign(const RefCounter &ref)`

**Returns:** `void`

Assigns another counted object into this one

##### `removeref(—)`

**Returns:** ``

##### `addref(—)`

**Returns:** ``

##### `refcheck(—)`

**Returns:** `bool`

Checks if the reference is still alive

##### `addref(—)`

**Returns:** `void`

Adds a count to the reference

##### `removeref(—)`

**Returns:** `void`

Destroys

##### `getrefcount(—)`

**Returns:** `int`

returns the number of references.

##### `newinstance(—)`

**Returns:** `void`

creates a new instance of the contained data. Effectively this creates a new reference counter with value of 1. Old reference is not reduced.

