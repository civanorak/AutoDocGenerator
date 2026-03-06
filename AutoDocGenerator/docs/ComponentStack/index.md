# ComponentStack

&gt; Auto-generated documentation for the **ComponentStack** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ComponentStack`

**Namespace:** `Gorgon`

Automatic sizing will not be in effect Automatic sizing will be in effect Automatic sizing will be in effect and will resize to next size units. This is more effective horizontally. Autosizing will only make the widget grow Autosizing will only make the widget grow to next unit size. Autosizing will only make the widget shrink Autosizing will only make the widget shrink. It will be resized to a unit size.

#### Methods

##### `AddToStack(const ComponentTemplate &temp, bool reversed)`

**Returns:** `void`

Initializes a component stack with the given size. Generators are used to create widgets for the placeholders. If a function is empty or returns nullptr, neither a substack nor a widget will be placed there. Initiates a component stack with default size Destructor Adds the given component to the top of the stack. This function will be called to add all components in the given template

##### `ReplaceCondition(ComponentCondition from, ComponentCondition to, bool transition = true)`

**Returns:** `void`

Replaces a condition with another one

##### `AddCondition(ComponentCondition condition, bool transition = true)`

**Returns:** `void`

Adds a condition and its associated components to the stack

##### `ReplaceCondition(ComponentCondition::Always, condition, transition)`

**Returns:** ``

##### `RemoveCondition(ComponentCondition condition, bool transition = true)`

**Returns:** `void`

Removes a condition and its associated components

##### `ReplaceCondition(condition, ComponentCondition::Always, transition)`

**Returns:** ``

##### `HasCondition(ComponentCondition condition)`

**Returns:** `bool`

Returns if the given condition is in effect.

##### `FinalizeTransitions(—)`

**Returns:** `void`

Finalizes on-going transitions immediately

##### `SetData(ComponentTemplate::DataEffect effect, const std::string &text)`

**Returns:** `void`

Sets the data for a specific data effect. This value will be cached by the stack for condition changes. This variant supports string based data.

##### `SetData(ComponentTemplate::DataEffect effect, const Graphics::Drawable &image)`

**Returns:** `void`

Sets the data for a specific data effect. This value will be cached by the stack for condition changes. This variant supports image based data. Ownership of the image stays with the caller.

##### `GetTextData(ComponentTemplate::DataEffect effect)`

**Returns:** `std::string`

Returns the text data. If data is not set, this will return empty string.

##### `RemoveData(ComponentTemplate::DataEffect effect)`

**Returns:** `void`

Returns the image data. If data is not set, this will return nullptr. Removes the data associated with data effect. This will remove all data variants together.

##### `SetValue(float first)`

**Returns:** `void`

Sets the value for this stack. Value of the stack can affect various properties of components. This will set the individual channels separately. Values should be between 0 and 1.

##### `SetValue(float first, float second)`

**Returns:** `void`

Sets the value for this stack. Value of the stack can affect various properties of components. This will set the individual channels separately. Values should be between 0 and 1.

##### `SetValue(float first, float second, float third)`

**Returns:** `void`

Sets the value for this stack. Value of the stack can affect various properties of components. This will set the individual channels separately. Values should be between 0 and 1.

##### `SetValue(float first, float second, float third, float fourth, bool instant = false)`

**Returns:** `void`

Sets the value for this stack. Value of the stack can affect various properties of components. This will set the individual channels separately. Values should be between 0 and 1.

##### `SetValue(Geometry::Pointf pos)`

**Returns:** `void`

Sets the value for the stack using a point in coordinate system

##### `SetValue(Geometry::Point3D pos)`

**Returns:** `void`

Sets the value for the stack using a point in coordinate system

##### `SetValue(Graphics::RGBAf color)`

**Returns:** `void`

Sets the value for the stack using a color

##### `SetValue(Graphics::RGBA color)`

**Returns:** `void`

Sets the value for the stack using a color

##### `GetValue(—)`

**Returns:** `std::array<float, 4>`

Returns the value of the stack

##### `GetTargetValue(—)`

**Returns:** `std::array<float, 4>`

Returns the value of the stack

##### `SetValueTransitionSpeed(std::array<float, 4> val)`

**Returns:** `void`

Changes the value transition speed. A speed of 0 will disable smooth transition. The unit is values per second

##### `ReturnTransitionalValue(—)`

**Returns:** `void`

Whether GetValue returns the current transitional value, this will also enable value event to be called every time transitional value is updated

##### `ReturnTargetValue(—)`

**Returns:** `void`

Whether GetValue returns the target value. This is the default mode.

##### `SetRepeat(ComponentTemplate::RepeatMode mode, std::vector<std::array<float, 4>> data)`

**Returns:** `void`

Sets the function that will be called whenever the value is changed Sets the function that will be used to convert a value to a string. The handler will receive the value channel, data effect that is causing the translation and the value that needs to be transformed. Sets the function that will be used perform Ceil operation in unit sizes. If not set, unit width of the template will be used. Sets the repeat with the given mode to the given vector. Use std::move(data) for efficient transfer

##### `checkrepeatupdate(mode)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, float first)`

**Returns:** `void`

Adds a new repeating point to the given mode. Empty values will be set as 0.

##### `AddRepeat(mode, first, 0, 0, 0)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, float first, float second)`

**Returns:** `void`

Adds a new repeating point to the given mode. Empty values will be set as 0.

##### `AddRepeat(mode, first, second, 0, 0)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, float first, float second, float third)`

**Returns:** `void`

Adds a new repeating point to the given mode. Empty values will be set as 0.

##### `AddRepeat(mode, first, second, third, 0)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, float first, float second, float third, float fourth)`

**Returns:** `void`

Adds a new repeating point to the given mode.

##### `checkrepeatupdate(mode)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, Geometry::Pointf pos)`

**Returns:** `void`

Adds a new repeating point to the given mode. Empty values will be set as 0.

##### `AddRepeat(mode, pos.X, pos.Y, 0, 0)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, Geometry::Point3D pos)`

**Returns:** `void`

Adds a new repeating point to the given mode. Empty values will be set as 0.

##### `AddRepeat(mode, pos.X, pos.Y, pos.Z, 0)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, Graphics::RGBAf color)`

**Returns:** `void`

Adds a new repeating point to the given mode.

##### `AddRepeat(mode, color.R, color.G, color.B, color.A)`

**Returns:** ``

##### `AddRepeat(ComponentTemplate::RepeatMode mode, Graphics::RGBA color)`

**Returns:** `void`

Adds a new repeating point to the given mode.

##### `RemoveRepeats(ComponentTemplate::RepeatMode mode)`

**Returns:** `void`

Removes all repeat points from the given mode. Call RemoveAllConditions along with this function if you are using conditions for repeats.

##### `checkrepeatupdate(mode)`

**Returns:** ``

##### `SetConditionOf(ComponentTemplate::RepeatMode mode, int index, ComponentCondition condition)`

**Returns:** `void`

Sets the condition of a specific repeat index. Nothing will happen if index is out of bounds or condition does not exist. Setting condition to always will effectively remove the condition.

##### `if(repeatconditions[mode][index] != condition)`

**Returns:** ``

##### `checkrepeatupdate(mode)`

**Returns:** ``

##### `RemoveAllConditionsOf(ComponentTemplate::RepeatMode mode)`

**Returns:** `void`

Removes all conditions for a repeat mode.

##### `checkrepeatupdate(mode)`

**Returns:** ``

##### `Update(—)`

**Returns:** ``

@} Notifies the stack about a size change

##### `if(updaterequired)`

**Returns:** ``

##### `Update(bool immediate)`

**Returns:** `void`

Returns the template used by this stack Returns the template used by the component with given tag Returns the widget associated with the tag. If such widget does not exists nullptr will be returned instead. Updates the layout of the component stack Updates the layout of the component stack

##### `ResetAnimation(—)`

**Returns:** `void`

##### `IsDisabled(—)`

**Returns:** `bool`

Returns if this component stack is disabled. Both disabling and enabling animations are counted as disabled.

##### `SetEMSize(int value)`

**Returns:** `void`

Changes the default emsize of 10. This value can be overridden.

##### `SetUnitSize(int unitsize, int spacing)`

**Returns:** `void`

Changes the unitsize. Default value is obtained from the template.

##### `HandleMouse(Input::Mouse::Button accepted = Input::Mouse::Button::All)`

**Returns:** `void`

This function instructs stack to handle mouse to automatically change hover/down states, unless disabled state is active. Propagates to substacks.

##### `TagHasSubstack(ComponentTemplate::Tag tag)`

**Returns:** `bool`

Returns whether the component marked with the tag has a substack. If multiple components are marked to have substack, only the first one is considered. If the tag does not exist this function will return false.

##### `CoordinateToValue(ComponentTemplate::Tag tag, Geometry::Point location, bool relative = false)`

**Returns:** `std::array<float, 4>`

Returns the substack that the component with the given tag has. If it does not exit, this function will throw. Use TagHasSubStack to ensure the tag has a substack. Translates the given coordinates back to values using value scaling and channel mapping. Only works if the value affects the component location or size. If component with the specified tag does not exist, this function will simply return {0, 0, 0, 0}. If relative is set, the calculation will not take starting location into account and will return relative change in value when relative change in location happens.

##### `TranslateCoordinates(ComponentTemplate::Tag tag, Geometry::Point location)`

**Returns:** `Geometry::Point`

Translates the given coordinates to component space in pixels.

##### `TranslateCoordinates(int ind, Geometry::Point location)`

**Returns:** `Geometry::Point`

Translates the given coordinates to component space in pixels.

##### `TransformCoordinates(ComponentTemplate::Tag tag, Geometry::Point location)`

**Returns:** `Geometry::Pointf`

Translates the given coordinates to component space from 0 to 1.

##### `TransformCoordinates(int ind, Geometry::Point location)`

**Returns:** `Geometry::Pointf`

Translates the given coordinates to component space from 0 to 1.

##### `IndexOfTag(ComponentTemplate::Tag tag)`

**Returns:** `int`

Returns the index of the component with the specified tag. This function may cause update thus may take time to execute. If tag not found, this will return -1.

##### `TagBounds(ComponentTemplate::Tag tag)`

**Returns:** `Geometry::Bounds`

Returns the boundaries of the component marked with the given tag. This function may cause update thus may take time to execute. The bounds are within the parent. If tag does not exit, bounds of the entire stack will be returned.

##### `HasLayer(int ind)`

**Returns:** `bool`

Returns if the component at the given index has a layer.

##### `BoundsOf(int ind)`

**Returns:** `Geometry::Bounds`

Returns the layer of the given component index. If the item does not have a layer, this function will create a new one for it. In the worst case, this function will return the object itself as a layer. Layer is probably a graphics layer, you may use RTTI to query layer type. Returns the boundaries of the component with the given index. The bounds are from the top level.

##### `ComponentAt(Geometry::Point location)`

**Returns:** `int`

Returns the index of the component at the given location.

##### `ComponentAt(location, b)`

**Returns:** `return`

##### `ComponentAt(Geometry::Point location, Geometry::Bounds &bounds)`

**Returns:** `int`

Returns the index of the component at the given location while returning the bounds of the component.

##### `ComponentExists(int ind)`

**Returns:** `bool`

Returns if a component at ind exists. If ind is negative or out of range, this function simply returns false.

##### `SetTagLocation(ComponentTemplate::Tag tag, Geometry::Point location)`

**Returns:** `void`

Returns the template at the given index. If the index does not exists, this function may crash. Use ComponentExists function to check if it is safe to use the index. Set a fixed location for a tagged component

##### `Update(—)`

**Returns:** ``

##### `GetTagLocation(ComponentTemplate::Tag tag)`

**Returns:** `Geometry::Point`

##### `RemoveTagLocation(ComponentTemplate::Tag tag)`

**Returns:** `void`

Removes the fixed location for a set tagged component

##### `SetTagSize(ComponentTemplate::Tag tag, Geometry::Size size)`

**Returns:** `void`

Set a fixed size for a tagged component

##### `Update(—)`

**Returns:** ``

##### `GetTagSize(ComponentTemplate::Tag tag)`

**Returns:** `Geometry::Size`

##### `RemoveTagSize(ComponentTemplate::Tag tag)`

**Returns:** `void`

Removes the fixed size for a set tagged component

##### `Update(—)`

**Returns:** ``

##### `EnableTagWrap(ComponentTemplate::Tag tag)`

**Returns:** `void`

Enables text wrapping on a specific tag, default is enabled.

##### `Update(—)`

**Returns:** ``

##### `DisableTagWrap(ComponentTemplate::Tag tag)`

**Returns:** `void`

Disables text wrapping on a specific tag, default is enabled.

##### `Update(—)`

**Returns:** ``

##### `SetAutosize(Autosize horizontal, Autosize vertical)`

**Returns:** `void`

Sets whether the ComponentStack should be autosized. Autosize uses the set size for text width.

##### `Update(—)`

**Returns:** ``

##### `Refresh(—)`

**Returns:** `void`

##### `update(—)`

**Returns:** ``

##### `GetAutosize(—)`

**Returns:** `std::pair<Autosize, Autosize>`

Returns the autosize mode of the stack

##### `SetWidget(ComponentTemplate::Tag tag, Widget *wgt)`

**Returns:** `void`

Adds or replaces a generator for a specific tag Sets the widget for a given tag. If same tag exists multiple times, the last one will get the widget

##### `RemoveGenerator(ComponentTemplate::Tag tag)`

**Returns:** `void`

Removes the generator for a specific tag

##### `Update(—)`

**Returns:** ``

##### `RemoveFrameEvent(—)`

**Returns:** `void`

Sets a function to be called before update check Sets a function to be called before every update Sets a function to be called after every update before rendering Sets a function to be called after every render Removes the function that will be called before update check

##### `RemoveBeforeUpdateEvent(—)`

**Returns:** `void`

Removes the function that will be called before every update

##### `RemoveUpdateEvent(—)`

**Returns:** `void`

Removes the function that will be called after every update before rendering

##### `RemoveRenderEvent(—)`

**Returns:** `void`

Removes the function that will be called after every render

##### `for(auto stack : substacks)`

**Returns:** ``

@} Sets the mouse down event. If HandleMouse function is called, this function will first perform mouse event transition, then it will call this handler.

##### `for(auto stack : substacks)`

**Returns:** ``

Sets the mouse up event. If HandleMouse function is called, this function will first perform mouse event transition, then it will call this handler. This event will be called even if mouse down is not handled.

##### `for(auto stack : substacks)`

**Returns:** ``

Sets the mouse down event. If HandleMouse function is called, this function will first perform mouse event transition, then it will call this handler.

##### `move_fn(ComponentTemplate::NoTag, location)`

**Returns:** ``

Sets the mouse mvoe event. If HandleMouse function is called, this function will first perform mouse event transition, then it will call this handler. If this event is not handled mouse move event of the layer will not be handled too.

##### `for(auto stack : substacks)`

**Returns:** ``

##### `for(auto stack : substacks)`

**Returns:** ``

Sets the mouse over event that is fired when the mouse moves over the component stack or a substack. it will not be fired for mouse moving over a specific component. If HandleMouse function is called, this function will first perform mouse event transition, then it will call this handler.

##### `for(auto stack : substacks)`

**Returns:** ``

Sets the mouse out event that is fired when the mouse moves over the component stack or a substack. it will not be fired for mouse moving over a specific component. If HandleMouse function is called, this function will first perform mouse event transition, then it will call this handler. This event will be called even if mouse over is not handled.

##### `for(auto stack : substacks)`

**Returns:** ``

Sets mouse enter and leave events to be called automatically.

##### `if(stack == -1)`

**Returns:** ``

Sets the handler for scroll (HScroll or VScroll), zoom and rotate events. All these events depend on specific hardware and may not be available. @} If any text is rendered using AdvancedPrinter, this function will return regions supplied by the renderer. Only one set of regions will be kept; therefore, there should only be one active component that has AdvancedPrinter. This event is fired when condition is changed. returns the element at the stack with the given stack offset. If stack is -1, this function will return top of the stack. 0 is at the bottom of the stack

##### `update(—)`

**Returns:** `void`

Return the component at the given index with the requested condition. Returns top of stack if condition does not exist. Calculates the position results from the anchoring the given component to the area determined by the given size and margin. Offset is used to move away from the anchor and may result reversing of direction. Calculates the position results from the anchoring the given component to another component starts the update chain

##### `update(Component &parent, const std::array<float, 4> &value, int ind, int textwidth = -1, bool autosize = false)`

**Returns:** `void`

updates a specific container component

##### `render(Component &component, Graphics::Layer &parentlayer, Geometry::Point offset, const std::array<float, 4> &value, Graphics::RGBAf color = 1.f, int ind = -1)`

**Returns:** `void`

renders the given component, rendering will use parent layer if the component does not have its own layer. Index is for repeated components, it is the index of the repeat to be rendered. Unlike Layer::Render function, this function does not run every frame.

##### `grow(—)`

**Returns:** `void`

grows the size of the stack

##### `getemsize(const Component &comp)`

**Returns:** `int`

returns the size of the emdash

##### `getbaseline(const Component &comp)`

**Returns:** `int`

returns the baseline point of the component

##### `gettextheight(const Component &comp)`

**Returns:** `int`

returns the height of the component

##### `calculatevalue(int channel, const Component &comp)`

**Returns:** `float`

Calculates the value of the given channel for the given component. Uses stored value

##### `calculatevalue(const std::array<float, 4> &data, int channel, const Component &comp)`

**Returns:** `float`

Calculates the value of the given channel for the given component. Uses the supplied value.

##### `checkrepeatupdate(ComponentTemplate::RepeatMode mode)`

**Returns:** `void`

Checks if a specific type of repeating component requires update

##### `addcondition(ComponentCondition from, ComponentCondition to, ComponentCondition hint = ComponentCondition::None)`

**Returns:** `bool`

Adds the given condition. To should contain the final condition even if there is no transition. If there is no transition, from should be None and hint should contain previous state if it exists.

##### `removecondition(ComponentCondition from, ComponentCondition to)`

**Returns:** `bool`

Erases the given condition. To should contain the final condition to be removed. Caller should erase transition


---

## Enums

### `Stage`

**Namespace:** `Gorgon`


### `Autosize`

**Namespace:** `Gorgon`


---

## Functions

### `r1000(float v)`

**Returns:** `static float`



### `IsIn(Anchor left, Anchor right)`

**Returns:** `bool`



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `Add(mouse)`

**Returns:** ``



### `Add(base)`

**Returns:** ``



### `addcondition(ComponentCondition::None, ComponentCondition::Always)`

**Returns:** ``



### `if(handlingmouse)`

**Returns:** ``



### `AddCondition(ComponentCondition::Hover)`

**Returns:** ``



### `mouseenter()`

**Returns:** ``



### `over_fn(ComponentTemplate::NoTag)`

**Returns:** ``



### `if(handlingmouse)`

**Returns:** ``



### `mouseleave()`

**Returns:** ``



### `out_fn(ComponentTemplate::NoTag)`

**Returns:** ``



### `if(handlingmouse)`

**Returns:** ``



### `if(btn && mousebuttonaccepted)`

**Returns:** ``



### `AddCondition(ComponentCondition::Down)`

**Returns:** ``



### `down_fn(ComponentTemplate::NoTag, location, btn)`

**Returns:** ``



### `if(handlingmouse)`

**Returns:** ``



### `if(btn && mousebuttonaccepted)`

**Returns:** ``



### `click_fn(ComponentTemplate::NoTag, location, btn)`

**Returns:** ``



### `up_fn(ComponentTemplate::NoTag, location, btn)`

**Returns:** ``



### `Resize(size)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], false)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], false)`

**Returns:** ``



### `for(auto &p : storage)`

**Returns:** ``



### `if(si == stackcapacity)`

**Returns:** ``



### `grow()`

**Returns:** ``



### `if(fn)`

**Returns:** ``



### `if(w)`

**Returns:** ``



### `if(from != ComponentCondition::None)`

**Returns:** ``



### `if(to == ComponentCondition::Disabled)`

**Returns:** ``



### `for(auto iter = conditions.begin()`

**Returns:** ``



### `RemoveCondition(c, false)`

**Returns:** ``



### `if(from == ComponentCondition::None)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], false)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], false)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], true)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], false)`

**Returns:** ``



### `for(int i=0; i<temp.GetCount()`

**Returns:** ``



### `AddToStack(temp[i], true)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `ConditionChanged()`

**Returns:** ``



### `if(erased)`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `for(int j=stacksizes[i]-1; j>=0; j--)`

**Returns:** ``



### `if(remove)`

**Returns:** ``



### `if(j == stacksizes[i]-1)`

**Returns:** ``



### `for(int k=j; k<stacksizes[i]-1; k++)`

**Returns:** ``



### `if(to == ComponentCondition::Disabled)`

**Returns:** ``



### `ReplaceCondition(ComponentCondition::Disabled, d)`

**Returns:** ``



### `if(from == ComponentCondition::None)`

**Returns:** ``



### `for(const auto &t : transitions)`

**Returns:** ``



### `if(t.first.second == to)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `removecondition(to, from)`

**Returns:** ``



### `addcondition(from, to)`

**Returns:** ``



### `removecondition(to, from)`

**Returns:** ``



### `addcondition(ComponentCondition::None, to)`

**Returns:** ``



### `for(const auto &t : transitions)`

**Returns:** ``



### `if(t.first.second == from)`

**Returns:** ``



### `addcondition(t.first.first, to)`

**Returns:** ``



### `addcondition(ComponentCondition::Always, to)`

**Returns:** ``



### `addcondition(ComponentCondition::None, to)`

**Returns:** ``



### `removecondition(ComponentCondition::None, from)`

**Returns:** ``



### `addcondition(from, to)`

**Returns:** ``



### `if(from != ComponentCondition::Always)`

**Returns:** ``



### `removecondition(ComponentCondition::None, from)`

**Returns:** ``



### `removecondition(ComponentCondition::Always, from)`

**Returns:** ``



### `if(to != ComponentCondition::Always)`

**Returns:** ``



### `addcondition(ComponentCondition::Always, to)`

**Returns:** ``



### `for(auto iter = transitions.begin()`

**Returns:** ``



### `removecondition(c.first.first, c.first.second)`

**Returns:** ``



### `addcondition(ComponentCondition::None, future_transitions[c.first.second], c.first.first)`

**Returns:** ``



### `addcondition(ComponentCondition::None, c.first.second, c.first.first)`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `if(stacksizes[i] > 0)`

**Returns:** ``



### `if(!wasset)`

**Returns:** ``



### `if(updatereq)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `if(stacksizes[i] > 0)`

**Returns:** ``



### `if(!wasset)`

**Returns:** ``



### `if(updatereq)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `if(stacksizes[i] > 0)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `for(int i=0; i<4; i++)`

**Returns:** ``



### `value_fn()`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `if(stacksizes[i] > 0)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `if(immediate)`

**Returns:** ``



### `update()`

**Returns:** ``



### `frame_fn()`

**Returns:** ``



### `for(auto iter = transitions.begin()`

**Returns:** ``



### `if(dur <= delta)`

**Returns:** ``



### `removecondition(c.first.first, c.first.second)`

**Returns:** ``



### `addcondition(ComponentCondition::None, c.first.second, c.first.first)`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `for(int i=0; i<4; i++)`

**Returns:** ``



### `ReplaceCondition(it.first, it.second)`

**Returns:** ``



### `if(changed)`

**Returns:** ``



### `value_fn()`

**Returns:** ``



### `update()`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `update()`

**Returns:** ``



### `update()`

**Returns:** ``



### `update()`

**Returns:** ``



### `while(cur->parent != -1)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `TranslateCoordinates(ind, location)`

**Returns:** `return`



### `TransformCoordinates(ind, location)`

**Returns:** `return`



### `update()`

**Returns:** ``



### `for(int i=0; i<cont.GetCount()`

**Returns:** ``



### `if(stacksizes[cont[i]])`

**Returns:** ``



### `other_fn(ComponentTemplate::NoTag, Input::Mouse::EventType::Scroll_Vert, location, amount)`

**Returns:** `return`



### `other_fn(ComponentTemplate::NoTag, Input::Mouse::EventType::Scroll_Hor, location, amount)`

**Returns:** `return`



### `other_fn(ComponentTemplate::NoTag, Input::Mouse::EventType::Rotate, location, amount)`

**Returns:** `return`



### `other_fn(ComponentTemplate::NoTag, Input::Mouse::EventType::Zoom, location, amount)`

**Returns:** `return`



### `for(auto stack : substacks)`

**Returns:** ``



### `if(vs == ComponentTemplate::UseTransition)`

**Returns:** ``



### `if(!comp.reversed)`

**Returns:** ``



### `if(valueordering[channel] == 0)`

**Returns:** ``



### `while(i <= ComponentTemplate::ValueSourceMaxPower)`

**Returns:** ``



### `if(!c)`

**Returns:** ``



### `switch(src)`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `for(int i=stacksizes[ind]-1; i>=0; i--)`

**Returns:** ``



### `free(data)`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `switch(pa)`

**Returns:** ``


Determines the location of the component in relation to its parent.


### `switch(ca)`

**Returns:** ``



### `switch(pa)`

**Returns:** ``



### `switch(ca)`

**Returns:** ``



### `beforeupdate_fn()`

**Returns:** ``



### `for(auto &s : storage)`

**Returns:** ``



### `if(stacksizes[0])`

**Returns:** ``



### `for(auto &r : repeated)`

**Returns:** ``



### `for(int i=0; i<indices; i++)`

**Returns:** ``



### `if(stacksizes[i] > 0)`

**Returns:** ``



### `if(!ceilfn)`

**Returns:** ``



### `if(autosize.first != Autosize::None || autosize.second != Autosize::None)`

**Returns:** ``



### `if(rootsize.Width > 0)`

**Returns:** ``



### `switch(autosize.first)`

**Returns:** ``



### `if(sz.Width > rootsize.Width)`

**Returns:** ``



### `if(sz.Width < rootsize.Width)`

**Returns:** ``



### `if(sz.Width > rootsize.Width)`

**Returns:** ``



### `if(sz.Width < rootsize.Width)`

**Returns:** ``



### `if(rootsize.Height > 0)`

**Returns:** ``



### `switch(autosize.second)`

**Returns:** ``



### `if(sz.Height > rootsize.Height)`

**Returns:** ``



### `if(sz.Height < rootsize.Height)`

**Returns:** ``



### `if(sz.Height > rootsize.Height)`

**Returns:** ``



### `if(sz.Height < rootsize.Height)`

**Returns:** ``



### `update_fn()`

**Returns:** ``



### `if(stacksizes[0])`

**Returns:** ``



### `render_fn()`

**Returns:** ``



### `calculatemargin(int l, int r)`

**Returns:** `int`



### `for(auto it=substacks.begin()`

**Returns:** ``



### `for(auto &t : temp)`

**Returns:** ``



### `if(fn)`

**Returns:** ``



### `if(w)`

**Returns:** ``



### `for(int i=0; i<stacksizes[ind]; i++)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `for(auto it=substacks.begin()`

**Returns:** ``



### `for(auto &t : temp)`

**Returns:** ``



### `if(w)`

**Returns:** ``



### `for(int i=0; i<stacksizes[ind]; i++)`

**Returns:** ``



### `Update()`

**Returns:** ``



### `for(int i=0; i<cont.GetCount()`

**Returns:** ``



### `while(j < jtarget)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &temp, const std::array<float, 4> &val, int emsize, int)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &temp, const std::array<float, 4> &val, int emsize, int index)`

**Returns:** ``



### `if(!ishor)`

**Returns:** `else`



### `if(xfree)`

**Returns:** ``



### `if(yfree)`

**Returns:** ``



### `if(!xfree)`

**Returns:** ``



### `if(stage == middle)`

**Returns:** ``



### `if(!yfree)`

**Returns:** ``



### `if(stage == middle)`

**Returns:** ``



### `if(widthch == -1)`

**Returns:** ``



### `if(heightch == -1)`

**Returns:** ``



### `update(comp, val, index, tw, true)`

**Returns:** ``



### `if(rectangular)`

**Returns:** ``



### `if(st.primary)`

**Returns:** `else`



### `if(valuetotext && d >= ComponentTemplate::AutoStart && d <= ComponentTemplate::AutoEnd)`

**Returns:** `else`



### `if(text != "")`

**Returns:** ``



### `if(rectangular)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &temp, const std::array<float, 4> &val, int emsize, int)`

**Returns:** ``



### `if(ishor)`

**Returns:** ``



### `if(!ishor)`

**Returns:** `else`



### `if(!xfree)`

**Returns:** ``



### `if(stage == middle)`

**Returns:** ``



### `if(!yfree)`

**Returns:** ``



### `if(stage == middle)`

**Returns:** ``



### `if(anch)`

**Returns:** ``



### `if(ishor)`

**Returns:** ``



### `switch(panch)`

**Returns:** ``



### `if(xch == -1)`

**Returns:** ``



### `if(ych == -1)`

**Returns:** ``



### `if(anch)`

**Returns:** `else`



### `anchortoparent(parent, comp, temp, offset, margin, parent.innersize)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &temp, const std::array<float, 4> &, int, int ind)`

**Returns:** ``



### `if(ishor)`

**Returns:** ``



### `if(comp.anchorotherside)`

**Returns:** ``



### `if(comp.anchorotherside)`

**Returns:** ``



### `if(ishor)`

**Returns:** ``



### `if(startmost)`

**Returns:** ``



### `if(endmost)`

**Returns:** ``



### `if(endmost)`

**Returns:** `else`



### `if(startmost)`

**Returns:** ``



### `if(endmost)`

**Returns:** ``



### `if(endmost)`

**Returns:** `else`



### `if(parent.size.Width == 0)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &, const std::array<float, 4> &, int, int)`

**Returns:** ``



### `if(parent.size.Height == 0)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &, const std::array<float, 4> &, int, int)`

**Returns:** ``



### `if(h < b)`

**Returns:** ``



### `forallcomponents([&](Component &comp, const ComponentTemplate &temp, const std::array<float, 4> &val, int, int index)`

**Returns:** ``



### `update(comp, val, index)`

**Returns:** ``



### `if(st.layer)`

**Returns:** ``



### `if(st.primary)`

**Returns:** ``



### `for(int i=0; i<cont.GetCount()`

**Returns:** ``



### `if(stacksizes[cont[i]])`

**Returns:** ``



### `render(compparent, *target, offset, val, color)`

**Returns:** ``



### `render(repeated[&temp][ind], *target, offset, val, color, ind)`

**Returns:** ``



### `render(r, *target, offset, val, color, index++)`

**Returns:** ``



### `if(st.secondary)`

**Returns:** ``



### `if(img)`

**Returns:** ``



### `for(auto &r : regions)`

**Returns:** ``



### `if(rectangular)`

**Returns:** ``


