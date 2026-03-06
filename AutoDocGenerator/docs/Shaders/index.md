# Shaders

&gt; Auto-generated documentation for the **Shaders** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `FillShader`

**Namespace:** `Gorgon`

#### Methods

##### `tomask(ShaderMode::ToMask)`

**Returns:** ``

##### `switch(mode)`

**Returns:** ``

##### `UpdateUniform(id, value)`

**Returns:** ``

##### `UpdateUniform(id, value)`

**Returns:** ``

##### `FillShader(ShaderMode mode)`

**Returns:** ``


### `MaskedFillShader`

**Namespace:** `Gorgon`

#### Methods

##### `UpdateUniform(id, value)`

**Returns:** ``

##### `UpdateUniform(id, value)`

**Returns:** ``

##### `glActiveTexture(GL_TEXTURE1)`

**Returns:** ``

##### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``

##### `MaskedFillShader(—)`

**Returns:** ``


---

## Enums

### `ShaderMode`

**Namespace:** `Gorgon`


---

## Functions

### `ModeName(ShaderMode mode)`

**Returns:** `static std::string`



### `switch(mode)`

**Returns:** ``



### `switch(mode)`

**Returns:** ``



### `InitializeWithSource(Simple_V, Simple_F)`

**Returns:** ``



### `InitializeWithSource(Simple_V, ToMask_F)`

**Returns:** ``



### `InitializeWithSource(Masked_V, Masked_F)`

**Returns:** ``



### `switch(mode)`

**Returns:** ``



### `InitializeWithSource(Simple_V, Alpha_F)`

**Returns:** ``



### `InitializeWithSource(Simple_V, ToMask_F)`

**Returns:** ``



### `InitializeWithSource(Masked_V, MaskedAlpha_F)`

**Returns:** ``



### `switch(mode)`

**Returns:** ``



### `InitializeWithSource(NoTex_V, Fill_F)`

**Returns:** ``



### `InitializeWithSource(NoTex_V, ToMaskFill_F)`

**Returns:** ``



### `InitializeWithSource(MaskedNoTex_V, MaskedFill_F)`

**Returns:** ``



### `switch(mode)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``


Sets texture coordinates


### `glActiveTexture(GL_TEXTURE0)`

**Returns:** ``


Sets diffuse texture


### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `SimpleShader(ShaderMode mode)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``


Sets texture coordinates


### `glActiveTexture(GL_TEXTURE0)`

**Returns:** ``


Sets diffuse texture


### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `glActiveTexture(GL_TEXTURE1)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``



### `MaskedShader()`

**Returns:** ``



### `tomask(ShaderMode::ToMask)`

**Returns:** ``



### `switch(mode)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``


Sets texture coordinates


### `glActiveTexture(GL_TEXTURE0)`

**Returns:** ``


Sets alpha texture


### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `AlphaShader(ShaderMode mode)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``


Sets texture coordinates


### `glActiveTexture(GL_TEXTURE0)`

**Returns:** ``


Sets alpha texture


### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``



### `UpdateUniform(id, value)`

**Returns:** ``



### `glActiveTexture(GL_TEXTURE1)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, value)`

**Returns:** ``



### `MaskedAlphaShader()`

**Returns:** ``


