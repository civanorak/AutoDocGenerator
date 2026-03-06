# Listbox

&gt; Auto-generated documentation for the **Listbox** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `ListBase`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `GetCount(—)`

**Returns:** `virtual long`

Returns the item at the given point. This operator will not perform bounds checking. Returns the item at the given point. This operator will not perform bounds checking. Returns the number of elements in the list.

##### `virtual` `getindex(const W_ &widget)`

**Returns:** `virtual long`

For internal use. Returns the first widget used to represent any item at within the listbox. This function will return nullptr if there are no items in the list.

##### `virtual` `Refresh(—)`

**Returns:** `virtual void`

This function should refresh the contents of the listbox. Normally, calling this function is not necessary as it is handled internally. This function may defer refresh to next frame.


### `LBTRF_blank`

**Namespace:** `internal`

Contains no extra data and does not assume anything about W_

#### Methods

##### `LBTRF_blank(—)`

**Returns:** ``

##### `apply(long, W_ &, const T_ &, Geometry::Point p, Geometry::Size)`

**Returns:** `void`

##### `tag(long, const T_ &, Geometry::Point, Geometry::Size)`

**Returns:** `UI::ComponentTemplate::Tag`

##### `prepare(W_ &)`

**Returns:** `void`

##### `insert(long, long)`

**Returns:** `void`

##### `move(long, long)`

**Returns:** `void`

##### `remove(long, long)`

**Returns:** `void`


### `LBTRF_ListItem`

**Namespace:** `internal`

Contains no extra data, W_ must be compatible with ListItem

#### Methods

##### `SetOddEven(bool value)`

**Returns:** `void`

Sets if Odd/even styling should be used. Default is on.

##### `GetOddEven(—)`

**Returns:** `bool`

Returns wether Odd/even styling is in effect

##### `LBTRF_ListItem(—)`

**Returns:** ``

##### `apply(long, W_ &w, const T_ &, Geometry::Point p, Geometry::Size)`

**Returns:** `void`

##### `if(oddeven)`

**Returns:** ``

##### `tag(long, const T_ &, Geometry::Point, Geometry::Size)`

**Returns:** `UI::ComponentTemplate::Tag`

##### `prepare(W_ &)`

**Returns:** `void`

##### `insert(long, long)`

**Returns:** `void`

##### `move(long, long)`

**Returns:** `void`

##### `remove(long, long)`

**Returns:** `void`


### `LBSELTR_Single`

**Namespace:** `internal`

#### Methods

##### `HasSelectedItem(—)`

**Returns:** `bool`

Returns true if this listbox has a selected item.

##### `GetSelectedIndex(—)`

**Returns:** `long`

Returns the selected item. If nothing is selected this function will throw. You may check if there is a selection using HasSelectedItem function. Returns the selected item. If nothing is selected this function will throw. You may check if there is a selection using HasSelectedItem function. Changing the returned value will not automatically refresh the contents. Returns the index of the selected item. -1 will be returned if nothing is selected.

##### `SetSelectedIndex(long index)`

**Returns:** `void`

Sets the selection to the given index. If index in not within the bounds this function will throw std::out_of_range exception. -1 can be used to remove selected item.

##### `if(focusonly)`

**Returns:** ``

##### `if(index == -1)`

**Returns:** ``

##### `if(elm != nullptr)`

**Returns:** ``

##### `if(index != -1)`

**Returns:** ``

##### `ChangedEvent(selectedindex)`

**Returns:** ``

##### `SetFocusIndex(long value)`

**Returns:** `void`

Sets the index of the focused element. If set to -1, nothing is focused

##### `if(focusonly)`

**Returns:** ``

##### `SetSelectedIndex(value)`

**Returns:** ``

##### `if(value != -1)`

**Returns:** ``

##### `GetFocusIndex(—)`

**Returns:** `long`

Returns the index of the focused element. If nothing is focused, returns -1.

##### `RemoveSelection(—)`

**Returns:** `void`

##### `SetSelectedIndex(-1)`

**Returns:** ``

##### `SetSelection(const T_ &item)`

**Returns:** `void`

Selects the first item that has the given value. If item does not exists, this function will remove the selection

##### `IsSelectionFollowingFocus(—)`

**Returns:** `bool`

Returns true if the selected item is the focused item. Default is true. When set to false, an item can be focused without being selected. A listbox with radio buttons should have this value set to false.

##### `SetSelectionFollowsFocus(bool value)`

**Returns:** `void`

Sets whether the selected item is the focused item. Default is true. When set to false, an item can be focused without being selected. A listbox with radio buttons should have this value set to false.

##### `if(!focusonly && value)`

**Returns:** ``

##### `if(focusindex != -1)`

**Returns:** ``

##### `if(selectedindex != focusindex)`

**Returns:** ``

##### `ChangedEvent(selectedindex)`

**Returns:** ``

##### `GetSelectedItem(—)`

