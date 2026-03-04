# Embedding

> Auto-generated documentation for the **Embedding** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `MappedFunction`

**Namespace:** `Scripting`

This class wraps a C++ function into an overload. It can be constructed using MapFunction.

#### Methods

##### `if(ismethod)`

**Returns:** ``

Constructor


### `extractvector`

**Namespace:** `Scripting`


### `is_nontmpref`

**Namespace:** `Scripting`


### `is_nonconstref`

**Namespace:** `Scripting`


### `MappedOperator`

**Namespace:** `Scripting`

#### Methods

##### `Function(name, help, *parent, {}, Scripting::OperatorTag)`

**Returns:** ``

Constructor, returntype and parent could be nullptr, tags are optional.

##### `ASSERT(returntype, "Operators should have a return type", 1, 1)`

**Returns:** ``

##### `ASSERT(parent, "Operators should belong a class", 1, 1)`

**Returns:** ``

##### `Function(name, help, *parent, {}, Scripting::OperatorTag)`

**Returns:** ``

##### `for(auto overload : overloads)`

**Returns:** ``

##### `AddOverload(F_ fn, const Type *returntype, const Type *rhs)`

**Returns:** `void`

Adds a new operator overload

##### `ASSERT(returntype, "Operators should have a return type", 1, 1)`

**Returns:** ``


### `MappedROInstanceMember`

**Namespace:** `Scripting`

#### Methods

##### `ASSERT(type, "Type cannot be nullptr", 1, 2)`

**Returns:** ``

##### `ASSERT(constant==istypeconst, "Constness of "+name+" does not match with its implementation")`

**Returns:** ``

##### `static` `deref(const T2_ val)`

**Returns:** `static typename std::enable_if<istypeptr, typename std::remove_pointer<T2_>::type>::type`

##### `static` `toptr(T2_ val)`

**Returns:** `static typename std::enable_if<istypeptr, T2_>::type`

##### `static` `clstoptr(const C2_ val)`

**Returns:** `static typename std::enable_if<std::is_pointer<C2_>::value, const C2_>::type`

##### `getnonref(Data &data)`

**Returns:** `typename std::enable_if<std::is_copy_constructible<T2_>::value, Data>::type`

##### `getnonref(data)`

**Returns:** `return`

Constructor


### `MappedInstanceMember`

**Namespace:** `Scripting`

#### Methods

##### `if(ref)`

**Returns:** ``

Constructor

##### `ASSERT(std::is_pointer<T_>::value, "Member "+name+" marked as reference but its source is not, should be a pointer")`

**Returns:** ``

##### `ASSERT(!constant || ref, "Non-reference constant instance members becomes readonly, choose a readonly embedder for "+name)`

**Returns:** ``

##### `ConstantException("Given item")`

**Returns:** `throw`

##### `ConstantException("Value for "+this->name, "Given value for "+this->name+" is constant")`

**Returns:** `throw`

##### `if(this->reference)`

**Returns:** ``

##### `if(this->reference)`

**Returns:** ``


### `MappedROInstanceMember_Function`

**Namespace:** `Scripting`

#### Methods

##### `ASSERT(type, "Type cannot be nullptr", 1, 2)`

**Returns:** ``

##### `ASSERT(parent, "Parent cannot be nullptr", 1, 2)`

**Returns:** ``


### `MappedInstanceMember_Function`

**Namespace:** `Scripting`


### `MappedROStaticDataMember`

**Namespace:** `Scripting`

#### Methods

##### `ASSERT(type, "Type cannot be nullptr", 1, 2)`

**Returns:** ``

##### `getnonref(—)`

**Returns:** `typename std::enable_if<std::is_copy_constructible<T2_>::value, Data>::type`

##### `GetValue(—)`

**Returns:** `T_`

If T_ is not a pointer, uses the value as initial value and stores the current value locally. The stored value can be accessed using GetValue function. If T_ is a pointer, it will be modified while modifying the value Returns the value stored in this data

##### `getnonref(—)`

**Returns:** `return`

