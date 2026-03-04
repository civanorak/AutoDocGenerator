# SliderBase

> Auto-generated documentation for the **SliderBase** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `floattype`

**Namespace:** `slider`


### `Base`

**Namespace:** `slider`

#### Methods

##### `SetController(smooth.controller)`

**Returns:** ``

##### `virtual` `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `setblueprint(bp)`

**Returns:** ``

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `Resize(this->bp->DefaultSize)`

**Returns:** ``

##### `clearcaches(—)`

**Returns:** ``

##### `if(this->bp)`

**Returns:** ``

##### `setupbuttons(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `virtual` `MouseHandler(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `virtual bool`

##### `if(event==input::mouse::Event::Left_Click)`

**Returns:** ``

##### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, Blueprint::Down, Blueprint::Style_None)`

**Returns:** ``

##### `value_changed(—)`

**Returns:** ``

##### `value_changed(—)`

**Returns:** ``

##### `value_changed(—)`

**Returns:** ``

##### `value_changed(—)`

**Returns:** ``

##### `value_changed(—)`

**Returns:** ``

##### `value_changed(—)`

**Returns:** ``

##### `if(event==input::mouse::Event::Move)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `if(!rule_over)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `if(rule_over)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `if(event==input::mouse::Event::Over)`

**Returns:** ``

##### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, Blueprint::Normal, Blueprint::Hover)`

**Returns:** ``

##### `if(event==input::mouse::Event::Out)`

**Returns:** ``

##### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, Blueprint::Hover, Blueprint::Normal)`

**Returns:** ``

##### `Draw(—)`

**Returns:** ``

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, Blueprint::Normal, Blueprint::Disabled)`

**Returns:** ``

##### `setstyle(Blueprint::Disabled)`

**Returns:** ``

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, Blueprint::Disabled, Blueprint::Normal)`

**Returns:** ``

##### `setstyle(Blueprint::Hover)`

**Returns:** ``

##### `setstyle(Blueprint::Normal)`

**Returns:** ``

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `playsound(Blueprint::NotFocused, Blueprint::Focused, Blueprint::Normal, Blueprint::Style_None)`

**Returns:** ``

##### `setfocus(Blueprint::Focused)`

**Returns:** ``

##### `virtual` `Draw(—)`

**Returns:** `virtual void`

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `virtual` `KeyboardHandler(input::keyboard::Event::Type event, input::keyboard::Key Key)`

**Returns:** `virtual bool`

##### `virtual` `IsVertical(—)`

**Returns:** `virtual bool`

##### `clearcaches(—)`

**Returns:** ``

##### `playsound(Blueprint::FocusType focusfrom, Blueprint::FocusType focusto, Blueprint::StyleType from, Blueprint::StyleType to)`

**Returns:** `void`

##### `if(bp)`

