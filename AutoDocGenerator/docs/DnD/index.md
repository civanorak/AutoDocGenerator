# DnD

&gt; Auto-generated documentation for the **DnD** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `DropTarget`

**Namespace:** `Gorgon`

#### Methods

##### `Drop(Geometry::Point location)`

**Returns:** `friend void`

##### `CancelDrag(—)`

**Returns:** `friend void`

##### `ResetHitCheck(—)`

**Returns:** `void`

@name Event handling @{ Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Sets hit check function. When set, events only occur if hit check returns true. Events follow hit check in a sequential manner, thus, if a handler is called, this means hit check has already succeeded in the current layout. This variant accepts class member function. Removes hit check handler, default action for hit check is to return true.

##### `ResetOver(—)`

**Returns:** `void`

Sets over function. If set, called whenever an object is dragged over this layer. If event handler returns true, source will receive over event as well. Sets over function. If set, called whenever an object is dragged over this layer. If event handler returns true, source will receive over event as well. Sets over function. If set, called whenever an object is dragged over this layer. If event handler returns true, source will receive over event as well. This variant accepts class member function. Sets over function. If set, called whenever an object is dragged over this layer. If event handler returns true, source will receive over event as well. This variant accepts class member function. Sets over function. If set, called whenever an object is dragged over this layer. If event handler returns true, source will receive over event as well. This variant accepts class member function. Sets over function. If set, called whenever an object is dragged over this layer. If event handler returns true, source will receive over event as well. This variant accepts class member function. Removes over handler, default action for over is to return true.

##### `ResetOut(—)`

**Returns:** `void`

Sets out function. If set, called whenever an object is dragged out of this layer. This event is called even if over returns false. Sets out function. If set, called whenever an object is dragged out of this layer. This event is called even if over returns false. Sets out function. If set, called whenever an object is dragged out of this layer. This event is called even if over returns false. This variant accepts class member function. Sets out function. If set, called whenever an object is dragged out of this layer. This event is called even if over returns false. This variant accepts class member function. Sets out function. If set, called whenever an object is dragged out of this layer. This event is called even if over returns false. This variant accepts class member function. Sets out function. If set, called whenever an object is dragged out of this layer. This event is called even if over returns false. This variant accepts class member function. Removes out handler.

##### `ResetMove(—)`

**Returns:** `void`

Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Sets move function. If set, called repeatedly as long as the object is over this layer. Returning false from this event's handler will cause drag operation to move out of this layer. This variant accepts class member function. Removes move handler, default is to continue the drag operation.

##### `ResetDrop(—)`

**Returns:** `void`

Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Sets drop function. If set, called whenever an object is dropped to this layer. Returning false from this event's handler will cause drag operation to be canceled. This variant accepts class member function. Removes drop handler, default is to cancel the drag operation.

##### `ResetCancel(—)`

**Returns:** `void`

Sets cancel function. If set, called whenever the DnD event that is accepted to be over this layer is canceled. Sets cancel function. If set, called whenever the DnD event that is accepted to be over this layer is canceled. Sets cancel function. If set, called whenever the DnD event that is accepted to be over this layer is canceled. This variant accepts class member function. Sets cancel function. If set, called whenever the DnD event that is accepted to be over this layer is canceled. This variant accepts class member function. Sets cancel function. If set, called whenever the DnD event that is accepted to be over this layer is canceled. This variant accepts class member function. Sets cancel function. If set, called whenever the DnD event that is accepted to be over this layer is canceled. This variant accepts class member function. Removes cancel handler.


### `DragSource`

**Namespace:** `Gorgon`

@} Propagates a mouse event. Some events will be called directly.

#### Methods

##### `Drop(Geometry::Point location)`

**Returns:** `friend void`

##### `CancelDrag(—)`

**Returns:** `friend void`

##### `ResetOver(—)`

**Returns:** `void`

