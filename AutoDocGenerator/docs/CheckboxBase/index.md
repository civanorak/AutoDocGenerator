# CheckboxBase

&gt; Auto-generated documentation for the **CheckboxBase** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `Base`

**Namespace:** `checkbox`

#### Methods

##### `draw(—)`

**Returns:** ``

##### `virtual` `SetBlueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `setblueprint(bp)`

**Returns:** ``

##### `virtual` `Focus(—)`

**Returns:** `virtual bool`

##### `virtual` `Disable(—)`

**Returns:** `virtual void`

##### `virtual` `Enable(—)`

**Returns:** `virtual void`

##### `virtual` `Draw(—)`

**Returns:** `virtual void`

##### `virtual` `GetSize(—)`

**Returns:** `virtual utils::Size`

##### `clearcaches(—)`

**Returns:** ``

##### `virtual` `prepare(—)`

**Returns:** `virtual void`

##### `virtual` `wr_loaded(—)`

**Returns:** `virtual void`

##### `virtual` `draw(—)`

**Returns:** `virtual void`

##### `lineheight(Blueprint::Line *line, int w=0)`

**Returns:** `int`

##### `drawline(int id, Blueprint::TransitionType transition, int y, int reqh, int h)`

**Returns:** `void`

##### `virtual` `setblueprint(const widgets::Blueprint &bp)`

**Returns:** `virtual void`

##### `clearcaches(—)`

**Returns:** `void`

##### `setstate(int state)`

**Returns:** `void`

##### `getstate(—)`

**Returns:** `int`

##### `setfocus(Blueprint::FocusType type)`

**Returns:** `void`

##### `setstyle(Blueprint::StyleType type)`

**Returns:** `void`

##### `down(—)`

**Returns:** `void`

##### `up(—)`

**Returns:** `void`

##### `click(—)`

**Returns:** `void`

##### `triggerwait(—)`

**Returns:** `void`

##### `over(—)`

**Returns:** `void`

##### `out(—)`

**Returns:** `void`

##### `setautosize(AutosizeModes::Type autosize)`

**Returns:** `void`

##### `Draw(—)`

**Returns:** ``

##### `getautosize(—)`

**Returns:** `AutosizeModes::Type`

##### `settextwrap(bool textwrap)`

**Returns:** `void`

##### `Draw(—)`

**Returns:** ``

##### `gettextwrap(—)`

**Returns:** `bool`

##### `settext(const std::string &text)`

**Returns:** `void`

##### `Draw(—)`

**Returns:** ``

##### `gettext(—)`

**Returns:** `std::string`

##### `setunderline(input::keyboard::Key key)`

**Returns:** `void`

##### `Draw(—)`

**Returns:** ``

##### `getunderline(—)`

**Returns:** `input::keyboard::Key`

##### `seticon(graphics::RectangularGraphic2D *icon)`

**Returns:** `void`

##### `Draw(—)`

**Returns:** ``

##### `virtual` `containerenabledchanged(bool state)`

**Returns:** `virtual void`

##### `virtual` `loosefocus(bool force)`

**Returns:** `virtual bool`

##### `virtual` `clickcompleted(—)`

**Returns:** `virtual void`

##### `virtual` `detach(ContainerBase *container)`

**Returns:** `virtual bool`

##### `virtual` `located(ContainerBase* container, utils::SortedCollection<WidgetBase>::Wrapper *w, int Order)`

**Returns:** `virtual void`

##### `playsound(Blueprint::FocusType focusfrom, Blueprint::FocusType focusto, int statefrom, int stateto, Blueprint::StyleType stylefrom, Blueprint::StyleType styleto)`

**Returns:** `void`

##### `focus_anim_finished(—)`

**Returns:** `void`

##### `state_anim_finished(—)`

**Returns:** `void`

##### `style_anim_finished(—)`

**Returns:** `void`

##### `calculatesize(—)`

**Returns:** `void`

##### `Base(const Base &)`

**Returns:** ``


---

## Functions

### `if(bprovider)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(iconp)`

**Returns:** ``



### `if(font && text!="")`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `if(symbolp)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(iconp)`

**Returns:** ``



### `if(font && text!="")`

**Returns:** ``



### `if(textp)`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `if(symbolp)`

**Returns:** ``



### `if(line->WidthMode==Blueprint::Auto)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(iconp)`

**Returns:** ``



### `if(iconp->SizingMode==Placeholder::MaximumAvailable || maximumsized==0 || extra<0)`

**Returns:** ``



### `if(maximumsized==0 || extra<0)`

**Returns:** ``



### `if(font && text!="")`

**Returns:** ``



### `if(textp)`

**Returns:** ``



### `if(textp->SizingMode==Placeholder::MaximumAvailable || maximumsized==0 || extra<0)`

**Returns:** ``



### `if(maximumsized==0 || extra<0)`

**Returns:** ``



### `if(textwrap)`

**Returns:** ``



### `if(underline)`

**Returns:** ``



### `if(ch>-1)`

**Returns:** ``



### `if(textwrap)`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `if(symbolp)`

**Returns:** ``



### `if(symbolp->SizingMode==Placeholder::MaximumAvailable || maximumsized==0 || extra<0)`

**Returns:** ``



### `if(maximumsized==0 || extra<0)`

**Returns:** ``



### `if(sh==0)`

**Returns:** ``



### `prepare()`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `for(int i=1;i<=3;i++)`

**Returns:** ``



### `if(lines[i])`

**Returns:** ``



### `if(extra>0 && maximumsizedlines>0)`

**Returns:** ``



### `for(int i=1;i<=3;i++)`

**Returns:** ``