**Returns:** `return`

##### `GetSelectedItem(—)`

**Returns:** `return`

##### `LBSELTR_Single(—)`

**Returns:** ``

##### `sel_clicked(long index, W_ &w)`

**Returns:** `void`

##### `if(focusonly)`

**Returns:** ``

##### `ChangedEvent(index)`

**Returns:** ``

##### `sel_toggled(long index, W_ &w)`

**Returns:** `void`

##### `if(focusonly)`

**Returns:** ``

##### `ChangedEvent(index)`

**Returns:** ``

##### `sel_apply(long index, W_ &w, const T_ &)`

**Returns:** `void`

##### `if(index == focusindex)`

**Returns:** ``

##### `if(index == selectedindex)`

**Returns:** ``

##### `sel_prepare(W_ &w)`

**Returns:** `void`

##### `sel_insert(long index, long count)`

**Returns:** `void`

##### `sel_move(long index, long target)`

**Returns:** `void`

##### `if(index == focusindex)`

**Returns:** ``

##### `if(index > focusindex && target <= focusindex)`

**Returns:** `else`

##### `if(index < focusindex && target > focusindex)`

**Returns:** `else`

##### `if(index == selectedindex)`

**Returns:** ``

##### `if(index > selectedindex && target <= selectedindex)`

**Returns:** `else`

##### `if(index < selectedindex && target > selectedindex)`

**Returns:** `else`

##### `sel_remove(long index, long count)`

**Returns:** `void`

##### `if(index <= focusindex)`

**Returns:** ``

##### `if(index+count > focusindex)`

**Returns:** ``

##### `if(index <= selectedindex)`

**Returns:** ``

##### `if(index+count > selectedindex)`

**Returns:** ``

##### `ChangedEvent(-1)`

**Returns:** ``

##### `sel_destroy(W_ &w)`

**Returns:** `void`

##### `if(&w == selected)`

**Returns:** ``

##### `reapplyfocus(—)`

**Returns:** `void`

##### `if(focusindex != -1)`

**Returns:** ``


### `LBSELTR_Multi`

**Namespace:** `internal`


### `SelectionIndexHelper`

**Namespace:** `internal`

#### Methods

##### `begin(—)`

**Returns:** `auto`

##### `end(—)`

**Returns:** `auto`


### `SelectionHelper`

**Namespace:** `internal`

#### Methods

##### `begin(—)`

**Returns:** `auto`

##### `ItemIterator(me, l.selected, 0)`

**Returns:** `return`

##### `end(—)`

**Returns:** `auto`

##### `begin(—)`

**Returns:** `auto`

##### `ConstItemIterator(me, l.selected, 0)`

**Returns:** `return`

##### `end(—)`

**Returns:** `auto`


### `ItemIterator_`

**Namespace:** `internal`

#### Methods

##### `isvalid(—)`

**Returns:** `bool`

Default constructor, creates an iterator pointing to invalid location Copies another iterator Satisfies the needs of Iterator

##### `moveby(long amount)`

**Returns:** `bool`

##### `isvalid(—)`

**Returns:** `return`

##### `compare(const ItemIterator_ &it)`

**Returns:** `bool`

##### `set(const ItemIterator_ &it)`

**Returns:** `void`

##### `distance(const ItemIterator_ &it)`

**Returns:** `long`

##### `isbefore(const ItemIterator_ &it)`

**Returns:** `bool`


### `ConstItemIterator`

**Namespace:** `internal`

Regular iterator. @see Container::Iterator Const iterator allows iteration of const collections

#### Methods

##### `ConstItemIterator(const ItemIterator &it)`

**Returns:** ``

Regular iterators can be converted to const iterators


### `LBSTR_STLVector`

**Namespace:** `internal`

#### Methods

##### `Add(T_ val)`

**Returns:** `void`

Adds the given item to the listbox

##### `Add(T_ val, A_&& ...rest)`

**Returns:** `void`

Adds the given items to the listbox

##### `Insert(long before, T_ val)`

**Returns:** `void`

Inserts the given item before the given location. You may use Find to find the location of a specific item. If location is -1, then item is added at the end.

##### `if(before == -1)`

**Returns:** ``

##### `Add(val)`

**Returns:** ``

##### `Insert(long before, T_ val, A_&& ...rest)`

**Returns:** `void`

Inserts the given items before the given location. You may use Find to find the location of a specific item. If location is -1, then items are added at the end.

##### `if(before == -1)`

**Returns:** ``

##### `Add(val, rest...)`

**Returns:** ``

##### `Remove(long index)`

**Returns:** `void`

Removes the item at the given index.

##### `MoveBefore(long index, long before)`

**Returns:** `void`

Moves the item at the given index before the given location. If before is -1 or equal or larger than the number of items, then the item is moved to the end.

##### `if(index>before)`

**Returns:** `else`

##### `Find(const T_ &item, long start = 0)`

