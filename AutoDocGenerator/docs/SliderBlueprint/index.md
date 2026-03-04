# SliderBlueprint

> Auto-generated documentation for the **SliderBlueprint** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Blueprint`

**Namespace:** `slider`


### `GroupMode`

**Namespace:** `slider`

#### Methods

##### `GroupMode(const Group &g)`

**Returns:** ``


### `Element`

**Namespace:** `slider`

#### Methods

##### `GetGID(—)`

**Returns:** `GID::Type`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`


### `Group`

**Namespace:** `slider`

#### Methods

##### `GetGID(—)`

**Returns:** `GID::Type`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`

##### `updatemapping(—)`

**Returns:** `void`


---

## Enums

### `OrientationType`

**Namespace:** `slider`


### `TransitionType`

**Namespace:** `slider`


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



### `if(gid==GID::Slider_Element_Props)`

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



### `if(gid==GID::Slider_Group_Props)`

**Returns:** `else`



### `if(gid==GID::Slider_Element)`

**Returns:** `else`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Slider_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->DefaultSize)`

**Returns:** ``



### `ReadFrom(Data, bp->AlphaAnimation)`

**Returns:** ``



### `if(gid==GID::Slider_Group)`

**Returns:** `else`



### `for(auto it=bp->Subitems.First()`

**Returns:** ``



### `updatemapping()`

**Returns:** ``



### `if(focus.to!=Blueprint::Focus_None)`

**Returns:** ``



### `if(focus.to==Blueprint::Focus_None)`

**Returns:** ``



### `if(focus.from!=Focus_None)`

**Returns:** ``



### `hasstyleanimation(OrientationType o, FocusMode f, StyleMode style)`

**Returns:** `AnimationInfo`



### `HasStyleAnimation(OrientationType o, FocusMode focus, StyleMode style)`

**Returns:** `AnimationInfo`



### `HasFocusAnimation(OrientationType o, FocusMode focus)`

**Returns:** `AnimationInfo`



### `GetAlternatives(Group** &groups, OrientationType o, FocusMode focus)`

**Returns:** `void`



### `for(int i=0;i<3 && groups[i];i++)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `for(int i=0;i<3 && groups[i];i++)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None || style.from!=Blueprint::Normal)`

**Returns:** ``



### `GetGID()`

**Returns:** `virtual GID::Type`



### `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`


