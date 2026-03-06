# Compilers

&gt; Auto-generated documentation for the **Compilers** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Base`

**Namespace:** `Compilers`

The base class for compilers

#### Methods

##### `virtual` `Compile(const std::string &input, unsigned long pline)`

**Returns:** `virtual unsigned`

Asks the compiler to compile the given input. Returns the number of instructions generated from the code. Compiler is free to request additional input by returning zero. This does not necessarily mean there is no compilable source in the given input it may simply be an incomplete line. When there is no more input, caller should finish compilation by calling Finalize

##### `virtual` `Finalize(—)`

**Returns:** `virtual void`

Finalizes the compilation. Compiler may throw an error about missing constructs at this point.

##### `HasScope(—)`

**Returns:** `bool`

Returns if this compiler is bound to a scope


### `Intermediate`

**Namespace:** `Compilers`

Returns the scope that compiler will compile The instructions that are compiled The current scope the compiler is compiling, can be nullptr Intermediate language complier

#### Methods

##### `Intermediate(scope)`

**Returns:** `return *new`

##### `storedfn(const std::string &input, int &ch)`

**Returns:** `void`

##### `fncall(const std::string &input, int &ch, bool allowmethod=true)`

**Returns:** `void`

##### `varassign(const std::string &input, int &ch)`

**Returns:** `void`

##### `memberassign(const std::string &input, int &ch)`

**Returns:** `void`

##### `parsevalue(const std::string &input, int &ch)`

**Returns:** `Value`

##### `parsetemporary(const std::string &input, int &ch)`

**Returns:** `unsigned long`

##### `eatwhite(const std::string &input, int &ch)`

**Returns:** `void`

##### `jinst(std::string input, int &ch)`

**Returns:** `void`


### `Programming`

**Namespace:** `Compilers`

Programming dialect compiler

#### Methods

##### `Programming(scope)`

**Returns:** `return *new`

##### `extractline(std::string &input, std::string &prepared)`

**Returns:** `void`

##### `transformpos(int ch, int &oline, int &och)`

**Returns:** `void`


### `charmarker`

**Namespace:** `Compilers`


---

## Functions

### `Disassemble(const Instruction *)`

**Returns:** `std::string`


Disassembles the given instruction


### `Disassemble(const Instruction &inst)`

**Returns:** `inline std::string`


Disassembles the given instruction


### `Disassemble(InputSource &source, std::ostream &out)`

**Returns:** `void`


Disassembles entire input source to the given stream