**Returns:** `long`

Return the index of the first item that has the given value. Returns -1 if item not found.

##### `Reserve(long amount)`

**Returns:** `void`

Allocates memory for the given amount of items

##### `Clear(—)`

**Returns:** `void`

Clears all items from the listbox

##### `begin(—)`

**Returns:** `auto`

##### `begin(—)`

**Returns:** `auto`

##### `end(—)`

**Returns:** `auto`

##### `end(—)`

**Returns:** `auto`

##### `LBSTR_STLVector(—)`

**Returns:** ``

@}

##### `getsize(—)`

**Returns:** `long`


### `LBSTR_Collection`

**Namespace:** `internal`

#### Methods

##### `Add(T_ &val)`

**Returns:** `void`

Adds the given item to the list

##### `Add(T_ &val, A_& ...rest)`

**Returns:** `void`

##### `Insert(long before, T_ &val)`

**Returns:** `void`

##### `Insert(const T_ &before, T_ &val)`

**Returns:** `void`

##### `Remove(long index)`

**Returns:** `void`

##### `Remove(const T_ &item)`

**Returns:** `void`

##### `Delete(const T_ &item)`

**Returns:** `void`

Deletes an item from the listbox. Deleting both removes the item from the list and free the item itself. If given item does not exists, this function deletes the item and does nothing else

##### `if(index == -1)`

**Returns:** ``

##### `Delete(long index)`

**Returns:** `void`

Deletes the item with the given index

##### `MoveBefore(long index, long before)`

**Returns:** `void`

##### `Find(const T_ &item)`

**Returns:** `long`

Return the location of the given item. Returns -1 if item not found.

##### `Clear(—)`

**Returns:** `void`

Removes all elements without destroying them

##### `DeleteAll(—)`

**Returns:** `void`

Deletes and removes all elements in the listbox

##### `Destroy(—)`

**Returns:** `void`

Deletes and removes all elements in the listbox. This function also clears the memory associated with the storage.

##### `Reserve(long amount)`

**Returns:** `void`

Allocates memory for the given amount of items

##### `begin(—)`

**Returns:** `auto`

##### `begin(—)`

**Returns:** `auto`

##### `end(—)`

**Returns:** `auto`

##### `end(—)`

**Returns:** `auto`

##### `LBSTR_Collection(—)`

**Returns:** ``

@}

##### `getsize(—)`

**Returns:** `long`


### `two`

**Namespace:** `listbox`


### `two`

**Namespace:** `listbox`


### `ItemData`

**Namespace:** `listbox`

#### Methods

##### `Get(—)`

**Returns:** `T_`


### `collectionboxelementcompare`

**Namespace:** `listbox`

#### Methods

##### `predicate(*l.item, *r.item)`

**Returns:** `return`


### `listboxelementcompare`

**Namespace:** `listbox`

#### Methods

##### `predicate(l.item, r.item)`

**Returns:** `return`


### `valueaccessor`

**Namespace:** `listbox`

#### Methods

##### `static` `Get(const ItemData<T_> data)`

**Returns:** `static T_`

##### `static` `StorageToReturnType(T_ storage)`

**Returns:** `static T_`

##### `static` `ParamToStorageType(T_ storage)`

**Returns:** `static T_`

##### `static` `Set(ItemData<T_> &data, const T_ &v)`

**Returns:** `static void`

##### `static` `New(const T_ &v)`

**Returns:** `static ItemData<T_>`


### `ptraccessor`

**Namespace:** `listbox`

#### Methods

##### `static` `Set(ItemData<T_*> &data, T_ &v)`

**Returns:** `static void`

##### `static` `New(T_ &v)`

**Returns:** `static ItemData<T_*>`


### `Basic`

**Namespace:** `listbox`


### `Iterator`

**Namespace:** `listbox`

#### Methods

##### `int(—)`

**Returns:** `operator unsigned`

##### `current(—)`

**Returns:** `typename Ac_::returntype&`

##### `moveby(int amount)`

**Returns:** `bool`

##### `if(index<0)`

**Returns:** ``

##### `isvalid(—)`

**Returns:** `bool`

##### `compare(const Iterator &it)`

**Returns:** `bool`

##### `set(const Iterator &it)`

**Returns:** `void`

##### `distance(const Iterator &it)`

**Returns:** `int`

##### `isbefore(const Iterator &it)`

**Returns:** `bool`


### `SelectionIterator`

**Namespace:** `listbox`

#### Methods

##### `int(—)`

**Returns:** `operator unsigned`

##### `moveby(1)`

**Returns:** ``

##### `current(—)`

**Returns:** `typename Ac_::returntype&`

##### `moveby(int amount)`

**Returns:** `bool`

##### `if(amount>0)`

**Returns:** ``

##### `if(amount<0)`

**Returns:** `else`

##### `while(index>0 && amount)`

**Returns:** ``

##### `if(index<0)`

**Returns:** ``

