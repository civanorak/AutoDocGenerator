# OpenGL

&gt; Auto-generated documentation for the **OpenGL** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `switch(id)`

**Returns:** ``



### `getGLColorMode(Graphics::ColorMode mode)`

**Returns:** `GLenum`



### `switch(mode)`

**Returns:** ``



### `settexturedata(Texture tex, const Containers::Image &data)`

**Returns:** `void`



### `glPixelStorei(GL_UNPACK_ALIGNMENT, 1)`

**Returns:** ``



### `glPixelStorei(GL_PACK_ALIGNMENT, 1)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, tex)`

**Returns:** ``



### `glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)`

**Returns:** ``



### `glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)`

**Returns:** ``



### `glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)`

**Returns:** ``



### `glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)`

**Returns:** ``



### `GenerateTexture(const Containers::Image &data)`

**Returns:** `Texture`



### `glGenTextures(1, &tex)`

**Returns:** ``



### `settexturedata(tex, data)`

**Returns:** ``



### `GenerateEmptyTexture(const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `Texture`



### `glGenTextures(1, &tex)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, tex)`

**Returns:** ``



### `glTexImage2D(GL_TEXTURE_2D, 0, colormode, size.Width, size.Height, 0, colormode, GL_UNSIGNED_BYTE, NULL)`

**Returns:** ``



### `glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)`

**Returns:** ``



### `glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)`

**Returns:** ``



### `ResizeTexture(Texture tex, const Geometry::Size &size, Graphics::ColorMode mode)`

**Returns:** `void`



### `glBindTexture(GL_TEXTURE_2D, tex)`

**Returns:** ``



### `glTexImage2D(GL_TEXTURE_2D, 0, colormode, size.Width, size.Height, 0, colormode, GL_UNSIGNED_BYTE, NULL)`

**Returns:** ``



### `UpdateTexture(Texture tex, const Containers::Image &data)`

**Returns:** `void`



### `settexturedata(tex, data)`

**Returns:** ``



### `CopyToTexture(Texture tex, const Containers::Image &data, Geometry::Point target)`

**Returns:** `void`



### `glPixelStorei(GL_UNPACK_ALIGNMENT, 1)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, tex)`

**Returns:** ``



### `CopyToTexture(Texture tex, const Containers::Image &data, Geometry::Bounds source, Geometry::Point target)`

**Returns:** `void`



### `glPixelStorei(GL_UNPACK_ALIGNMENT, 1)`

**Returns:** ``



### `glPixelStorei(GL_UNPACK_SKIP_PIXELS, source.Left)`

**Returns:** ``



### `glPixelStorei(GL_UNPACK_SKIP_ROWS, source.Top)`

**Returns:** ``



### `glBindTexture(GL_TEXTURE_2D, tex)`

**Returns:** ``



### `glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0)`

**Returns:** ``



### `glPixelStorei(GL_UNPACK_SKIP_ROWS, 0)`

**Returns:** ``



### `glPixelStorei(GL_UNPACK_ROW_LENGTH, 0)`

**Returns:** ``



### `DestroyTexture(Texture tex)`

**Returns:** `void`



### `glDeleteTextures(1, &tex)`

**Returns:** ``



### `RenderToTexture(FrameBuffer &buffer)`

**Returns:** `void`



### `RenderToScreen()`

**Returns:** `void`



### `glBindFramebuffer(GL_FRAMEBUFFER, 0)`

**Returns:** ``



### `SetupContext(const Geometry::Size &size)`

**Returns:** `void`



### `exit(2)`

**Returns:** ``



### `glShadeModel(GL_SMOOTH)`

**Returns:** ``



### `glColor4f(1.0f, 1.0f, 1.0f, 1.0f)`

**Returns:** ``



### `glEnable(GL_DEPTH_TEST)`

**Returns:** ``



### `glDepthFunc(GL_LEQUAL)`

**Returns:** ``



### `glEnable(GL_BLEND)`

**Returns:** ``



### `SetDefaultClear()`

**Returns:** ``



### `SetDefaultBlending()`

**Returns:** ``



### `glEnable(GL_TEXTURE_2D)`

**Returns:** ``



### `glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)`

**Returns:** ``



### `glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)`

**Returns:** ``



### `glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)`

**Returns:** ``



### `glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)`

**Returns:** ``



### `glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)`

**Returns:** ``



### `glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)`

**Returns:** ``



### `glFrontFace(GL_CCW)`

**Returns:** ``



### `glEnable(GL_DEBUG_OUTPUT)`

**Returns:** ``



### `glDebugMessageCallback(&debug_proc, nullptr)`

**Returns:** ``



### `Resize(size)`

**Returns:** ``



### `Clear()`

**Returns:** ``



### `glFlush()`

**Returns:** ``



### `glFinish()`

**Returns:** ``



### `SetDefaultBlending()`

**Returns:** `void`



### `glBlendFuncSeparate(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_ONE_MINUS_DST_ALPHA, GL_ONE)`

**Returns:** ``



### `SetDefaultClear()`

**Returns:** `void`



### `glClearColor(0.4f, 0.2f, 0.0f, 0.0f)`

**Returns:** ``



### `glClearDepth(1.0f)`

**Returns:** ``



### `Resize(const Geometry::Size &size)`

**Returns:** `void`



### `glViewport(0, 0, size.Width, size.Height)`

**Returns:** ``



### `Clear()`

**Returns:** `void`



### `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)`

**Returns:** ``



### `LoadFunctions()`

**Returns:** `void`



### `if(!glBindFramebuffer)`

**Returns:** ``



### `if(!glBindRenderbuffer)`

**Returns:** ``



### `if(!glBindFramebuffer)`

**Returns:** ``



### `if(!glBindRenderbuffer)`

**Returns:** ``



### `LoadFunctions()`

**Returns:** `void`



### `LoadGLFunctions()`

**Returns:** `void`


