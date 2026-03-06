# MemoryStream

&gt; Auto-generated documentation for the **MemoryStream** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `MemoryInputBuffer`

**Namespace:** `Gorgon`

This class is an input only memory stream buffer. Use MemoryInputStream to create a stream

#### Methods

##### `underflow(—)`

**Returns:** `int_type`

##### `uflow(—)`

**Returns:** `int_type`

##### `pbackfail(int_type ch)`

**Returns:** `int_type`

##### `showmanyc(—)`

**Returns:** `std::streamsize`

##### `seekoff(off_type off, std::ios_base::seekdir way, std::ios_base::openmode which)`

**Returns:** `pos_type`

##### `if(way == std::ios_base::cur)`

**Returns:** ``

##### `if(way == std::ios_base::end)`

**Returns:** `else`

##### `seekpos(pos_type sp, std::ios_base::openmode which)`

**Returns:** `pos_type`


### `MemoryInputStream`

**Namespace:** `Gorgon`

#### Methods

##### `rdbuf(—)`

**Returns:** `delete`

