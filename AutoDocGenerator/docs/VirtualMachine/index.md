# VirtualMachine

&gt; Auto-generated documentation for the **VirtualMachine** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Symbol`

**Namespace:** `Scripting`

Represents a symbol, can be a variable, type, function or constant.


### `VirtualMachine`

**Namespace:** `Scripting`

Namespace that this symbol is in. For variables, namespc could be local Type of the symbol The object This class defines a virtual environment for scripts to run.

#### Methods

##### `VirtualMachine(bool automaticreset=true, std::ostream &out=std::cout, std::istream &in=std::cin)`

**Returns:** `explicit`

Default constructor

##### `ExecuteStatement(const std::string &code, InputProvider::Dialect dialect = InputProvider::Programming)`

**Returns:** `bool`

Executes a single statement in this virtual machine. This operation will create a new input scope and run the code within that scope.

##### `ExecuteFunction(const Function *fn, const std::vector<Data> &params, bool method)`

**Returns:** `Data`

Executes a function in the current scope

##### `Run(—)`

**Returns:** `void`

This method starts the virtual machine

##### `Run(std::shared_ptr<ScopeInstance> scope)`

**Returns:** `void`

This method starts the virtual machine with the given scopeinstance

##### `Run(unsigned executiontarget)`

**Returns:** `void`

This method starts the virtual machine @param executiontarget depth of aimed execution. This value should be less than the current.

##### `Start(InputProvider &input)`

**Returns:** `void`

This method starts the virtual machine with the given input source

##### `Begin(InputProvider &input)`

**Returns:** `void`

This method begins a new execution scope without starting execution

##### `CompileCurrent(—)`

**Returns:** `void`

Commands virtual machine to compile current execution scope. Might cause issues with interactive input sources.

##### `AddLibrary(const Library &library)`

**Returns:** `void`

Includes a new library to be used in this virtual machine

##### `RemoveLibrary(const Library &library)`

**Returns:** `void`

Removes a library

##### `UsingNamespace(const Namespace &name)`

**Returns:** `void`

Imports symbols of a namespace to the list of global symbols

##### `UsingNamespace(const std::string &name)`

**Returns:** `void`

Imports symbols of a namespace to the list of global symbols

##### `Jump(unsigned long line)`

**Returns:** `void`

Changes the current executing line.

##### `Jump(SourceMarker marker)`

**Returns:** `void`

Changes the current executing line. This function checks if the marker is in this execution scope. If not, it throws.

##### `LongJump(SourceMarker marker)`

**Returns:** `void`

Changes current executing line. This function can jump to a previous execution point. Useful for keywords like try/catch

##### `FindSymbol(const std::string &original, bool reference=false, bool allownull=false)`

**Returns:** `Data`

Finds the given symbol and resolves its value

##### `static` `Exists(—)`

**Returns:** `static bool`

Returns the current VM for this thread. Returns the current VM for this thread.

##### `IsVariableSet(const std::string &name)`

**Returns:** `bool`

##### `GetVariable(const std::string &name)`

**Returns:** `Variable`

##### `SetVariable(const std::string &name, Data data, bool ref=false)`

**Returns:** `void`

##### `UnsetVariable(const std::string &name)`

**Returns:** `void`

##### `AttachCommandConsole(—)`

**Returns:** `void`

Creates a new InputSource using a console input provider. Also creates an activates a new execution scope using this input source.

##### `DetachCommandConsole(—)`

**Returns:** `bool`

If there is an attached command console, this function detaches that console, stops execution and returns true. Otherwise, it returns false.

##### `SetOutput(std::ostream &out, bool deleteonchange=false)`

**Returns:** `void`

Redirects the output stream to the given stream

##### `SetInput(std::istream &in)`

**Returns:** `void`

Redirects input stream to the given stream

##### `ResetOutput(—)`

**Returns:** `void`

Returns the output stream Returns the input stream. Resets the output stream to default stream that is given in the constructor

##### `ResetInput(—)`

**Returns:** `void`

Resets the input stream to default stream that is given in the constructor

##### `Activate(—)`

**Returns:** `void`

Activate this VM for this thread. This VM will automatically activate when Start is issued, therefore, this is mostly used for debugging

##### `GetScopeInstanceCount(—)`

**Returns:** `unsigned`

Returns the number of active execution scopes. If this number is 0, VM cannot be started without providing additional code source.

##### `GetMarkerForNext(—)`

**Returns:** `SourceMarker`

Returns the current exection scope Returns the code marker for the next line.

##### `GetReturnValue(—)`

**Returns:** `Data`

Returns the data returned from the last executed script

##### `Reset(—)`

**Returns:** `void`

Returns from the currently running script and sets return data to the given value. Sets the handler for special identifiers. These are application defined variables and values. Unless they are returned as references, they will be considered as readonly. Characters @, %, !, and $ are treated as special identifiers. They could be functions too. Resets any runtime information that this VM has. This includes all scopes and global variables

##### `execute(const Instruction* inst)`

**Returns:** `void`

Internal, returns pointer to the variable. Can return nullptr. Only searches in VM variables Allows read-only access to libraries This system allows objects of automatic lifetime.

##### `callfunction(const Function *fn, bool method, const std::vector<Value> &params)`

**Returns:** `Data`

##### `callvariant(const Function *fn, const Function::Overload *variant, bool method, const std::vector<Value> &params)`

**Returns:** `Data`

##### `getvalue(const Value &val, bool reference=false)`

**Returns:** `Data`

##### `functioncall(const Instruction *inst, bool memberonly, bool method)`

**Returns:** `void`

##### `activatescopeinstance(std::shared_ptr<ScopeInstance> instance)`

**Returns:** `void`

##### `addsymbol(const StaticMember &symbol)`

**Returns:** `void`


---

## Functions

### `Activate()`

**Returns:** ``



### `init_builtin()`

**Returns:** ``



### `AddLibrary(Integrals)`

**Returns:** ``



### `AddLibrary(Keywords)`

**Returns:** ``



### `AddLibrary(Reflection)`

**Returns:** ``



### `AddLibrary(Math)`

**Returns:** ``



### `for(const auto &lib : libraries)`

**Returns:** ``



### `Begin(input)`

**Returns:** ``



### `Run()`

**Returns:** ``



### `Activate()`

**Returns:** ``



### `activatescopeinstance(toplevel)`

**Returns:** ``



### `UsingNamespace(Integrals)`

**Returns:** ``



### `UsingNamespace(Keywords)`

**Returns:** ``



### `if(target<0)`

**Returns:** ``



### `Run(target)`

**Returns:** ``



### `activatescopeinstance(scope)`

**Returns:** ``



### `Run(target)`

**Returns:** ``



### `if(returnimmediately)`

**Returns:** ``



### `if(inst)`

**Returns:** ``



### `if(inst==nullptr)`

**Returns:** ``



### `execute(inst)`

**Returns:** ``



### `catch(Exception &ex)`

**Returns:** ``



### `fixparameter(Data &param, const Type &pdef, bool ref, const std::string &error)`

**Returns:** `void`



### `switch(original[0])`

**Returns:** ``



### `if(spec)`

**Returns:** ``



### `if(spechandler)`

**Returns:** ``



### `SymbolNotFoundException(original, SymbolType::Identifier, "Special identifier "+original+" cannot be found")`

**Returns:** `throw`



### `SymbolNotFoundException(cname, SymbolType::Identifier, "While searching for: "+original)`

**Returns:** `throw`



### `while(name!="")`

**Returns:** ``



### `if(!nmspc)`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Identifier, name+" is null")`

