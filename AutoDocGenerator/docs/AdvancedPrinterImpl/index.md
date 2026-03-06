# AdvancedPrinterImpl

&gt; Auto-generated documentation for the **AdvancedPrinterImpl** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `linesettings`

**Namespace:** `Gorgon`


### `openregioninfo`

**Namespace:** `Gorgon`


### `lineinfo`

**Namespace:** `Gorgon`


### `selectioninfo`

**Namespace:** `Gorgon`


---

## Functions

### `for(auto &sty : fonts)`

**Returns:** ``



### `if(!temp)`

**Returns:** ``



### `if(underlineon)`

**Returns:** ``



### `if(strikeon)`

**Returns:** ``



### `MOVEIT()`

**Returns:** ``



### `MOVEIT()`

**Returns:** ``



### `switch(cmd)`

**Returns:** ``



### `if(bits&0b100000)`

**Returns:** ``



### `if(bits & 0b00001)`

**Returns:** ``



### `if(ind != -1)`

**Returns:** ``



### `if(bits & 0b00010)`

**Returns:** ``



### `if(bits & 0b00100)`

**Returns:** ``



### `if(bits & 0b01000)`

**Returns:** ``



### `if(bits & 0b10000)`

**Returns:** ``



### `switchtoscript()`

**Returns:** ``



### `if(m&1)`

**Returns:** ``



### `if(m&2)`

**Returns:** ``



### `if(m&1)`

**Returns:** ``



### `if(m&2)`

**Returns:** ``



### `while(p != internal::ST)`

**Returns:** ``



### `MOVEIT()`

**Returns:** ``



### `while(p != internal::ST)`

**Returns:** ``



### `MOVEIT()`

**Returns:** ``



### `if(openregions[i].ID == ind && openregions[i].finishat == -1)`

**Returns:** ``



### `while(p != internal::ST)`

**Returns:** ``



### `MOVEIT()`

**Returns:** ``



### `MOVEIT()`

**Returns:** ``



### `switch(cmd)`

**Returns:** ``



### `switchtoscript()`

**Returns:** ``



### `if(underlineon)`

**Returns:** ``



### `if(strikeon)`

**Returns:** ``



### `switch(cmd)`

**Returns:** ``



### `switch(g)`

**Returns:** ``



### `if(selbg.set)`

**Returns:** ``



### `if(end == 0 || maxh == 0)`

**Returns:** ``



### `for(auto it = acc.begin()`

**Returns:** ``



### `if(it->g == '\t')`

**Returns:** ``



### `if(sps > 0)`

**Returns:** ``



### `if(letters && target/letters >= 1)`

**Returns:** ``



### `if(sps > 0 && target > 0)`

**Returns:** ``



### `if(target == 0)`

**Returns:** ``



### `for(auto it = acc.begin()`

**Returns:** ``



### `for(auto &s : selections)`

**Returns:** ``



### `if(s.startat >= end)`

**Returns:** ``



### `if(s.startat >= 0 && s.startat < end)`

**Returns:** ``



### `if(s.startat == -1 && end != 0)`

**Returns:** `else`



### `if(s.finishat != -1 && s.finishat < end)`

**Returns:** ``



### `if(s.selimg.set)`

**Returns:** ``



### `imgr(s.selimg.val, bnds, 1.0f, false)`

**Returns:** ``



### `boxr(bnds, s.selbg, 0, {0.0f})`

**Returns:** ``



### `for(int i = 0; i<end; i++)`

**Returns:** ``



### `Translate(acc[i].location, xoff, maxb-acc[i].baseline+extralineoffset)`

**Returns:** ``



### `if(nl == 0)`

**Returns:** ``



### `for(; end<acc.size()`

**Returns:** ``



### `Translate(acc[end].location, xoff, maxb-acc[end].baseline+extralineoffset)`

**Returns:** ``



### `for(auto &s : selections)`

**Returns:** ``



### `if(s.startat >= end)`

**Returns:** ``



### `if(s.finishat > end)`

**Returns:** ``



### `if(s.finishat != -1)`

**Returns:** `else`



### `for(auto &r : openregions)`

**Returns:** ``



### `if(r.startat >= 0 && r.startat < end)`

