# Alignment

&gt; Auto-generated documentation for the **Alignment** module of the Gorgon C++ Game Engine.


## Contents

- [Enums](#enums)
- [Functions](#functions)

---

## Enums

### `Type`

**Namespace:** `Alignment`


---

## Functions

### `IsLeft(Type t)`

**Returns:** `inline bool`



### `IsRight(Type t)`

**Returns:** `inline bool`



### `IsCenter(Type t)`

**Returns:** `inline bool`



### `IsTop(Type t)`

**Returns:** `inline bool`



### `IsBottom(Type t)`

**Returns:** `inline bool`



### `IsMiddle(Type t)`

**Returns:** `inline bool`



### `IsValid(Type t)`

**Returns:** `inline bool`



### `SetLeft(Type t)`

**Returns:** `inline Type`



### `SetRight(Type t)`

**Returns:** `inline Type`



### `SetCenter(Type t)`

**Returns:** `inline Type`



### `SetTop(Type t)`

**Returns:** `inline Type`



### `SetBottom(Type t)`

**Returns:** `inline Type`



### `SetMiddle(Type t)`

**Returns:** `inline Type`



### `CalculateLocation(Type Align, const basic_Rectangle2D<T_> &target, const basic_Size2D<T_> &object)`

**Returns:** `inline basic_Point2D<T_>`



### `CalculateLocation(Type Align, const basic_Bounds2D<T_> &target, const basic_Size2D<T_> &object)`

**Returns:** `inline basic_Point2D<T_>`



### `CalculateLocation(Type Align, const basic_Rectangle2D<T_> &target, const basic_Size2D<T_> &object, const Margins &margins)`

**Returns:** `inline basic_Point2D<T_>`



### `CalculateLocation(Type Align, const basic_Bounds2D<T_> &target, const basic_Size2D<T_> &object, const Margins &margins)`

**Returns:** `inline basic_Point2D<T_>`


