# Folder

> Auto-generated documentation for the **Folder** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Folder`

**Namespace:** `Gorgon`

This is basic folder resource, it contains other resources.

#### Methods

##### `Folder(—)`

**Returns:** ``

Default constructor

##### `Folder(File &file)`

**Returns:** ``

Constructs a folder over a specific file, it does not add the folder to the tree of the file though

##### `Folder(std::weak_ptr<File> file)`

**Returns:** ``

##### `Add(Base &resource)`

**Returns:** `void`

Destructor 01010000h, (System, Folder) @name Collection related @{ These functions allows modification of folder's children Adds a the given resource to this folder

##### `Add(Base *resource)`

**Returns:** `void`

Adds a the given resource to this folder

##### `Insert(Base &resource, long before)`

**Returns:** `void`

Inserts a the given resource to this folder before the given index

##### `Insert(Base *resource, long before)`

**Returns:** `void`

Inserts a the given resource to this folder before the given index

##### `MoveBefore(long index, long before)`

**Returns:** `void`

Moves the given item to the given position. It is possible to specify GetCount() as before to move the item to the end.

##### `MoveBefore(Base &item, long before)`

**Returns:** `void`

Moves the given item to the given position. It is possible to specify GetCount() as before to move the item to the end.

##### `Remove(Base &resource)`

**Returns:** `void`

Removes the given item

##### `Delete(Base &resource)`

**Returns:** `void`

Deletes the given item properly, minding any links

##### `setparenttonullptr(resource)`

**Returns:** ``

##### `GetCount(—)`

**Returns:** `int`

Returns the number of items contained

##### `Exists(int index)`

**Returns:** `bool`

Returns an item with the given index Returns an item with the given index Returns an item with the given index Checks whether an item in the given index is present

##### `Exists(const std::string &name)`

**Returns:** `bool`

Checks whether an item with the given name is present

##### `SetUseNameMap(bool value)`

**Returns:** `void`

Sets if the name map will be created on load. Defaults to false

##### `GetUseNameMap(—)`

**Returns:** `bool`

##### `Load(bool shallow=false)`

**Returns:** `bool`

@} @name Typecasting access @{ These functions allow access to children by casting them to the requested type Returns the item at the given index performing dynamic_cast to the given type. This function propagates bad_cast exception from dynamic_cast, does not perform range check Returns the item at the given index performing dynamic_cast to the given type. This function propagates bad_cast exception from dynamic_cast, does not perform range check @throw std::runtime_error if the given name is not found Returns the item at the given index performing dynamic_cast to the given type. This function returns nullptr if object cannot be casted to the given type. Returns the item at the given index performing dynamic_cast to the given type. This function returns nullptr if object cannot be casted to the given type. @throw std::runtime_error if the given name is not found @} Loads this resource if it is not loaded yet @param  shallow only loads immediate children of this resource

##### `IsLoaded(—)`

**Returns:** `bool`

Returns whether this resource is loaded

##### `load(std::shared_ptr<Reader> data, unsigned long size, bool first, bool shallow, bool load)`

**Returns:** `bool`

Prepares children to be used /This function loads a folder resource from the given file This is the actual load function. This function requires already opened and precisely positioned input stream


---

## Functions

### `if(reallyloadnames)`

**Returns:** ``



### `for(auto &child : children)`

**Returns:** ``



### `if(!f)`

**Returns:** ``



### `if(ret)`

**Returns:** ``



### `Resolve(file)`

**Returns:** ``



### `if(fullyloaded)`

**Returns:** ``



### `if(!load || onlyfirst)`

**Returns:** ``



### `if(!file)`

**Returns:** ``



### `LoadError(LoadError::NoFileObject, "There is no file object related with this folder.")`

**Returns:** `throw`



### `while(!target)`

**Returns:** ``



### `if(gid==GID::Folder_Names)`

**Returns:** ``



### `if(gid==GID::Folder_Props)`

**Returns:** `else`



### `if(load && gid==GID::Folder)`

**Returns:** `else`



### `if(onlyfirst)`

**Returns:** ``



### `if(resource)`

**Returns:** ``



### `if(onlyfirst)`

**Returns:** ``



### `if(!onlyfirst && load)`

**Returns:** ``



### `for(auto &base : children)`

**Returns:** ``


