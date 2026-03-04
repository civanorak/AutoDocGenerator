# Environment

> Auto-generated documentation for the **Environment** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Listener`

**Namespace:** `internal`

#### Methods

##### `AudioLoop(—)`

**Returns:** `friend void`

##### `orientcalc(—)`

**Returns:** ``

##### `SetLocation(const Geometry::Point3D &location)`

**Returns:** `void`

Changes the current location of the listener, if automatic speed calculation is set, this function will infer speed and the location of the listener.

##### `poscalc(—)`

**Returns:** ``

##### `SetOrientation(const Geometry::Point3D &up, const Geometry::Point3D &orientation)`

**Returns:** `void`

Changes the orientation of the listener. This function is not cheap and should not be used if it can be avoided. In the default orientation Z is up and the listener is facing + in the Y axis

##### `orientcalc(—)`

**Returns:** ``

##### `SetOrientation(const Geometry::Point3D &location)`

**Returns:** `void`

Changes the orientation of the listener. This function is not cheap and should not be used if it can be avoided. In the default orientation Z is up and the listener is facing + in the Y axis

##### `orientcalc(—)`

**Returns:** ``

##### `GetLocation(—)`

**Returns:** `Geometry::Point3D`

Returns the current location of the listener.

##### `poscalc(—)`

**Returns:** `void`

##### `orientcalc(—)`

**Returns:** `void`


### `Environment`

**Namespace:** `internal`

#### Methods

##### `AudioLoop(—)`

**Returns:** `friend void`

##### `init(—)`

**Returns:** ``

##### `SetAttuniationFactor(float value)`

**Returns:** `void`

Changes the attunation factor, higher values will attunate sound more, causing a faster fall off.

##### `SetHeadRadius(float value)`

**Returns:** `void`

Changes the radius of the head of listener.

##### `SetNonBlocked(float value)`

**Returns:** `void`

Changes the percent of sound not blocked by the head. This calculation might change in time.

##### `SetAuricleAngle(float value)`

**Returns:** `void`

Changes the difference of hearing direction cause by the auricles.

##### `SetSpeakerLocation(int index, Geometry::Point3D value)`

**Returns:** `void`

Sets the real world location of the speakers.

##### `init(—)`

**Returns:** ``

##### `init(—)`

**Returns:** `void`

Returns the current listener object Currently active environment.

##### `updateorientation(—)`

**Returns:** `void`


---

## Functions

### `for(int i=0; i<4; i++)`

**Returns:** ``



### `for(int i=0; i<4; i++)`

**Returns:** ``



### `updateorientation()`

**Returns:** ``



### `for(int i=0; i<4; i++)`

**Returns:** ``



### `poscalc()`

**Returns:** ``