Returns the value stored in this data

##### `if(constant)`

**Returns:** ``

##### `if(istypeptr)`

**Returns:** ``

##### `if(istypeptr)`

**Returns:** ``


### `MappedStaticDataMember`

**Namespace:** `Scripting`

#### Methods

##### `if(ref)`

**Returns:** ``

If T_ is a non-pointer type or T_ is pointer and ref is set to true, the value would be used as initial value. It is possible to access current value through GetValue function. If T_ is a pointer and ref is false value is used as the storage.

##### `ASSERT(std::is_pointer<T_>::value, "Member "+name+" marked as reference but its source is not, should be a pointer")`

**Returns:** ``

##### `ASSERT(!constant || ref, "Non-reference constant instance members becomes readonly, choose a readonly embedder for "+name)`

**Returns:** ``

##### `ConstantException("Value for "+this->name, "Given value for "+this->name+" is constant")`

**Returns:** `throw`

##### `if(this->reference)`

**Returns:** ``


### `MappedValueType`

**Namespace:** `Scripting`

#### Methods

##### `MapConstructor(ParameterList params)`

**Returns:** `void`

##### `T_(args...)`

**Returns:** `return`

##### `ConstantException("")`

**Returns:** `throw`

Converts a data of this type to string. This function should never throw, if there is no data to display, recommended this play is either [ EMPTY ], or Typename #id Parses a string into this data. This function is allowed to throw.

##### `if(ptr!=nullptr)`

**Returns:** ``

##### `addcopyconst(—)`

**Returns:** ``

##### `T_(o)`

**Returns:** `return`

##### `addcopyconst(—)`

**Returns:** ``


### `MappedReferenceType`

**Namespace:** `Scripting`

#### Methods

##### `MapConstructor(ParameterList params)`

**Returns:** `void`

Converts a data of this type to string. This function should never throw, if there is no data to display, recommended display is either [ EMPTY ], or Typename #id

##### `if(ptr!=nullptr)`

**Returns:** ``

Parses a string into this data. This function is allowed to throw.

##### `addcopyconst(—)`

**Returns:** ``

##### `addcopyconst(—)`

**Returns:** ``


### `InternalReferenceType`

**Namespace:** `Scripting`

@cond INTERNAL Automatically generates Type to be used internally, will always return same constructed type for the same embedded type


### `InternalValueType`

**Namespace:** `Scripting`

Automatically generates Type to be used internally, will always return same constructed type for the same embedded type. Requires T_ to be default constructible


### `ExtractFromHelper`

**Namespace:** `Scripting`


### `MappedEventType`

**Namespace:** `Scripting`

@endcond

#### Methods

##### `constargs(int index, std::vector<Data> &ret, const std::vector<Parameter> params, T_ arg, Params_&& ...rest)`

**Returns:** `void`

##### `constargs(int index, std::vector<Data> &ret, const std::vector<Parameter> params)`

**Returns:** `void`

##### `callfn(const Scripting::Function *fn, std::vector<Data> args, Function::Overload *single)`

**Returns:** `R_`

##### `catch(SymbolNotFoundException &)`

**Returns:** ``

##### `callfn(O_& obj, const Scripting::Function *fn, std::vector<Data> args, Function::Overload *single)`

**Returns:** ``

##### `catch(SymbolNotFoundException &)`

**Returns:** ``

##### `callfn(fn, args, single)`

**Returns:** `return`

##### `registerfn(E_ *ev, const Scripting::Function *fn)`

**Returns:** ``

##### `for(auto &ovs : {&fn->Overloads, &fn->Methods})`

**Returns:** ``

##### `for(auto &ov : *ovs)`

**Returns:** ``

##### `callfn(fn, pars, overload)`

**Returns:** `return`

##### `registerfn(E_ *ev, const Scripting::Function *fn)`

**Returns:** ``

##### `for(auto &ovs : {&fn->Overloads, &fn->Methods})`

**Returns:** ``

##### `for(auto &ov : *ovs)`

**Returns:** ``