@name Event handling @{ Sets over function. If set, called whenever an object is dragged over to a target and the target accepts over event. Sets over function. If set, called whenever an object is dragged over to a target and the target accepts over event. Sets over function. If set, called whenever an object is dragged over to a target and the target accepts over event. This variant accepts class member function. Sets over function. If set, called whenever an object is dragged over to a target and the target accepts over event. This variant accepts class member function. Sets over function. If set, called whenever an object is dragged over to a target and the target accepts over event. This variant accepts class member function. Sets over function. If set, called whenever an object is dragged over to a target and the target accepts over event. This variant accepts class member function. Removes over handler, default action for over is to return true.

##### `ResetOut(—)`

**Returns:** `void`

Sets out function. If set, called whenever an object is dragged out of the layer that accepted over event. Sets out function. If set, called whenever an object is dragged out of the layer that accepted over event. Sets out function. If set, called whenever an object is dragged out of the layer that accepted over event. This variant accepts class member function. Sets out function. If set, called whenever an object is dragged out of the layer that accepted over event. This variant accepts class member function. Sets out function. If set, called whenever an object is dragged out of the layer that accepted over event. This variant accepts class member function. Sets out function. If set, called whenever an object is dragged out of the layer that accepted over event. This variant accepts class member function. Removes out handler.

##### `ResetMove(—)`

**Returns:** `void`

Sets move handler. If set, called continuously until the drag operation is complete. Sets move handler. If set, called continuously until the drag operation is complete. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. Sets move handler. If set, called continuously until the drag operation is complete. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Sets move handler. If set, called continuously until the drag operation is complete. This variant accepts class member function. Removes move handler, default is to continue the drag operation.

##### `ResetAccept(—)`

**Returns:** `void`

Sets accept function. If set, called whenever drag operation is accepted. Sets accept function. If set, called whenever drag operation is accepted. Sets accept function. If set, called whenever drag operation is accepted. This variant accepts class member function. Sets accept function. If set, called whenever drag operation is accepted. This variant accepts class member function. Sets accept function. If set, called whenever drag operation is accepted. This variant accepts class member function. Sets accept function. If set, called whenever drag operation is accepted. This variant accepts class member function. Removes accept handler.

##### `ResetCancel(—)`

**Returns:** `void`

Sets accept function. If set, called whenever drag operation is canceled. Sets accept function. If set, called whenever drag operation is canceled. Sets accept function. If set, called whenever drag operation is canceled. This variant accepts class member function. Sets accept function. If set, called whenever drag operation is canceled. This variant accepts class member function. Sets accept function. If set, called whenever drag operation is canceled. This variant accepts class member function. Sets accept function. If set, called whenever drag operation is canceled. This variant accepts class member function. Removes cancel handler.


### `DragInfo`

**Namespace:** `Gorgon`

@}

#### Methods

##### `DragInfo(—)`

**Returns:** ``

Constructor, requires the source for drag operation Constructor, requires the source for drag operation

##### `AddTextData(const std::string &text)`

**Returns:** `void`

Adds text data to this info object

##### `AddFileData(const std::string &text)`

**Returns:** `void`

Adds file data to this info object

##### `AddData(ExchangeData &data)`

**Returns:** `void`

Adds data to this info object, ownership of the data is not transfered

##### `AssumeData(ExchangeData &data)`

**Returns:** `void`

Adds data to this info object, ownership of the data is transfered

##### `HasData(Resource::GID::Type type)`

**Returns:** `bool`

Check whether this drag info has the given data

##### `DataReady(—)`

**Returns:** `void`

Marks drag data as ready.

##### `IsDataReady(—)`

**Returns:** `bool`

Check wheather the drag data is ready

##### `begin(—)`

**Returns:** `Containers::Collection<ExchangeData>::Iterator`

For range based iteration

##### `end(—)`

**Returns:** `Containers::Collection<ExchangeData>::Iterator`

For range based iteration

##### `GetSize(—)`

**Returns:** `int`

Returns the data associated with the given type, throws runtime_error if data does not exists. Returns the data at the given index Returns the number of data stored in this object

##### `HasTarget(—)`

**Returns:** `bool`

If this drag operation has a target. The target should accept drag over event for it to be registered

##### `SetTarget(DropTarget &value)`

**Returns:** `void`

Returns the target of the drag operation. The target should accept drag over event for it to be registered. Throws runtime_error if target does not exists Sets the target of the drag operation. This function is automatically called. Manually calling this function might have unintended consequences.

