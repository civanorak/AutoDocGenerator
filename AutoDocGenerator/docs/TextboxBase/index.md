# TextboxBase

> Auto-generated documentation for the **TextboxBase** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Base`

**Namespace:** `textbox`

#### Methods

##### `virtual` `IsVisible(—)`

**Returns:** `virtual bool`

##### `virtual` `IsEnabled(—)`

**Returns:** `virtual bool`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `virtual` `Draw(—)`

**Returns:** `virtual void`

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `virtual` `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `setblueprint(bp)`

**Returns:** ``

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `virtual` `MouseHandler(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `virtual bool`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `adjustscrolls(—)`

**Returns:** `void`

##### `prepare(—)`

**Returns:** `void`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `clearcaches(—)`

**Returns:** `void`

##### `virtual` `detach(ContainerBase *container)`

**Returns:** `virtual bool`

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `if(style.from == widgets::Blueprint::Disabled || style.to == widgets::Blueprint::Disabled)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Disabled)`

**Returns:** ``

##### `virtual` `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `if(BaseLayer)`

**Returns:** ``

##### `setupvscroll(bool allow, bool show, bool autohide)`

**Returns:** `void`

##### `adjustscrolls(—)`

**Returns:** ``

##### `settext(const std::string &value)`

**Returns:** `void`

##### `if(text!=value)`

**Returns:** ``

##### `if(caretlocation==l)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `gettext(—)`

**Returns:** `std::string`

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

##### `setcaretlocation(int location)`

**Returns:** `void`

##### `if(caretlocation!=location)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getcaretlocation(—)`

**Returns:** `int`

##### `setselection(int start, int end)`

**Returns:** `void`

##### `if(selectionstart!=start || caretlocation!=end)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getselectionstart(—)`

**Returns:** `int`

##### `setprefix(const std::string &value)`

**Returns:** `void`

##### `if(prefix!=value)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getprefix(—)`

**Returns:** `std::string`

##### `setsuffix(const std::string &value)`

**Returns:** `void`

##### `if(suffix!=value)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getsuffix(—)`

**Returns:** `std::string`

##### `makepassive(—)`

**Returns:** `void`

##### `if(!passive)`

**Returns:** ``

##### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `makeactive(—)`

**Returns:** `void`

##### `if(passive)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `setpassive(const bool &value)`

**Returns:** `void`

##### `getpassive(—)`

**Returns:** `bool`

##### `setreadonly(const bool &value)`

**Returns:** `void`

##### `if(readonly!=value)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getreadonly(—)`

**Returns:** `bool`

##### `setnoselection(const bool &value)`

**Returns:** `void`

##### `if(noselection!=value)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `getnoselection(—)`

**Returns:** `bool`

##### `virtual` `textchanged(—)`

**Returns:** `virtual void`

##### `virtual` `validatetext(std::string &str)`

**Returns:** `virtual void`

##### `style_anim_finished(—)`

**Returns:** `void`

##### `setstyle(Blueprint::StyleType type)`

**Returns:** `void`

##### `vscrollto(int where)`

**Returns:** `void`

##### `vscrollby(int amount)`

**Returns:** `void`

##### `virtual` `vscroll_change(—)`

**Returns:** `virtual void`

##### `if(vscroll.bar.Value!=-scroll.y)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `playsound(Blueprint::StyleType stylefrom, Blueprint::StyleType styleto)`

**Returns:** `void`

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`


### `cscroll`

**Namespace:** `textbox`


---

## Functions

### `prepare()`

**Returns:** ``



### `if(outerborder)`

**Returns:** ``



### `if(innerborder)`

**Returns:** ``



### `if(font)`

**Returns:** ``



### `if(text!="")`

**Returns:** ``



### `caretposition(0, 0)`

**Returns:** `Point`



### `if(caret)`

**Returns:** ``



### `if(selstart!=selend && selection)`

**Returns:** ``



### `selb(eprint[1].Out.position, eprint[2].Out.position)`

**Returns:** `Bounds`



### `caretposition(0, 0)`

**Returns:** `Point`



### `caretsize(0, 0)`

**Returns:** `Size`



### `if(caret)`

**Returns:** ``



### `if(caret)`

**Returns:** ``



### `if(overlay)`

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



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `lastlocation(0, 0)`

**Returns:** `static Point`



### `if(event==Event::Left_Down)`

**Returns:** ``



### `if(font)`

**Returns:** ``



### `if(event==Event::Move && mdown)`

**Returns:** ``



### `if(lastlocation!=location)`

**Returns:** ``



### `if(event==Event::Left_Up)`

**Returns:** ``



### `if(event==Event::Over)`

**Returns:** ``



### `playsound(widgets::Blueprint::Normal, widgets::Blueprint::Hover)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Hover)`

**Returns:** ``



### `if(event==Event::Out)`

**Returns:** ``



### `playsound(widgets::Blueprint::Hover, widgets::Blueprint::Normal)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``



