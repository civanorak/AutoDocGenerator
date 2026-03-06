# Hashmap

&gt; Auto-generated documentation for the **Hashmap** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Hashmap`

**Namespace:** `Containers`

#### Methods

##### `Iterator_(—)`

**Returns:** ``

Iterators are derived from this class. Any operations on uninitialized iterators is undefined behavior. @copydoc Gorgon::Container::Iterator Default constructor, creates an iterator pointing to an invalid location

##### `Remove(—)`

**Returns:** `void`

Copies another iterator Removes the item pointed by this iterator from the container. @warning: This operation will move iterator one step forward. Meaning that a simple for loop will not be sufficient to selectively remove items. If an item is removed from the container, iterator should not be incremented.

##### `if(container==nullptr)`

**Returns:** ``

##### `Delete(—)`

**Returns:** `void`

Deletes the item pointed by this iterator from the container. @warning: This operation will move iterator one step forward. Meaning that a simple for loop will not be sufficient to selectively remove items. If an item is removed from the container, iterator should not be incremented.

##### `if(container==nullptr)`

**Returns:** ``

##### `SetItem(typename H_::ValueType &newitem, bool deleteprev=false)`

**Returns:** `void`

Changes the current item. If deleteprev is set, the previous item will be deleted

##### `if(deleteprev)`

**Returns:** ``

##### `current(—)`

**Returns:** `Type`

@cond INTERAL Satisfies the needs of Iterator

##### `isvalid(—)`

**Returns:** `bool`

##### `moveby(long amount)`

**Returns:** `bool`

##### `if(amount>0)`

**Returns:** ``

##### `isvalid(—)`

**Returns:** `return`

##### `compare(const Iterator_ &it)`

**Returns:** `bool`

##### `set(const Iterator_ &it)`

**Returns:** `void`

##### `distance(const Iterator_ &it)`

**Returns:** `long`

##### `isbefore(const Iterator_ &it)`

**Returns:** `bool`

##### `set(iterator)`

**Returns:** ``

@endcond Assignment operator


### `ConstIterator`

**Namespace:** `Containers`

Regular iterator. @see Container::Iterator Const iterator allows iteration of const collections

#### Methods

##### `ConstIterator(const Iterator &it)`

**Returns:** ``

Regular iterators can be converted to const iterators

##### `Remove(—)`

**Returns:** `void`

##### `Delete(—)`

**Returns:** `void`

##### `SetKey(const K_ &newkey)`

**Returns:** `void`


---

## Functions

### `Hashmap()`

**Returns:** ``


Default constructor


### `for(auto &p : list)`

**Returns:** ``


Filling constructor. This constructor uses initializer list of std::pair&lt;K_, T_*&gt;. This function works faster by forwarding the lsit to underlying storage. However, it cannot deal with nullptr entries, thus can leave the container in undefined state. A test agains this case is performed for debug builds.


### `assert(p.second && "Element is nullptr")`

**Returns:** ``



### `Hashmap(std::initializer_list<std::pair<const K_, T_&>> list)`

**Returns:** ``


Filling constructor. This constructor uses initializer list of std::pair&lt;K_, T_&&gt;


### `for(auto &p : list)`

**Returns:** ``



### `Hashmap(std::initializer_list<T_*> list)`

**Returns:** ``


Filling constructor that takes the keys using KeyFn function. This constructor handles nullptr entries by ignoring them.


### `assert(KeyFn && "Key retrieval function should be set.")`

**Returns:** ``



### `for(auto &p : list)`

**Returns:** ``



### `if(p)`

**Returns:** ``



### `Hashmap(Hashmap &&other)`

**Returns:** ``


Copy constructor is disabled Move constructor


### `Swap(other)`

**Returns:** ``



### `Duplicate()`

**Returns:** `Hashmap`



### `Swap(Hashmap &other)`

**Returns:** `void`


Swaps two hashmaps


### `swap(mapping, other.mapping)`

**Returns:** ``



### `RemoveAll()`

**Returns:** ``


Copy constructor is disabled Move constructor, does not delete elements.


### `Swap(other)`

**Returns:** ``



### `Add(const K_ &key, T_ &obj, bool deleteprev = false)`

**Returns:** `void`


Adds the given item with the related key. If the key already exists, the object it points to is changed. If deleteprev is set, previous object at the key is deleted.


### `if(deleteprev)`

**Returns:** ``



### `Add(const K_ &key, T_ *obj, bool deleteprev = false)`

**Returns:** `void`


Adds the given item with the related key. If the key already exists, the object it points to is changed. If deleteprev is set, previous object at the key is deleted. If obj is nullptr and the key exists in the map, it is removed.


### `if(obj)`

**Returns:** ``



### `if(deleteprev)`

**Returns:** ``



### `if(deleteprev)`

**Returns:** ``



### `Add(T_ &obj, bool deleteprev=false)`

**Returns:** `void`


Adds the given item by retrieving the related key. If the key already exists, the object it points to is changed. If deleteprev is set, previous object at the key is deleted.


### `assert(KeyFn!=nullptr && "Key retrieval function should be set.")`

**Returns:** ``



### `Add(T_ *obj, bool deleteprev=false)`

**Returns:** `void`


Adds the given item by retrieving the related key. If the key already exists, the object it points to is changed. If deleteprev is set, previous object at the key is deleted. If obj is nullptr and the key exists in the map, it is removed.


### `assert(KeyFn!=nullptr && "Key retrieval function should be set.")`

**Returns:** ``



### `Add({}, obj, deleteprev)`

**Returns:** ``



### `Remove(const K_ &key)`

**Returns:** `void`


Removes the item with the given key from the mapping. If the item does not exists, this request is simply ignored. This function does not delete the item.


### `Delete(const K_ &key)`

**Returns:** `void`


Removes the item with the given key from the mapping and deletes it. If the item does not exists, this request is simply ignored


### `RemoveAll()`

**Returns:** `void`


Removes all elements from this mapping without deleting them. Additonally, any memory that is being used by std::map is not freed.


### `Collapse()`

**Returns:** `void`


Clears the contents of the map and releases the memory used for the list. Items are not freed.


### `swap(mapping, newmap)`

**Returns:** ``



### `DeleteAll()`

**Returns:** `void`


Deletes and removes all the elements of this map.


### `for(auto &p : mapping)`

**Returns:** ``



### `Destroy()`

**Returns:** `void`


Deletes and removes all the elements of this map, in addition to destroying data used.


### `for(auto &p : mapping)`

**Returns:** ``



### `Collapse()`

**Returns:** ``



### `GetCount()`

**Returns:** `long`


Returns the number of elements in the map


### `GetSize()`

**Returns:** `long`


Returns the number of elements in the map


### `properthrow(key)`

**Returns:** ``


If not found throws.


### `Exists(const K_ &key)`

**Returns:** `bool`


Checks if an element with the given key exists


### `FindObject(const T_ &obj)`

**Returns:** `Iterator`


Finds the given key in the hashmap and returns iterator for it. An !IsValid() iterator is returned if item is not found


### `for(auto it = mapping.begin()`

**Returns:** ``



### `if(it->second == &obj)`

**Returns:** ``



### `Iterator(*this, it)`

**Returns:** `return`



### `FindObject(const T_ &obj)`

**Returns:** `ConstIterator`


Finds the given key in the hashmap and returns iterator for it. An !IsValid() iterator is returned if item is not found


### `for(auto it = mapping.begin()`

**Returns:** ``



### `if(it->second == &obj)`

**Returns:** ``



### `Iterator(*this, it)`

**Returns:** `return`



### `Find(const K_ &key)`

**Returns:** `Iterator`


Finds the given key in the hashmap and returns iterator for it. An !IsValid() iterator is returned if item is not found


### `Find(const K_ &key)`

**Returns:** `ConstIterator`


Finds the given key in the hashmap and returns iterator for it. An !IsValid() iterator is returned if item is not found


### `begin()`

**Returns:** `Iterator`


@name Iterator related @{ begin iterator


### `end()`

**Returns:** `Iterator`


end iterator


### `First()`

**Returns:** `Iterator`


returns the iterator to the first item


### `Last()`

**Returns:** `Iterator`


returns the iterator to the last item


### `Iterator(*this, it)`

**Returns:** `return`



### `begin()`

**Returns:** `ConstIterator`


begin iterator


### `end()`

**Returns:** `ConstIterator`


end iterator


### `First()`

**Returns:** `ConstIterator`


returns the iterator to the first item


### `Last()`

**Returns:** `ConstIterator`


returns the iterator to the last item


### `ConstIterator(*this, it)`

**Returns:** `return`



### `properthrow(const K__ &key)`

**Returns:** `typename std::enable_if<TMP::IsStreamable<K__>::Value, void>::type`


@}


### `ASSERT(false, "Item not found", 0, 8)`

**Returns:** ``



### `swap(Hashmap<K_, T_, KeyFn, M_, C_> &left, Hashmap<K_, T_, KeyFn, M_, C_> &right)`

**Returns:** `void`


