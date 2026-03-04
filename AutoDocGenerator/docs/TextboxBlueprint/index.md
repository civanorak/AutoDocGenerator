# TextboxBlueprint

> Auto-generated documentation for the **TextboxBlueprint** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Blueprint`

**Namespace:** `textbox`


### `Element`

**Namespace:** `textbox`

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



### `if(gid==GID::Textbox_Element_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->Duration)`

**Returns:** ``



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Textbox_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->DefaultSize)`

**Returns:** ``



### `ReadFrom(Data, bp->AlphaAnimation)`

**Returns:** ``



### `if(gid==GID::Textbox_Element)`

**Returns:** `else`



### `if(cp)`

**Returns:** ``



### `updatemapping()`

**Returns:** ``



### `HasStyleAnimation(StyleMode style)`

**Returns:** `AnimationInfo`



### `AnimationInfo(Forward, Mapping[style.from][style.to]->Duration)`

**Returns:** `return`



### `AnimationInfo(Forward, Mapping[style.to][style.from]->Duration)`

**Returns:** `return`



### `GetGID()`

**Returns:** `virtual GID::Type`



### `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from!=widgets::Blueprint::Normal && style.to!=widgets::Blueprint::Normal)`

**Returns:** ``



### `updatemapping()`

**Returns:** `void`


