# FrameBuffer

&gt; Auto-generated documentation for the **FrameBuffer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `FrameBuffer`

**Namespace:** `Gorgon`

#### Methods

##### `Resize(const Geometry::Size &size)`

**Returns:** `friend void`

##### `FrameBuffer(—)`

**Returns:** ``

Does not perform any action, allows late generation of buffers.

##### `Generate(depth)`

**Returns:** ``

Generates a frame buffer. If software frame buffer does not work, this will create only a texture. Use UpdateTexture to update the texture. See Generate.

##### `Generate(bool depth)`

**Returns:** `void`

Generates a frame buffer. If software frame buffer does not work, this will create only a texture. Use UpdateTexture to update the texture. This function will cause the system to switch to render to screen.

##### `Destroy(—)`

**Returns:** `void`

Destroys the frame buffer

##### `Destroy(—)`

**Returns:** ``

##### `IsReady(—)`

**Returns:** `bool`

Returns if the frame buffer ready

##### `IsFunctional(—)`

**Returns:** `bool`

Returns if the frame buffer is fully functional.

##### `GetTexture(—)`

**Returns:** `Texture`

Returns the texture of this buffer

##### `Use(—)`

**Returns:** `void`

Begin using this frame buffer.

##### `RenderToScreen(—)`

**Returns:** `void`

Stop using this buffer and render to screen instead

##### `static` `UpdateSizes(—)`

**Returns:** `static void`

Updates the size of all framebuffers


---

## Functions

### `glGenFramebuffers(1, &buffer)`

**Returns:** ``



### `glBindFramebuffer(GL_FRAMEBUFFER, buffer)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, 0)`

**Returns:** ``



### `glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texture, 0)`

**Returns:** ``



### `if(gendepth && glBindRenderbuffer)`

**Returns:** ``



### `glGenRenderbuffers(1, &depth)`

**Returns:** ``



### `glBindRenderbuffer(GL_RENDERBUFFER, depth)`

**Returns:** ``



### `glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, sz.Width, sz.Height)`

**Returns:** ``



### `glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, depth)`

**Returns:** ``



### `glDrawBuffers(1, DrawBuffers)`

**Returns:** ``



### `glBindFramebuffer(GL_FRAMEBUFFER, 0)`

**Returns:** ``



### `for(FrameBuffer &buffer : buffers)`

**Returns:** ``



### `if(buffer.depth)`

**Returns:** ``



### `glBindRenderbuffer(GL_RENDERBUFFER, buffer.depth)`

**Returns:** ``



### `glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, sz.Width, sz.Height)`

**Returns:** ``



### `glDeleteFramebuffers(1, &buffer)`

**Returns:** ``



### `DestroyTexture(texture)`

**Returns:** ``



### `if(depth)`

**Returns:** ``



### `glDeleteRenderbuffers(1, &depth)`

**Returns:** ``



### `glBindFramebuffer(GL_FRAMEBUFFER, buffer)`

**Returns:** ``


