# PanelBase

> Auto-generated documentation for the **PanelBase** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Base`

**Namespace:** `panel`

#### Methods

##### `Base(—)`

**Returns:** ``

##### `clearcaches(—)`

**Returns:** ``

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

##### `virtual` `Show(bool setfocus=true)`

**Returns:** `virtual void`

##### `virtual` `Hide(—)`

**Returns:** `virtual void`

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_containerenabledchanged(*it, true)`

**Returns:** ``

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `setstyle(widgets::Blueprint::Disabled)`

**Returns:** ``

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_containerenabledchanged(*it, false)`

**Returns:** ``

##### `virtual` `IsActive(—)`

**Returns:** `virtual bool`

##### `virtual` `RedrawAll(—)`

**Returns:** `virtual void`

##### `virtual` `Resize(utils::Size Size)`

**Returns:** `virtual void`

##### `adjustcontrols(—)`

**Returns:** ``

##### `Resize(int W, int H)`

**Returns:** `void`

##### `virtual` `SetContentSize(utils::Size Size)`

**Returns:** `virtual void`

##### `SetContentSize(int W, int H)`

**Returns:** `void`

##### `virtual` `Draw(—)`

**Returns:** `virtual void`

##### `virtual` `GetUsableSize(—)`

**Returns:** `virtual utils::Size`

##### `prepare(—)`

**Returns:** ``

##### `virtual` `GetOverheadMargins(—)`

**Returns:** `virtual utils::Margins`

##### `prepare(—)`

**Returns:** ``

##### `virtual` `RemoveFocus(—)`

**Returns:** `virtual bool`

##### `virtual` `Deactivate(—)`

**Returns:** `virtual void`

##### `RemoveFocus(—)`

**Returns:** ``

##### `MoveBy(utils::Point amount)`

**Returns:** `void`

##### `virtual` `Move(utils::Point Location)`

**Returns:** `virtual void`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `if(!Focused)`

**Returns:** ``

##### `if(!allownofocus)`

**Returns:** ``

##### `FocusFirst(—)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Active)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Active)`

**Returns:** ``

##### `virtual` `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `setblueprint(bp)`

**Returns:** ``

##### `virtual` `MouseHandler(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `virtual bool`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `virtual` `WidgetBoundsChanged(—)`

**Returns:** `virtual void`

##### `adjustscrolls(—)`

**Returns:** ``

##### `virtual` `AbsoluteLocation(—)`

**Returns:** `virtual utils::Point`

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `clearcaches(—)`

**Returns:** `void`

##### `adjustlayers(—)`

**Returns:** `void`

##### `adjustscrolls(—)`

**Returns:** `void`

##### `adjustcontrols(—)`

**Returns:** `void`

##### `virtual` `calculatevscrollback(int usableheight)`

**Returns:** `virtual int`

##### `for(auto i=Widgets.First()`

**Returns:** ``

##### `prepare(—)`

**Returns:** `void`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `freeze(—)`

**Returns:** `void`

##### `unfreeze(—)`

**Returns:** `void`

##### `adjustscrolls(—)`

**Returns:** ``

##### `virtual` `focus_changed(WidgetBase *newwidget)`

**Returns:** `virtual void`

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `if(!Focused)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `if(force)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `virtual` `detach(ContainerBase *container)`

**Returns:** `virtual bool`

##### `virtual` `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `adjustcontrols(—)`

**Returns:** ``

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `if(style.from == widgets::Blueprint::Disabled || style.to == widgets::Blueprint::Disabled)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Disabled)`

**Returns:** ``

##### `for(auto it=Widgets.First()`

**Returns:** ``

##### `call_widget_containerenabledchanged(*it, state)`

**Returns:** ``

##### `setupvscroll(bool allow, bool show, bool autohide, bool dragscroll=false)`

**Returns:** `void`

##### `adjustscrolls(—)`

**Returns:** ``

##### `setallowmove(const bool &value)`

**Returns:** `void`

