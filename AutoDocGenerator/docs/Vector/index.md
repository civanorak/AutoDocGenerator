# Vector

&gt; Auto-generated documentation for the **Vector** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `PushBackUnique(V_ &vector, T_ &&val)`

**Returns:** `void`


This function push_backs an item to the given vector if the item does not exists in the vector


### `for(const auto &e : vector)`

**Returns:** ``



### `PushBackUnique(V_ &vector, const T_ &val, P_ pred)`

**Returns:** `void`


This function push_backs an item to the given vector if the item does not exists in the vector using the given predicate


### `for(const auto &e : vector)`

**Returns:** ``



### `PushBackOrUpdate(V_ &vector, T_ &&val)`

**Returns:** `void`


This function push_backs an item to the given vector if the item does not exists in the vector, if the item is found, it will be updated


### `for(auto &e : vector)`

**Returns:** ``



### `PushBackOrUpdate(V_ &vector, const T_ &val, P_ pred)`

**Returns:** `void`


This function push_backs an item to the given vector if the item does not exists in the vector using the given predicate, if the item is found, it will be updated


### `for(auto &e : vector)`

**Returns:** ``