**Returns:** `throw`



### `if(!type)`

**Returns:** ``



### `SymbolNotFoundException(original, SymbolType::Identifier, "Cannot find symbol: "+cname)`

**Returns:** `throw`



### `SymbolNotFoundException(original, SymbolType::Identifier, "Cannot find symbol: "+cname)`

**Returns:** `throw`



### `SymbolNotFoundException(original, SymbolType::Identifier, "Cannot find symbol: "+cname)`

**Returns:** `throw`



### `SymbolNotFoundException(name, SymbolType::Identifier, name+" is null")`

**Returns:** `throw`



### `switch(name[0])`

**Returns:** ``



### `if(spec)`

**Returns:** ``



### `if(spechandler)`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Identifier, "Special identifier "+name+" cannot be found")`

**Returns:** `throw`



### `if(var)`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Variable)`

**Returns:** `throw`



### `switch(name[0])`

**Returns:** ``



### `if(spec)`

**Returns:** ``



### `if(spechandler)`

**Returns:** ``



### `ConstantException(name)`

**Returns:** `throw`



### `if(!done)`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Identifier, "Special identifier "+name+" cannot be found")`

**Returns:** `throw`



### `if(var)`

**Returns:** ``



### `if(ref)`

**Returns:** ``



### `if(var)`

