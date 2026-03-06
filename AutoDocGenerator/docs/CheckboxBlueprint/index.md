# CheckboxBlueprint

&gt; Auto-generated documentation for the **CheckboxBlueprint** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Blueprint`

**Namespace:** `checkbox`


### `StateMode`

**Namespace:** `checkbox`

#### Methods

##### `int(—)`

**Returns:** `operator`

##### `swap(—)`

**Returns:** `StateMode`

##### `StateMode(to, from)`

**Returns:** `return`


### `GroupMode`

**Namespace:** `checkbox`

#### Methods

##### `GroupMode(const Group &g)`

**Returns:** ``


### `LineContents`

**Namespace:** `checkbox`

#### Methods

##### `LineContents(int v)`

**Returns:** ``


### `Line`

**Namespace:** `checkbox`

#### Methods

##### `GetGID(—)`

**Returns:** `GID::Type`

##### `GetContent(int id)`

**Returns:** `LineContentType`

##### `if(id==0)`

**Returns:** ``

##### `if(id==1)`

**Returns:** `else`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`


### `Element`

**Namespace:** `checkbox`

#### Methods

##### `GetGID(—)`

**Returns:** `GID::Type`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`


### `Group`

**Namespace:** `checkbox`

#### Methods

##### `GetGID(—)`

**Returns:** `GID::Type`

##### `virtual` `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`

##### `updatemapping(—)`

**Returns:** `void`


---

## Enums

### `StateNumbers`

**Namespace:** `checkbox`


### `SizingMode`

**Namespace:** `checkbox`


### `LineContentType`

**Namespace:** `checkbox`


### `TransitionType`

**Namespace:** `checkbox`


### `HeightType`

**Namespace:** `checkbox`


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



### `if(gid==GID::Checkbox_Line_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->Height)`

**Returns:** ``



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Checkbox_Element_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->Duration)`

**Returns:** ``



### `if(gid==GID::Checkbox_Line)`

**Returns:** `else`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Checkbox_Group_Props)`

**Returns:** `else`



### `if(gid==GID::Checkbox_Element)`

**Returns:** `else`



### `ReadFrom(Data, gid)`

**Returns:** ``



### `ReadFrom(Data, size)`

**Returns:** ``



### `if(gid==resource::GID::Guid)`

**Returns:** ``



### `if(gid==resource::GID::SGuid)`

**Returns:** `else`



### `if(gid==GID::Checkbox_Props)`

**Returns:** `else`



### `ReadFrom(Data, bp->DefaultSize)`

**Returns:** ``



### `ReadFrom(Data, bp->AlphaAnimation)`

**Returns:** ``



### `if(gid==GID::Checkbox_Group)`

**Returns:** `else`



### `if(f.to!=Blueprint::Focus_None)`

**Returns:** ``



### `if(s.to!=0)`

**Returns:** ``



### `if(focus.to==Blueprint::Focus_None && state.to==0)`

**Returns:** ``



### `if(focus.from!=Blueprint::NotFocused)`

**Returns:** ``



### `if(state.from!=1)`

**Returns:** ``



### `if(focus.to==Blueprint::Focus_None)`

**Returns:** `else`



### `if(focus.from!=Blueprint::NotFocused)`

**Returns:** ``



### `if(state.to==0)`

**Returns:** `else`



### `if(state.from!=1)`

**Returns:** ``



### `for(auto it=Subitems.First()`

**Returns:** ``



### `updatemapping()`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `Prepare(GGEMain &main, resource::File &file)`

**Returns:** `virtual void`



### `hasstyleanimation(FocusMode f, StateMode s, StyleMode style)`

**Returns:** `AnimationInfo`



### `HasStyleAnimation(FocusMode focus, StateMode state, StyleMode style)`

**Returns:** `AnimationInfo`



### `HasStateAnimation(StateMode state)`

**Returns:** `AnimationInfo`



### `HasFocusAnimation(FocusMode focus)`

**Returns:** `AnimationInfo`



### `GetAlternatives(Group** &groups, FocusMode focus, StateMode state)`

**Returns:** `void`



### `for(int i=0;i<5 && groups[i];i++)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None || style.from!=Blueprint::Normal)`

**Returns:** ``



### `for(int i=0;i<5 && groups[i];i++)`

**Returns:** ``



### `GetGID()`

**Returns:** `virtual GID::Type`


