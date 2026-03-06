# Tinting

&gt; Auto-generated documentation for the **Tinting** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Tinting`

**Namespace:** `gge`

/This effect tints a given colorizable target. Tinting is animated from a given value to another one

#### Methods

##### `Tinting(graphics::Colorizable2DLayer *Target, bool create=false)`

**Returns:** ``

/Initializes the effect /Initializes the effect /Initializes the effect

##### `Tinting(graphics::Colorizable2DLayer &Target, bool create=false)`

**Returns:** ``

/Initializes the effect

##### `Setup(graphics::RGBint From, graphics::RGBint To, int Time)`

**Returns:** `void`

/Sets source and destination to the given values and allows time duration to reach the destination

##### `Setup(graphics::RGBint To, int Time)`

**Returns:** `void`

/Sets current destination to the given value and allows time duration to reach it

##### `IsFinished(—)`

**Returns:** `bool`

##### `SetTarget(graphics::Colorizable2DLayer *target)`

**Returns:** `void`

##### `SetTarget(graphics::Colorizable2DLayer &target)`

**Returns:** `void`

##### `virtual` `Progress(—)`

**Returns:** `virtual animation::ProgressResult::Type`

/Target of this effect


---

## Functions

### `if(Time)`

**Returns:** ``



### `if(from.a>to.a)`

**Returns:** ``



### `if(from.r>to.r)`

**Returns:** ``



### `if(from.g>to.g)`

**Returns:** ``



### `if(from.b>to.b)`

**Returns:** ``


