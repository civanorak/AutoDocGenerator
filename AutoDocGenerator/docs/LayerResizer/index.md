# LayerResizer

&gt; Auto-generated documentation for the **LayerResizer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `LayerResizer`

**Namespace:** `gge`

/This effect resizes a given layer. Resize operation is animated from a given value to another one

#### Methods

##### `Setup(utils::Rectangle From, utils::Rectangle To, int Time)`

**Returns:** `void`

/Target of this effect /Initializes the effect /Initializes the effect /Initializes the effect /Initializes the effect /Sets source and destination to the given values and allows time duration to reach the destination

##### `Setup(utils::Rectangle To, int Time)`

**Returns:** `void`

/Sets current destination to the given value and allows time duration to reach it

##### `virtual` `Progress(—)`

**Returns:** `virtual animation::ProgressResult::Type`


---

## Functions

### `if(Time)`

**Returns:** ``



### `if(from.Left>to.Left)`

**Returns:** ``



### `if(from.Top>to.Top)`

**Returns:** ``



### `if(from.Width>to.Width)`

**Returns:** ``



### `if(from.Height>to.Height)`

**Returns:** ``


