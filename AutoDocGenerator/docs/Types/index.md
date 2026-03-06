# Types

&gt; Auto-generated documentation for the **Types** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)

---

## Classes

### `Range`

**Namespace:** `Gorgon`

This class represents a range of values. Generally, start is assumed to be included while end is excluded.

#### Methods

##### `Normalize(—)`

**Returns:** `void`

Normalizes the range ensuring Start is less than or equal to the end.

##### `if(Start > End)`

**Returns:** ``

##### `Difference(—)`

**Returns:** `T_`

Returns the difference between start and end


### `Empty`

**Namespace:** `Gorgon`

A class that has no members and can be used as placeholder

#### Methods

##### `NumberOfSetBits(uint32_t i)`

**Returns:** `inline int`

Returns the number of bits that are 1 in a number

##### `CeilToPowerOf2(uint32_t v)`

**Returns:** `inline uint32_t`

Calculate the smalllest power of two larger than this value

##### `FitInto(T_ &v, T_ min, T_ max)`

**Returns:** `void`

Performs clamping on the given value.

##### `Clamp(T_ v, T_ min, T_ max)`

**Returns:** `T_`

Performs clamping on the given value and returns the result.

##### `Between(T_ v, T_ min, T_ max)`

**Returns:** `bool`

Returns if the given number is within the given range including min but excluding max

##### `Between(Range<T_> range, T_ v)`

**Returns:** `bool`

Returns if the given number is within the given range including min but excluding max

##### `BetweenInclusive(T_ v, T_ min, T_ max)`

**Returns:** `bool`

Returns if the given number is within the given range including min and max

##### `Sign(T_ val)`

**Returns:** `int`

##### `PositiveMod(T_ value, T_ mod)`

**Returns:** `T_`

Returns positive modulus as in case in maths

##### `Mirror(T_ value, T_ size)`

**Returns:** `T_`

Returns mirror of the values.

##### `MultiLess(const T1_ &left, const T2_ &right)`

**Returns:** `bool`

Performs a multi-tiered comparison. Supplied the values of current object and other object in alternating fashion.

##### `MultiLess(const T1_ &left, const T2_ &right, const A_ & ...rest)`

**Returns:** `bool`

##### `MultiLess(rest...)`

**Returns:** `return`

##### `Angle(Float degrees)`

**Returns:** `inline Float`

Converts the given degrees to radians


### `AssumeOwnershipTag`

**Namespace:** `Gorgon`

Where acceptable, denotes that the object will assume the ownership


### `Updatable`

**Namespace:** `Gorgon`

Marks an object that can be updated

#### Methods

##### `virtual` `Update(—)`

**Returns:** `virtual void`


---

## Enums

### `YesNoAuto`

**Namespace:** `Gorgon`

This enumeration helps with systems that has boolen parameters that can be detected automatically, but can also be overriden.


### `YesNoUnset`

**Namespace:** `Gorgon`

This enumeration helps with systems that has boolen parameters that can be unset/empty.


### `Parity`

**Namespace:** `Gorgon`

Marks the parity as Odd or Even. Not every target will support None, but it is provided for places that support it.


### `ItemPosition`

**Namespace:** `Gorgon`

Defines where an item is located in a list


### `Axis`

**Namespace:** `Gorgon`

Defines a cardinal direction

