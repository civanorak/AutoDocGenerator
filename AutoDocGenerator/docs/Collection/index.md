# Collection

&gt; Auto-generated documentation for the **Collection** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Collection`

**Namespace:** `Containers`

Collection is a container for reference typed objects. A container never copies its elements nor destroys unless requested specifically. Internally, a collection stores its objects in a vector as pointers. This class supports move semantics. Also copying of a collection is disabled for performance reasons. Use Duplicate method to create a duplicate of a collection.


### `sorter`

**Namespace:** `Containers`

#### Methods

##### `predicate(*left, *right)`

**Returns:** `return`


### `Iterator_`

**Namespace:** `Containers`

Iterators are derived from this class @copydoc Gorgon::Container::Iterator

#### Methods

##### `Remove(—)`

**Returns:** `void`

Default constructor, creates an iterator pointing to invalid location Copies another iterator Removes the item pointed by this iterator. The iterator position will point the previous item, so that the next item will not be missed when iterator is incremented. This allows easy removal of elements using a simple for loop.

##### `Delete(—)`

**Returns:** `void`

Deletes the item pointed by this iterator. The iterator position will point the previous item, so that the next item will not be missed when iterator is incremented. This allows easy removal of elements using a simple for loop.

##### `isvalid(—)`

**Returns:** `bool`

@cond INTERAL Satisfies the needs of Iterator

##### `isinrange(—)`

**Returns:** `bool`

##### `moveby(long amount)`

**Returns:** `bool`

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


### `Adder`

**Namespace:** `Containers`

@cond INTERNAL


---

## Functions

### `Collection(T_ &t, Args_ &... args)`

**Returns:** ``


@endcond Default constructor Initializing constructor. @warning Visual studio erroneously allows rvalues (function return values or temporaries) to be bound to normal references. This means, its possible to pass those without getting an error. This problem is fixed by setting warning 4239 to cause an error. If working with older libraries that require this behavior, @code use #pragma warning(disable: 4329) @endcode before including necessary header.


### `Add(t, args...)`

**Returns:** ``



### `Collection(T_ *t, Args_ *... args)`

**Returns:** ``


Initializing constructor. @warning Visual studio erroneously allows rvalues (function return values or temporaries) to be bound to normal references. This means, its possible to pass those without getting an error. This problem is fixed by setting warning 4239 to cause an error. If working with older libraries that require this behavior, use @code #pragma warning(disable: 4329) @endcode before, including necessary header.


### `Add(t, args...)`

**Returns:** ``



### `Collapse()`

**Returns:** ``


Disabled Disabled Move constructor Move assignment


### `Swap(Collection &col)`

**Returns:** `void`


Swaps the given collection with this one


### `Duplicate()`

**Returns:** `Collection`


Duplicates this collection. Copy constructor is disabled for performance reasons. Therefore, this function is necessary to duplicate a collection


### `GetCount()`

**Returns:** `long`


Returns number of elements


### `GetSize()`

**Returns:** `long`


Returns number of elements


### `Add(T_* Data)`

**Returns:** `bool`


Adds the given item to the end of the list if it is not already in the list


### `Add(T_& data)`

**Returns:** `bool`


Adds a the given item to the end of the list if it is not already in the list


### `Add(&data)`

**Returns:** `return`



### `Push(T_* Data)`

**Returns:** `bool`


Adds the given item to the end of the list if it is not already in the list


### `Add(Data)`

**Returns:** `return`



### `Push(T_& data)`

**Returns:** `bool`


Adds a the given item to the end of the list if it is not already in the list


### `Add(data)`

**Returns:** `return`



### `Add(T_* Data, Args_ *... args)`

**Returns:** `int`


Removes and returns the last item in the collection Adds the given item to the end of the list, returns the number of added elements


### `Add(T_& data, Args_ &... args)`

**Returns:** `int`


Adds a the given item to the end of the list


### `Add(t)`

**Returns:** ``


Creates a new item and adds to the end of the collection


### `Insert(T_* data, long before)`

**Returns:** `bool`


this method adds the given object in front of the reference. You may use the size of the collection for this function to behave like Add.


### `Add(data)`

**Returns:** `return`



### `Insert(T_& data, long before)`

**Returns:** `bool`


this method adds the given object in front of the reference. You may use the size of the collection for this function to behave like Add.


### `Insert(&data, before)`

**Returns:** `return`



### `Insert(T_* data, const T_ &before)`

**Returns:** `bool`


this method adds the given object in front of the reference. You may use the size of the collection for this function to behave like Add.


### `Insert(T_& data, const T_ &before)`

**Returns:** `bool`


this method adds the given object in front of the reference. You may use the size of the collection for this function to behave like Add.


### `Insert(t, before)`

**Returns:** ``


Creates a new item and inserts it before the given reference. You may use the size of the collection for this function to behave like Add.


### `Insert(t, before)`

**Returns:** ``


Creates a new item and inserts it before the given reference. You may use the size of the collection for this function to behave like Add.


### `MoveBefore(long index, long before)`

**Returns:** `void`


this method moves the given object in the collection in front of the reference


### `if(index>before)`

**Returns:** ``



### `MoveBefore(long index, const T_ &before)`

**Returns:** `void`


this method moves the given object in the collection in front of the reference


### `MoveBefore(const T_ &index, long before)`

**Returns:** `void`


this method moves the given object in the collection in front of the reference


### `MoveBefore(const T_ &index, const T_ &before)`

**Returns:** `void`


this method moves the given object in the collection in front of the reference


### `Add(Data)`

**Returns:** ``


Adds items to the end of the list. Use comma to add more than one item


### `Adder(*this)`

**Returns:** `return`



### `Add(&data)`

**Returns:** ``


Adds items to the end of the list. Use comma to add more than one item


### `Adder(*this)`

**Returns:** `return`



### `Remove(long index)`

**Returns:** `void`


Removes an item from the collection using its index


### `Remove(const T_ *item)`

**Returns:** `void`


Removes an item from the collection using its pointer. If the item does not exists, nothing is done.


### `Remove(l)`

**Returns:** ``



### `Remove(const T_ &data)`

**Returns:** `void`


Removes an item from the collection using its reference. If the item does not exists, nothing is done.


### `Remove(&data)`

**Returns:** ``



### `Remove(ConstIterator &it)`

**Returns:** `void`



### `Remove(Iterator &it)`

**Returns:** `void`



### `Delete(long index)`

**Returns:** `void`


Deletes an item from the collection using its index. Deleting both removes the item from the list and free the item itself.


### `Delete(const T_ *item)`

**Returns:** `void`


Deletes an item from the collection using its pointer. Deleting both removes the item from the list and free the item itself. If given item does not exists, this function deletes the item and does nothing else


### `if(l==-1)`

**Returns:** ``



### `Delete(l)`

**Returns:** ``



### `Delete(T_& data)`

**Returns:** `void`


Deletes an item from the collection using its reference. Deleting both removes the item from the list and free the item itself. If given item does not exists, this function deletes the item and does nothing else


### `Delete(&data)`

**Returns:** ``



### `Delete(ConstIterator &it)`

**Returns:** `void`



### `Delete(Iterator &it)`

**Returns:** `void`



### `Find(const T_ *item)`

**Returns:** `Iterator`


Searches the position of a given item, if not found end iterator returned


### `Find(const T_ &item)`

**Returns:** `Iterator`


Searches the position of a given item, if not found end iterator returned


### `Find(const T_ *item)`

**Returns:** `ConstIterator`


Searches the position of a given item, if not found end iterator returned


### `Find(const T_ &item)`

**Returns:** `ConstIterator`


Searches the position of a given item, if not found end iterator returned


### `FindLocation(const T_ *item)`

**Returns:** `long`


Searches the position of a given item, if not found -1 is returned


### `FindLocation(const T_ &item)`

**Returns:** `long`


Searches the position of a given item, if not found -1 is returned


### `FindLocation(&item)`

**Returns:** `return`



### `Sort()`

**Returns:** `void`


Sorts items in the collection. Regular std::sort cannot work on collections as assignment will copy objects Sorts items in the collection. Regular std::sort cannot work on collections as assignment will copy objects


### `begin()`

**Returns:** `Iterator`


Returns the element at the given index. Checks and throws if out of range Returns the element at the given index. Checks and throws if out of range Returns the item at a given index Returns the item at a given index @name Iterator related @{ begin iterator


### `Iterator(*this, 0)`

**Returns:** `return`



### `end()`

**Returns:** `Iterator`


end iterator


### `First()`

**Returns:** `Iterator`


returns the iterator to the first item


### `Iterator(*this, 0)`

**Returns:** `return`



### `Last()`

**Returns:** `Iterator`


returns the iterator to the last item


### `begin()`

**Returns:** `ConstIterator`


begin iterator


### `ConstIterator(*this, 0)`

**Returns:** `return`



### `end()`

**Returns:** `ConstIterator`


end iterator


### `First()`

**Returns:** `ConstIterator`


returns the iterator to the first item


### `ConstIterator(*this, 0)`

**Returns:** `return`



### `Last()`

**Returns:** `ConstIterator`


returns the iterator to the last item


### `Clear()`

**Returns:** `void`


@} Removes all items from the list, allocated memory for the list stays


### `Collapse()`

**Returns:** `void`


Clears the contents of the collection and releases the memory used for the list. Items are not freed.


### `swap(newlist, list)`

**Returns:** ``



### `DeleteAll()`

**Returns:** `void`


Deletes and removes all elements in the collection


### `Destroy()`

**Returns:** `void`


Destroys the entire collection, effectively deleting the contents and the list including all the memory used by it.


### `swap(newlist, list)`

**Returns:** ``



### `Reserve(long amount)`

**Returns:** `void`


Allocates memory for the given amount of items


### `return(list == other.list)`

**Returns:** ``


Compares the contents of two collections


### `removeat(long absolutepos)`

**Returns:** `void`


Compares the contents of two collections @cond INTERNAL


### `Remove(absolutepos)`

**Returns:** ``



### `deleteat(long absolutepos)`

**Returns:** `void`



### `Delete(absolutepos)`

**Returns:** ``



### `swap(Collection<T_> &l, Collection<T_> &r)`

**Returns:** `inline void`


@endcond Swaps two collections

