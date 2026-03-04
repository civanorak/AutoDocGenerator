# BorderData

> Auto-generated documentation for the **BorderData** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `BorderData`

**Namespace:** `gge`

#### Methods

##### `if(autowidth)`

**Returns:** ``

##### `SetObject(resource::ResizableObject &object)`

**Returns:** `void`

##### `ContentBounds(utils::Bounds outer)`

**Returns:** `utils::Bounds`

##### `DrawingBound(utils::Bounds outer)`

**Returns:** `utils::Bounds`

##### `DrawAround(graphics::ImageTarget2D& Target, utils::Bounds bounds)`

**Returns:** `void`

##### `virtual` `DeleteAnimation(—)`

**Returns:** `virtual void`

##### `virtual` `SetController(animation::Timer &controller, bool owner=false)`

**Returns:** `virtual void`


### `BorderDataResource`

**Namespace:** `gge`

#### Methods

##### `GetGID(—)`

**Returns:** `GID::Type`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`


---

## Functions

### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::BorderData_Props)`

**Returns:** `else`



### `ReadFrom(Data, bdr->Margins)`

**Returns:** ``



### `ReadFrom(Data, bdr->Padding)`

**Returns:** ``



### `ReadFrom(Data, bdr->BorderWidth)`

**Returns:** ``


