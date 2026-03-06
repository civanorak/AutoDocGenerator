# PanelBlueprint

&gt; Auto-generated documentation for the **PanelBlueprint** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Blueprint`

**Namespace:** `panel`


### `Element`

**Namespace:** `panel`

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



### `if(gid==GID::Panel_Element_Props)`

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



### `if(gid==GID::Panel_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->DefaultSize)`

**Returns:** ``



### `ReadFrom(Data, bp->AlphaAnimation)`

**Returns:** ``



### `if(gid==GID::Panel_Element)`

**Returns:** `else`



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



### `updatemapping()`

**Returns:** `void`



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from!=widgets::Blueprint::Normal && style.to!=widgets::Blueprint::Normal)`

**Returns:** ``



### `GetOpacity(StyleMode style)`

**Returns:** `Byte`



### `if(Mapping[style.from][style.to])`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(Mapping[style.to][style.from])`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(Mapping[style.from][Blueprint::Style_None])`

**Returns:** ``



### `if(style.from!=widgets::Blueprint::Normal && style.to!=widgets::Blueprint::Normal)`

**Returns:** ``



### `if(Mapping[widgets::Blueprint::Normal][Blueprint::Style_None])`

**Returns:** ``



### `GetBGOpacity(StyleMode style)`

**Returns:** `Byte`



### `if(Mapping[style.from][style.to])`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(Mapping[style.to][style.from])`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(Mapping[style.from][Blueprint::Style_None])`

**Returns:** ``



### `if(style.from!=widgets::Blueprint::Normal && style.to!=widgets::Blueprint::Normal)`

**Returns:** ``



### `if(Mapping[widgets::Blueprint::Normal][Blueprint::Style_None])`

**Returns:** ``