##### `isvalid(—)`

**Returns:** `bool`

##### `compare(const SelectionIterator &it)`

**Returns:** `bool`

##### `set(const SelectionIterator &it)`

**Returns:** `void`

##### `distance(const SelectionIterator &it)`

**Returns:** `int`

##### `if(ind>it.index)`

**Returns:** ``

##### `while(ind>it.index)`

**Returns:** ``

##### `if(ind<it.index)`

**Returns:** `else`

##### `while(ind<it.index)`

**Returns:** ``

##### `isbefore(const SelectionIterator &it)`

**Returns:** `bool`


### `Collectionbox`

**Namespace:** `listbox`

#### Methods

##### `Add(T_ &value)`

**Returns:** `void`

##### `Add(T_ *value)`

**Returns:** `void`

##### `Add(*value)`

**Returns:** ``

##### `Insert(T_ &value, const  T_ *before)`

**Returns:** `void`

##### `Insert(T_ &value, const  T_ &before)`

**Returns:** `void`

##### `Insert(T_ &value, unsigned before)`

**Returns:** `void`

##### `insert(value, before)`

**Returns:** ``

##### `Insert(T_ *value, const  T_ *before)`

**Returns:** `void`

##### `Insert(*value, before)`

**Returns:** ``

##### `Insert(T_ *value, const  T_ &before)`

**Returns:** `void`

##### `Insert(*value, &before)`

**Returns:** ``

##### `Insert(T_ *value, unsigned before)`

**Returns:** `void`

##### `Insert(*value, before)`

**Returns:** ``

##### `MoveBefore(T_ &value, const T_ &before)`

**Returns:** `void`

##### `MoveBefore(T_ &value, unsigned before)`

**Returns:** `void`

##### `MoveBefore(unsigned index, const T_ &before)`

**Returns:** `void`

##### `MoveBefore(unsigned index, unsigned before)`

**Returns:** `void`

##### `Remove(T_ &item)`

**Returns:** `void`

##### `Remove(T_ *item)`

**Returns:** `void`

##### `Remove(unsigned index)`

**Returns:** `void`

##### `Delete(T_ &item)`

**Returns:** `void`

##### `Delete(T_ *item)`

**Returns:** `void`

##### `Delete(unsigned index)`

**Returns:** `void`

##### `DeleteAll(—)`

**Returns:** `void`

##### `Destroy(—)`

**Returns:** ``

##### `Destroy(—)`

**Returns:** `void`

##### `for(auto it=this->items.begin()`

**Returns:** ``

##### `SetSelected(T_ &item)`

**Returns:** `void`

##### `Find(const T_& item)`

**Returns:** `unsigned`

##### `for(auto it=this->items.begin()`

**Returns:** ``

##### `Find(const T_ *item)`

**Returns:** `unsigned`

##### `Sort(—)`

**Returns:** `void`

##### `setValue(T_ *value)`

**Returns:** `void`

##### `SetSelected(*value)`

**Returns:** ``

##### `virtual` `selectionchanged(—)`

**Returns:** `virtual void`

##### `ChangeEvent(—)`

**Returns:** ``

##### `virtual` `reordered(—)`

**Returns:** `virtual void`

##### `ReorderEvent(—)`

**Returns:** ``

##### `virtual` `clicked(—)`

**Returns:** `virtual void`

##### `ItemClickEvent(—)`

**Returns:** ``


### `Listbox`

**Namespace:** `listbox`

#### Methods

##### `Add(const T_ &value)`

**Returns:** `void`

##### `Add(—)`

**Returns:** `void`

##### `Insert(const T_ &value, unsigned before)`

**Returns:** `void`

##### `MoveBefore(unsigned index, unsigned before)`

**Returns:** `void`

##### `RemoveAll(const T_ &item)`

**Returns:** `void`

##### `for(int i=0;i<this->items.size()`

**Returns:** ``

##### `Remove(unsigned index)`

**Returns:** `void`

##### `Sort(—)`

**Returns:** `void`

##### `setValue(const T_ &value)`

**Returns:** `void`

##### `if(this->selectiontype==listbox::Basic<T_, listbox::valueaccessor<T_>, CF_, GetIcon>::SingleSelect)`

**Returns:** ``

##### `for(unsigned i=0;i<this->items.size()`

**Returns:** ``

##### `if(this->items[i].item==value)`

**Returns:** ``

##### `for(unsigned i=0;i<this->items.size()`

**Returns:** ``

##### `if(this->items[i].item==value)`

**Returns:** ``

##### `getValue(—)`

**Returns:** `T_`

##### `T_(—)`

**Returns:** `return`

##### `virtual` `selectionchanged(—)`

**Returns:** `virtual void`

##### `ChangeEvent(—)`

**Returns:** ``

##### `virtual` `reordered(—)`

**Returns:** `virtual void`

##### `ReorderEvent(—)`

**Returns:** ``

