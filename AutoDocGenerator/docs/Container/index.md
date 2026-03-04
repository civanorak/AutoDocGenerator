# Container

> Auto-generated documentation for the **Container** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `ContainerBase`

**Namespace:** `gge`

#### Methods

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

##### `IsHidden(—)`

**Returns:** `inline bool`

##### `virtual` `Show(bool setfocus=false)`

**Returns:** `virtual void`

##### `if(setfocus && !Focused)`

**Returns:** ``

##### `FocusFirst(—)`

**Returns:** ``

##### `virtual` `Hide(—)`

**Returns:** `virtual void`

##### `RemoveFocus(—)`

**Returns:** ``

##### `ToggleVisibility(—)`

**Returns:** `void`

##### `Hide(—)`

**Returns:** `else`

##### `SetVisibility(bool visible)`

**Returns:** `void`

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

##### `IsDisabled(—)`

**Returns:** `inline bool`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_containerenabledchanged(*it, true)`

**Returns:** ``

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_containerenabledchanged(*it, false)`

**Returns:** ``

##### `ToggleEnabled(—)`

**Returns:** `void`

##### `Disable(—)`

**Returns:** `else`

##### `SetEnabled(bool enabled)`

**Returns:** `void`

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `GetWidth(—)`

**Returns:** `int`

##### `GetHeight(—)`

**Returns:** `int`

##### `virtual` `Resize(utils::Size Size)`

**Returns:** `virtual void`

##### `Reorganize(—)`

**Returns:** ``

##### `Resize(int W, int H)`

**Returns:** `void`

##### `SetWidth(int W)`

**Returns:** `void`

##### `SetHeight(int H)`

**Returns:** `void`

##### `virtual` `GetUsableSize(—)`

**Returns:** `virtual utils::Size`

##### `GetUsableWidth(—)`

**Returns:** `int`

##### `GetUsableHeight(—)`

**Returns:** `int`

##### `virtual` `GetOverheadMargins(—)`

**Returns:** `virtual utils::Margins`

##### `virtual` `AbsoluteLocation(—)`

**Returns:** `virtual utils::Point`

##### `AbsoluteLeft(—)`

**Returns:** `int`

##### `AbsoluteTop(—)`

**Returns:** `int`

##### `virtual` `HasFocused(—)`

**Returns:** `virtual bool`

##### `virtual` `FocusFirst(—)`

**Returns:** `virtual bool`

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `if(it->isvisible && it->isenabled)`

**Returns:** ``

##### `virtual` `FocusNext(—)`

**Returns:** `virtual bool`

##### `if(it->isvisible && it->isenabled)`

**Returns:** ``

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `if(it->isvisible && it->isenabled)`

**Returns:** ``

##### `virtual` `FocusPrevious(—)`

**Returns:** `virtual bool`

##### `if(it->isvisible && it->isenabled)`

**Returns:** ``

##### `for(auto it=Widgets.Last()`

**Returns:** ``

##### `if(it->isvisible && it->isenabled)`

**Returns:** ``

##### `virtual` `RemoveFocus(—)`

**Returns:** `virtual bool`

##### `focus_changed(NULL)`

**Returns:** ``

##### `virtual` `ForceRemoveFocus(—)`

**Returns:** `virtual void`

##### `call_widget_loosefocus(Focused, true)`

**Returns:** ``

##### `focus_changed(NULL)`

**Returns:** ``

##### `virtual` `HasDefault(—)`

**Returns:** `virtual bool`

##### `virtual` `SetDefault(WidgetBase &widget)`

**Returns:** `virtual void`

##### `virtual` `RemoveDefault(—)`

**Returns:** `virtual void`

##### `virtual` `HasCancel(—)`

**Returns:** `virtual bool`

##### `virtual` `SetCancel(WidgetBase &widget)`

**Returns:** `virtual void`

##### `virtual` `RemoveCancel(—)`

**Returns:** `virtual void`

##### `IsTabSwitchEnabled(—)`

**Returns:** `bool`

##### `EnableTabSwitch(—)`

**Returns:** `void`

##### `DisableTabSwitch(—)`

**Returns:** `void`

##### `ToggleTabSwitchEnabledState(—)`

**Returns:** `void`

##### `SetTabSwitchEnabledState(bool state)`

**Returns:** `void`

##### `call_widget_located(widget, w, Order)`

**Returns:** ``

##### `WidgetBoundsChanged(—)`

**Returns:** ``

##### `virtual` `RemoveWidget(WidgetBase &widget)`

**Returns:** `virtual bool`

##### `RemoveFocus(—)`

**Returns:** ``

##### `RemoveDefault(—)`

**Returns:** ``

##### `RemoveCancel(—)`

**Returns:** ``

##### `WidgetBoundsChanged(—)`

**Returns:** ``

##### `AddWidget(*widget, Order)`

**Returns:** `return`

##### `RemoveWidget(WidgetBase *widget)`

**Returns:** `bool`

