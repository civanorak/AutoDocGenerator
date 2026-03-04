# KeyRepeater

> Auto-generated documentation for the **KeyRepeater** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `eventunregisterhelper`

**Namespace:** `internal`

#### Methods

##### `virtual` `unregister(—)`

**Returns:** `virtual void`


### `eventunregisterer`

**Namespace:** `internal`


### `KeyRepeater`

**Namespace:** `internal`

#### Methods

##### `KeyRepeater(E_ &event, const std::initializer_list<Key> &keys, int delay = 100)`

**Returns:** ``

Default constructor Registers this repeater to the given event and registers the given keys

##### `KeyRepeater(const std::initializer_list<Key> &keys, int delay = 100)`

**Returns:** ``

Registers this repeater to the given event and registers the given keys

##### `RegisterTo(E_ &event, bool ignoremodified = false)`

**Returns:** `void`

Disable copy constructor Destructor Registers this repeater to the given event to obtain press and release actions. This event handler will only work for registered keys and will return 0 for all other keys. If ignoremodified is set, keys will not be triggered when a modifier key is pressed. This class depends on the event and should be destroyed or UnregisteredFrom before the event is destroyed.

##### `UnregisterFrom(—)`

**Returns:** ``

##### `UnregisterFrom(—)`

**Returns:** `void`

Unregisters this repeater from its registered event

##### `Register(Key key)`

**Returns:** `void`

Registers the given key to be repeated. Registering keys are necessary only for automatic key acquisition from an event.

##### `Register(Key key, T_ &&... args)`

**Returns:** `void`

Registers the given keys to be repeated. Registering keys are necessary only for automatic key acquisition from an event.

##### `Unregister(Key key)`

**Returns:** `void`

Unregisters a key from this repeater. Unregistering a key will trigger a release if key is pressed. The key can be pressed again later on using Press function however, it will not automatically be acquired from the event that this repeater is registered to.

##### `Release(key)`

**Returns:** ``

##### `IsKeyRegistered(Key key)`

**Returns:** `bool`

Returns whether a given is registered for automatic management.

##### `Press(Key key)`

**Returns:** `void`

Presses a key, effectively simulating keydown. Depeding on the settings, this may trigger repeat instantly.

##### `Release(Key key)`

**Returns:** `void`

Releases a key may cause a repeat.

##### `IsPressed(Key key)`

**Returns:** `bool`

Checks if a key is pressed

##### `SetRepeatOnPress(bool value)`

**Returns:** `void`

Sets whether the key will be repeated instantly when pressed.

##### `GetRepeatOnPress(—)`

**Returns:** `bool`

Returns whether the key will be repeated instantly when pressed.

##### `SetRepeatOnRelease(bool value)`

**Returns:** `void`

Sets if the key should be repeated right after the key is released.

##### `GetRepeatOnRelease(—)`

**Returns:** `bool`

Returns if the key will be repeated right after the key is released

##### `SetInitialDelay(int value)`

**Returns:** `void`

Sets the initial delay before the first (or second if instant repeat is on) key is repeated in milliseconds. Set 0 to disable.

##### `GetInitialDelay(—)`

**Returns:** `bool`

Returns the initial delay before the first (or second if instant repeat is on) key is repeated in milliseconds.

##### `SetDelay(int value)`

**Returns:** `void`

Repeat delay between successive repeat events in milliseconds. This is the initial value and can be altered by acceleration.

##### `GetDelay(—)`

**Returns:** `int`

Returns the delay between successive repeats in milliseconds.

##### `SetAcceleration(int value)`

**Returns:** `void`

Change in repeat delay per repeat in milliseconds, positive values will reduce delay by the given amount. You may use negative values to slow down.

##### `GetAcceleration(—)`

**Returns:** `int`

Returns the change in repeat delay per repeat in milliseconds, positive values will reduce delay by the given amount. You may use negative values to slow down.

##### `SetAccelerationStart(int value)`

**Returns:** `void`

Sets the number of repeats after which the acceleration will start excluding first press if repeat on press is set.

##### `GetAccelerationStart(—)`

**Returns:** `int`

Returns the number of repeats after which the acceleration will start excluding first press if repeat on press is set.

##### `SetAccelerationCount(int value)`

**Returns:** `void`

Set how many times acceleration can be applied. This number is counted after acceleration start.

##### `GetAccelerationCount(—)`

**Returns:** `int`

Returns how many times acceleration can be applied. This number is counted after acceleration start.

##### `GetFinalDelay(—)`

**Returns:** `int`

Returns the final delay between repeat events in milliseconds after acceleration is completed.

##### `SetupAcceleration(int startdelay, int finaldelay, int rampup)`

**Returns:** `void`

This function allows easy setup for acceleration by supplying starting delay, final delay and the time it should take to reach final delay. This function will calculate nearest values to match the given setup.

##### `KeyEvent(Key &key, float amount)`

**Returns:** `bool`

This function is used to handle key events


### `repeatinfo`

**Namespace:** `internal`

Press event that is called everytime a key is pressed.


---

## Functions

### `Register(key)`

**Returns:** ``



### `SetDelay(delay)`

**Returns:** ``



### `if(cur < lastprogress)`

**Returns:** ``



### `for(auto &p : pressedkeys)`

**Returns:** ``



### `while(p.second.delay < curdelta)`

**Returns:** ``



### `Repeat(p.first)`

**Returns:** ``



### `if(acceleration && accelerationstart < p.second.count)`

**Returns:** ``



### `if(p.second.count < accelerationstart + accelerationcount)`

**Returns:** ``



### `if(initialdelay)`

**Returns:** ``



### `Repeat(key)`

**Returns:** ``



### `if(repeatonrelease)`

**Returns:** ``



### `Repeat(key)`

**Returns:** ``



### `SetDelay(startdelay)`

**Returns:** ``



### `SetAccelerationStart(0)`

**Returns:** ``



### `SetAccelerationCount(c)`

**Returns:** ``



### `if(amount)`

**Returns:** ``



### `Press(key)`

**Returns:** ``



### `Release(key)`

**Returns:** ``



### `RegisterTo(event)`

**Returns:** ``



### `Register(key)`

**Returns:** ``



### `SetDelay(delay)`

**Returns:** ``


