# ResizableObjectResource

&gt; Auto-generated documentation for the **ResizableObjectResource** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ResizableObject`

**Namespace:** `gge`

#### Methods

##### `SetObject(resource::ResizableObject &object)`

**Returns:** `void`

##### `virtual` `SetController(animation::Timer &controller, bool owner=false)`

**Returns:** `virtual void`

##### `virtual` `DeleteAnimation(—)`

**Returns:** `virtual void`


### `ResizableObjectResource`

**Namespace:** `gge`

#### Methods

##### `virtual` `GetGID(—)`

**Returns:** `virtual GID::Type`

##### `ControllerWithFillMode(ControllerFillModes h, ControllerFillModes v)`

**Returns:** `graphics::SizeController2D`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`


---

## Enums

### `ControllerFillModes`

**Namespace:** `gge`


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



### `if(gid==GID::ResizableObj_Props)`

**Returns:** `else`


