# Data

> Auto-generated documentation for the **Data** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Data`

**Namespace:** `Gorgon`

#### Methods

##### `append(const T_ &values, const std::string &prefix, const R_ &reflectionobj)`

**Returns:** `void`

##### `append(const T_ &values, const std::string &prefix, const R_ &reflectionobj, TMP::Sequence<S_...>)`

**Returns:** `void`

##### `namedtransform(T_ &values, const std::string &prefix, const R_ &reflectionobj)`

**Returns:** ``

##### `namedtransform(T_ &values, const std::string &prefix, const R_ &reflectionobj, TMP::Sequence<S_...>)`

**Returns:** `void`

##### `namedtransform(T_ &values, const std::string &prefix, const R_ &reflectionobj)`

**Returns:** ``

##### `namedtransform(T_ &values, const std::string &prefix, const R_ &reflectionobj)`

**Returns:** ``

##### `namedtransform(T_ &values, const std::string &prefix, const R_ &reflectionobj, TMP::Sequence<S_...>)`

**Returns:** `void`

##### `Data(—)`

**Returns:** ``

Iterator for the data resource Constant iterator for the data resource Creates an empty Data

##### `Append(values, reflectionobj)`

**Returns:** ``

This constructor accepts a reflected struct and turns it into a resource data. The types are tried to be matched with the built-in data resources. Second parameter allows named reflection.

##### `Append(values, prefix, reflectionobj)`

**Returns:** ``

This constructor accepts a reflected struct and turns it into a resource data. The types are tried to be matched with the built-in data resources. Multiple objects having same member names can be saved to a single data using second parameter, which appends a prefix to object members. Third parameter allows named reflection.

##### `static_assert(R_::IsGorgonReflection, "The template argument R_ for this constructor should be reflection type of the struct.")`

**Returns:** ``

This function accepts a reflected struct and appends it to the resource data. The types are tried to be matched with the built-in data resources. Multiple objects having same member names can be saved to a single data using second parameter, which appends a prefix to object members. Third parameter allows named reflection.

##### `Append(values, "", reflectionobj)`

**Returns:** ``

##### `static_assert(R_::IsGorgonReflection, "The template argument R_ for this constructor should be reflection type of the struct.")`

**Returns:** ``

This function accepts a reflected struct and appends it to the resource data. The types are tried to be matched with the built-in data resources. Multiple objects having same member names can be saved to a single data using second parameter, which appends a prefix to object members. Third parameter allows named reflection.

##### `Append(T_ value)`

**Returns:** ``

Appends the given data to the end of this data resource

##### `Append(T_ &value)`

**Returns:** ``

Appends the given resource object to the end of this data resource

##### `Append(const std::string &name, T_ value)`

**Returns:** ``

Appends the given data to the end of this data resource with the specified name

##### `Append(const std::string &name, T_ &value)`

**Returns:** ``

Appends the given resource object to the end of this data resource with the specified name

##### `Insert(int value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, int value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(float value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, float value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(const std::string &value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, const std::string &value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(const char *value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, const char *value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Geometry::Point value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Geometry::Point value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Geometry::Pointf value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Geometry::Pointf value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Geometry::Size value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Geometry::Size value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Geometry::Rectangle value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Geometry::Rectangle value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Geometry::Bounds value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Geometry::Bounds value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Geometry::Margin value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Geometry::Margin value, int before)`

**Returns:** `void`

##### `Insert(Base *value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(const std::string &name, Base *value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(Base &value, int before)`

**Returns:** `void`

Inserts a data item to the given position

##### `Insert(&value, before)`

**Returns:** ``

##### `Insert(const std::string &name, Base &value, int before)`

**Returns:** `void`

Inserts a data item to the given position with the specified name

##### `Insert(name, &value, before)`

**Returns:** ``

##### `Get(int index)`

**Returns:** `T_`

Transforms the members of this resource data to the given struct. Members are matched by name. This version does not transfer the ownership of the object data. Transforms the members of this resource data to the given struct. Members are matched by name starting with prefix. This version does not transfer the ownership of the object data. Transforms the members of this resource data to the given struct. Members are matched by name. Any resource objects that are transformed into the structure are released. Transforms the members of this resource data to the given struct. Members are matched by name starting with prefix. Any resource objects that are transformed into the structure are released. Returns the data with the given index; use GetObject in order to get resource objects.

##### `static_assert(std::is_same<T_, int>::value, "Unknown data type.")`

**Returns:** ``

##### `Get(const std::string &name)`

**Returns:** `T_`

Returns the data with the given name; use GetObject in order to get resource objects.

##### `static_assert(std::is_same<T_, int>::value, "Unknown data type.")`

**Returns:** ``

##### `begin(—)`

**Returns:** `ConstIterator`

Returns the resource object at the given index Returns the resource object with the given name Can be used to iterate over data objects

##### `end(—)`

**Returns:** `ConstIterator`

Can be used to iterate over data objects

##### `begin(—)`

**Returns:** `Iterator`

Can be used to iterate over data objects

##### `end(—)`

**Returns:** `Iterator`

Can be used to iterate over data objects

##### `for(auto &item : items)`

**Returns:** ``

Returns the data item with the given index Returns the data item with the given name

##### `FindIndex(const std::string &name)`

**Returns:** `int`

Returns the index of the data item with the given name. This function will return -1 if there is no such data item with the specified name exists

##### `for(auto &item : items)`

**Returns:** ``

##### `GetCount(—)`

**Returns:** `int`

Returns the number data items in this data resource

##### `Remove(int index)`

**Returns:** `void`

Removes the item at the given index. The data item will be destroyed.

##### `Remove(const std::string &name)`

**Returns:** `void`

Removes the item with the given name. The data item will be destroyed.

##### `if(ind==-1)`

**Returns:** ``

##### `Remove(ind)`

**Returns:** ``

##### `if(ind==-1)`

**Returns:** ``

Releases the data item with the given index. The data item will not be destroyed Releases the data item with the given name. The data item will not be destroyed

##### `Release(ind)`

**Returns:** `return`

##### `Add(DataItem &item)`

**Returns:** `void`

Adds the given data item to this data resource. Ownership of the item is transferred to this Data

##### `Insert(DataItem &item, int before)`

**Returns:** `void`

Inserts the given data item to this data resource before the specified index. Ownership of the item is transferred to this Data

##### `virtual` `save(Writer &writer)`

**Returns:** `virtual void`

Loads a data resource Destructor


### `Data`

**Namespace:** `Scripting`

#### Methods

##### `static` `Invalid(—)`

**Returns:** `static Data`

Constructs an invalid data object. Data object does not perform validity check therefore, use of this function should be very limited.

##### `Data(—)`

**Returns:** ``

Constructs an invalid data. Performing any operation on this data might cause crashes. Never use this constructor unless its absolutely necessary

##### `Data(const Data &other)`

**Returns:** ``

Copy constructor

##### `Data(Data &&other)`

**Returns:** ``

Move constructor

##### `Data(const Type *type, const Any &data, bool isreference=false, bool isconstant=false)`

**Returns:** ``

Any constructor. Allows both data and type to be specified

##### `Data(const Type &type)`

**Returns:** ``

Any constructor. Allows both data and type to be specified Default value constructor. Value of the data is determined from the type

##### `IsNull(—)`

**Returns:** `bool`

Assignment operator

##### `GetValue(—)`

**Returns:** ``

Returns the value of this data in the requested format

##### `if(isconstant)`

**Returns:** ``

##### `GetValue(—)`

**Returns:** ``

Returns the value of this data in the requested format

##### `if(isconstant)`

**Returns:** ``

##### `CastException("Value", "Reference")`

**Returns:** `throw`

##### `CastException("Value", "Reference")`

**Returns:** `throw`

##### `GetValue(—)`

**Returns:** ``

Returns the value of this data in the requested format

##### `if(isconstant)`

**Returns:** ``

##### `CastException("Const reference", "Reference")`

**Returns:** `throw`

##### `CastException("Value", "Reference")`

**Returns:** `throw`

##### `CastException("Value", "Reference")`

**Returns:** `throw`

##### `ReferenceValue(—)`

**Returns:** ``

Returns the value of this data in the requested format. Requested type should ideally be a reference. Though this is not a requirement.

##### `ASSERT(type, "Type is not set", 1, 2)`

**Returns:** ``

##### `ReferenceValue(—)`

**Returns:** ``

Returns the value of this data in the requested format. Requested type should ideally be a reference. Though this is not a requirement.

##### `ASSERT(type, "Type is not set", 1, 2)`

**Returns:** ``

##### `GetData(—)`

**Returns:** `Any`

Returns the data contained in this data element

##### `GetReference(—)`

**Returns:** `Data`

##### `DeReference(—)`

**Returns:** `Data`

##### `SetParent(const Data data)`

**Returns:** `void`

##### `RemoveParent(—)`

**Returns:** `void`

##### `IsValid(—)`

**Returns:** `bool`

Returns if the data is in a valid state

##### `IsReference(—)`

**Returns:** `bool`

Returns if this data contains a reference

##### `IsConstant(—)`

**Returns:** `bool`

Returns if this data is constant

##### `MakeConstant(—)`

**Returns:** `void`

Makes this data a constant

##### `Delete(—)`

**Returns:** `void`

Attempts to delete the data contained in this data

##### `ASSERT(type, "Type is not set", 1, 2)`

**Returns:** ``

Returns the type of the data

##### `ToString(—)`

**Returns:** `std::string`

##### `check(—)`

**Returns:** `void`

Stored data Type of the data Is a reference, data is a ptr to the original type This data is a constant and should not be changed


---

## Functions

### `for(auto &item : items)`

**Returns:** ``



### `while(!target)`

**Returns:** ``



### `if(data)`

**Returns:** ``



### `check()`

**Returns:** ``



### `if(isconstant)`

**Returns:** ``



### `ASSERT(type, "Type is not set", 1, 5)`

**Returns:** ``



### `ASSERT(type, "Type is not set", 1, 5)`

**Returns:** ``



### `CastException("Value type", "Reference", "Value typed objects cannot be deleted explicitly.")`

**Returns:** `throw`



### `ASSERT(type, "Type is not set", 1, 5)`

**Returns:** ``



### `if(isconstant)`

**Returns:** ``



### `if(isconstant)`

**Returns:** ``



### `ASSERT(type, "Type is not set", 1, 5)`

**Returns:** ``



### `if(isconstant)`

**Returns:** ``



### `ASSERT(type, "Type is not set", 1, 5)`

**Returns:** ``



### `if(!isconstant)`

**Returns:** ``



### `ASSERT(type, "Type is not set", 1, 5)`

**Returns:** ``