**Returns:** ``



### `FlowException("No active execution scope")`

**Returns:** `throw`



### `switch(val.Type)`

**Returns:** ``



### `CastException("literal", "reference")`

**Returns:** `throw`



### `if(reference)`

**Returns:** ``



### `CastException("non reference temporary", "reference")`

**Returns:** `throw`



### `if(reference)`

**Returns:** ``



### `if(var)`

**Returns:** ``



### `CastException("non-reference special variable", "reference")`

**Returns:** `throw`



### `GetVariable(val.Name)`

**Returns:** `return`



### `FindSymbol(val.Name, reference)`

**Returns:** `return`



### `if(count==0)`

**Returns:** ``


Calls the given function with the given values.


### `if(count==1)`

**Returns:** ``


... better error reporting


### `callvariant(fn, &fn->Methods[0], method, incomingparams)`

**Returns:** `return`



### `callvariant(fn, &fn->Overloads[0], method, incomingparams)`

**Returns:** `return`



### `callvariant(fn, &fn->Overloads[0], method, incomingparams)`

**Returns:** `return`



### `callvariant(fn, &fn->Methods[0], method, incomingparams)`

**Returns:** `return`



### `catch(const CastException &)`

**Returns:** ``



### `for(const auto &var : variants)`

**Returns:** ``



### `for(const Parameter &param : var.Parameters)`

**Returns:** ``



### `if(c==-1)`

**Returns:** ``



### `if(c==-1)`

**Returns:** ``



### `if(method)`

**Returns:** ``



### `list(fn->Methods, 0)`

**Returns:** ``



### `list(fn->Overloads, 1000)`

**Returns:** ``



### `list(fn->Overloads, 0)`

**Returns:** ``



### `list(fn->Methods, 1000)`

**Returns:** ``



### `callvariant(fn, var, method, incomingparams)`

**Returns:** `return`


... better error reporting


### `if(pin->Type==ValueType::Variable)`

**Returns:** ``



### `NullValueException("$"+pin->Name)`

**Returns:** `throw`



### `NullValueException("parent parameter")`

**Returns:** `throw`



### `for(const Parameter &pdef : variant->Parameters)`

**Returns:** ``



### `if(pin->Type==ValueType::Variable || pin->Type==ValueType::Identifier)`

**Returns:** ``



### `if(pin->Type==ValueType::Literal)`

**Returns:** `else`



### `InstructionException("Reference type can only be represented string literals and variables")`

**Returns:** `throw`



### `InstructionException("Reference type can only be represented string literals and variables")`

**Returns:** `throw`



### `if(pin->Type==ValueType::Identifier || pin->Type==ValueType::Variable)`

**Returns:** ``



### `NullValueException("$"+pin->Name)`

**Returns:** `throw`



### `if(pin->Type==ValueType::Identifier || pin->Type==ValueType::Variable)`

**Returns:** ``



### `NullValueException("$"+pin->Name)`

**Returns:** `throw`



### `for(auto &opt : pdef.Options)`

**Returns:** ``



### `for(auto &opt : pdef.Options)`

**Returns:** ``



### `if(!ok)`

**Returns:** ``



### `for(auto &opt : pdef.Options)`

**Returns:** ``



### `if(inst->Name.Type==ValueType::Literal)`

**Returns:** ``


Handles function/method call instructions


### `if(inst->Name.Type==ValueType::Identifier || inst->Name.Type==ValueType::Variable)`

**Returns:** `else`



