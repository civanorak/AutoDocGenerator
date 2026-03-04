# GarbageCollection

> Auto-generated documentation for the **GarbageCollection** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `GarbageCollection`

**Namespace:** `Containers`

This class acts like a regular collection, however, it performs garbage collection over its elements. This class requires T_ to have a non member function called ShouldBeCollected which should return whether the item should be collected by garbage collector. This function should be resolved through ADL

#### Methods

##### `Collect(—)`

**Returns:** `void`

##### `for(auto it=this->First()`

**Returns:** ``