##### `virtual` `clicked(—)`

**Returns:** `virtual void`

##### `ItemClickEvent(—)`

**Returns:** ``


---

## Enums

### `SelectionMethod`

**Namespace:** `internal`


### `EventMethod`

**Namespace:** `internal`

Clicking on the item will toggle its selected state Clicking on the item will set the selection to be that item only. Ctrl clicking toggles


### `SelectionTypes`

**Namespace:** `listbox`


---

## Functions

### `SetTextUsingFrom(const T_ &val, W_ &w)`

**Returns:** `void`



### `SetTextUsingFn(const T_ &val, W_ &w)`

**Returns:** `void`



### `GetTextUsingTo(W_ &w, T_ &val)`

**Returns:** `void`



### `SetSelectionMethod(SelectionMethod value)`

**Returns:** `void`


Event will be fired only once per action Even will be fired per changed item Changes selection method. Default method is toggle. In toggle method, clicking on an item will toggle its state without effecting other items. In UseCtrl method, if an item is clicked with Ctrl key pressed, it will be toggled. If Ctrl is not pressed, it will become the only selected item.


### `GetSelectionMethod()`

**Returns:** `SelectionMethod`


Returns the selection method.


### `SetEventMethod(EventMethod value)`

**Returns:** `void`


Changes event method. Default method is ForEachItem. In ForEachItem method, ChangedEvent will be fired for each item that is affected. index and status parameters will be set. If event method is set to Once, ChangedEvent will be fired once per action. index and status parameter will be set only if one item is affected. Otherwise, index will be set to -1 and status is set to false.


### `GetEventMethod()`

**Returns:** `EventMethod`


Returns the event method.


### `GetFocusIndex()`

**Returns:** `long`


Returns the index of the focused element. If nothing is focused, returns -1.


### `SetFocusIndex(long value)`

**Returns:** `void`


Sets the index of the focused element. If set to -1, nothing is focused


### `if(value != -1)`

**Returns:** ``



### `ClearSelection()`

**Returns:** `void`


Removes all items from the selection


### `if(event == Once)`

**Returns:** ``



### `ChangedEvent(-1, false)`

**Returns:** ``



### `for(auto ind : old)`

**Returns:** ``



### `ChangedEvent(ind, false)`

**Returns:** ``



### `SetSelection(long ind)`

**Returns:** `void`


Replaces the selection by the given index


### `SetSelection(std::vector<long>{ind})`

**Returns:** ``



### `SetSelection(std::vector<long> indices)`

**Returns:** `void`


Replaces the selection by the given indices


### `ClearSelection()`

**Returns:** ``



### `if(event == ForEachItem)`

**Returns:** ``



### `for(auto ind : selected)`

**Returns:** ``



### `ChangedEvent(ind, true)`

**Returns:** ``



### `ChangedEvent(-1, false)`

**Returns:** ``



### `SetSelection(P_&&... elms)`

**Returns:** `void`


Replaces the selection by the given indices


### `SetSelection({elms...})`

**Returns:** ``



### `AddToSelection(long ind)`

**Returns:** `void`


Adds the given index to the selection


### `AddToSelection(std::vector<long>{ind})`

**Returns:** ``



### `AddToSelection(std::vector<long> indices)`

**Returns:** `void`


Adds the given indices to the selection


### `ChangedEvent(*ind, true)`

**Returns:** ``



### `if(event == Once)`

**Returns:** ``



### `ChangedEvent(-1, false)`

**Returns:** ``



### `AddToSelection(P_&&... elms)`

**Returns:** `void`


Adds the given indices to the selection


### `AddToSelection({elms...})`

**Returns:** ``



### `IsSelected(long index)`

**Returns:** `bool`


Returns if the item in the given index is selected.


### `GetSelectionCount()`

**Returns:** `long`


Returns how many items are selected


### `RemoveFromSelection(long index)`

**Returns:** `void`


Removes the given index from the selection


### `ChangedEvent(index, false)`

**Returns:** ``



### `SelectAll()`

**Returns:** `void`


Selects all items


### `for(int i=0; i<elms; i++)`

**Returns:** ``



### `ChangedEvent(i, true)`

**Returns:** ``



### `ChangedEvent(-1, false)`

**Returns:** ``



### `InvertSelection()`

**Returns:** `void`


Inverts the selection.


### `for(int i=0; i<elms; i++)`

**Returns:** ``



### `ChangedEvent(i, false)`

**Returns:** ``



### `ChangedEvent(i, true)`

**Returns:** ``



### `ChangedEvent(-1, false)`

**Returns:** ``



### `sel_clicked(long index, W_ &w)`

**Returns:** `void`


Allows iteration of selected indices Allows iteration of selected items. If the iterated items is changed, list will not be automatically updated.


### `sel_toggled(long index, W_ &w, bool forcetoggle = true)`

**Returns:** `void`



### `if(method == Toggle || forcetoggle)`

