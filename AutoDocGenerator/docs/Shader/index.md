# Shader

&gt; Auto-generated documentation for the **Shader** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `CreateShader(GLenum type, const std::string& code, const std::string& name)`

**Returns:** `GLuint`



### `glCompileShader(shader)`

**Returns:** ``



### `glGetShaderiv(shader, GL_COMPILE_STATUS, &status)`

**Returns:** ``



### `if(status == GL_FALSE)`

**Returns:** ``



### `glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &log_length)`

**Returns:** ``



### `glGetShaderInfoLog(shader, log_length, nullptr, shader_log_message)`

**Returns:** ``



### `InsertDefines(std::string& code, const std::string& shader_defines)`

**Returns:** `void`



### `if(pos==std::string::npos)`

**Returns:** ``



### `if(geometryshader)`

**Returns:** ``



### `glDetachShader(program, geometryshader)`

**Returns:** ``



### `glDeleteShader(geometryshader)`

**Returns:** ``



### `if(fragmentshader)`

**Returns:** ``



### `glDetachShader(program, fragmentshader)`

**Returns:** ``



### `glDeleteShader(fragmentshader)`

**Returns:** ``



### `if(vertexshader)`

**Returns:** ``



### `glDetachShader(program, vertexshader)`

**Returns:** ``



### `glDeleteShader(vertexshader)`

**Returns:** ``



### `if(program)`

**Returns:** ``



### `glDeleteProgram(program)`

**Returns:** ``



### `glUseProgram(program)`

**Returns:** ``



### `SetupUBO(int size, int binding_point)`

**Returns:** `unsigned int`



### `glGenBuffers(1, &ubo)`

**Returns:** ``



### `glBindBuffer(GL_UNIFORM_BUFFER, ubo)`

**Returns:** ``



### `glBufferData(GL_UNIFORM_BUFFER, size, nullptr, GL_DYNAMIC_DRAW)`

**Returns:** ``



### `glBindBufferBase(GL_UNIFORM_BUFFER, binding_point, ubo)`

**Returns:** ``



### `UpdateUBO(unsigned int ubo, int size, void const * const data)`

**Returns:** `void`



### `glBindBuffer(GL_UNIFORM_BUFFER, ubo)`

**Returns:** ``



### `glBufferSubData(GL_UNIFORM_BUFFER, 0, size, data)`

**Returns:** ``



### `glUniform1i(ret, location)`

**Returns:** ``



### `glUniform1f(name, value)`

**Returns:** ``



### `glUniform1i(name, value)`

**Returns:** ``



### `glUniformBlockBinding(program, index, binding_point)`

**Returns:** ``



### `if(fragmentfile!="")`

**Returns:** ``



### `if(geometryfile!="")`

**Returns:** ``



### `InitializeWithSource(vertexsrc, fragmentsrc, geometrysrc, defines)`

**Returns:** ``



### `for(auto &p : defines)`

**Returns:** ``



### `InsertDefines(vertexsrc, definesstring)`

**Returns:** ``



### `glAttachShader(program, vertexshader)`

**Returns:** ``



### `if(fragmentsrc!="")`

**Returns:** ``



### `InsertDefines(fragmentsrc, definesstring)`

**Returns:** ``



### `glAttachShader(program, fragmentshader)`

**Returns:** ``



### `if(geometrysrc!="")`

**Returns:** ``



### `InsertDefines(geometrysrc, definesstring)`

**Returns:** ``



### `glAttachShader(program, geometryshader)`

**Returns:** ``



### `glLinkProgram(program)`

**Returns:** ``



### `glGetProgramiv(program, GL_LINK_STATUS, &status)`

**Returns:** ``



### `if(status == GL_FALSE)`

**Returns:** ``



### `glGetProgramiv(program, GL_INFO_LOG_LENGTH, &log_length)`

**Returns:** ``



### `glGetProgramInfoLog(program, log_length, nullptr, program_log_message)`

**Returns:** ``



### `SetupUBO(int size, int binding_point)`

**Returns:** `unsigned int`



### `UpdateUBO(unsigned int ubo, int size, void const * const data)`

**Returns:** `void`



### `Use()`

**Returns:** `void`



### `IsInitialized()`

**Returns:** `bool`



### `LocateUniform(const std::string& name)`

**Returns:** `int`



### `BindTexture(const std::string &name, int location)`

**Returns:** `int`



### `UpdateUniform(int name, float value)`

**Returns:** `void`



### `UpdateUniform(int name, int value)`

**Returns:** `void`



### `UpdateUniform(int name, const Geometry::Point3D &value)`

**Returns:** `void`



### `UpdateUniform(int name, const QuadVertices &value)`

**Returns:** `void`



### `UpdateUniform(int name, const QuadTextureCoords &value)`

**Returns:** `void`



### `UpdateUniform(int name, const Graphics::RGBAf &value)`

**Returns:** `void`



### `BindUBO(const std::string& name, UBOBindingPoint::Type bindingPoint)`

**Returns:** `void`



### `InitializeWithSource(vertexsrc, fragmentsrc, "", defines)`

**Returns:** ``



### `InitializeFromFiles(vertexfile, fragmentfile, "", defines)`

**Returns:** ``


