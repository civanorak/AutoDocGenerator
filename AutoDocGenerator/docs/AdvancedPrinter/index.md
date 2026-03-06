# AdvancedPrinter

&gt; Auto-generated documentation for the **AdvancedPrinter** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `AdvancedPrinter`

**Namespace:** `Gorgon`


### `Region`

**Namespace:** `Gorgon`


### `glyphmark`

**Namespace:** `Gorgon`

Prints the given text. Unlike regular print function, this function returns the collected regions and has more options. If stopoffscreen is true, once the printing goes out of screen, it will be stopped. This may cause issues in systems that use negative vertical offset.


### `setvalrel`

**Namespace:** `Gorgon`


### `setvalrelmargin`

**Namespace:** `Gorgon`

#### Methods

##### `rel({left.rel, top.rel, right.rel, bottom.rel})`

**Returns:** ``


### `setvalrelper`

**Namespace:** `Gorgon`


### `setval`

**Namespace:** `Gorgon`


---

## Functions

### `if(thickness != 0)`

**Returns:** ``



### `if(g != 0xffff)`

**Returns:** ``



### `if(g != 0xffff)`

**Returns:** ``



### `if(l.Y >= location.Y)`

**Returns:** ``



### `if(maxdoney < l.Y)`

**Returns:** ``



### `if(l.Y >= location.Y)`

**Returns:** ``



### `if(maxdoney < l.Y)`

**Returns:** ``



### `if(index <= ind)`

**Returns:** ``



### `if(index <= ind)`

**Returns:** ``



### `findfont(NamedFont::Larger)`

**Returns:** `return`



### `findfont(NamedFont::Bold)`

**Returns:** `return`



### `findfont(NamedFont::Italic)`

**Returns:** `return`



### `findfont(NamedFont::Script)`

**Returns:** `return`



### `findfont(NamedFont::Small)`

**Returns:** `return`



### `findfont(NamedFont::FixedWidth)`

**Returns:** `return`



### `findfont(NamedFont::Bold)`

**Returns:** `return`



### `findfont(NamedFont::FixedWidth)`

**Returns:** `return`



### `findfont(NamedFont::Italic)`

**Returns:** `return`



### `AdvancedPrinter(const AdvancedPrinter &other)`

**Returns:** ``



### `RegisterFont(Byte index, const StyledPrinter &renderer)`

**Returns:** `void`


Sets the font for the given index


### `RegisterFont(NamedFont index, const StyledPrinter &renderer)`

**Returns:** `void`


Sets the font for the given index


### `RegisterColor(Byte index, const RGBA &forecolor, const RGBA &backcolor)`

**Returns:** `void`


Returns the font at the given index Returns the font at the given index Registers a pair of fore and background colors with the given index. Use indexes starting from Color::User for custom colors


### `RegisterColor(Color::Designation index, const RGBA &forecolor, const RGBA &backcolor)`

**Returns:** `void`


Registers a pair of fore and background colors with the given index.


### `RegisterColors(const Color::PairPack &pack)`

**Returns:** `void`


Registers all colors from the supplied pack.


### `for(auto p : pack)`

**Returns:** ``



### `RegisterColor(p.first, p.second.Forecolor, p.second.Backcolor)`

**Returns:** ``



### `UseColors(const Color::PairPack &pack)`

**Returns:** `void`


Replaces all registed colors with the supplied pack.


### `for(auto p : pack)`

**Returns:** ``



### `RegisterColor(p.first, p.second.Forecolor, p.second.Backcolor)`

**Returns:** ``



### `RegisterImage(Byte index, const RectangularDrawable &image)`

**Returns:** `void`


Registers the given image to be used in the advanced print


### `SetBreakingLetters(std::vector<Char> letters)`

**Returns:** `void`


Registers the given image to be used in the advanced print Adds breaking glyphs. A line can be wrapped after a breaking letter. Spaces are breaking and cannot be removed from the list.


### `SetDefaultFont(NamedFont value)`

**Returns:** `void`


Returns the list of breaking glyphs. You can change the returned vector. Returns the list of breaking glyphs. Sets the default font that will be used at the start.


### `SetDefaultFont(Byte value)`

**Returns:** `void`


Sets the default font that will be used at the start.


### `AdvancedPrint(target, text, l, width, wrap, stopoffscreen)`

**Returns:** `return`


This is the advanced operation which allows user to submit functions that will perform the rendering. First one is glyph render. It will be given the renderer to be used, the second is box renderer, bounds, background color, border thickness and border color will be given to this function. The final one draws a horizontal line from a point with the given width and thickness. For wordwrap to work, width should be set to a positive value  If you wish to call this function, you must include AdvancedPrinterImp.h. Prints the given text. Unlike regular print function, this function returns the collected regions and has more options. If stopoffscreen is true, once the printing goes out of screen, it will be stopped. This may cause issues in systems that use negative vertical offset.


### `AdvancedPrint(target, text, location, 0)`

**Returns:** ``



### `readint(std::string::const_iterator &it, std::string::const_iterator end, Glyph &cur, long &curindex)`

**Returns:** `int16_t`



### `MOVEIT(ret)`

**Returns:** ``



### `readcolor(std::string::const_iterator &it, std::string::const_iterator end, Glyph &cur, long &curindex)`

**Returns:** `RGBA`



### `MOVEIT(col)`

**Returns:** ``



### `MOVEIT(col)`

**Returns:** ``



### `readindex(std::string::const_iterator &it, std::string::const_iterator end, Glyph &cur, long &curindex)`

**Returns:** `Byte`



### `MOVEIT(ret)`

**Returns:** ``



### `readalpha(std::string::const_iterator &it, std::string::const_iterator end, Glyph &cur, long &curindex)`

**Returns:** `Byte`



### `MOVEIT(ret)`

**Returns:** ``



### `readvalrel(std::string::const_iterator &it, std::string::const_iterator end, Glyph &cur, bool relper, long &curindex)`

**Returns:** `setvalrel`



### `setvalrel()`

**Returns:** `return`



### `if(mode&0b10)`

**Returns:** ``



### `setvalrel(true, val, rel)`

**Returns:** `return`



### `readvalrelper(std::string::const_iterator &it, std::string::const_iterator end, Glyph &cur, bool relper, long &curindex)`

**Returns:** `setvalrelper`



### `setvalrelper()`

**Returns:** `return`



### `if(mode&0b10)`

**Returns:** ``



### `setvalrelper(true, val, rel, per)`

**Returns:** `return`