### `if(inst->Name.Type==ValueType::Temp)`

**Returns:** `else`



### `SymbolNotFoundException(functionname, SymbolType::Function, "Cannot convert "+functionname+" to a function")`

**Returns:** `throw`



### `SymbolNotFoundException(inst->Name.Name, SymbolType::Function)`

**Returns:** `throw`



### `if(functionname=="return")`

**Returns:** ``



### `if(scope.returns.type)`

**Returns:** ``



### `fixparameter(data, *scope.returns.type, scope.returns.reference, "")`

**Returns:** ``



### `if(scope.returns.constant)`

**Returns:** ``



### `Return(data)`

**Returns:** ``



### `Return()`

**Returns:** ``



### `if(!fn)`

**Returns:** ``



### `if(!memberonly)`

**Returns:** ``



### `catch(const SymbolNotFoundException &)`

**Returns:** ``



### `SymbolNotFoundException(functionname, SymbolType::Function, "Cannot convert "+functionname+" to a function")`

**Returns:** `throw`



### `if(functionname=="{}")`

**Returns:** ``



### `SymbolNotFoundException(functionname, SymbolType::Function, "Cannot convert "+functionname+" to a function")`

**Returns:** `throw`



### `if(inst->Store)`

**Returns:** ``



### `NoReturnException(functionname)`

**Returns:** `throw`



### `if(inst->Type==InstructionType::Assignment)`

**Returns:** ``



### `SetVariable(inst->Name.Name, v, inst->Reference)`

**Returns:** ``



### `if(inst->Type==InstructionType::SaveToTemp)`

**Returns:** `else`



### `if(inst->Type==InstructionType::FunctionCall)`

**Returns:** `else`



### `functioncall(inst, false, false)`

**Returns:** ``



### `if(inst->Type==InstructionType::MemberFunctionCall)`

**Returns:** `else`



### `functioncall(inst, true, false)`

**Returns:** ``



### `if(inst->Type==InstructionType::MethodCall)`

**Returns:** `else`



### `functioncall(inst, false, true)`

**Returns:** ``



### `if(inst->Type==InstructionType::MemberMethodCall)`

**Returns:** `else`



### `functioncall(inst, true, true)`

**Returns:** ``



### `if(inst->Type==InstructionType::MemberToTemp || inst->Type==InstructionType::MemberToVar || inst->Type==InstructionType::MemberAssignment)`

**Returns:** `else`



### `if(inst->Type==InstructionType::MemberAssignment)`

**Returns:** ``



### `if(!member)`

**Returns:** ``



### `if(inst->Type==InstructionType::MemberAssignment)`

**Returns:** ``



### `if(inst->Type==InstructionType::MemberToVar)`

**Returns:** `else`



### `if(inst->Type==InstructionType::RemoveTemp)`

**Returns:** `else`



### `if(highesttemp==inst->Store)`

**Returns:** ``



### `if(inst->Type==InstructionType::Jump)`

**Returns:** `else`



### `if(inst->Type==InstructionType::JumpTrue)`

**Returns:** `else`



### `if(inst->Type==InstructionType::JumpFalse)`

**Returns:** `else`



### `if(inst->Type==InstructionType::DeclOverload)`

**Returns:** `else`



### `if(inst->Parameters[1].Type==ValueType::Literal)`

**Returns:** ``



### `for(unsigned i=3; i<inst->Parameters.size()`

**Returns:** ``



### `for(auto v : ptemp.options)`

**Returns:** ``



### `fixparameter(d, *ptype, false, "")`

**Returns:** ``



### `ss(code)`

**Returns:** `std::stringstream`



### `si(ss, dialect)`

**Returns:** `StreamInput`



### `Start(si)`

**Returns:** ``



### `for(auto &d : params)`

**Returns:** ``



### `callfunction(fn, method, pars)`

**Returns:** `return`



### `for(const auto &member : name.Members)`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Namespace, "Symbol "+name+" is not a namespace")`

**Returns:** `throw`



### `if(!nmspc)`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Namespace, name+" is null")`

**Returns:** `throw`



### `UsingNamespace(*nmspc)`

**Returns:** ``