**Returns:** ``



### `if(r.finishat >= 0 && r.finishat < end)`

**Returns:** ``



### `for(auto &u : underlines)`

**Returns:** ``



### `if(u.startat >= 0 && u.startat < end)`

**Returns:** ``



### `if(u.startat == -1 && end != 0)`

**Returns:** `else`



### `if(u.finishat >= 0 && u.finishat < end)`

**Returns:** ``



### `for(auto &s : strikes)`

**Returns:** ``



### `if(s.startat >= 0 && s.startat < end)`

**Returns:** ``



### `if(s.startat == -1 && end != 0)`

**Returns:** `else`



### `if(s.finishat >= 0 && s.finishat < end)`

**Returns:** ``



### `if(beginparag)`

**Returns:** ``



### `for(auto &gm : acc)`

**Returns:** ``



### `if(nl != -1)`

**Returns:** ``



### `for(auto &r : openregions)`

**Returns:** ``



### `if(r.startat >= end)`

**Returns:** ``



### `if(r.finishat != -1 && r.finishat <= end)`

**Returns:** ``



### `if(r.finishat == end)`

**Returns:** ``



### `if(r.finishat != -1)`

**Returns:** ``



### `for(auto &u : underlines)`

**Returns:** ``



### `if(u.startat >= end)`

**Returns:** ``



### `if(u.finishat != -1 && u.finishat <= end)`

**Returns:** ``



### `if(u.finishat == end)`

**Returns:** ``



### `liner(u.start, u.end, u.y + u.yoffset, u.thickness, u.color)`

**Returns:** ``



### `liner(u.start, u.end, u.y + u.yoffset, u.thickness, u.color)`

**Returns:** ``



### `if(u.finishat != -1)`

**Returns:** ``



### `for(auto &s : strikes)`

**Returns:** ``



### `if(s.startat >= end)`

**Returns:** ``



### `if(s.finishat != -1 && s.finishat <= end)`

**Returns:** ``



### `if(s.finishat == end)`

**Returns:** ``



### `liner(s.start, s.end, s.y + s.yoffset, s.thickness, s.color)`

**Returns:** ``



### `liner(s.start, s.end, s.y + s.yoffset, s.thickness, s.color)`

**Returns:** ``



### `if(s.finishat != -1)`

**Returns:** ``



### `if(baselineoffset < 0)`

**Returns:** ``



### `changeprinter(backup, true)`

**Returns:** ``



### `if(baselineoffset > 0)`

**Returns:** `else`



### `changeprinter(backup, true)`

**Returns:** ``



### `changeprinter(printer)`

**Returns:** ``



### `for(auto it = text.begin()`

**Returns:** ``



### `if(g == internal::CSI)`

**Returns:** ``



### `CSI(it, end)`

**Returns:** ``



### `if(g == internal::SCI)`

**Returns:** ``



### `SCI(it, end)`

**Returns:** ``



### `if(newline)`

**Returns:** ``



### `if(beginparag)`

**Returns:** ``



### `if(g == '\t')`

**Returns:** ``



### `if(prev && !newline && g != '\t')`

**Returns:** `else`



### `if(g != '\t')`

**Returns:** `else`



### `if(dounderline)`

**Returns:** ``



### `if(g == '\t' && !underlinesettings.tabs)`

**Returns:** ``



### `if(dounderline)`

**Returns:** ``



### `if(!underlineon)`

**Returns:** ``



### `if(underlineon)`

**Returns:** ``



### `if(dostrike)`

**Returns:** ``



### `if(g == '\t' && !strikesettings.tabs)`

**Returns:** ``



### `if(dostrike)`

**Returns:** ``



### `if(!strikeon)`

**Returns:** ``



### `if(strikeon)`

**Returns:** ``



### `if(baselineoffset != 0)`

**Returns:** ``



### `if(wrapwidth && wrap && cur.X > wrapwidth + location.X)`

**Returns:** ``



### `if(lastbreak == 0)`

**Returns:** ``



### `if(ind == 1)`

**Returns:** ``



### `for(; lastbreak>0; lastbreak--)`

**Returns:** ``



### `if(baselineoffset == 0 && blosave != 0)`

**Returns:** ``


