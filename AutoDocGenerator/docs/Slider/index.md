# Slider

> Auto-generated documentation for the **Slider** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Slider`

**Namespace:** `gge`

#### Methods

##### `virtual` `getValue(—)`

**Returns:** `virtual T_`

##### `setValue(const T_ &value)`

**Returns:** `void`

##### `getMin(—)`

**Returns:** `T_`

##### `setMin(const T_ &value)`

**Returns:** `void`

##### `getMax(—)`

**Returns:** `T_`

##### `setMax(const T_ &value)`

**Returns:** `void`

##### `getAnimationDuration(—)`

**Returns:** `int`

##### `setAnimationDuration(const int &value)`

**Returns:** `void`

##### `getOrientation(—)`

**Returns:** `OrientationType`

##### `setOrientation(const OrientationType &orientation)`

**Returns:** `void`

##### `setShowTicks(const bool &value)`

**Returns:** `void`

##### `getShowTicks(—)`

**Returns:** `bool`

##### `setTickDistance(const floattype &value)`

**Returns:** `void`

##### `getTickDistance(—)`

**Returns:** `floattype`

##### `setShowNumbers(const bool &value)`

**Returns:** `void`

##### `getShowNumbers(—)`

**Returns:** `bool`

##### `setNumberDistance(const int &value)`

**Returns:** `void`

##### `getNumberDistance(—)`

**Returns:** `int`

##### `setValueAnimation(const bool &value)`

**Returns:** `void`

##### `getValueAnimation(—)`

**Returns:** `bool`

##### `setStepsize(const T_ &value)`

**Returns:** `void`

##### `getStepsize(—)`

**Returns:** `T_`

##### `setNumberFormat(const NumberFormatType &value)`

**Returns:** `void`

##### `getNumberFormat(—)`

**Returns:** `NumberFormatType`

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`

##### `virtual` `value_changed(—)`

**Returns:** `virtual void`

##### `ChangeEvent(—)`

**Returns:** ``


---

## Enums

### `OrientationType`

**Namespace:** `gge`


### `SliderInteractivity`

**Namespace:** `internal`


### `SliderValueMapping`

**Namespace:** `internal`


---

## Functions

### `refreshvalue()`

**Returns:** ``


@endcond


### `setupinteractivity()`

**Returns:** ``



### `SetValue(const T_ &value, bool instant = false)`

**Returns:** `void`


Sets the current value of the slider. If instant is set to true, the value will be set instantly without any animations.


### `setval(value, instant)`

**Returns:** ``



### `GetValue()`

**Returns:** `T_`


Gets the current value of the slider


### `SetMaximum(const T_ &value)`

**Returns:** `void`


Sets the maximum value that this slider reaches up to. If equal to minimum, progress will display 0.


### `if(valuemapping == internal::SliderValueMapping::ValueAndRange)`

**Returns:** ``



### `SetSmoothChangeSpeedRatio(changespeed)`

**Returns:** ``



### `SetSmoothChangeSpeed(unitspersec)`

**Returns:** ``



### `refreshvalue()`

**Returns:** ``



### `GetMaximum()`

**Returns:** `T_`


Returns the current maximum value.


### `SetMinimum(const T_ &value)`

**Returns:** `void`


Sets the minimum value that this slider reaches up to. If equal to maximum, progress will display 0.


### `if(valuemapping == internal::SliderValueMapping::ValueAndRange)`

**Returns:** ``



### `SetSmoothChangeSpeedRatio(changespeed)`

**Returns:** ``



### `SetSmoothChangeSpeed(unitspersec)`

**Returns:** ``



### `refreshvalue()`

**Returns:** ``



### `SetLimits(T_ min, T_ max, bool exchange = true)`

**Returns:** `void`


Sets minimum and maximum limits. If minimum is equal to maximum, progress will display 0. SliderBase will always keep the value between minimum and maximum. If maximum is less than minimum, this function will automatically exchange these values if exchange is set. If exchange is not set, they will both be set to T_{}, effectively locking progress at 0. Do not use this function if your type is not a regular numeric type


### `if(exchange && min > max)`

**Returns:** ``



### `swap(min, max)`

**Returns:** ``



### `if(valuemapping == internal::SliderValueMapping::ValueAndRange)`

**Returns:** ``



### `SetSmoothChangeSpeedRatio(changespeed)`

**Returns:** ``



### `SetSmoothChangeSpeed(unitspersec)`

**Returns:** ``



### `refreshvalue()`

**Returns:** ``



### `GetMinimum()`

**Returns:** `T_`


Returns the current minimum value.


### `set(value)`

**Returns:** ``


Sets the current value of the slider


