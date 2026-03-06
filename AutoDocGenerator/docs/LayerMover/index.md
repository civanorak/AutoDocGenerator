# LayerMover

&gt; Auto-generated documentation for the **LayerMover** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `LayerMover`

**Namespace:** `gge`

/This effect moves a given layer. Moving operation is animated from a given value to another one

#### Methods

##### `LayerMover(LayerBase *Target, animation::Timer &controller, bool owner=false)`

**Returns:** ``

/Target of this effect /Initializes the effect

##### `LayerMover(LayerBase &Target, animation::Timer &controller, bool owner=false)`

**Returns:** ``

/Initializes the effect

##### `LayerMover(LayerBase *Target, bool create=false)`

**Returns:** ``

/Initializes the effect

##### `LayerMover(LayerBase &Target, bool create=false)`

**Returns:** ``

/Initializes the effect

##### `Setup(utils::Point From, utils::Point To, int Time)`

**Returns:** `void`

/Sets source and destination to the given values and allows time duration to reach the destination

##### `Setup(utils::Point To, int Time)`

**Returns:** `void`

/Sets current destination to the given value and allows time duration to reach it

##### `virtual` `isFinished(—)`

**Returns:** `virtual bool`

##### `virtual` `Progress(—)`

**Returns:** `virtual animation::ProgressResult::Type`


---

## Functions

### `if(Time)`

**Returns:** ``



### `if(from.x>to.x)`

**Returns:** ``



### `if(from.y>to.y)`

**Returns:** ``


