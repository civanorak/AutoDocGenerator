# Timer

&gt; Auto-generated documentation for the **Timer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Timer`

**Namespace:** `Gorgon`

Millisecond based timer. This class allows performance calculations. Constructing a new timer effectively starts it. However, explicit start might be used to exclude the time passed from the Timer construction or last Tick. All output functions are constant and do not modify the timer. Because of this, a Tick method might be necessary. The display functions will always report the time passed at the last tick. Pause function is not required and not included. Pause can be performed by issuing a Tick and using Start at the end of the pause. This class has a very low memory and processing overhead.  *Example:* @code // Counts the time passed in longoperation functions Timer timer; longoperation(); std::cout&lt;&lt;timer.Tick()&lt;&lt;std::endl; anotheroperation(); timer.Start(); longoperation(); timer.Tick().ShowDialog(); //Tick function can be cascaded @endcode

#### Methods

##### `Start(—)`

**Returns:** `void`

Default constructor. Starts the timer right away. If another start point is required, issuing a Start method before calling Tick will over ride previous starting point. @param  passed can be specified to start the timer from the given duration. Starts the timer from this instant. Any progress since the last Tick will be ignored. This allows pausing and starting the timer after construction.

##### `Get(—)`

**Returns:** `unsigned`

Counts the time since the last Start, Tick, Set, Reset or from the contruction of the timer and adds this duration to time passed. Use Get method to retrieve total ellapsed time. @return Returns back the timer itself. This allows cascaded calling. @see Timer Returns total time passed. This value updates only when Tick method is called. Therefore, to get a recent value, Tick method should be called prior to this method.

##### `Set(unsigned passed)`

**Returns:** `void`

Changes the passed time. Adjusts starting time of the timer.

##### `unsigned(—)`

**Returns:** `operator`

Returns total time passed. This value updates only when Tick method is called. Therefore, to get a recent value, Tick method should be called prior to this method.

##### `Reset(—)`

**Returns:** `void`

Resets the passed time. Adjusts starting time of the timer.

##### `Set(0)`

**Returns:** ``