##### `RemoveWidget(*widget)`

**Returns:** `return`

##### `RemoveAllWidgets(—)`

**Returns:** `void`

##### `ForceRemoveFocus(—)`

**Returns:** ``

##### `RemoveDefault(—)`

**Returns:** ``

##### `RemoveCancel(—)`

**Returns:** ``

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_detach(it)`

**Returns:** ``

##### `WidgetBoundsChanged(—)`

**Returns:** ``

##### `virtual` `IsActive(—)`

**Returns:** `virtual bool`

##### `virtual` `Deactivate(—)`

**Returns:** `virtual void`

##### `virtual` `RedrawAll(—)`

**Returns:** `virtual void`

##### `for(auto it=Widgets.Last()`

**Returns:** ``

##### `virtual` `Reorganize(—)`

**Returns:** `virtual void`

##### `if(!organizing)`

**Returns:** ``

##### `if(organizer)`

**Returns:** ``

##### `virtual` `WidgetBoundsChanged(—)`

**Returns:** `virtual void`

##### `Reorganize(—)`

**Returns:** ``

##### `virtual` `SetAccessKey(WidgetBase &widget, input::keyboard::Key Key)`

**Returns:** `virtual void`

##### `virtual` `ResetAccessKey(int Key)`

**Returns:** `virtual void`

##### `virtual` `GetAccessKey(WidgetBase &widget)`

**Returns:** `virtual input::keyboard::Key`

##### `for(auto it=AccessKeys.begin()`

**Returns:** ``

##### `IsAccessKeysEnabled(—)`

**Returns:** `bool`

##### `EnableAccessKeys(—)`

**Returns:** `void`

##### `if(!accesskeysenabled)`

**Returns:** ``

##### `for(auto it=AccessKeys.begin()`

**Returns:** ``

##### `DisableAccessKeys(—)`

**Returns:** `void`

##### `if(accesskeysenabled)`

**Returns:** ``

##### `for(auto it=AccessKeys.begin()`

**Returns:** ``

##### `ToggleAccessKeysEnabledState(—)`

**Returns:** `void`

##### `EnableAccessKeys(—)`

**Returns:** ``

##### `DisableAccessKeys(—)`

**Returns:** ``

##### `SetAccessKeysEnabledState(bool state)`

**Returns:** `void`

##### `EnableAccessKeys(—)`

**Returns:** ``

##### `DisableAccessKeys(—)`

**Returns:** ``

##### `HasOrganizer(—)`

**Returns:** `bool`

##### `virtual` `SetOrganizer(Organizer &organizer)`

**Returns:** `virtual void`

##### `Reorganize(—)`

**Returns:** ``

##### `SetOrganizer(Organizer *organizer)`

**Returns:** `void`

##### `virtual` `RemoveOrganizer(—)`

**Returns:** `virtual void`

##### `RemoveOrganizer(—)`

**Returns:** ``

##### `virtual` `focus_changing(WidgetBase *newwidget)`

**Returns:** `virtual bool`

##### `virtual` `focus_changed(WidgetBase *newwidget)`

**Returns:** `virtual void`

##### `PerformStandardKeyboardActions(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `bool`

##### `if(tabswitch)`

**Returns:** ``

##### `if(event==input::keyboard::Event::Char && Key==input::keyboard::KeyCodes::Tab)`

**Returns:** ``

##### `if(input::keyboard::Modifier::Current==input::keyboard::Modifier::None)`

**Returns:** ``

##### `FocusNext(—)`

**Returns:** ``

##### `if(input::keyboard::Modifier::Current==input::keyboard::Modifier::Shift)`

**Returns:** `else`

##### `FocusPrevious(—)`

**Returns:** ``

##### `if(accesskeysenabled)`

**Returns:** ``

##### `DistributeKeyboardEvent(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `bool`

##### `if(Focused)`

**Returns:** ``

##### `if(event==input::keyboard::Event::Up && UpHandler)`

**Returns:** ``

##### `PerformStandardKeyboardActions(event, Key)`

**Returns:** `return`

##### `setfocus(WidgetBase *widget)`

**Returns:** `bool`

##### `focus_changed(widget)`

**Returns:** ``

##### `widget_visibility_change(WidgetBase *widget, bool state)`

**Returns:** `void`

##### `FocusNext(—)`

**Returns:** ``

##### `Reorganize(—)`

**Returns:** ``

##### `call_widget_loosefocus(WidgetBase *widget, bool force=false)`

**Returns:** `bool`

##### `call_widget_locating(WidgetBase &widget, int Order)`

**Returns:** `bool`

##### `call_widget_detach(WidgetBase &widget)`

**Returns:** `bool`

##### `call_widget_located(WidgetBase &widget, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `void`

##### `call_widget_accesskeystatechanged(WidgetBase &widget)`

**Returns:** `void`

##### `call_widget_containerenabledchanged(WidgetBase &widget, bool state)`

**Returns:** `void`