### `if(vscroll.allow && event==Event::VScroll)`

**Returns:** ``



### `vscrollby(-amount)`

**Returns:** ``



### `if(passive)`

**Returns:** ``



### `if(event==Event::Down && Modifier::Current==Modifier::None)`

**Returns:** ``



### `if(Key==input::keyboard::KeyCodes::Enter)`

**Returns:** ``



### `AcceptEvent()`

**Returns:** ``



### `if(Key==KeyCodes::Left)`

**Returns:** ``



### `setcaretlocation(caretlocation-1)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::Right)`

**Returns:** ``



### `setcaretlocation(caretlocation+1)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::Home)`

**Returns:** ``



### `setcaretlocation(0)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::End)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::Delete)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(caretlocation!=selectionstart)`

**Returns:** ``



### `if(selectionstart<caretlocation)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `if(event==Event::Down && Modifier::Current==Modifier::Shift)`

**Returns:** ``



### `if(Key==KeyCodes::Left)`

**Returns:** ``



### `setselection(selectionstart, caretlocation-1)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::Right)`

**Returns:** ``



### `setselection(selectionstart, caretlocation+1)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::Home)`

**Returns:** ``



### `setselection(selectionstart, 0)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(Key==KeyCodes::End)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(!readonly && Key==KeyCodes::Backspace)`

**Returns:** ``



### `if(caretlocation!=selectionstart)`

**Returns:** ``



### `if(selectionstart<caretlocation)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `if(caretlocation)`

**Returns:** `else`



### `setcaretlocation(caretlocation-1)`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `if(!readonly)`

**Returns:** `else`



### `if(Key >= 32 && allow)`

**Returns:** ``



### `if(caretlocation!=selectionstart)`

**Returns:** ``



### `if(selectionstart<caretlocation)`

**Returns:** ``



### `validatetext(s)`

**Returns:** ``



### `if(s!="")`

**Returns:** ``



### `setcaretlocation(caretlocation+1)`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `if(event==Event::Down && Modifier::Current==Modifier::Ctrl)`

**Returns:** ``



### `if(Key=='a' || Key=='A')`

**Returns:** ``



### `validatetext(s)`

**Returns:** ``



### `if(s!="")`

**Returns:** ``



### `if(caretlocation!=selectionstart)`

**Returns:** ``



### `if(selectionstart<caretlocation)`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `if(Key=='c' || Key=='C')`

**Returns:** `else`



### `if(caretlocation!=selectionstart)`

**Returns:** ``



### `if(selectionstart<caretlocation)`

**Returns:** ``



### `if(caretlocation!=selectionstart)`

**Returns:** ``



### `if(selectionstart<caretlocation)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `textchanged()`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(bp->Mapping[stylefrom][styleto] && bp->Mapping[stylefrom][styleto]->Sound)`

**Returns:** ``



### `playsound(widgets::Blueprint::Normal, Blueprint::Active)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Focused_Style)`

**Returns:** ``



### `playsound(widgets::Blueprint::Disabled, widgets::Blueprint::Normal)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``



### `playsound(widgets::Blueprint::Normal, widgets::Blueprint::Disabled)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Disabled)`

**Returns:** ``



### `playsound(widgets::Blueprint::Active, widgets::Blueprint::Active)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Hover)`

**Returns:** ``



### `setstyle(widgets::Blueprint::Normal)`

**Returns:** ``



### `AcceptEvent()`

**Returns:** ``



### `clearcaches()`

**Returns:** ``



### `if(this->bp)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `for(auto i=BorderCache.begin()`

**Returns:** ``



### `for(auto i=ImageCache.begin()`

**Returns:** ``