### `SetRange(const T_ &value)`

**Returns:** `void`


Sets the range the container can display. This is used to show how much more the scroller can be scrolled.


### `if(valuemapping == internal::SliderValueMapping::ValueAndRange)`

**Returns:** ``



### `SetSmoothChangeSpeedRatio(changespeed)`

**Returns:** ``



### `SetSmoothChangeSpeed(unitspersec)`

**Returns:** ``



### `GetRange()`

**Returns:** `T_`


Returns the range the container can display. This is used to show how much more the scroller can be scrolled.


### `SetSmallChange(const T_ &value)`

**Returns:** `void`


Sets the amount of change on a small change action. This action could be click of arrow buttons, keyboard keys or mouse scroll.


### `GetSmallChange()`

**Returns:** `T_`


Returns the amount of change on a small change action. This action could be click of bar or keyboard keys (page up/down)


### `SetLargeChange(const T_ &value)`

**Returns:** `void`


Sets the amount of change on a large change action. This action could be click of bar or keyboard keys (page up/down).


### `GetLargeChange()`

**Returns:** `T_`


Returns the amount of change on a large change action. This action could be click of arrow buttons, keyboard keys or mouse scroll.


### `T_()`

**Returns:** `operator`


Returns the current value of the slider


### `get()`

**Returns:** `return`



### `Focus()`

**Returns:** `return`



### `DisableSmoothChange()`

**Returns:** `void`


Disables smooth change


### `SetSmoothChangeSpeed(0)`

**Returns:** ``



### `SetSmoothChangeSpeed(T_ value)`

**Returns:** `void`


Adjusts the smooth change speed. Given value is in values per second, default value is max and maybe sync to the maximum value.


### `SetSmoothChangeSpeedRatio(float value)`

**Returns:** `void`


Adjusts the smooth change speed. Given value is in values per second, default value is 1 and will be sync to the maximum value.


### `if(valuemapping == internal::SliderValueMapping::OneValue)`

**Returns:** ``



### `if(valuemapping == internal::SliderValueMapping::ValueAndRange)`

**Returns:** `else`



### `if(m == 0 || r == 1)`

**Returns:** ``



### `GetSmoothChangeSpeed()`

**Returns:** `T_`


Returns the smooth change speed. If smooth change is disabled, this value will be 0.


### `FloatToValue(changespeed, min, max)`

**Returns:** `return`



### `GetSmoothChangeSpeedRatio()`

**Returns:** `float`


Returns the smooth change in ratio to the maximum. 1 means full progress will be done in 1 second.


### `IsSmoothChangeEnabled()`

**Returns:** `bool`


Returns if the smooth change is enabled.


### `get()`

**Returns:** `T_`


This property controls the maximum value that the slider can have This property controls the minimum value that the slider can have This is used to show how much more the scroller can be scrolled. Controls the amount of change on a small change action. This action could be click of arrow buttons, keyboard keys or mouse scroll. Controls the amount of change on a large change action. This action could be click of bar or keyboard keys (page up/down). Returns the value in the box


### `set(const T_ &val)`

**Returns:** `void`


Changes the value in the box


### `setval(val)`

**Returns:** ``



### `actualmax()`

**Returns:** ``



### `actualmax()`

**Returns:** ``



### `setval(T_ val, bool instant = false)`

**Returns:** `bool`



### `if(value != val)`

**Returns:** ``



### `valuechanged(value)`

**Returns:** ``



### `refreshvalue(instant)`

**Returns:** ``



### `refreshvalue(bool instant = false)`

**Returns:** `virtual void`



### `refreshme(instant)`

**Returns:** ``



### `valuechanged(T_)`

**Returns:** `virtual void`



### `refreshme(bool instant = false)`

**Returns:** ``



### `refreshme(bool instant = false)`

**Returns:** ``



### `setupinteractivity()`

**Returns:** ``



### `setupinteractivity()`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::DragBarTag)`

**Returns:** ``



### `if(val > curval)`

**Returns:** ``



### `if(val < curval)`

**Returns:** `else`



### `if(tag == UI::ComponentTemplate::IncrementTag)`

**Returns:** `else`



### `if(tag == UI::ComponentTemplate::DecrementTag)`

**Returns:** `else`



### `if(tag == UI::ComponentTemplate::NoTag)`

**Returns:** ``



### `if(tag == UI::ComponentTemplate::DragTag)`

**Returns:** ``



### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `if(btn == Input::Mouse::Button::Left)`

**Returns:** ``



### `if(type == Input::Mouse::EventType::Scroll_Vert || type == Input::Mouse::EventType::Scroll_Hor)`

**Returns:** ``