##### `getallowmove(—)`

**Returns:** `bool`

##### `setshowtitle(bool value)`

**Returns:** `void`

##### `if(value!=showtitle)`

**Returns:** ``

##### `adjustcontrols(—)`

**Returns:** ``

##### `Reorganize(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getshowtitle(—)`

**Returns:** `bool`

##### `settitle(const std::string &value)`

**Returns:** `void`

##### `if(title.Text!=value)`

**Returns:** ``

##### `gettitle(—)`

**Returns:** `std::string`

##### `seticon(graphics::RectangularGraphic2D *value)`

**Returns:** `void`

##### `setallowresize(const bool &value)`

**Returns:** `void`

##### `getallowresize(—)`

**Returns:** `bool`

##### `setallownofocus(const bool &value)`

**Returns:** `void`

##### `getallownofocus(—)`

**Returns:** `bool`

##### `setpadding(const utils::Margins &value)`

**Returns:** `void`

##### `Reorganize(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getpadding(—)`

**Returns:** `utils::Margins`

##### `setallowvscroll(const bool &value)`

**Returns:** `void`

##### `if(vscroll.allow!=value)`

**Returns:** ``

##### `if(!vscroll.allow && scroll.y)`

**Returns:** ``

##### `vscrollto(0)`

**Returns:** ``

##### `adjustscrolls(—)`

**Returns:** ``

##### `getallowvscroll(—)`

**Returns:** `bool`

##### `setshowvscroll(bool value)`

**Returns:** `void`

##### `if(vscroll.show!=value)`

**Returns:** ``

##### `adjustscrolls(—)`

**Returns:** ``

##### `Reorganize(—)`

**Returns:** ``

##### `getshowvscroll(—)`

**Returns:** `bool`

##### `setsetautohidevscroll(const bool &value)`

**Returns:** `void`

##### `if(vscroll.autohide!=value)`

**Returns:** ``

##### `adjustscrolls(—)`

**Returns:** ``

##### `getsetautohidevscroll(—)`

**Returns:** `bool`

##### `setallowtabswitch(const bool &value)`

**Returns:** `void`

##### `getallowtabswitch(—)`

**Returns:** `bool`

##### `setdisplay(const bool &value)`

**Returns:** `void`

##### `if(display!=value)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getdisplay(—)`

**Returns:** `bool`

##### `if(showtitlebtn!=value)`

**Returns:** ``

##### `adjustcontrols(—)`

**Returns:** ``

##### `getshowtitlebtn(—)`

**Returns:** `bool`

##### `setshowdialogbtn(const bool &value)`

**Returns:** `void`

##### `if(showdialogbtn!=value)`

**Returns:** ``

##### `adjustcontrols(—)`

**Returns:** ``

##### `getshowdialogbtn(—)`

**Returns:** `bool`

##### `getcontrolmargins(—)`

**Returns:** `utils::Margins`

##### `placetitlebutton(WidgetBase &btn)`

**Returns:** `void`

##### `adjustcontrols(—)`

**Returns:** ``

##### `Reorganize(—)`

**Returns:** ``

##### `placedialogbutton(WidgetBase &btn)`

**Returns:** `void`

##### `adjustcontrols(—)`

**Returns:** ``

##### `Reorganize(—)`

**Returns:** ``

##### `style_anim_finished(—)`

**Returns:** `void`

##### `setstyle(Blueprint::StyleType type)`

**Returns:** `void`

##### `vscrollto(int where)`

**Returns:** `void`

##### `vscrollby(int amount)`

**Returns:** `void`

##### `getvscroll(—)`

**Returns:** `int`

##### `virtual` `vscroll_change(—)`

**Returns:** `virtual void`

##### `ScrollingEvent(allow)`

**Returns:** ``

##### `if(!allow)`

**Returns:** ``

##### `adjustlayers(—)`

