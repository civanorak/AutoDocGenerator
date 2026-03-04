# Random

> Auto-generated documentation for the **Random** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `random_initializer`

**Namespace:** `gge`

#### Methods

##### `random_initializer(—)`

**Returns:** ``


---

## Functions

### `Random()`

**Returns:** `T_`



### `Random(T_ min, T_ max)`

**Returns:** `T_`



### `Random(Byte min, Byte max)`

**Returns:** `inline Byte`



### `Random(char min, char max)`

**Returns:** `inline char`



### `Random(int min, int max)`

**Returns:** `inline int`



### `Random(Range<T_> range)`

**Returns:** `T_`



### `Random(Range<Byte> range)`

**Returns:** `inline Byte`



### `Random(Range<char> range)`

**Returns:** `inline char`



### `Random(Range<int> range)`

**Returns:** `inline int`



### `Random(std::vector<T_> &vec)`

**Returns:** `inline T_`



### `Random(const gge::utils::Bounds &bounds)`

**Returns:** `inline gge::utils::Point`



### `Shuffle(const I_ &beg, const I_ &end)`

**Returns:** `inline void`



### `for(int i=0;i<diff;i++)`

**Returns:** ``



### `RandomFill(I_ &begin, I_ &end)`

**Returns:** `void`



### `for(auto i=begin;i!=end;++i)`

**Returns:** ``



### `RandomFill(O_ &obj)`

**Returns:** `void`



### `for(auto i=obj.begin()`

**Returns:** ``



### `RandomFill(O_ &obj, T_ min, T_ max)`

**Returns:** `void`



### `for(auto i=obj.begin()`

**Returns:** ``



### `RandomFill(T_ *begin, T_ *end)`

**Returns:** `void`



### `for(auto i=begin;i!=end;++i)`

**Returns:** ``



### `RandomFill(I_ &begin, I_ &end, T_ min, T_ max)`

**Returns:** `void`



### `for(auto i=begin;i!=end;++i)`

**Returns:** ``



### `RandomFill(T_ *begin, T_ *end, T_ min, T_ max)`

**Returns:** `void`



### `for(auto i=begin;i!=end;++i)`

**Returns:** ``