##### `RemoveTarget(—)`

**Returns:** `void`

Removes the target of the drag operation. This function is automatically called. Manually calling this function might have unintended consequences.

##### `HasSource(—)`

**Returns:** `bool`

Whether this object has a source.

##### `MarkAsOS(—)`

**Returns:** `void`

Returns the drag source. Throws runtime_error if source does not exists Marks this DnD operation coming from OS

##### `IsFromOS(—)`

**Returns:** `bool`

Returns whether the DnD operation is coming from OS.


### `windaccess`

**Namespace:** `Gorgon`


---

## Functions

### `needsclip(Input::Mouse::EventType event)`

**Returns:** `bool`



### `for(auto &d : data)`

**Returns:** ``



### `for(auto &d : data)`

**Returns:** ``



### `initdrag()`

**Returns:** `void`



### `startdrag()`

**Returns:** `void`



### `DragStarted(*DragOperation)`

**Returns:** ``



### `begindrag()`

**Returns:** `void`



### `initdrag()`

**Returns:** ``



### `begindrag(DragSource &source)`

**Returns:** `void`



### `initdrag()`

**Returns:** ``



### `if(event == Input::Mouse::EventType::HitCheck)`

**Returns:** ``



### `dotransformandclip(true)`

**Returns:** ``



### `reverttransformandclip()`

**Returns:** ``



### `dotransformandclip(true)`

**Returns:** ``



### `reverttransformandclip()`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Over)`

**Returns:** ``



### `if(over)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Out)`

**Returns:** `else`



### `out(*this, op)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Move)`

**Returns:** `else`



### `if(ret)`

**Returns:** ``



### `propagate_mouseevent(Mouse::EventType::Out, location, button, amount, handlers)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Up)`

**Returns:** `else`



### `Drop(curlocation)`

**Returns:** ``



### `if(event == Input::Mouse::EventType::Down)`

**Returns:** `else`



### `if(event == Input::Mouse::EventType::HitCheck)`

**Returns:** `else`



### `finishdrag(bool success)`

**Returns:** `void`



### `DragEnded(op, success)`

**Returns:** ``



### `Drop(Geometry::Point location)`

**Returns:** `void`



### `CancelDrag()`

**Returns:** ``



### `if(ret)`

**Returns:** ``



### `finishdrag(true)`

**Returns:** ``



### `CancelDrag()`

**Returns:** ``



### `CancelDrag()`

**Returns:** `void`



### `finishdrag(false)`

**Returns:** ``



### `begindrag(DragSource &source)`

**Returns:** `void`


Destructor Current Drag operation, could be nullptr, denoting there is none. It is better to use GetDragOperation function. This event is fired whenever a drag operation begins This event is fired whenever a drag operation ends. Second parameter is set to true if the drag is accepted, if canceled it will be set to false. First parameter might not be reliable as this event is called after cancel/accept events. @cond never


### `begindrag()`

**Returns:** `void`



### `begindrag(D_ &&data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(const std::string &data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(const char *data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(std::string &data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(char *data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(DragSource &source, D_ &&data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(DragSource &source, const std::string &data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(DragSource &source, std::string &data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(DragSource &source, char *data, A_&& ... rest)`

**Returns:** `void`



### `begindrag(DragSource &source, const char *data, A_&& ... rest)`

**Returns:** `void`



### `startdrag()`

**Returns:** `void`


@endcond @cond internal


### `startdrag()`

**Returns:** ``


@endcond Begins a drag operation using the given source and data. Data will be assigned immediately for events to work properly. Additional data items can be added later if additional data become available at a later time.


### `startdrag()`

**Returns:** ``


Begins a drag operation using the given data, without a source. Data will be assigned immediately for events to work properly. Additional data items can be added later if additional data become available at a later time. It is not possible to receive any drag related events without a source.


### `initdrag()`

**Returns:** `void`



### `initdrag()`

**Returns:** ``


Prepares the drag operation. This function does not fully start the drag operation. You should call StartDrag after setting the data of the drag object


### `initdrag()`

**Returns:** ``