**Returns:** ``



### `ChangedEvent(index, false)`

**Returns:** ``



### `ChangedEvent(index, true)`

**Returns:** ``



### `if(Input::Keyboard::CurrentModifier == Input::Keyboard::Modifier::Ctrl)`

**Returns:** ``



### `ChangedEvent(index, false)`

**Returns:** ``



### `ChangedEvent(index, true)`

**Returns:** ``



### `SetSelection(index)`

**Returns:** ``



### `sel_apply(long index, W_ &w, const T_ &)`

**Returns:** `void`



### `if(index == focusindex)`

**Returns:** ``



### `sel_prepare(W_ &w)`

**Returns:** `void`



### `sel_insert(long index, long count)`

**Returns:** `void`



### `for(; item != selected.end()`

**Returns:** ``



### `sel_move(long index, long target)`

**Returns:** `void`



### `if(index == focusindex)`

**Returns:** ``



### `if(index > focusindex && target <= focusindex)`

**Returns:** `else`



### `if(index < focusindex && target > focusindex)`

**Returns:** `else`



### `if(index < target)`

**Returns:** ``



### `while(from < to)`

**Returns:** ``



### `if(shifted != from)`

**Returns:** ``



### `while(from > to)`

**Returns:** ``



### `if(shifted != from)`

**Returns:** ``



### `sel_remove(long index, long count)`

**Returns:** `void`



### `if(index <= focusindex)`

**Returns:** ``



### `if(index+count > focusindex)`

**Returns:** ``



### `if(*item < index+count)`

**Returns:** ``



### `sel_destroy(W_ &w)`

**Returns:** `void`



### `reapplyfocus()`

**Returns:** `void`



### `if(focusindex != -1)`

**Returns:** ``



### `for(auto &p : widgetlist)`

**Returns:** ``


@endcond Returns the item at the given point. This operator will not perform bounds checking. Changing the returned value will not automatically refresh the contents. Returns the item at the given point. This operator will not perform bounds checking. Returns the number of elements in the list.


### `TW_(v, *w)`

**Returns:** ``



### `if(y == 0)`

**Returns:** ``



### `if(scroller)`

**Returns:** ``



### `if(scroller->Range >= scroller->Maximum)`

**Returns:** ``



### `ScrollTo(float y)`

**Returns:** `void`


Scrolls the contents of the listbox so that the it will start displaying items from the given location in list items. This function takes columns into account.


### `if(scrollspeed == 0)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `if(!isscrolling)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `ScrollBy(float y)`

**Returns:** `void`


Scrolls the contents an additional amount of items.


### `ScrollOffset()`

**Returns:** `float`


Returns the current scroll offset.


### `SetOverscroll(float value)`

**Returns:** `void`


Sets the amount of extra scrolling distance after the bottom-most widget is completely visible in pixels. Default is 0. Does not apply if everything is visible.


### `if(scroller)`

**Returns:** ``



### `GetOverscroll()`

**Returns:** `float`


Returns the amount of extra scrolling distance after the bottom-most widget is completely visible in pixels.


### `SetScrollDistance(int value)`

**Returns:** `void`


Sets the scroll distance per click in pixels. Default depends on the default size of the listbox.


### `GetScrollDistance()`

**Returns:** `int`


Returns the scroll distance per click


### `DisableSmoothScroll()`

**Returns:** `void`


Disables smooth scrolling of the panel


### `SetSmoothScrollSpeed(0)`

**Returns:** ``



### `SetSmoothScrollSpeed(int value)`

**Returns:** `void`


Adjusts the smooth scrolling speed of the listbox. Given value is in items per second, default value is 20.


### `GetSmoothScrollSpeed()`

**Returns:** `int`


Returns the smooth scrolling speed of the listbox. If smooth scroll is disabled, this value will be 0.


### `IsSmoothScrollEnabled()`

**Returns:** `bool`


Returns if the smooth scroll is enabled.


### `SetMaximumScrollDuration(int value)`

**Returns:** `void`


Sets the the duration that scrolling can take. This speeds up scrolling if the distance is too much. This value is not exact and scrolling will slow down as it gets close to the target. However, total scroll duration cannot exceed twice this value. The time is in milliseconds and default value is 500.


### `GetMaximumScrollDuration()`

**Returns:** `int`


Returns how long a scrolling operation can take.


### `GetMaximumDisplayedElements()`

**Returns:** `float`


This may not be a perfect number


### `GetInteriorSize()`

**Returns:** `Geometry::Size`



### `EnsureVisible(long index)`

**Returns:** `void`


Ensures the given index is completely visible on the screen.


### `ScrollTo(targetind)`

**Returns:** ``



### `EnsureVisible(index)`

**Returns:** ``



### `if(key == Keycodes::Space)`

**Returns:** ``



### `if(w)`

**Returns:** ``



### `FitHeight(const UI::UnitDimension &maxsize)`

