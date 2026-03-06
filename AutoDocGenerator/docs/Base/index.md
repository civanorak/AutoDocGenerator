# Base

&gt; Auto-generated documentation for the **Base** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Base`

**Namespace:** `Resource`

This class is the base for all Gorgon Resources. @warning This class is rather heavy and should not be used for small objects that are planned to be created a lot of.

#### Methods

##### `Base(—)`

**Returns:** ``

Default constructor

##### `virtual` `GetGID(—)`

**Returns:** `virtual GID::Type`

This function shall return Gorgon ID of this resource

##### `virtual` `Resolve(File &file)`

**Returns:** `virtual void`

This function shall resolve links or similar constructs. This function is intended to be called after a file is loaded. It has no meaning for in memory constructed resource trees. Default behavior is to pass the request to children.

##### `virtual` `Prepare(—)`

**Returns:** `virtual void`

This function shall prepare this resource to be used after resource is loaded. Default behavior is to pass the request to children

##### `virtual` `Discard(—)`

**Returns:** `virtual void`

This function shall discard any transitional data which is not vital after Prepare function is issued. This data can be image pixel buffer sound data buffer. Default behavior is to pass the request to children

##### `virtual` `IsEqual(const SGuid &guid)`

**Returns:** `virtual bool`

This function tests whether this object has the given SGuid

##### `virtual` `GetGuid(—)`

**Returns:** `virtual SGuid`

Returns the guid of the object

##### `virtual` `SetGuid(SGuid guid)`

**Returns:** `virtual void`

Changes the guid of the object

##### `virtual` `SetName(const std::string &name)`

**Returns:** `virtual void`

Returns the name of this object. @warning The object names are loaded only upon request Sets the name of the object

##### `HasParent(—)`

**Returns:** `bool`

Returns whether this object has a parent

##### `if(!root)`

**Returns:** ``

Returns the parent. If no parent set, this function throws std::runtime_error Returns the pointer to the parent. This function may return nullptr Returns the root of this resource. Root of a resource is always exists, in case of no parent, the root is the object itself. Note that this value is cached and maintained. In rare cases, it will be recalculated.

##### `if(!parent)`

**Returns:** ``

##### `begin(—)`

**Returns:** `const Containers::Collection<Base>::ConstIterator`

Allows easy iteration through range based fors

##### `end(—)`

**Returns:** `const Containers::Collection<Base>::ConstIterator`

Allows easy iteration through range based fors

##### `cbegin(—)`

**Returns:** `const Containers::Collection<Base>::ConstIterator`

Beginning of children

##### `cend(—)`

**Returns:** `const Containers::Collection<Base>::ConstIterator`

End of children

##### `DeleteResource(—)`

**Returns:** `bool`

Safely deletes the resource. If the resource is being used more a single place, this method will not delete the resource, instead it will decrement the reference count and returns false.

##### `Save(Writer &writer)`

**Returns:** `void`

Saves this object into the given writer. The writer should be open prior to this call

##### `virtual` `save(Writer &writer)`

**Returns:** `virtual void`

The children this object have. The elements in const collections are modifiable, therefore, its possible to modify properties of the children. However, children should be added to the object using member methods as some objects do not allow children, or allow children that are of specific type. **INTERNAL**, Reference count, used in linking mechanism. @warning Never change or rely on this value unless you know the internal mechanics of linking system. Any uninformed changes may cause leaks or worse, double deletion and crash of the program. Destructor, Always children gets destroyed first

##### `destroychildren(—)`

**Returns:** `void`

Destroys the children of this resource

##### `setparenttonullptr(Base &base)`

**Returns:** `void`

Sets the parent of an object to nullptr, provides access.


### `Base`

**Namespace:** `Organizers`

#### Methods

##### `AttachTo(WidgetContainer &container)`

**Returns:** `void`

Ensuring correct destruction Attaches this organizer to a container

##### `RemoveFrom(—)`

**Returns:** `void`

Removes the organizer from the container

##### `IsAttached(—)`

**Returns:** `bool`

Returns if this organizer is attached to a container

##### `PauseReorganize(—)`

**Returns:** `void`

Returns the container that this organizer is attached to. If organizer is not attached, this function will throw. Stops reorganizing. Even manual calls to reorganize will be ignored until StartReorganize is issued which will immediately reorganize everything.

##### `StartReorganize(—)`

**Returns:** `void`

Starts reorganizing. If paused, this will also call Reorganize.

##### `Reorganize(—)`

**Returns:** `void`

Reorganizes the widgets that are organized by this organizer

##### `IsReorganizing(—)`

**Returns:** `bool`

Adds the given widget to the attached container. Adds the given text as a label to the attached container Returns if the organizer is currently working

##### `virtual` `attachmentchanged(—)`

**Returns:** `virtual void`

Called when the attachment of the organizer is changed

##### `virtual` `reorganize(—)`

**Returns:** `virtual void`

Should reorganize the contents of the organizer. This will only be called if the organizer is attached.


---

## Functions

### `for(auto it=children.First()`

**Returns:** ``



### `for(auto &child : *this)`

**Returns:** ``



### `for(auto &child : *this)`

**Returns:** ``



### `destroychildren()`

**Returns:** ``



### `for(auto it=children.First()`

**Returns:** ``



### `if(it->parent==this)`

**Returns:** ``



### `save(writer)`

**Returns:** ``



### `attachmentchanged()`

**Returns:** ``



### `attachmentchanged()`

**Returns:** ``



### `Reorganize()`

**Returns:** ``



### `reorganize()`

**Returns:** ``



### `Add(l)`

**Returns:** ``