Prepares the drag operation. This function does not fully start the drag operation. You should call StartDrag after setting the data of the drag object


### `startdrag()`

**Returns:** ``


Starts the drag operation. You should first call PrepareDrag and set the data before starting the drag operation.


### `IsDragging()`

**Returns:** `inline bool`


@cond internal @endcond Returns whether a drag operation is in progress


### `IsDragPrepared()`

**Returns:** `inline bool`


Returns whether a drag operation is available


### `CancelDrag()`

**Returns:** `void`


Returns the current drag operation, throws if IsDragPrepared is false Cancel the current drag operation.


### `Drop(Geometry::Point location = {0, 0})`

**Returns:** `void`


Drop the current drag object. If there is no target receiving it, it will be canceled


### `while(widetext[0])`

**Returns:** ``



### `GlobalUnlock(stgmed.hGlobal)`

**Returns:** ``



### `ReleaseStgMedium(&stgmed)`

**Returns:** ``



### `GlobalUnlock(stgmed.hGlobal)`

**Returns:** ``



### `ReleaseStgMedium(&stgmed)`

**Returns:** ``



### `handledndenter(XEvent event, Window &wind)`

**Returns:** `void`



### `windp(wind)`

**Returns:** `windaccess`



### `if(event.xclient.data.l[1] & 1)`

**Returns:** ``



### `for(auto atom : atoms)`

**Returns:** ``



### `handledndleave(XEvent, Window &wind)`

**Returns:** `void`



### `windp(wind)`

**Returns:** `windaccess`



### `handlednddrop(XEvent event, Window &wind)`

**Returns:** `void`



### `windp(wind)`

**Returns:** `windaccess`



### `if(data->xdnd.filelist)`

**Returns:** ``



### `if(data->xdnd.utf8 || data->xdnd.string)`

**Returns:** ``



### `handledndposition(XEvent event, Window &wind)`

**Returns:** `void`



### `if(data->xdnd.filelist)`

**Returns:** ``



### `if(data->xdnd.utf8 || data->xdnd.string)`

**Returns:** ``



### `handledndselectionnotify(XEvent event, Window &wind)`

**Returns:** `void`



### `windp(wind)`

**Returns:** `windaccess`



### `if(data->xdnd.filelist)`

**Returns:** ``



### `XGetWindowProperty(WindowManager::display, data->handle, event.xselection.property, 0, 0, 0, AnyPropertyType, &type, &format, &len, &bytes, &dat)`

**Returns:** ``



### `if(bytes)`

**Returns:** ``



### `if(i-p>1)`

**Returns:** ``



### `XFree(dat)`

**Returns:** ``



### `XDeleteProperty(WindowManager::display, data->handle, event.xselection.property)`

**Returns:** ``



### `if(data->xdnd.utf8 || data->xdnd.string)`

**Returns:** `else`



### `XGetWindowProperty(WindowManager::display, data->handle, event.xselection.property, 0, 0, 0, AnyPropertyType, &type, &format, &len, &bytes, &dat)`

**Returns:** ``



### `if(bytes)`

**Returns:** ``



### `XFree(dat)`

**Returns:** ``



### `XDeleteProperty(WindowManager::display, data->handle, event.xselection.property)`

**Returns:** ``



### `if(data->xdnd.drop == 1)`

**Returns:** ``



### `handledndevent(XEvent event, Window &wind)`

**Returns:** `void`



### `switch(event.type)`

**Returns:** ``



### `if(event.xclient.message_type==WindowManager::XdndEnter)`

**Returns:** ``



### `handledndenter(event, wind)`

**Returns:** ``



### `if(event.xclient.message_type==WindowManager::XdndPosition)`

**Returns:** `else`



### `handledndposition(event, wind)`

**Returns:** ``



### `if(event.xclient.message_type==WindowManager::XdndLeave)`

**Returns:** `else`



### `handledndleave(event, wind)`

**Returns:** ``



### `if(event.xclient.message_type==WindowManager::XdndDrop)`

**Returns:** `else`



### `handlednddrop(event, wind)`

**Returns:** ``



### `handledndselectionnotify(event, wind)`

**Returns:** ``