**Returns:** `bool`


This function will try to set the height of the listbox to contain all its elements. If the size necessary to do so is larger than maxsize, then maxsize will be used and this function will return false. This function may give up before fully exceeding maxsize if elements have different heights. But it will never surpass maxsize.


### `FitHeight(float elms)`

**Returns:** `bool`


This function will try to set the height of the listbox to contain all its elements. If the size necessary to do so is larger than maxsize, then maxsize will be used and this function will return false. This function may give up before fully exceeding maxsize if elements have different heights. But it will never surpass maxsize.


### `Focus()`

**Returns:** ``



### `ScrollBy(-amount*scrolldist)`

**Returns:** ``



### `switch(key)`

**Returns:** ``



### `if(ind != org)`

**Returns:** ``



### `EnsureVisible(ind)`

**Returns:** ``



### `fitheight(int maxpixels)`

**Returns:** `bool`



### `if(expected < maxpixels)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `for(auto &p : widgets)`

**Returns:** ``



### `updatescroll()`

**Returns:** `void`



### `if(target < cur)`

**Returns:** ``



### `if(cur - dist <= target)`

**Returns:** ``



### `if(target > cur)`

**Returns:** `else`



### `if(cur + dist >= target)`

**Returns:** ``



### `Refresh()`

**Returns:** ``



### `if(done)`

**Returns:** ``



### `Refresh()`

**Returns:** ``


For internal use. Returns the widget used to represent the item at the given index. This function will return nullptr if the index does not currently have a visual representation. This is not an edge case, any item that is not in view will most likely not have a representation. For internal use. Returns the first widget used to represent any item at within the listbox. This function will return nullptr if there are no items in the list.


### `Activate()`

**Returns:** `virtual bool`



### `Activate()`

**Returns:** `virtual bool`



### `Activate()`

**Returns:** `virtual bool`



### `Activate()`

**Returns:** `virtual bool`



### `test(...)`

**Returns:** `template <typename C> static two`



### `test(...)`

**Returns:** `template <typename C> static two`



### `GetIcon(const T_ &item)`

**Returns:** `typename std::enable_if<has_GetIcon<T_>::value && has_HasIcon<T_>::value, graphics::RectangularGraphic2D *>::type`



### `Clear()`

**Returns:** `void`



### `GetCount()`

**Returns:** `int`



### `AddRange(const I_ &begin, const I_ &end)`

**Returns:** `void`



### `add(*it)`

**Returns:** ``



### `AddAll(const C_ &container)`

**Returns:** `void`



### `for(auto it=container.begin()`

**Returns:** ``



### `add(*it)`

**Returns:** ``



### `Refresh()`

**Returns:** `void`



### `adjustitems()`

**Returns:** ``



### `HasSelection()`

**Returns:** `bool`



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `ActiveIndex()`

**Returns:** `int`



### `SetIndex(unsigned index)`

**Returns:** `void`



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `if(index!=activeindex)`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `ClearSelection()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `Select(unsigned index)`

**Returns:** `void`



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `if(activeindex!=index)`

**Returns:** ``



### `if(activeindex!=-1)`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(!items[index].selected)`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `SelectAll()`

**Returns:** `void`



### `for(auto it=items.begin()`

**Returns:** ``



### `Deselect()`

**Returns:** `void`



### `ClearSelection()`

**Returns:** ``



### `Deselect(unsigned index)`

**Returns:** `void`



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `if(items[index].selected)`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(items[index].selected)`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `ClearSelection()`

**Returns:** `void`



### `for(auto it=items.begin()`

**Returns:** ``



### `IsSelected(unsigned index)`

**Returns:** `bool`



### `begin()`

**Returns:** `Iterator<T_, A_>`



### `end()`

**Returns:** `Iterator<T_, A_>`



### `First()`

**Returns:** `Iterator<T_, A_>`



### `begin()`

**Returns:** `return`



### `Last()`

**Returns:** `Iterator<T_, A_>`



### `selbegin()`

**Returns:** `SelectionIterator<T_, A_>`



### `selend()`

**Returns:** `SelectionIterator<T_, A_>`



### `FirstSelected()`

**Returns:** `SelectionIterator<T_, A_>`



### `selbegin()`

**Returns:** `return`



### `LastSelected()`

**Returns:** `SelectionIterator<T_, A_>`



### `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`



### `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key key)`

**Returns:** `virtual bool`



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `Select(activeindex+1)`

**Returns:** ``



### `EnsureVisible()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(key==KeyCodes::Up && activeindex>0)`

**Returns:** ``



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `Select(activeindex-1)`

**Returns:** ``



### `EnsureVisible()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(key==KeyCodes::PageDown)`

**Returns:** ``



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `Select(target)`

**Returns:** ``



### `EnsureVisible()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(key==KeyCodes::PageUp)`

**Returns:** ``



### `if(target<0)`

**Returns:** ``



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `Select(target)`

**Returns:** ``



### `EnsureVisible(target)`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `Select(0)`

**Returns:** ``



### `EnsureVisible()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `if(key==KeyCodes::End)`

