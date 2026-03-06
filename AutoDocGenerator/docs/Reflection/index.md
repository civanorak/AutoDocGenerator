# Reflection

&gt; Auto-generated documentation for the **Reflection** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Parameter`

**Namespace:** `Types`

Marks the object as optional Marks the object as a reference. When this tag affects types, it marks the type as a reference type, meaning it will always be moved around as a reference. When this tag affects parameters, object becomes a reference to the parameter Marks the object as input Marks the object as output. This may set ReferenceTag and unset InputTag. Denotes that a function has a method variant Marks an object as repeatable Used only in functions with console dialect. When set, this tag allows last parameter to contain spaces Marks object as a keyword Makes the object private, allowing only access from it parent Makes the object public, allowing it to be accessed from all Makes an object static Makes a function operator Marks a parameter or a function constant Denotes a function that returns const Makes this parameter a variable accepting parameter. Variable parameters are type checked against supplied type, however, they are always passed as strings denoting the name of the variable Makes a constructor implicit Allows a parameter to be NULL Marks a data member readonly, so that it can be manipulated, but cannot be changed

#### Methods

##### `swap(options, this->Options)`

**Returns:** ``

Constructs a new parameter. All information regarding to a parameter should be specified in the constructor. After construction parameter is non-mutable. options, tags, and defaultvalue are optional

##### `UnpackTags(tags...)`

**Returns:** ``

##### `GetName(—)`

**Returns:** `std::string`

@cond INTERNAL @endcond Copy assignment Compares two parameters, not very reliable, it does not check defaultvalue and options Returns the name of the parameter

##### `GetHelp(—)`

**Returns:** `std::string`

Returns the help related with this parameter

##### `IsOptional(—)`

**Returns:** `bool`

Returns the type of the parameter Checks if the parameter is optional

##### `IsReference(—)`

**Returns:** `bool`

Checks if the parameter is a reference. When a parameter is a reference, its passed as a reference or pointer. Therefore, this value can be changed. Literal values cannot be passed as references.

##### `IsConstant(—)`

**Returns:** `bool`

Checks if this parameter accepts a constant value

##### `IsVariable(—)`

**Returns:** `bool`

If true, this parameter is a variable and its name is given to the function as a string.

##### `AllowsNull(—)`

**Returns:** `bool`

If true, a null reference can be passed to this parameter

##### `GetDefaultValue(—)`

**Returns:** `Data`

Returns the default value for this parameter

##### `ASSERT(optional, name+" parameter does not have default value")`

**Returns:** ``

##### `UnpackTags(—)`

**Returns:** `void`

Allowed values for this parameter

##### `UnpackTags(Tag tag, Params_ ...tags)`

**Returns:** `void`

##### `switch(tag)`

**Returns:** ``

##### `UnpackTags(tags...)`

**Returns:** ``


### `Member`

**Namespace:** `Types`

#### Methods

##### `GetName(—)`

**Returns:** `std::string`

Returns the name of this member.

##### `GetHelp(—)`

**Returns:** `std::string`

Returns the help string. Help strings may contain markdown notation.

##### `virtual` `IsInstanceMember(—)`

**Returns:** `virtual bool`

Returns if this member is an instance member

##### `GetQualifiedName(—)`

**Returns:** `std::string`

Returns the namespace qualified name of this member

##### `virtual` `SetParent(const Member &parent)`

**Returns:** `virtual void`

Changes the parent of the member. Subclasses may perform additional checks when the parent is determined. Subclass should *always* call parent class' SetParent function first


### `StaticMember`

**Namespace:** `Types`

The name of the datamember Help string of the datamember

#### Methods

##### `IsInstanceable(—)`

**Returns:** `bool`

A type An event type, which contains additional information about an event Enumeration, which is also a type Namespace, which is also a type Data member Function, functions can also be represented as data members Static fixed constant Whether this member can be used to instantiate an object. Determined using GetMemberType

##### `virtual` `GetMemberType(—)`

**Returns:** `virtual MemberType`

Returns the type of this member.

##### `virtual` `Get(—)`

**Returns:** `virtual Data`

Returns the value of this static member. For types and functions, this function returns type and function objects.


### `StaticDataMember`

**Namespace:** `Types`

#### Methods

##### `StaticDataMember(name, help, type, false, false, false)`

**Returns:** ``

##### `StaticDataMember(name, help, type, false, false, false)`

**Returns:** ``

##### `UnpackTags(first)`

**Returns:** ``

##### `UnpackTags(rest...)`

**Returns:** ``

##### `Set(Data &newval)`

**Returns:** `void`

Changes the value of this member

##### `if(readonly)`

**Returns:** ``

##### `ReadOnlyException(name)`

**Returns:** `throw`

##### `set(newval)`

**Returns:** ``

##### `IsConstant(—)`

**Returns:** `bool`

Gets data from the datamember Returns the type of this static member Returns whether this member is a constant

##### `IsReference(—)`

**Returns:** `bool`

Returns whether this member is a reference

##### `IsReadonly(—)`

**Returns:** `bool`

Returns whether this member is read-only. Read-only members cannot be assigned to, however, their state can be altered using its data members or functions.

##### `virtual` `set(Data &newval)`

**Returns:** `virtual void`

Implementers of static data member should overload this function for assignment. If readonly is set, this function will not be called, instead, the public set function will throw readonly exception.

##### `virtual` `get(—)`

**Returns:** `virtual Data`

This function should return the data. It is overloaded to enforce modifiers.

##### `UnpackTags(—)`

**Returns:** `void`

Type of the datamember This instance member is a constant This instance member is a reference Marks this instance as read-only

##### `UnpackTags(Tag tag, Params_ ...tags)`

**Returns:** `void`

##### `switch(tag)`

**Returns:** ``

##### `UnpackTags(tags...)`

**Returns:** ``


### `Function`

**Namespace:** `Types`


### `Overload`

**Namespace:** `Types`

#### Methods

##### `swap(parameters, this->parameters)`

**Returns:** ``

Regular constructor that can take as many tags as needed.

##### `unpacktags(tags...)`

**Returns:** ``

##### `swap(parameters, this->parameters)`

**Returns:** ``

A full constructor

##### `IsSame(const Overload &var)`

**Returns:** `bool`

Compares two variants if they have the same signature

##### `StretchLast(—)`

**Returns:** `bool`

Returns if the last parameter of this function should be stretched. If true, in console dialect, spaces in the last parameter are not treated as parameter separator as if it is in quotes. Helpful for functions like echo. But also helpful for keywords that requires their own parsing.

##### `RepeatLast(—)`

**Returns:** `bool`

Returns if the last parameter of this function should be repeated. If true last parameter can be specified any number of times. This number can be obtained from data list supplied to function stub. If both StretchTag and RepeatTag is specified, in console dialect stretch is used, while in programming dialect repeat is used.

##### `IsConstant(—)`

**Returns:** `bool`

Returns whether this function is a constant

##### `ReturnsRef(—)`

**Returns:** `bool`

This function variant returns a reference to a value rather than the value itself

##### `ReturnsConst(—)`

**Returns:** `bool`

This function variant returns a constant

##### `ASSERT(parent, "Parent is not set")`

**Returns:** ``

Returns the function this variant belongs

##### `HasReturnType(—)`

**Returns:** `bool`

Returns whether this variant returns a value

##### `ASSERT(returntype, "This function does not return a value")`

**Returns:** ``

Returns the type this variant returns

##### `IsImplicit(—)`

**Returns:** `bool`

Returns if this variant can be used as implicit conversion

##### `virtual` `Call(bool ismethod, const std::vector<Data> &parameters)`

**Returns:** `virtual Data`

##### `unpacktags(—)`

**Returns:** `void`

The parameters of this overload @cond INTERNAL

##### `unpacktags(Tag tag, P_ ...rest)`

**Returns:** `void`

##### `switch(tag)`

**Returns:** ``

##### `ASSERT(false, "Unknown tag", 2, 16)`

**Returns:** ``

##### `unpacktags(rest...)`

**Returns:** ``

##### `virtual` `dochecks(bool ismethod)`

**Returns:** `virtual void`

@endcond This function should perform validity checks on the variant. The base function should be called unless similar checks are repeated


### `InstanceMember`

**Namespace:** `Types`

@endcond

#### Methods

##### `Get(Data &source)`

**Returns:** `Data`

Constructor Returns the type of this data member Gets data from the datamember

##### `Set(Data &source, Data &value)`

**Returns:** `void`

Sets the data of the data member, if the source is a reference, this function should perform in place replacement of the value

##### `if(readonly)`

**Returns:** ``

##### `ReadOnlyException(name)`

**Returns:** `throw`

##### `set(source, value)`

**Returns:** ``

##### `IsConstant(—)`

**Returns:** `bool`

Returns whether this member is a constant

##### `IsReference(—)`

**Returns:** `bool`

Returns whether this member is a reference

##### `IsReadonly(—)`

**Returns:** `bool`

Returns whether this member is read-only. Read-only members cannot be assigned to, however, their state can be altered using its data members or functions.

##### `virtual` `set(Data &source, Data &value)`

**Returns:** `virtual void`

This function should perform set operation

##### `virtual` `get(Data &source)`

**Returns:** `virtual Data`

This function should return the value of this member

##### `virtual` `typecheck(const Type *type)`

**Returns:** `virtual void`

Type checks the parent


### `Namespace`

**Namespace:** `Types`

Type of the datamember This instance member is a constant This instance member is a reference Marks this instance as read-only

#### Methods

##### `Members(members)`

**Returns:** ``

##### `virtual` `AddMember(StaticMember &member)`

**Returns:** `virtual void`

Adds a new member to this namespace

##### `virtual` `AddMember(StaticMember *member)`

**Returns:** `virtual void`

Adds a new member to this namespace

##### `ASSERT(member!=nullptr, "Member is null")`

**Returns:** ``

##### `virtual` `AddMembers(std::initializer_list<StaticMember*> newmembers)`

**Returns:** `virtual void`

Adds a list of members to this namespace

##### `for(auto member : newmembers)`

**Returns:** ``

##### `ASSERT(member!=nullptr, "Member is null")`

**Returns:** ``

##### `virtual` `AddMembers(std::vector<StaticMember*> newmembers)`

**Returns:** `virtual void`

Adds a list of members to this namespace

##### `for(auto member : newmembers)`

**Returns:** ``

##### `ASSERT(member!=nullptr, "Member is null")`

**Returns:** ``

##### `ValueOf(const std::string &name)`

**Returns:** `Data`

Convenience function, returns the namespace with the given name. Types are also considered as namespaces as they are derived from it. If there is no such namespace, symbol not found error is given. Convenience function, returns the type with the given name. If there is no such type, symbol not found error is given. Any class that is derived from type is also valid. Convenience function, returns the function with the given name. If there is no such function, symbol not found error is given. Convenience function, returns the value of the symbol with the given name.

##### `SymbolNotFoundException(name, SymbolType::Identifier, "Symbol "+name+" cannot be found.")`

**Returns:** `throw`


### `Type`

**Namespace:** `Types`

List of static members


### `Inheritance`

**Namespace:** `Types`

Morphing is not possible Already that type This is an upcasting, but not a direct one This is a down casting This is a type casting


### `Constant`

**Namespace:** `Types`

Instance members of this type Default value of this type. Default value is sometimes used for type checking and it is vital for the system to work correctly Constructors of this type. They can also act like conversion from operators. Implicit conversion constructors should have their flag set. Inheritance list. Inherited symbols This lists all parents of this type in the entire hierarchy. Whether this type is a reference type


### `EventType`

**Namespace:** `Types`

Returns the type of the constant Allows printing of types Events allow an easy mechanism to program logic into actions instead of checking actions continuously. This system is vital for UI programming. Events are basically function descriptors.

#### Methods

##### `swap(parameters, this->parameters)`

**Returns:** ``

##### `HasReturnType(—)`

**Returns:** `bool`

Returns whether event handlers should return a value

##### `ASSERT(returntype, "This event does not allow returns")`

**Returns:** ``

Returns the return type expected from the handlers.


### `EnumType`

**Namespace:** `Types`

Read only list of parameters Parameters that every event handler should accept. The return type of this event, if it is allowed to return a value


### `ElementInitializer`

**Namespace:** `Types`


### `Library`

**Namespace:** `Types`


---

## Enums

### `Tag`

**Namespace:** `Types`

Tags define behavior of reflection objects


### `MemberType`

**Namespace:** `Types`

Possible member types


### `MorphType`

**Namespace:** `Types`

There are multiple ways to morph a type to another, this enumeration holds these types


---

## Functions

### `if(keyword)`

**Returns:** ``



### `for(const auto &var : constructor.Overloads)`

**Returns:** ``



### `for(const auto &pdef : var.Parameters)`

**Returns:** ``



### `if(status!=-1)`

**Returns:** ``



### `for(const auto &param : parameters)`

**Returns:** ``



### `compare(l, r)`

**Returns:** `return`



### `AddMember(constructor)`

**Returns:** ``



### `if(type==this)`

**Returns:** ``



### `catch(const std::bad_cast &)`

**Returns:** ``



### `if(downcasting)`

**Returns:** ``



### `for(auto t : type.parents)`

**Returns:** ``



### `for(auto t : type.InheritsFrom)`

**Returns:** ``



### `for(const auto &o : type.Members)`

**Returns:** ``



### `for(const auto &o : type.InstanceMembers)`

**Returns:** ``



### `for(const auto &s : type.inheritedsymbols)`

**Returns:** ``



### `for(const Parameter &p : parameters)`

**Returns:** ``



### `if(ismethod)`

**Returns:** ``



### `if(this->parent)`

**Returns:** ``



### `ASSERT(!isoperator, "Operators cannot be static members.")`

**Returns:** ``



### `SymbolNotFoundException(name, SymbolType::Type, "Type "+name+" cannot be found.")`

**Returns:** `throw`



### `SymbolNotFoundException(name, SymbolType::Type, "Symbol "+name+" is not a type.")`

**Returns:** `throw`



### `SymbolNotFoundException(name, SymbolType::Type, "Type "+name+" cannot be found.")`

**Returns:** `throw`



### `SymbolNotFoundException(name, SymbolType::Type, "Symbol "+name+" is not a type.")`

**Returns:** `throw`



### `SymbolNotFoundException(name, SymbolType::Function, "Function "+name+" cannot be found.")`

**Returns:** `throw`



### `SymbolNotFoundException(name, SymbolType::Function, "Symbol "+name+" is not a function.")`

**Returns:** `throw`



### `GetNameOf(const T_ &val)`

**Returns:** `std::string`



### `GetHelpOf(const T_ &val)`

**Returns:** `std::string`



### `unpacktags(tag)`

**Returns:** ``


Modifiable parameters of this overload Return type of this function variant. If nullptr this function does not return a value. If true, in console dialect, spaces in the last parameter are not treated as parameter separator as if it is in quotes. Helpful for functions like echo If true last parameter can be specified any number of times. This number can be obtained from data list supplied to function stub. Only meaningful in class member functions. If true this function can be access from outside the type itself Makes this function constant. Only works on member functions. This function variant returns a reference This function variant returns a constant, useful with references The parent function of this variant If the parent function is constructor, marks this variant as an implicit type conversion Regular constructor with both overloads and methods specified a long with at least a single tag


### `unpacktags(tags...)`

**Returns:** ``



### `for(auto &variant : overloads)`

**Returns:** ``



### `AddOverload(variant)`

**Returns:** ``



### `for(auto &variant : methods)`

**Returns:** ``



### `AddMethod(variant)`

**Returns:** ``



### `init()`

**Returns:** ``



### `unpacktags(tag)`

**Returns:** ``


Regular constructor with overloads specified a long with at least a single tag


### `unpacktags(tags...)`

**Returns:** ``



### `for(auto &overload : overloads)`

**Returns:** ``



### `AddOverload(overload)`

**Returns:** ``



### `init()`

**Returns:** ``



### `for(auto &overload : overloads)`

**Returns:** ``


Regular constructor with both overloads and methods without any tags


### `AddOverload(overload)`

**Returns:** ``



### `for(auto &overload : methods)`

**Returns:** ``



### `AddMethod(overload)`

**Returns:** ``



### `init()`

**Returns:** ``



### `init()`

**Returns:** ``


Full constructor


### `IsKeyword()`

**Returns:** `bool`


Returns if this function is actually a keyword.


### `IsStatic()`

**Returns:** `bool`


Returns if this function is static. Only meaningful when the function is a member function.


### `IsMember()`

**Returns:** `bool`


Returns if this function is a member function of a type.


### `IsOperator()`

**Returns:** `bool`


Returns if this function is an operator


### `ASSERT(parent, "This function does not have an owner.", 1, 5)`

**Returns:** ``


If this function is a member function, returns the owner object. If this function is not a member function, this function crashes.


### `AddOverload(Overload &overload)`

**Returns:** `virtual void`


Adds the given overload to this function after performing necessary checks


### `for(const auto &v : overloads)`

**Returns:** ``



### `AmbiguousSymbolException(name, SymbolType::Function, "Ambiguous function variant")`

**Returns:** `throw`



### `AddMethod(Overload &overload)`

**Returns:** `virtual void`


Adds the given overload as a method to this function after performing necessary checks


### `ASSERT(!isoperator, "Operators cannot be methods\n in function "+name, 1, 3)`

**Returns:** ``



### `for(const auto &v : methods)`

**Returns:** ``



### `AmbiguousSymbolException(name, SymbolType::Function, "Ambiguous function variant")`

**Returns:** `throw`



### `AddOverload(Overload *overload)`

**Returns:** `virtual void`


Adds the given overload to this function after performing necessary checks


### `ASSERT(overload, "Empty variant\n in function "+name)`

**Returns:** ``



### `AddOverload(*overload)`

**Returns:** ``



### `AddMethod(Overload *overload)`

**Returns:** `virtual void`


Adds the given overload as a method to this function after performing necessary checks


### `ASSERT(overload, "Empty variant\n in function "+name)`

**Returns:** ``



### `AddMethod(*overload)`

**Returns:** ``



### `unpacktags()`

**Returns:** `void`


The list of overloads this function has The list of methods this function has @cond INTERNAL


### `unpacktags(Tag tag, P_ ...rest)`

**Returns:** `void`



### `switch(tag)`

**Returns:** ``



### `ASSERT(!isoperator, "A function cannot be a static operator")`

**Returns:** ``



### `ASSERT(!staticmember, "A function cannot be a static operator")`

**Returns:** ``



### `ASSERT(parent, "Operators should be member functions")`

**Returns:** ``



### `ASSERT(false, "Unknown tag", 2, 16)`

**Returns:** ``



### `unpacktags(rest...)`

**Returns:** ``



### `init()`

**Returns:** `void`



### `for(auto member : newmembers)`

**Returns:** ``


Adds a static member to this type Adds a static member to this type Adds a list of static members to this type


### `for(auto member : newmembers)`

**Returns:** ``


Adds a list of static members to this type


### `AddMember(InstanceMember &member)`

**Returns:** `virtual void`


Adds a list of instance members to this type


### `AddMember(InstanceMember *member)`

**Returns:** `virtual void`


Adds a list of instance members to this type


### `ASSERT(member!=nullptr, "Member is null")`

**Returns:** ``



### `AddMembers(std::initializer_list<InstanceMember*> newmembers)`

**Returns:** `virtual void`


Adds an instance member to this type


### `for(auto member : newmembers)`

**Returns:** ``



### `ASSERT(member!=nullptr, "Member is null")`

**Returns:** ``



### `AddMembers(std::vector<InstanceMember*> newmembers)`

**Returns:** `virtual void`


Adds an instance member to this type


### `for(auto member : newmembers)`

**Returns:** ``



### `ASSERT(member!=nullptr, "Member is null")`

**Returns:** ``



### `AddConstructors(std::initializer_list<Function::Overload*> elements)`

**Returns:** `void`


Adds the given constructors


### `for(auto element : elements)`

**Returns:** ``



### `AddConstructor(Function::Overload &element)`

**Returns:** `void`


Adds the given constructor


### `AddInheritance(const Type &type, Inheritance::ConversionFunction from, Inheritance::ConversionFunction to)`

**Returns:** `void`


Adds an inheritance parent. from and to function should handle reference and constness of the data. Inheritance should be added in order. After using a class as a parent, no parent should be added to that class


### `GetDefaultValue()`

**Returns:** `Any`


Returns the value of the type


### `IsReferenceType()`

**Returns:** `bool`


Returns whether this type is a reference type.


### `MorphTo(const Type &type, Data source, bool allowtypecast=true)`

**Returns:** `Data`


Morphs the given data into the target type.


### `CanMorphTo(const Type &type)`

**Returns:** `MorphType`


Check if it is possible to morph this type to the other


### `for(const auto &ctor : constructor.Overloads)`

**Returns:** ``


Compares two types Compares two types Converts this type to its pointer This function returns type casting function from a given type to this one. If type casting is not found, this function will return nullptr. If implicit conversion requirement is set only the constructors that are allowed to be used implicitly is considered.


### `Construct(const std::vector<Data> &parameters)`

**Returns:** `Data`


!Unsafe. Constructs a new object from the given parameters. Requires parameters to be the exact type.


### `Delete(const Data &obj)`

**Returns:** `void`


Deletes the object


### `deleteobject(obj)`

**Returns:** ``



### `Compare(const Data &l, const Data &r)`

**Returns:** `bool`


This function compares two instances of this type. Both left and right should of this type.


### `ToString(const Data &)`

**Returns:** `virtual std::string`


Converts a data of this type to string. This function should never throw, if there is no data to display, recommended this play is either [ EMPTY ], or Typename #id


### `Parse(const std::string &)`

**Returns:** `virtual Data`


Parses a string into this data. This function is allowed to throw.


### `Assign(Data &l, const Data &r)`

**Returns:** `virtual void`


Assigns the value of the second parameter to the first, reference types can ignore this function


### `deleteobject(const Data &)`

**Returns:** `virtual void`


Constructors of this type. They can also act like conversion from operators. Implicit conversion constructors should have their flag set. Parents of this type. This includes indirect parents as well Inheritance list. Inherited symbols Type interface used for this type. If this type is a reference type, pointer-to-type and const pointer-to-type are used. Destructor This function should delete the given object.


### `compare(const Data &l, const Data &r)`

**Returns:** `virtual bool`


This function should compare two instances of the type. Not required for reference types as pointers will be compared


### `for(const ElementInitializer &element : elements)`

**Returns:** ``



### `AddMember(elm)`

**Returns:** ``



### `add(const ElementInitializer &element)`

**Returns:** `void`


Ordered list of allowed values


### `AddMember(elm)`

**Returns:** ``



### `Reflection("Reflection", "This library contains reflection objects")`

**Returns:** `Library`



### `if(type==nullptr)`

**Returns:** ``



### `InitReflection()`

**Returns:** `void`



### `for(auto o : p.Options)`

**Returns:** ``



### `for(auto p : o->Parameters)`

**Returns:** ``



### `for(const auto &o : fn->Overloads)`

**Returns:** ``



### `for(const auto &o : fn->Methods)`

**Returns:** ``



### `for(auto it=n.Members.First()`

**Returns:** ``



### `for(auto it=n.Members.First()`

**Returns:** ``



### `for(auto it=n.Members.First()`

**Returns:** ``



### `for(const auto &m : n->Members)`

**Returns:** ``



### `for(const auto &m : t->InstanceMembers)`

**Returns:** ``



### `for(const auto &m : t->InheritsFrom)`

**Returns:** ``



### `for(auto p : e->Parameters)`

**Returns:** ``



### `for(auto o : e->Ordered)`

**Returns:** ``



### `for(auto var : vars)`

**Returns:** ``



### `for(auto var : vars)`

**Returns:** ``



### `for(std::pair<std::string, Variable> var : vars)`

**Returns:** ``


