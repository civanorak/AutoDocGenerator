# Iterator

&gt; Auto-generated documentation for the **Iterator** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Iterator`

**Namespace:** `Containers`

Generic iterator interface. Derive from this class supplying self, type, and distance type Following functions should be implemented for Iterators. They are publicly shaped by this class. These functions are not virtually defined, this allows inlining and reduces memory usage @code protected: T_& current() const				... bool moveby(int amount)			... bool isvalid() const			    ... bool compare(const I_ &) const	... void set(const I_ &)			    ... D_  distance(const I_ &) const   ... bool isbefore(const I_ &) const  ... @endcode

#### Methods

##### `Iterator(—)`

**Returns:** ``

Cannot be constructed unless overridden

##### `MoveBy(int amount)`

**Returns:** `bool`

Returns current item Returns current item Moves the iterator by the given amount

##### `Next(—)`

**Returns:** `bool`

Advances the iterator to the next item

##### `Previous(—)`

**Returns:** `bool`

Moves to the previous item

##### `IsValid(—)`

**Returns:** `bool`

Checks if the iterator is pointing to a valid item

##### `bool(—)`

**Returns:** `explicit operator`

Checks if the operator is pointing to a valid item

##### `IsValid(—)`

**Returns:** `return`

##### `Compare(const I_ &iterator)`

**Returns:** `bool`

Index notation Compares two iterators if they point to the same item

##### `Distance(const I_ &iterator)`

**Returns:** `D_`

Returns the distance to the given iterator

##### `iterator(—)`

**Returns:** `return`

Compares two iterators if they point to the same item Checks whether current operator is after the given Checks if the current operator is before the given Checks whether current operator is after or at the same point Checks whether current operator is before or at the same point Compares this iterator with another Moves this iterator to the item pointed by the given Returns the distance to the given iterator Creates a new iterator adding the given offset Creates a new iterator subtracting the given offset Moves the D_ by the given offset to forwards

##### `iterator(—)`

**Returns:** `return`

Moves the iterator by the given offset to backwards

##### `iterator(—)`

**Returns:** `return`

Moves the iterator to forwards

##### `iterator(—)`

**Returns:** `return`

Moves the iterator to backwards


### `ValueIterator`

**Namespace:** `Containers`

Moves the iterator to forwards Moves the iterator to backwards Dereferences the operator to get its value Dereferences the operator to access its values Generic iterator interface. Derive from this class supplying self, type, and distance type Following functions should be implemented for Iterators. They are publicly shaped by this class. These functions are not virtually defined, this allows inlining and reduces memory usage @code protected: T_& current() const				... bool moveby(int amount)			... bool isvalid() const			    ... bool compare(const I_ &) const	... void set(const I_ &)			    ... D_  distance(const I_ &) const   ... bool isbefore(const I_ &) const  ... @endcode

#### Methods

##### `ValueIterator(—)`

**Returns:** ``

Cannot be constructed unless overridden

##### `Current(—)`

**Returns:** `T_`

Returns current item

##### `MoveBy(int amount)`

**Returns:** `bool`

Moves the iterator by the given amount

##### `Next(—)`

**Returns:** `bool`

Advances the iterator to the next item

##### `Previous(—)`

**Returns:** `bool`

Moves to the previous item

##### `IsValid(—)`

**Returns:** `bool`

Checks if the iterator is pointing to a valid item

##### `bool(—)`

**Returns:** `explicit operator`

Checks if the operator is pointing to a valid item

##### `IsValid(—)`

**Returns:** `return`

##### `Compare(const I_ &iterator)`

**Returns:** `bool`

Index notation Compares two iterators if they point to the same item

##### `Distance(const I_ &iterator)`

**Returns:** `D_`

Returns the distance to the given iterator

##### `iterator(—)`

**Returns:** `return`

Compares two iterators if they point to the same item Checks whether current operator is after the given Checks if the current operator is before the given Checks whether current operator is after or at the same point Checks whether current operator is before or at the same point Compares this iterator with another Moves this iterator to the item pointed by the given Returns the distance to the given iterator Creates a new iterator adding the given offset Creates a new iterator subtracting the given offset Moves the D_ by the given offset to forwards

##### `iterator(—)`

**Returns:** `return`

Moves the iterator by the given offset to backwards

##### `iterator(—)`

**Returns:** `return`

Moves the iterator to forwards

##### `iterator(—)`

**Returns:** `return`

Moves the iterator to backwards


### `Iterator`

**Namespace:** `internal`

@endcond  This iterator allows iteration of directories. It is a forward only iterator. An empty iterator can be used for end(). Also instead of comparing the iterator with end, IsValid() function could be used.

#### Methods

##### `Iterator(const std::string &directory, const std::string &pattern="*")`

**Returns:** `explicit`

Creates a new iterator from the given directory and pattern. @param  directory is the directory to be iterated. Should exists, otherwise it will throw PathNotFoundError @param  pattern wildcard pattern to match paths against @throw  PathNotFoundError if the given directory does not exists

##### `Iterator(const Iterator &other)`

**Returns:** ``

 Move constructor  Copy constructor

##### `Swap(Iterator &other)`

**Returns:** `void`

 Empty constructor. Effectively generates end iterator  Assignment  Destructor  Swaps iterators, used for move semantics

##### `swap(data, other.data)`

**Returns:** ``

##### `swap(basedir, other.basedir)`

**Returns:** ``

##### `swap(current, other.current)`

**Returns:** ``

##### `Get(—)`

**Returns:** `std::string`

Returns the current path. @throw std::runtime_error (debug only) if the iterator is not vali

##### `if(!data || current=="")`

**Returns:** ``

##### `if(!data || current=="")`

**Returns:** ``

Returns the current path. @throw std::runtime_error (debug only) if the iterator is not vali

##### `Get(—)`

**Returns:** `return`

Returns the current path. @throw std::runtime_error (debug only) if the iterator is not valid

##### `Get(—)`

**Returns:** `return`

Returns the current path. @throw std::runtime_error (debug only) if the iterator is not valid

##### `Current(—)`

**Returns:** `std::string`

Returns the current path. @throw std::runtime_error (debug only) if the iterator is not valid

##### `Get(—)`

**Returns:** `return`

##### `Next(—)`

**Returns:** ``

 Move to the next path in the directory

##### `Next(—)`

**Returns:** ``

 Moves directory by i elements  Move to the next path in the directory, return unmodified iterator

##### `Next(—)`

**Returns:** `bool`

Next path in the directory @return true if the iterator is valid @throw std::runtime_error (debug only) if the iterator is not valid

##### `Destroy(—)`

**Returns:** `void`

Destroys the current iterator. @cond INTERNAL Should set both data and current to empty @endcond

##### `IsValid(—)`

**Returns:** `bool`

 Checks whether the iterator is valid


### `Iterate`

**Namespace:** `internal`

 Compares two iterators  Compares two iterators

#### Methods

##### `begin(—)`

**Returns:** `Iterator`

##### `end(—)`

**Returns:** `Iterator`


---

## Functions

### `Remove(const I_ &first, const I_ &end)`

**Returns:** `void`


Moves the iterator to forwards Moves the iterator to backwards Dereferences the operator to get its value This function works with collection iterators


### `for(I_ i=first; i!=end; ++i)`

**Returns:** ``



### `Delete(const I_ &first, const I_ &end)`

**Returns:** `void`


This function works with collection iterators


### `for(I_ i=first; i!=end; ++i)`

**Returns:** ``



### `Find(const I_ &first, const I_ &end, const T_ &item)`

**Returns:** `I_`


This function works with collection iterators


### `for(I_ i=first; i!=end; ++i)`

**Returns:** ``



### `I_()`

**Returns:** `return`



### `AddCopy(C_ &target, const I_ &it)`

**Returns:** `void`


This function copies the contents of the given iterator as long as it can be dereferenced to the given container using Add method.


### `for(I_ i=it; i.IsValid()`

**Returns:** ``



### `AddCopy(C_ &target, const I_ &begin, const I_ &end)`

**Returns:** `void`


This function copies the contents of the given iterator to the given iterator into the given container using Add method.


### `for(I_ i=begin; i!=end; ++i)`

**Returns:** ``



### `AddCopy(std::vector<T_, A_> &target, const I_ &it)`

**Returns:** `void`


This function copies the contents of the given iterator to the given iterator into the given vector using push_back method.


### `for(I_ i=it; i.IsValid()`

**Returns:** ``



### `AddCopy(std::vector<T_, A_> &target, const I_ &begin, const I_ &end)`

**Returns:** `void`


This function copies the contents of the given iterator as long as it can be dereferenced into the given vector using push_back method.


### `for(I_ i=begin; i!=end; i++)`

**Returns:** ``



### `for(auto &e : vec)`

**Returns:** ``


Allows streaming of vectors


### `swap(Iterator &l, Iterator &r)`

**Returns:** `inline void`


 Swaps two iterators


### `Collect(std::vector<std::string> paths, F_ checkfn, int maxdepth = -1)`

**Returns:** `std::vector<std::string>`


Collects all files matching the given predicate to a vector. Vector contains paths relative to the given path. @param paths are files/directories that will be collected @param checkfn is a function taking a string, returning bool. Return true to add the file into the collection @param maxdepth is the recursion depth. -1 means infinite


### `for(auto it = Iterator(name)`

**Returns:** ``



### `Collect(const std::string &path, F_ checkfn, int maxdepth = -1)`

**Returns:** `std::vector<std::string>`


Collects all files matching the given predicate to a vector. Filenames in the vector contains the path as well. @param path is the directory to start collecting @param checkfn is a function taking a string, returning bool. Return true to add the file into the collection @param maxdepth is the recursion depth. -1 means infinite


### `Collect({path}, checkfn, maxdepth)`

**Returns:** `return`



### `Collect(const std::string &path, int maxdepth = -1)`

**Returns:** `inline std::vector<std::string>`


Collects all files in the given directory to a vector. Filenames in the vector contains the path as well. @param path is the directory to start collecting @param maxdepth is the recursion depth. -1 means infinite


### `Collect({path}, [](auto)`

**Returns:** `return`



### `Collect(std::vector<std::string> paths, int maxdepth = -1)`

**Returns:** `inline std::vector<std::string>`


Collects all given files to a vector with controllable depth. Filenames in the vector contains the path as well. @param paths are files/directories that will be collected @param maxdepth is the recursion depth. -1 means infinite


### `Collect(std::vector<std::string> paths, const std::vector<std::string> &extensions, int maxdepth = -1)`

**Returns:** `inline std::vector<std::string>`


Collects all given files to a vector if their extension matches the supplied list. Filenames in the vector contains the path as well. @param paths are files/directories that will be collected @param extensions are the allowed file extensions, enter only lowercase extensions @param maxdepth is the recursion depth. -1 means infinite