##### `callfn(obj, fn, pars, overload)`

**Returns:** `return`


### `MappedStringEnum`

**Namespace:** `Scripting`

#### Methods

##### `for(auto &s : strings)`

**Returns:** ``

strings parameter should contain, name and help of enum entries. Names could be any of the alternative names listed in the enum strings

##### `if(binary)`

**Returns:** ``

##### `ret(' ', digits)`

**Returns:** `std::string`

##### `for(unsigned i=0;i<digits;i++)`

**Returns:** ``

##### `ret(' ', digits)`

**Returns:** `std::string`

##### `for(unsigned i=0;i<digits;i++)`

**Returns:** ``

##### `MappedStringEnum(name, help, {}, defval, binary)`

**Returns:** ``

This constructor adds all elements without any help. Consider using the constructor that enables help text for enum items.

##### `ConstantException("")`

**Returns:** `throw`

##### `if(ptr!=nullptr)`

**Returns:** ``


---

## Functions

### `ToEmptyString(const T_ &)`

**Returns:** `std::string`



### `ParseThrow(const std::string &)`

**Returns:** `T_`



### `castto(const Data &d)`

**Returns:** `>::type`



### `castto(const Data &d)`

**Returns:** `>::type`



### `if(std::is_reference<T_>::value)`

**Returns:** ``



### `if(isref)`

**Returns:** ``



### `accumulatevector(const std::vector<Data> &parameters)`

**Returns:** ``



### `accumulatevector(const std::vector<Data> &parameters)`

**Returns:** ``



### `for(unsigned i=P_; i<parameters.size()`

**Returns:** ``



### `cast(const std::vector<Data> &parameters)`

**Returns:** `>::Type`



### `ASSERT(extractvector<param<P_>>::isvector, "Repeating parameter should be a vector")`

**Returns:** ``



### `callfn(TMP::Sequence<S_...>, const std::vector<Data> &parameters)`

**Returns:** ``



### `callfn(TMP::Sequence<S_...>, const std::vector<Data> &parameters)`

**Returns:** ``



### `callfn(TMP::Sequence<S_...>, const std::vector<Data> &parameters)`

**Returns:** ``



### `callfn(TMP::Sequence<S_...>, const std::vector<Data> &parameters)`

**Returns:** ``



### `checkparam()`

**Returns:** `void`



### `if(P_==0 && ismember)`

**Returns:** ``



### `if(is_nonconstref<T>::value)`

**Returns:** ``



### `if(std::is_pointer<T>::value)`

**Returns:** `else`



### `if(P_==0 && ismember)`

**Returns:** ``



### `if(std::is_reference<T>::value)`

**Returns:** `else`



### `if(!ismember || P_!=0)`

**Returns:** ``



### `if(std::is_const<T>::value)`

**Returns:** `else`



### `if(P_==0 && ismember)`

**Returns:** ``



### `if(P_==0 && ismember)`

**Returns:** ``



### `if(P_==0 && ismember)`

**Returns:** ``



### `check(TMP::Sequence<S_...>)`

**Returns:** `void`



### `if(std::is_same<typename traits::ReturnType, void>::value)`

**Returns:** ``



### `if(returnsconst)`

**Returns:** ``



### `if(returnsconst)`

**Returns:** ``



### `if(implicit)`

**Returns:** ``



### `to_(val)`

**Returns:** `return`



### `to_(val)`

**Returns:** `return`



### `if(implicit)`

**Returns:** ``



### `if(implicit)`

**Returns:** ``



### `if(implicit)`

**Returns:** ``



### `if(implicit)`

**Returns:** ``



### `MappedROInstanceMember_Function(reader, name, help, membertype, parenttype, true, false, true)`

**Returns:** `return new`



### `ExtractFromData(const Data &d)`

**Returns:** `R_`



### `h(d)`

**Returns:** `return`



### `MapDynamicInheritance(Type *type, Type *inherited)`

**Returns:** `void`



### `ASSERT(type && inherited, "Inheritance types cannot be nullptr")`

**Returns:** ``