### `if(lines[i] && lines[i]->HeightMode==Blueprint::MaximumAvailable)`

**Returns:** ``



### `if(extra<0 && totallines)`

**Returns:** `else`



### `for(int i=1;i<=3;i++)`

**Returns:** ``



### `if(lines[i])`

**Returns:** ``



### `for(int i=3;i>0;i--)`

**Returns:** ``



### `if(lines[i])`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `for(int i=1;i<=3;i++)`

**Returns:** ``



### `if(lines[i])`

**Returns:** ``



### `drawline(i, linetransitions[i], y, lineheights_org[i], lineheights[i])`

**Returns:** ``



### `if(overlay)`

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



### `if(currentstate!=type)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, currentstate, type, Blueprint::Normal, Blueprint::Style_None)`

**Returns:** ``



### `if(!bp)`

**Returns:** ``



### `if(state.from!=type || state.to!=0)`

**Returns:** ``



### `if(state.from!=type && state.to!=type && state.to!=0)`

**Returns:** ``



### `if(info)`

**Returns:** ``



### `if(state.from==type)`

**Returns:** ``



### `if(state.to==type)`

**Returns:** `else`



### `if(info.duration==-2)`

**Returns:** ``



### `if(info.duration==0)`

**Returns:** `else`



### `Draw()`

**Returns:** ``



### `if(next_state!=0)`

**Returns:** ``



### `setstate(v)`

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



### `if(info.duration==0)`

**Returns:** `else`



### `Draw()`

**Returns:** ``



### `if(next_style!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from==Blueprint::Down && next_style==Blueprint::Normal)`

**Returns:** ``



### `triggerwait()`

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



### `if(bp)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focused, 1, 0, Blueprint::Normal, Blueprint::Style_None)`

**Returns:** ``



### `setfocus(Blueprint::Focused)`

**Returns:** ``



### `playsound(Blueprint::Focused, Blueprint::NotFocused, 1, 0, Blueprint::Normal, Blueprint::Style_None)`

**Returns:** ``



### `setfocus(Blueprint::NotFocused)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, 1, 0, Blueprint::Disabled, Blueprint::Normal)`

**Returns:** ``



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, 1, 0, Blueprint::Normal, Blueprint::Disabled)`

**Returns:** ``



### `setstyle(Blueprint::Disabled)`

**Returns:** ``



### `prepare()`

**Returns:** ``



### `if(style.from == Blueprint::Disabled || style.to == Blueprint::Disabled)`

**Returns:** ``



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `setstyle(Blueprint::Disabled)`

**Returns:** ``



### `if(next_focus!=Blueprint::Focus_None)`

**Returns:** ``



### `setfocus(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(state.to!=0)`

**Returns:** ``



### `if(next_state!=0)`

**Returns:** ``



### `setstate(v)`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `if(style.to!=Blueprint::Style_None)`

**Returns:** ``



### `if(next_style!=Blueprint::Style_None)`

**Returns:** ``



### `if(style.from==Blueprint::Down && next_style==Blueprint::Normal)`

**Returns:** ``



### `triggerwait()`

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



### `if(BaseLayer)`

**Returns:** ``



### `if(!bp)`

**Returns:** ``



### `if(provider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `for(int i=1;i<=3;i++)`

**Returns:** ``



### `calculatesize()`

**Returns:** ``



### `if(autosize==AutosizeModes::None)`

**Returns:** ``



### `if(textwrap)`

**Returns:** ``



### `for(int l=1;l<=3;l++)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(line->Border)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(font && text!="")`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(iconp)`

**Returns:** ``



### `if(font && text!="" && textp)`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `if(symbolp)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `for(int l=1;l<=3;l++)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(font && text!="")`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `for(int i=0;i<3;i++)`

**Returns:** ``



### `if(icon && drawicon)`

**Returns:** ``



### `if(iconp)`

**Returns:** ``



### `if(font && text!="")`

**Returns:** ``



### `if(textp)`

**Returns:** ``



### `if(symbol && drawsymbol)`

**Returns:** ``



### `if(symbolp)`

**Returns:** ``



### `if(bprovider)`

**Returns:** ``



### `if(lineborder)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `for(int l=1;l<=3;l++)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `if(autosize==AutosizeModes::GrowOnly)`

**Returns:** ``



### `if(!mousedown)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, 1, 0, Blueprint::Normal, Blueprint::Down)`

**Returns:** ``



### `setstyle(Blueprint::Down)`

**Returns:** ``



### `if(mousedown)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, 1, 0, Blueprint::Down, Blueprint::Normal)`

**Returns:** ``



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `down()`

**Returns:** ``



### `if(style.to==Blueprint::Style_None)`

**Returns:** ``



### `triggerwait()`

**Returns:** ``



### `up()`

**Returns:** ``



### `if(!mouseover)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, 1, 0, Blueprint::Normal, Blueprint::Hover)`

**Returns:** ``



### `setstyle(Blueprint::Hover)`

**Returns:** ``



### `if(mouseover)`

**Returns:** ``



### `playsound(Blueprint::NotFocused, Blueprint::Focus_None, 1, 0, Blueprint::Hover, Blueprint::Normal)`

**Returns:** ``



### `setstyle(Blueprint::Normal)`

**Returns:** ``



### `if(this->bp)`

**Returns:** ``



### `clearcaches()`

**Returns:** ``



### `prepare()`

**Returns:** ``



### `calculatesize()`

**Returns:** ``



### `Draw()`

**Returns:** ``



### `for(auto i=BorderCache.begin()`

**Returns:** ``



### `for(auto i=ImageCache.begin()`

**Returns:** ``