**Returns:** ``

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`

##### `clearcaches(—)`

**Returns:** `void`

##### `for(auto i=BorderCache.begin()`

**Returns:** ``

##### `for(auto i=ImageCache.begin()`

**Returns:** ``


### `numberformat`

**Namespace:** `slider`


### `csmooth`

**Namespace:** `slider`

#### Methods

##### `issmooth(—)`

**Returns:** `bool`


### `cdisplay`

**Namespace:** `slider`


### `cmarkers`

**Namespace:** `slider`


### `cactions`

**Namespace:** `slider`


---

## Enums

### `RuleAction`

**Namespace:** `slider`


---

## Functions

### `prepare()`

**Returns:** `void`



### `draw()`

**Returns:** `virtual void`



### `containerenabledchanged(bool state)`

**Returns:** `virtual void`



### `if(style.from == Blueprint::Disabled || style.to == Blueprint::Disabled)`

**Returns:** ``



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `setstyle(Blueprint::Disabled)`

**Returns:** ``



### `detach(ContainerBase *container)`

**Returns:** `virtual bool`



### `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`



### `if(BaseLayer)`

**Returns:** ``



### `loosefocus(bool force)`

**Returns:** `virtual bool`



### `playsound(Blueprint::Focused, Blueprint::Focus_None, Blueprint::Normal, Blueprint::Style_None)`

**Returns:** ``



### `if(!symbol_mdown)`

**Returns:** ``



### `setfocus(Blueprint::NotFocused)`

**Returns:** ``



### `setfocus(Blueprint::FocusType type)`

**Returns:** `void`



### `setstyle(Blueprint::StyleType type)`

**Returns:** `void`



### `value_changed()`

**Returns:** `virtual void`



### `setupdisplay(bool symbol, bool rule, bool indicator, bool buttons, bool value, bool invertaxis=false, bool centerindicator=false, Alignment::Type valuelocation=Alignment::Middle_Center)`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `setsmoothingmode(bool symbol, bool indicator, bool value, bool valuedisplay=true, float speed=100)`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `setmarkers(bool ticks, bool numbers, bool namedlocations, floattype tickdistance=10, int numberdistance=2)`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `setactions(bool symbol_drag, RuleAction rule_action, bool keyboard, bool tick_click=false, bool number_click=false)`

**Returns:** `void`



### `setactive()`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `setpassive()`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `ispassive()`

**Returns:** `bool`



### `instantsetvalue(T_ value)`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `setvalue(T_ value)`

**Returns:** `void`



### `if(this->value!=value || smooth.targetvalue!=value)`

**Returns:** ``



### `if(duration>0)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `setvalue_smooth(T_ value)`

**Returns:** `void`



### `value_changed()`

**Returns:** ``



### `if(smooth.targetvalue!=value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getvalue()`

**Returns:** `T_`



### `setmax(T_ m)`

**Returns:** `void`



### `if(maximum!=m)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getmax()`

**Returns:** `T_`



### `setmin(T_ m)`

**Returns:** `void`



### `if(minimum!=m)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getmin()`

**Returns:** `T_`



### `setorientation(Blueprint::OrientationType orientation)`

**Returns:** `void`



### `Draw()`

**Returns:** ``



### `getorientation()`

**Returns:** `Blueprint::OrientationType`



### `ishorizontal()`

**Returns:** `bool`



### `return(orientation==Blueprint::Top || orientation==Blueprint::Bottom || orientation==Blueprint::Horizontal)`

**Returns:** ``



### `isvertical()`

**Returns:** `bool`



### `return(orientation==Blueprint::Left || orientation==Blueprint::Right || orientation==Blueprint::Vertical)`

**Returns:** ``



### `setsmoothingspeed(float speed)`

**Returns:** `void`



### `getsmoothingspeed()`

**Returns:** `float`



### `gettargetvalue()`

**Returns:** `T_`



### `setshowticks(bool ticks)`

**Returns:** `void`



### `if(ticks!=markers.ticks)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getshowticks()`

**Returns:** `bool`



### `setshowvalue(bool value)`

**Returns:** `void`



### `if(value!=display.value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getshowvalue()`

**Returns:** `bool`



### `settickdistance(floattype distance)`

**Returns:** `void`



### `if(markers.tickdistance!=distance)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `gettickdistance()`

**Returns:** `floattype`



### `setshownumbers(bool numbers)`

**Returns:** `void`



### `if(numbers!=markers.numbers)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getshownumbers()`

**Returns:** `bool`



### `setnumberdistance(int distance)`

**Returns:** `void`



### `if(markers.numberdistance!=distance)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getnumberdistance()`

**Returns:** `int`



### `setsmallchange(T_ smallchange)`

**Returns:** `void`



### `getsmallchange()`

**Returns:** `T_`



### `setlargechange(T_ largechange)`

**Returns:** `void`



### `getlargechange()`

**Returns:** `T_`



### `setsteps(T_ steps)`

**Returns:** `void`



### `setvalue(v)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `getsteps()`

**Returns:** `T_`



### `setnumberformat(numberformat value)`

**Returns:** `void`



### `if(format!=value && markers.numbers)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getnumberformat()`

**Returns:** `numberformat`



### `setvalueformat(numberformat value)`

**Returns:** `void`



### `if(valueformat!=value && display.value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getvalueformat()`

**Returns:** `numberformat`



### `setvaluelocation(Alignment::Type value)`

**Returns:** `void`



### `if(valuelocation!=value && display.value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getvaluelocation()`

**Returns:** `Alignment::Type`



### `setautosize(const AutosizeModes::Type &value)`

**Returns:** `void`



### `getautosize()`

**Returns:** `AutosizeModes::Type`



### `setkeyrepeattimeout(const int &value)`

**Returns:** `void`



### `getkeyrepeattimeout()`

**Returns:** `int`



### `setaxisinverse(const bool &value)`

**Returns:** `void`



### `if(display.inverseaxis!=value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getaxisinverse()`

**Returns:** `bool`



### `setcenterindicator(const bool &value)`

**Returns:** `void`



### `if(display.centerindicator!=value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getcenterindicator()`

**Returns:** `T_`



### `setindicatorstart(const T_ &value)`

**Returns:** `void`



### `if(indst_value!=value)`

**Returns:** ``



### `if(smooth.indicator && display.indicatorstart)`

**Returns:** ``



### `if(duration>0)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getindicatorstart()`

**Returns:** `T_`



### `setshowindicatorstart(const bool &value)`

**Returns:** `void`



### `if(display.indicatorstart!=value)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `getshowindicatorstart()`

**Returns:** `bool`



### `setcangetfocus(const bool &value)`

**Returns:** `void`



### `RemoveFocus()`

**Returns:** ``



### `getcangetfocus()`

**Returns:** `bool`



### `smallincrease()`

**Returns:** `void`



### `setvalue_smooth(value-smallchange)`

**Returns:** ``



### `setvalue_smooth(value+smallchange)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `smalldecrease()`

**Returns:** `void`



### `setvalue_smooth(value+smallchange)`

**Returns:** ``



### `setvalue_smooth(value-smallchange)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `largeincrease()`

**Returns:** `void`



### `setvalue_smooth(value-largechange)`

**Returns:** ``



### `setvalue_smooth(value+largechange)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `largedecrease()`

**Returns:** `void`



### `setvalue_smooth(value+largechange)`

**Returns:** ``



### `setvalue_smooth(value-largechange)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `tomax()`

**Returns:** `void`



### `if(display.inverseaxis)`

**Returns:** ``



### `setvalue_smooth(minimum)`

**Returns:** ``



### `setvalue_smooth(maximum)`

**Returns:** ``



### `tomin()`

**Returns:** `void`



### `if(display.inverseaxis)`

**Returns:** ``



### `setvalue_smooth(maximum)`

**Returns:** ``



### `setvalue_smooth(minimum)`

**Returns:** ``



### `begin_goup()`

**Returns:** `void`



### `begin_godown()`

**Returns:** `void`



### `end_goup()`

**Returns:** `void`



### `end_godown()`

**Returns:** `void`



### `symbol_mouse(input::mouse::Event::Type event, utils::Point location, int amount)`

**Returns:** `bool`



### `if(event==input::mouse::Event::Left_Down)`

**Returns:** ``



### `setstyle(Blueprint::Down)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(event==input::mouse::Event::Move && symbol_mdown)`

**Returns:** `else`



### `if(location!=symbol_mdownpos)`

**Returns:** ``



### `setvalue(v)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(event==input::mouse::Event::Left_Up)`

**Returns:** `else`



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `if(event==input::mouse::Event::Over)`

**Returns:** `else`



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `if(event==input::mouse::Event::Out)`

**Returns:** `else`



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `upbutton_mouse(input::mouse::Event event)`

**Returns:** `void`



### `if(event.event==input::mouse::Event::Left_Down)`

**Returns:** ``



### `Focus()`

**Returns:** ``



### `if(!goingup)`

**Returns:** ``



### `smalldecrease()`

**Returns:** ``



### `begin_goup()`

**Returns:** ``



### `if(event.event==input::mouse::Event::Right_Down)`

**Returns:** `else`



### `Focus()`

**Returns:** ``



### `if(!goingup)`

**Returns:** ``



### `largedecrease()`

**Returns:** ``



### `begin_goup()`

**Returns:** ``



### `end_goup()`

**Returns:** ``



### `downbutton_mouse(input::mouse::Event event)`

**Returns:** `void`



### `Focus()`

**Returns:** ``



### `if(event.event==input::mouse::Event::Left_Down)`

**Returns:** ``



### `if(!goingup)`

**Returns:** ``



### `smallincrease()`

**Returns:** ``



### `begin_godown()`

**Returns:** ``



### `if(event.event==input::mouse::Event::Right_Down)`

**Returns:** `else`



### `if(!goingup)`

**Returns:** ``



### `largeincrease()`

**Returns:** ``



### `begin_godown()`

**Returns:** ``



### `end_godown()`

**Returns:** ``



### `Progress()`

**Returns:** `virtual animation::ProgressResult::Type`



### `if(smooth.stepvalue>0 && smoothvalue>=smooth.targetvalue)`

**Returns:** ``



### `if(smooth.stepvalue<0 && smoothvalue<=smooth.targetvalue)`

**Returns:** `else`



### `if(smooth.value)`

**Returns:** ``



### `if(value!=smoothvalue)`

**Returns:** ``



### `value_changed()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(smooth.indst_stepvalue>0 && indst_smoothvalue>=smooth.indst_targetvalue)`

**Returns:** ``



### `if(smooth.indst_stepvalue<0 && indst_smoothvalue<=smooth.indst_targetvalue)`

**Returns:** `else`



### `Draw()`

**Returns:** ``



### `if(golarge)`

**Returns:** ``



### `if(goingup)`

**Returns:** ``



### `largedecrease()`

**Returns:** ``



### `if(goingdown)`

**Returns:** ``



### `largeincrease()`

**Returns:** ``



### `if(goingup)`

**Returns:** ``



### `smalldecrease()`

**Returns:** ``



### `if(goingdown)`

**Returns:** ``



### `smallincrease()`

**Returns:** ``



### `addnamedlocation(T_ location, const std::string &name="")`

**Returns:** `void`



### `removenamedlocation(T_ location)`

**Returns:** `void`



### `gettickvalue(int x)`

**Returns:** `T_`



### `gettextvalue(int x)`

**Returns:** `T_`



### `getrulevalue(int x)`

**Returns:** `T_`



### `focus_anim_finished()`

**Returns:** `void`



### `style_anim_finished()`

**Returns:** `void`



### `setupbuttons()`

**Returns:** `void`



### `drawtick(floattype v, utils::Point &location, bool reverse, utils::Size &size)`

**Returns:** `void`



### `drawtext(floattype v, Alignment::Type align, const std::string &str, utils::Bounds &inner, utils::Point &location, bool reverse, utils::Size &size)`

**Returns:** `void`



### `drawvalue(utils::Bounds &inner, int distance, bool reverse)`

**Returns:** `int`



### `printvalue(int x, int y, int w)`

**Returns:** `void`



### `if(actions.rule_action==LargeChange)`

**Returns:** ``



### `if(v>value)`

**Returns:** ``



### `if(markers.namedlocations)`

**Returns:** ``



### `for(auto i=namedlocations.begin()`

**Returns:** ``



### `if(d<mindist && i->second!="")`

**Returns:** ``



### `T_(v)`

**Returns:** `return`



### `if(markers.namedlocations)`

**Returns:** ``



### `for(auto i=namedlocations.begin()`

**Returns:** ``



### `if(d<mindist)`

**Returns:** ``



### `T_(v)`

**Returns:** `return`



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(next_style!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from!=Blueprint::Normal)`

**Returns:** ``



### `if(next_style==Blueprint::Disabled)`

**Returns:** ``



### `if(style.from==Blueprint::Disabled)`

**Returns:** `else`



### `if(next_style!=Blueprint::Normal)`

**Returns:** ``



### `setstyle(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(next_focus!=Blueprint::Focus_None)`

**Returns:** ``



### `setfocus(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(!bp)`

**Returns:** ``



### `if(focus.from!=type || focus.to!=Blueprint::Focus_None)`

**Returns:** ``



### `if(info)`

**Returns:** ``



### `if(focus.from==type)`

**Returns:** ``



### `if(focus.to==type)`

**Returns:** `else`



### `if(info.duration==-2)`

**Returns:** ``



### `if(info.duration==0)`

**Returns:** `else`



### `Draw()`

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



### `if(style.from!=Blueprint::Normal)`

**Returns:** ``



### `if(next_style==Blueprint::Disabled)`

**Returns:** ``



### `if(style.from==Blueprint::Disabled)`

**Returns:** `else`



### `if(next_style!=Blueprint::Normal)`

**Returns:** ``



### `setstyle(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `prepare()`

**Returns:** ``



### `if(autosize!=AutosizeModes::None)`

**Returns:** ``



### `if(rule && display.rule)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(display.buttons)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(rule && display.rule)`

**Returns:** ``



### `if(tick && markers.ticks)`

**Returns:** ``



### `if(font && markers.numbers)`

**Returns:** ``



### `if(rule && display.rule)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(display.buttons)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(rule && display.rule)`

**Returns:** ``



### `if(tick && markers.ticks)`

**Returns:** ``



### `if(display.buttons)`

**Returns:** ``



### `if(font && markers.numbers)`

**Returns:** ``



### `if(textp)`

**Returns:** ``



### `if(display.value && valuefont)`

**Returns:** ``



### `if(autosize==AutosizeModes::GrowOnly)`

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



### `if(iprovider)`

**Returns:** ``



### `if(iprovider)`

**Returns:** ``



### `if(iprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(display.buttons)`

**Returns:** ``



### `if(upbutton)`

**Returns:** ``



### `if(downbutton)`

**Returns:** ``



### `if(upbutton)`

**Returns:** ``



### `if(downbutton)`

**Returns:** ``



### `if(rule)`

**Returns:** ``



### `if(rule)`

**Returns:** ``



### `if(display.centerindicator)`

**Returns:** ``



### `if(orientation==Blueprint::Top || orientation==Blueprint::Left)`

**Returns:** `else`



### `drawvalue(inner, distance, reverse)`

**Returns:** ``



### `if(display.rule && rule)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(display.indicator && indicator)`

**Returns:** ``



### `if(smooth.indicator)`

**Returns:** ``



### `if(rule && display.rule)`

**Returns:** ``



### `if(rule)`

**Returns:** ``



### `if(display.indicatorstart)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(indst>indval)`

**Returns:** ``



### `if(indst>indval)`

**Returns:** ``



### `if(display.centerindicator)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** `else`



### `if(rule)`

**Returns:** ``



### `if(display.indicatorstart)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(indst>indval)`

**Returns:** ``



### `if(indst>indval)`

**Returns:** ``



### `if(display.centerindicator)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** `else`



### `if(rule && display.rule)`

**Returns:** ``



### `if(valuep)`

**Returns:** ``



### `if(valuep)`

**Returns:** ``



### `if(valuep)`

**Returns:** ``



### `printvalue(x, y, w)`

**Returns:** ``



### `if(tickmarkborder)`

**Returns:** ``



### `if(markers.ticks && markers.tickdistance && tick)`

**Returns:** ``



### `if(tickp)`

**Returns:** ``



### `if(markers.numbers && markers.tickdistance && markers.numberdistance && font)`

**Returns:** ``



### `if(tickp)`

**Returns:** ``



### `if(sz>0)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(markers.ticks && markers.tickdistance && tick)`

**Returns:** ``



### `p(0, 0)`

**Returns:** `Point`



### `if(tickp)`

**Returns:** ``



### `if(tickp && rule)`

**Returns:** ``



### `switch(orientation)`

**Returns:** ``



### `if(insiderule)`

**Returns:** ``



### `if(display.centerindicator)`

**Returns:** ``



### `if(markers.namedlocations)`

**Returns:** ``



### `for(auto i=namedlocations.begin()`

**Returns:** ``



### `for(floattype v=st;v<=ed;v+=markers.tickdistance)`

**Returns:** ``



### `drawtick(v, location, reverse, size)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(tickp)`

**Returns:** ``



### `if(markers.numbers && markers.tickdistance && markers.numberdistance && font)`

**Returns:** ``



### `p(0, 0)`

**Returns:** `Point`



### `if(textp)`

**Returns:** ``



### `if(markers.namedlocations)`

**Returns:** ``



### `for(auto i=namedlocations.begin()`

**Returns:** ``



### `drawtext(v, align, str, inner, location, reverse, size)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(textp)`

**Returns:** ``



### `if(ruleoverlay && display.rule)`

**Returns:** ``



### `if(symbol && display.symbol)`

**Returns:** ``



### `p(0, 0)`

**Returns:** `Point`



### `if(symbolp)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(overlay)`

**Returns:** ``



### `if(display.buttons)`

**Returns:** ``



### `if(bp)`

**Returns:** ``



### `if(!goingup)`

**Returns:** ``



### `smalldecrease()`

**Returns:** ``



### `begin_goup()`

**Returns:** ``



### `end_goup()`

**Returns:** ``



### `if(!goingdown)`

**Returns:** ``



### `smallincrease()`

**Returns:** ``



### `begin_godown()`

**Returns:** ``



### `end_godown()`

**Returns:** ``



### `if(event==Event::Down && Key==KeyCodes::PageUp)`

**Returns:** ``



### `if(!goingup)`

**Returns:** ``



### `largedecrease()`

**Returns:** ``



### `begin_goup()`

**Returns:** ``



### `if(event==Event::Up	&& Key==KeyCodes::PageUp)`

**Returns:** ``



### `end_goup()`

**Returns:** ``



### `if(event==Event::Down && Key==KeyCodes::PageDown)`

**Returns:** ``



### `if(!goingdown)`

**Returns:** ``



### `largeincrease()`

**Returns:** ``



### `begin_godown()`

**Returns:** ``



### `if(event==Event::Up	&& Key==KeyCodes::PageDown)`

**Returns:** ``



### `end_godown()`

**Returns:** ``



### `if(event==Event::Up && Key==KeyCodes::Home)`

**Returns:** ``



### `tomin()`

**Returns:** ``



### `if(event==Event::Up && Key==KeyCodes::End)`

**Returns:** ``



### `tomax()`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(display.centerindicator)`

**Returns:** ``



### `if(v!=minimum)`

**Returns:** ``



### `if(reverse)`

**Returns:** `else`



### `if(display.inverseaxis)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(rule)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(display.inverseaxis)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(reverse)`

**Returns:** ``



### `if(valuep)`

**Returns:** ``



### `printvalue(x, y, w)`

**Returns:** ``



### `if(display.indicatorstart)`

**Returns:** ``



### `if(smooth.valuedisplay)`

**Returns:** ``



### `if(indst<v)`

**Returns:** ``


