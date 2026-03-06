# Instruction

&gt; Auto-generated documentation for the **Instruction** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `Value`

**Namespace:** `Gorgon`

This value is a temporary and refers to a value calculated as the result of a function call This is a literal value This is a variable Marks this value as an identifier, either a constant or a variable For error checking purposes This class contains a parsed value. A value can be a temporary, literal, variable or a constant. For variables and constants, Name is stored. For a temporary, Result is stored, for a literal Value is stored.

#### Methods

##### `SetLiteral(const Scripting::Type *type, Any value)`

**Returns:** `void`

Used for variables and constants Used for literal values Type of this value. Used for temporary results

##### `SetLiteral(const Data &value)`

**Returns:** `void`

##### `SetStringLiteral(const std::string &value)`

**Returns:** `void`

##### `SetVariable(const std::string &name)`

**Returns:** `void`

##### `SetIdentifier(const std::string &name)`

**Returns:** `void`

##### `SetTemp(Byte index)`

**Returns:** `void`

##### `ToString(—)`

**Returns:** `std::string`

##### `if(Type==ValueType::Temp)`

**Returns:** ``

##### `if(Type==ValueType::Literal)`

**Returns:** `else`


### `Instruction`

**Namespace:** `Gorgon`

#### Methods

##### `Instruction(—)`

**Returns:** ``


---

## Enums

### `InstructionType`

**Namespace:** `Gorgon`

Describes the type of an instruction


### `ValueType`

**Namespace:** `Gorgon`

This value is not valid Marks instruction as a regular function call. Regular function calls can also be member functions, however, they cannot be data members. Marks this instruction as a member function call. This means the function is either a data member and will return or set the value of the member or a member function that will be called. Marks this instruction as a method call. Marks this instruction as access to a member, the result is stored in the given temporary. Member name is stored in RHS, temp index is stored in Store, and this pointer is stored in Parameters fields Marks this instruction as access to a member, the result is stored in the given variable. Member name is stored in RHS and the variable name is stored in Name fields Marks this instruction as member assignment. Name of the member is stored in the Name field, and the value to be assigned is stored in the RHS field. Marks this instruction as a member method call. Function name is passed in Name field. This pointer is the first element in the Parameters vector Marks instruction as an assignment. Marks instruction as a removal of a temporary. Temporary index should be stored in the Store member This instruction saves a value to the temporary Unconditionally jumps by the given offset. Offset should be in JumpOffset field Jumps by the given offset if RHS is false. Offset should be in JumpOffset field Jumps by the given offset if RHS is true. Offset should be in JumpOffset field Declares a new function overload. If the function does not exists, it will define the function Possible value types

