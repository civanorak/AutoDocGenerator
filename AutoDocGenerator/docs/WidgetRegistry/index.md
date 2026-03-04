# WidgetRegistry

> Auto-generated documentation for the **WidgetRegistry** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `WidgetRegistry`

**Namespace:** `gge`

#### Methods

##### `SetWRR(WidgetRegistryResource &wrr)`

**Returns:** `void`


### `CFonts`

**Namespace:** `gge`


### `CColors`

**Namespace:** `gge`


### `CButtons`

**Namespace:** `gge`


### `CBorders`

**Namespace:** `gge`


### `CTextboxes`

**Namespace:** `gge`


### `CCheckboxes`

**Namespace:** `gge`


### `CLabels`

**Namespace:** `gge`


### `CListboxes`

**Namespace:** `gge`


### `CSliders`

**Namespace:** `gge`


### `CScrollbars`

**Namespace:** `gge`


### `CProgressbars`

**Namespace:** `gge`


### `CPanels`

**Namespace:** `gge`


### `COthers`

**Namespace:** `gge`


### `Collection`

**Namespace:** `gge`

#### Methods

##### `begin(—)`

**Returns:** `typename std::map<std::string, T_&>::iterator`

##### `end(—)`

**Returns:** `typename std::map<std::string, T_&>::iterator`

##### `GetCount(—)`

**Returns:** `int`

##### `Exists(const std::string &key)`

**Returns:** `bool`


### `ImageCollection`

**Namespace:** `gge`


### `SoundCollection`

**Namespace:** `gge`


### `WidgetRegistryResource`

**Namespace:** `gge`

#### Methods

##### `virtual` `GetGID(—)`

**Returns:** `virtual GID::Type`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`

##### `virtual` `Resolve(resource::File &file)`

**Returns:** `virtual void`


---

## Functions

### `LoadWR(resource::File& File, std::istream &Data, int Size)`

**Returns:** `WidgetRegistryResource *`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==resource::GID::Folder)`

**Returns:** `else`



### `catch(...)`

**Returns:** ``



### `if(it->name=="")`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(it->name=="")`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(it->name=="")`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `LoadedEvent()`

**Returns:** ``


