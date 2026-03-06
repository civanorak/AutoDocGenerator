# Scope

&gt; Auto-generated documentation for the **Scope** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Line`

**Namespace:** `Gorgon`

@cond INTERNAL This class represents a logical line


### `SourceMarker`

**Namespace:** `Gorgon`

@endcond This class uniquely represents a source code line. uintptr_t is used for source to reduce dependency

#### Methods

##### `SourceMarker(—)`

**Returns:** ``

##### `return(source == other.source ? line<other.line : source<other.source)`

**Returns:** ``

##### `IsValid(—)`

**Returns:** `bool`

##### `GetSource(—)`

**Returns:** `uintptr_t`

##### `GetLine(—)`

**Returns:** `unsigned long`


### `Scope`

**Namespace:** `Gorgon`

#### Methods

##### `Scope(InputProvider &provider, const std::string &name, bool terminal=false)`

**Returns:** ``

Constructor requires an input provider and a name to define this input source

##### `Scope(Scope &parent, const std::string &name, bool terminal=false)`

**Returns:** ``

This constructor allows a scope without an input provider. This allows function like constructs to have their own scopes with designated source code supplied from external sources

##### `GetPhysicalLine(unsigned long line)`

**Returns:** `long`

Reads the instruction in the given line Current physical line

##### `IsInteractive(—)`

**Returns:** `bool`

Returns if this scope is interactive (i.e. code is entered by user)

##### `ReadyInstructionCount(—)`

**Returns:** `unsigned`

Current number of instructions that are prepared

##### `GetName(—)`

**Returns:** `std::string`

Returns the name of this scope

##### `SaveInstruction(Instruction inst, long pline)`

**Returns:** `void`

Saves an instruction to the scope

##### `SaveInstructions(const std::vector<Instruction> &insts)`

**Returns:** `void`

Saves a list of instructions to this scope

##### `for(auto &inst : insts)`

**Returns:** ``

##### `IsTerminal(—)`

**Returns:** `bool`

Returns if this scope is terminal scope. If a scope is terminal, variable lookup to the parent scopes terminates at this scope

##### `Instantiate(—)`

**Returns:** `std::shared_ptr<ScopeInstance>`

##### `Instantiate(ScopeInstance &current)`

**Returns:** `std::shared_ptr<ScopeInstance>`

##### `HasInstance(—)`

**Returns:** `bool`

##### `HasParent(—)`

**Returns:** `bool`

##### `SetVariable(const std::string &name, const Data &data)`

**Returns:** `void`

##### `UnsetVariable(const std::string &name)`

**Returns:** `bool`

##### `Unload(—)`

**Returns:** `void`

Unloads an input source by erasing all current data. Unload should only be called when no more callbacks can be performed and no more lines are left.

##### `swap(temp, lines)`

**Returns:** ``

##### `SetName(const std::string &name)`

**Returns:** `void`

In rare cases where scope name cannot be determined at the construction, this function can be used to set its name


### `Return`

**Namespace:** `Gorgon`

Every logical line at least up until current execution point. They are kept so that it is possible to jump back. Logical lines do not contain comments. Represents what could be returned from a scope instance


### `ScopeInstance`

**Namespace:** `Gorgon`

Return type, nullptr means anything Marked scope can return a constant. If the type is a value type and return is not marked as a reference, constant has no real implication Marks this return as a reference This is an instantiation of a scope

#### Methods

##### `Jumpto(unsigned long line)`

**Returns:** `void`

Jumps to the given line, line numbers start at zero.

##### `GetLineNumber(—)`

**Returns:** `unsigned long`

Returns the current executing logical line number

##### `GetMarkerForNext(—)`

**Returns:** `SourceMarker`

Returns a unique identifier for the next line in source code. This information can be used to go back across execution scopes. Useful for Try Catch like structures.

##### `GetMarkerForCurrent(—)`

**Returns:** `SourceMarker`

Returns a unique identifier for the next line in source code. This information can be used to go back across execution scopes. Useful for Try Catch like structures.

##### `GetName(—)`

**Returns:** `std::string`

Returns the code at the current line and increments the current line

##### `SetVariable(const std::string &name, const Data &data)`

**Returns:** `void`

##### `UnsetVariable(const std::string &name)`

**Returns:** `bool`

##### `Compile(—)`

**Returns:** `void`

Forces the compilation of entire scope

##### `MoveToEnd(—)`

**Returns:** `void`

Returns the code at the current line without incrementing it. Returns the code at the given line without changing current line.

##### `GetPhysicalLine(—)`

**Returns:** `long`

##### `SetReturn(Return returns)`

**Returns:** `void`

Returns the scope of this scope instance Sets the return type of this scope instance

##### `AddSymbol(const StaticMember &symbol)`

**Returns:** `void`

Adds a symbol to the symbol table of this scope

##### `FindSymbol(const std::string &name, bool reference)`

**Returns:** `Data`

Tries to find the given symbol (including variables)

##### `AmbiguousSymbolException(name, SymbolType::Identifier, "Could be one of: "+ambiguoussymbols[name])`

**Returns:** `throw`


---

## Functions

### `catch(Exception &err)`

**Returns:** ``


