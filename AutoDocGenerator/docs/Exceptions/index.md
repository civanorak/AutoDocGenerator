# Exceptions

> Auto-generated documentation for the **Exceptions** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `Exception`

**Namespace:** `Scripting`

#### Methods

##### `ASSERT_DUMP(false, message)`

**Returns:** ``

##### `GetType(—)`

**Returns:** `ExceptionType`

##### `virtual` `GetMessage(—)`

**Returns:** `virtual std::string`

##### `what(—)`

**Returns:** `return`

##### `virtual` `GetDetails(—)`

**Returns:** `virtual std::string`

##### `GetLine(—)`

**Returns:** `long`

##### `SetLine(long line)`

**Returns:** `void`

##### `ModifyLine(long line)`

**Returns:** `void`

##### `GetSourcename(—)`

**Returns:** `std::string`

##### `SetSourcename(const std::string &sourcename)`

**Returns:** `void`

##### `IsLineSet(—)`

**Returns:** `bool`


### `OutofBoundsException`

**Namespace:** `Scripting`


### `AmbiguousSymbolException`

**Namespace:** `Scripting`

#### Methods

##### `type(type)`

**Returns:** ``


### `SymbolNotFoundException`

**Namespace:** `Scripting`


### `NullValueException`

**Namespace:** `Scripting`

#### Methods

##### `name(symbolname)`

**Returns:** ``


### `UnexpectedKeywordException`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::UnexpectedKeyword, "The keyword " + keyword + " is not expected", linenumber)`

**Returns:** ``


### `FlowException`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::FlowError, message, linenumber)`

**Returns:** ``


### `MissingParameterException`

**Namespace:** `Scripting`


### `TooManyParametersException`

**Namespace:** `Scripting`


### `ParameterError`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::ParameterError, error, linenumber)`

**Returns:** ``


### `NoReturnException`

**Namespace:** `Scripting`


### `CastException`

**Namespace:** `Scripting`


### `InstructionException`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::InstructionError, message, linenumber)`

**Returns:** ``


### `ConstantException`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::Constant, identifier+" is a constant", linenumber)`

**Returns:** ``


### `FileNotFoundException`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::FileNotFound, "Cannot find or access file: "+filename, linenumber)`

**Returns:** ``


### `ReadOnlyException`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::ReadOnly, member+" is readonly", linenumber)`

**Returns:** ``


### `IOError`

**Namespace:** `Scripting`

#### Methods

##### `Exception(ExceptionType::IOError, "I/O" + type +" error is occured", linenumber)`

**Returns:** ``


### `ParseError`

**Namespace:** `Scripting`

This class contains information about a parse error. It is not intended to be used as an exception.


### `ParseError`

**Namespace:** `Gorgon`

This error will be thrown if a parsing function encounters with a general error


### `IllegalTokenError`

**Namespace:** `Gorgon`

Constructs a new parse error. Parse error codes should be between 0 and 999 with object id in front. For instance an object id of 11 should throw parse error 5 with code 110005 Error code This error will be thrown if a parsing function encounters with an illegal token


---

## Enums

### `ExceptionType`

**Namespace:** `Scripting`


### `SymbolType`

**Namespace:** `Scripting`