**Returns:** ``

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`


### `cscroll`

**Namespace:** `panel`


---

## Functions

### `prepare()`

**Returns:** ``



### `adjustlayers()`

**Returns:** ``



### `if(outerborder)`

**Returns:** ``



### `if(overlay)`

**Returns:** ``



### `if(outerborder)`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(next_style!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from!=widgets::Blueprint::Normal)`

**Returns:** ``



### `if(next_style==widgets::Blueprint::Disabled)`

**Returns:** ``



### `if(style.from==widgets::Blueprint::Disabled)`

**Returns:** `else`



### `if(next_style!=widgets::Blueprint::Normal)`

**Returns:** ``



### `setstyle(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(!bp)`

**Returns:** ``



### `if(style.from!=type || style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from!=type && style.to!=type && style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(info)`

**Returns:** ``



### `if(style.from==type)`

**Returns:** ``



### `if(style.to==type)`

**Returns:** `else`



### `if(info.duration==-2)`

**Returns:** ``



### `if(next_style!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from!=widgets::Blueprint::Normal)`

**Returns:** ``



### `if(next_style==widgets::Blueprint::Disabled)`

**Returns:** ``



### `if(style.from==widgets::Blueprint::Disabled)`

**Returns:** `else`



### `if(next_style!=widgets::Blueprint::Normal)`

**Returns:** ``



### `setstyle(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `prepare()`

**Returns:** ``



### `if(display)`

**Returns:** ``



### `if(innerborder)`

**Returns:** ``



### `if(scrollingborder)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(newwidget)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(vscroll.allow)`

**Returns:** ``



### `adjustlayers()`

**Returns:** ``



### `adjustlayers()`

**Returns:** ``



### `if(!allownofocus)`

**Returns:** `else`



### `RemoveFocus()`

**Returns:** ``



### `if(event==input::mouse::Event::Left_Down)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(allowmove)`

**Returns:** ``



### `if(event==input::mouse::Event::Left_Down)`

**Returns:** ``



### `if(event==input::mouse::Event::Move)`

**Returns:** ``



### `if(move_mdown && !move_ongoing)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Moving)`

**Returns:** ``



### `if(move_ongoing)`

**Returns:** ``



### `MoveBy(location-move_mlocation)`

**Returns:** ``



### `if(event==input::mouse::Event::Left_Up)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Active)`

**Returns:** ``



### `vscrollby(-amount)`

**Returns:** ``



### `adjustlayers()`

**Returns:** ``



### `adjustlayers()`

**Returns:** ``



### `adjustlayers()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(Container)`

**Returns:** ``



### `prepare()`

**Returns:** ``



### `bordermargins(0)`

**Returns:** `Margins`



### `if(outerborder)`

**Returns:** ``



### `if(innerborder)`

**Returns:** ``



### `align(Alignment::Middle_Right)`

**Returns:** `Alignment::Type`



### `margins(0)`

**Returns:** `Margins`



### `if(this->bp && this->bp->TitleButtonPlace)`

**Returns:** ``



### `for(auto i=titlebuttons.Last()`

**Returns:** ``



### `for(auto i=titlebuttons.Last()`

**Returns:** ``



### `align(Alignment::Middle_Right)`

**Returns:** `Alignment::Type`



### `margins(0)`

**Returns:** `Margins`



### `if(this->bp && this->bp->DialogButtonPlace)`

**Returns:** ``



### `for(auto i=dialogbuttons.Last()`

**Returns:** ``



### `for(auto i=dialogbuttons.Last()`

**Returns:** ``



### `if(showtitle)`

**Returns:** ``



### `adjustscrolls()`

**Returns:** ``



### `clearcaches()`

**Returns:** ``



### `for(auto i=titlebuttons.begin()`

**Returns:** ``



### `for(auto i=dialogbuttons.begin()`

**Returns:** ``



### `if(this->bp)`

**Returns:** ``



### `adjustcontrols()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `for(auto i=BorderCache.begin()`

**Returns:** ``



### `for(auto i=ImageCache.begin()`

**Returns:** ``