**Returns:** ``



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `EnsureVisible()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `EnsureVisible()`

**Returns:** `void`



### `EnsureVisible(activeindex)`

**Returns:** ``



### `EnsureVisible(int index)`

**Returns:** `void`



### `flushitemcount()`

**Returns:** ``



### `CenterItem()`

**Returns:** `void`



### `CenterItem(activeindex)`

**Returns:** ``



### `CenterItem(int index)`

**Returns:** `void`



### `flushitemcount()`

**Returns:** ``



### `setSelectionType(const SelectionTypes &value)`

**Returns:** `void`



### `if(selectiontype==MultiSelect && value!=MultiSelect)`

**Returns:** ``



### `getSelectionType()`

**Returns:** `SelectionTypes`



### `setItemHeight(const int &value)`

**Returns:** `void`



### `if(itemheight!=value)`

**Returns:** ``



### `for(auto widget=this->representations.begin()`

**Returns:** ``



### `itemheightchanged()`

**Returns:** ``



### `getItemHeight()`

**Returns:** `int`



### `setAutoUpdate(const bool &value)`

**Returns:** `void`



### `getAutoUpdate()`

**Returns:** `bool`



### `checkdelete()`

**Returns:** `virtual void`



### `elementheight()`

**Returns:** `virtual int`



### `adjustitems()`

**Returns:** `virtual void`



### `flushitemcount()`

**Returns:** `void`



### `if(initemcountqueue)`

**Returns:** ``



### `setitemcount(delayedcount)`

**Returns:** ``



### `doadjust()`

**Returns:** `void`



### `if(initemcountqueue)`

**Returns:** ``



### `for(unsigned i=organizer.GetTop()`

**Returns:** ``



### `trigger(ListItem &element, int index)`

**Returns:** `virtual void`



### `if(selectiontype==SingleSelect)`

**Returns:** ``



### `if(activeindex!=-1)`

**Returns:** ``



### `if(index!=activeindex)`

**Returns:** ``



### `if(selectiontype==ToggleSelect)`

**Returns:** `else`



### `if(selectiontype==MultiSelect)`

**Returns:** `else`



### `if(Modifier::Current==Modifier::Ctrl)`

**Returns:** ``



### `if(Modifier::Current==Modifier::Shift)`

**Returns:** `else`



### `for(int i=from;i<=to;i++)`

**Returns:** ``



### `if(!items[i].selected)`

**Returns:** ``



### `if(selectedcount!=1 || !items[index].selected)`

**Returns:** ``



### `ClearSelection()`

**Returns:** ``



### `if(notifyselection)`

**Returns:** ``



### `selectionchanged()`

**Returns:** ``



### `clicked()`

**Returns:** ``



### `adjustitems()`

**Returns:** ``



### `setAutoHeight(const bool &value)`

**Returns:** `void`



### `getAutoHeight()`

**Returns:** `bool`



### `setColumns(const int &value)`

**Returns:** `void`



### `getColumns()`

**Returns:** `int`



### `setAllowReorder(const bool &value)`

**Returns:** `void`



### `getAllowReorder()`

**Returns:** `bool`



### `wr_loaded()`

**Returns:** `virtual void`



### `itemadded(typename A_::paramtype &, int index)`

**Returns:** `virtual void`



### `itemremoving(int index)`

**Returns:** `virtual void`



### `delaysetitemcount(int count)`

**Returns:** `void`



### `add(typename A_::paramtype &v)`

**Returns:** `virtual void`



### `insert(typename A_::paramtype &v, unsigned before)`

**Returns:** `virtual void`



### `movebefore(unsigned index, unsigned before)`

**Returns:** `virtual void`



### `if(activeindex!=-1)`

**Returns:** ``



### `if(activeindex==index)`

**Returns:** ``



### `if(before==index || before==index+1)`

**Returns:** `else`



### `if(before<index)`

**Returns:** `else`



### `for(unsigned i=index;i>before;i--)`

**Returns:** ``



### `if(activeindex!=-1)`

**Returns:** ``



### `if(activeindex==index)`

**Returns:** ``



### `for(unsigned i=index;i<before-1;i++)`

**Returns:** ``



### `if(activeindex!=-1)`

**Returns:** ``



### `if(activeindex==index)`

**Returns:** ``



### `reordered()`

**Returns:** ``



### `remove(unsigned index)`

**Returns:** `virtual bool`



### `itemremoving(index)`

**Returns:** ``



### `if(activeindex==index)`

**Returns:** ``



### `if(items[index].selected)`

**Returns:** ``



### `selectionchanged()`

**Returns:** `virtual void`



### `reordered()`

**Returns:** `virtual void`



### `clicked()`

**Returns:** `virtual void`


