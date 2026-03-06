# Font

&gt; Auto-generated documentation for the **Font** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `glyphmark`

**Namespace:** `internal`


### `GlyphRange`

**Namespace:** `Gorgon`

This class represents a range of glyphs. Both start and end is included.

#### Methods

##### `Count(—)`

**Returns:** `int`

Creates a range that includes a single item. Value 0 is not a valid code point Returns the number of the glyphs in the range

##### `Normalize(—)`

**Returns:** `void`


### `GlyphRenderer`

**Namespace:** `internal`

#### Methods

##### `virtual` `Render(Glyph chr, TextureTarget &target, Geometry::Pointf location, RGBAf color)`

**Returns:** `virtual void`

This function should render the given character to the target at the specified location and color. If chr does not exists, this function should perform no action. location and color can be modified as per the needs of renderer. If the kerning returns integers location will always be an integer. Additionally, text renderers will place glyphs on 0 y position from the top. It is glyph renderer's task to ensure baseline of glyphs to line up.

##### `virtual` `GetOffset(Glyph chr)`

**Returns:** `virtual Geometry::Point`

This function should return the render offset of the requested glyph. If it does not exists, 0, 0 should be returned

##### `virtual` `GetSize(Glyph chr)`

**Returns:** `virtual Geometry::Size`

This function should return the size of the requested glyph. If it does not exists, 0x0 should be returned

##### `virtual` `GetCursorAdvance(Glyph g)`

**Returns:** `virtual float`

This function should return the number of pixels the cursor should advance after this glyph. This value will be added to kerning distance.

##### `virtual` `Exists(Glyph g)`

**Returns:** `virtual bool`

Returns true if the glyph exists

##### `virtual` `IsASCII(—)`

**Returns:** `virtual bool`

This function should return true if this font renderer supports only 7-bit ASCII

##### `virtual` `IsFixedWidth(—)`

**Returns:** `virtual bool`

This function should return true if this font is fixed width. This will suppress calls to GetSize function.

##### `virtual` `KerningDistance(Glyph left, Glyph right)`

**Returns:** `virtual Geometry::Pointf`

This function should return the additional distance between given glyphs. Returned value could be (in most cases it is) negative. Left and right are visual locations, they will not be reverted for right to left rendering.

##### `virtual` `GetEMSize(—)`

**Returns:** `virtual int`

Returns the size of the EM dash

##### `virtual` `GetMaxWidth(—)`

**Returns:** `virtual int`

Returns the width of widest glyph.

##### `virtual` `GetHeight(—)`

**Returns:** `virtual int`

Height of glyphs, actual size could be smaller but all glyphs should have the same virtual height. When drawn on the same y position, all glyphs should line up. Renderer can change actual draw location to compensate.

##### `virtual` `GetLetterHeight(bool asciionly = false)`

**Returns:** `virtual std::pair<int, int>`

Returns the offset (first) and maximum height (second) that is used by letters. Offset is the distance of the letter with max height to the top. This function uses � and j to calculate letter height when ascii only is not set. If ascii only is set, it uses A, f, j. If � is not found, this function simply reverts to using A.

##### `virtual` `GetDigitWidth(—)`

**Returns:** `virtual int`

Width of a digit, if digits do not have the same width, maximum should be returned. For practical reasons, this function is expected to consider arabic numerals.

##### `virtual` `GetBaseLine(—)`

**Returns:** `virtual float`

Baseline point of glyphs from the top.

##### `virtual` `GetLineGap(—)`

**Returns:** `virtual float`

This is the default distance between two consecutive lines. This distance can be modified by text renderers

##### `virtual` `GetLineThickness(—)`

**Returns:** `virtual float`

Should return the average thickness of a line. This information can be used to construct underline and strike through.

##### `virtual` `GetUnderlineOffset(—)`

**Returns:** `virtual int`

The position of the underline, if it is to be drawn.

##### `virtual` `NeedsPrepare(—)`

**Returns:** `virtual bool`

Should return if the glyph renderer requires preparation regarding the text given.

##### `virtual` `Prepare(const std::string &)`

**Returns:** `virtual void`

Notifies glyph renderer about a text to be rendered. If renderers require modification to their internal structures, they should mark them


### `TextPrinter`

**Namespace:** `internal`

#### Methods

##### `Print(TextureTarget &target, const std::string &text, Geometry::Pointf location)`

**Returns:** `void`

Prints the given text to the target. y coordinate is the top if the text. However, depending on the font, this value might exclude uppercase accents.

##### `print(target, text, location)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, Geometry::Point location)`

**Returns:** `void`

##### `print(target, text, location)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y)`

**Returns:** `void`

##### `print(target, text, {x, y})`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, Geometry::Point location, int w, TextAlignment align_override)`

**Returns:** `void`

##### `print(target, text, {location, w, 0}, align_override)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, Geometry::Point location, int w)`

**Returns:** `void`

##### `print(target, text, {location, w, 0})`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y, int w, TextAlignment align_override)`

**Returns:** `void`

##### `print(target, text, {x, y, w, 0}, align_override)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y, int w)`

**Returns:** `void`

##### `print(target, text, {x, y, w, 0})`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, Geometry::Point location, int w, TextAlignment align_override)`

**Returns:** `void`

##### `printnowrap(target, text, {location, w, 0}, align_override)`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, Geometry::Point location, int w)`

**Returns:** `void`

##### `printnowrap(target, text, {location, w, 0})`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, int x, int y, int w, TextAlignment align_override)`

**Returns:** `void`

##### `printnowrap(target, text, {x, y, w, 0}, align_override)`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, int x, int y, int w)`

**Returns:** `void`

##### `printnowrap(target, text, {x, y, w, 0})`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text)`

**Returns:** `void`

##### `virtual` `IsReady(—)`

**Returns:** `virtual bool`

Whether the render can render text

##### `virtual` `GetEMSize(—)`

**Returns:** `virtual int`

Returns the glyphrenderer that is used by this text renderer. It might be the text renderer itself. It is only safe to call this function if IsReady function has returned true. Returns the size of the EM dash

##### `virtual` `GetBaseLine(—)`

**Returns:** `virtual float`

Get the distance of baseline from the top of the text

##### `virtual` `GetHeight(—)`

**Returns:** `virtual int`

Get the distance of baseline from the top of the text

##### `virtual` `GetSize(const std::string &text)`

**Returns:** `virtual Geometry::Size`

Returns the size of the given text

##### `virtual` `GetSize(const std::string &text, int width)`

**Returns:** `virtual Geometry::Size`

Returns the size of the given text

##### `virtual` `GetCharacterIndex(const std::string &text, Geometry::Point location)`

**Returns:** `virtual int`

Returns the character index of glyph immediately after the given location. This function is Unicode aware.

##### `virtual` `GetCharacterIndex(const std::string &text, int w, Geometry::Point location, bool wrap = true)`

**Returns:** `virtual int`

Returns the character index of glyph immediately after the given location. This function is Unicode aware.

##### `virtual` `GetPosition(const std::string &text, int index)`

**Returns:** `virtual Geometry::Rectangle`

Returns the position of the glyph at the character index. If the character is not found, this will return std::numeric_limit&lt;int&gt;::min for x and y position. Size could be 0 if it cannot be determined.

##### `virtual` `GetPosition(const std::string &text, int w, int index, bool wrap = true)`

**Returns:** `virtual Geometry::Rectangle`

Returns the position of the glyph at the character index. If the character is not found, this will return std::numeric_limit&lt;int&gt;::min for x and y position. Size could be 0 if it cannot be determined.

##### `virtual` `print(TextureTarget &target, const std::string &text, Geometry::Point location)`

**Returns:** `virtual void`


### `BasicPrinter`

**Namespace:** `internal`

Should print the given text to the specified location and color. Width should be used to align the text. Unless width is 0, text should be wrapped. Even if width is 0, the alignment should be respected. For instance if width is 0 and align is right, text should end at the given location. Height of the rectangle can be left 0, thus unless explicitly requested, it should be ignored. Should print the given text to the specified location and color. Width should be used to align the text. Automatic wrapping should not be used. Should print the given text to the specified location and color. Width should be used to align the text. Automatic wrapping should not be used.

#### Methods

##### `Print(TextureTarget &target, const std::string &text, RGBAf color)`

**Returns:** `void`

##### `Print(TextureTarget &target, const std::string &text, Geometry::Point location, RGBAf color)`

**Returns:** `void`

##### `print(target, text, location, color)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y, RGBAf color)`

**Returns:** `void`

##### `print(target, text, {x, y}, color)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, Geometry::Point location, int w, TextAlignment align_override, RGBAf color)`

**Returns:** `void`

##### `print(target, text, {location, w, 0}, align_override, color)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, Geometry::Point location, int w, RGBAf color)`

**Returns:** `void`

##### `print(target, text, {location, w, 0}, color)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y, int w, TextAlignment align_override, RGBAf color)`

**Returns:** `void`

##### `print(target, text, {x, y, w, 0}, align_override, color)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y, int w, RGBAf color)`

**Returns:** `void`

##### `print(target, text, {x, y, w, 0}, color)`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, Geometry::Point location, int w, TextAlignment align_override, RGBAf color)`

**Returns:** `void`

##### `printnowrap(target, text, {location, w, 0}, align_override, color)`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, Geometry::Point location, int w, RGBAf color)`

**Returns:** `void`

##### `printnowrap(target, text, {location, w, 0}, color)`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, int x, int y, int w, TextAlignment align_override, RGBAf color)`

**Returns:** `void`

##### `printnowrap(target, text, {x, y, w, 0}, align_override, color)`

**Returns:** ``

##### `PrintNoWrap(TextureTarget &target, const std::string &text, int x, int y, int w, RGBAf color)`

**Returns:** `void`

##### `printnowrap(target, text, {x, y, w, 0}, color)`

**Returns:** ``

##### `SetDefaultAlignment(TextAlignment value)`

**Returns:** `void`

Changes the default alignment. It is possible to override default alignment through TextRenderer interface.

##### `GetDefaultAlignment(—)`

**Returns:** `TextAlignment`

Returns the current default alignment.

##### `SetColor(RGBAf value)`

**Returns:** `void`

Changes the the color of the text. Color can only be overridden through BasicFont interface.

##### `GetColor(—)`

**Returns:** `RGBAf`

Returns the current text color

##### `print(target, text, location, color)`

**Returns:** ``

##### `print(target, text, location, align, color)`

**Returns:** ``

##### `virtual` `print(TextureTarget &target, const std::string &text, Geometry::Point location, RGBAf color)`

**Returns:** `virtual void`

##### `printnowrap(target, text, location, align, color)`

**Returns:** ``

##### `print(target, text, location, defaultalign)`

**Returns:** ``

##### `print(target, text, location, defaultalign, color)`

**Returns:** ``

##### `printnowrap(target, text, location, defaultalign)`

**Returns:** ``

##### `printnowrap(target, text, location, defaultalign, color)`

**Returns:** ``


### `TextShadow`

**Namespace:** `internal`

Default alignment if none is specified Color of this renderer, can be overridden.


### `StyledPrinter`

**Namespace:** `internal`

#### Methods

##### `SetGlyphRenderer(GlyphRenderer &renderer)`

**Returns:** `void`

Renderer must be ready in order to calculate spacings correctly. If it will be initialized later, call ResetSpacing to reset all to defaults.

##### `SetColor(RGBAf value)`

**Returns:** `void`

Changes the color of the text

##### `GetColor(—)`

**Returns:** `RGBAf`

Returns color of the text

##### `SetShadow(TextShadow value)`

**Returns:** `void`

Changes text shadow

##### `DisableShadow(—)`

**Returns:** `void`

Disables text shadow

##### `UseFlatShadow(RGBAf color, Geometry::Pointf offset = {1.f, 1.f})`

**Returns:** `void`

Uses flat shadow for text

##### `GetShadow(—)`

**Returns:** `TextShadow`

Returns text shadow

##### `SetUnderline(bool value)`

**Returns:** `void`

Sets underlining for the text

##### `Underline(—)`

**Returns:** `void`

Underlines the text

##### `Underline(RGBAf color)`

**Returns:** `void`

Underlines the text with the given color

##### `GetUnderline(—)`

**Returns:** `bool`

Returns whether the text is underlined

##### `SetUnderlineColor(RGBAf value)`

**Returns:** `void`

Changes the underline color of the text. By default underline color will be the same as text color. To get default value, use ResetUnderlineColor function

##### `GetUnderlineColor(—)`

**Returns:** `RGBAf`

Returns the current underline color.

##### `ResetUnderlineColor(—)`

**Returns:** `void`

Sets underline color to match with text color

##### `SetStrike(bool value)`

**Returns:** `void`

Sets whether the text would be stroked

##### `Strike(—)`

**Returns:** `void`

Strikes the text

##### `Strike(RGBAf color)`

**Returns:** `void`

Strikes the text with the given color

##### `GetStrike(—)`

**Returns:** `bool`

Returns whether the text would stroked

##### `SetStrikeColor(RGBAf value)`

**Returns:** `void`

Changes the strike color of the text. By default strike color will be the same as text color. To get default value, use ResetStrikeColor function

##### `GetStrikeColor(—)`

**Returns:** `RGBAf`

Returns the current strike color.

##### `ResetStrikeColor(—)`

**Returns:** `void`

Sets strike color to match with text color

##### `SetStrikePosition(int value)`

**Returns:** `void`

Changes the strike position to the given value. Default value for strike position is automatically calculated, use ResetStrikePosition to get back to the default

##### `GetStrikePosition(—)`

**Returns:** `int`

Returns current strike position

##### `SetDefaultAlign(TextAlignment value)`

**Returns:** `void`

Sets the default alignment for the text

##### `AlignLeft(—)`

**Returns:** `void`

Aligns the text to the left, removes justify

##### `AlignRight(—)`

**Returns:** `void`

Aligns the text to the right, removes justify

##### `AlignCenter(—)`

**Returns:** `void`

Aligns the text to the center, removes justify

##### `GetDefaultAlign(—)`

**Returns:** `TextAlignment`

Returns the default alignment for the text

##### `SetJustify(bool value)`

**Returns:** `void`

Sets whether the text would be justified. Justify will not affect single line text as well last line of a paragraph.

##### `JustifyLeft(—)`

**Returns:** `void`

Aligns the text to the left, sets justify

##### `JustifyRight(—)`

**Returns:** `void`

Aligns the text to the right, sets justify

##### `JustifyCenter(—)`

**Returns:** `void`

Aligns the text to the center, sets justify

##### `GetJustify(—)`

**Returns:** `bool`

Returns whether the text would be justified

##### `SetLineSpacingPixels(int value)`

**Returns:** `void`

Sets the line spacing in pixels, this spacing is the space between two lines, from the descender of the first line to the ascender of the second.

##### `GetLineSpacingPixels(—)`

**Returns:** `int`

Returns the line spacing in pixels

##### `SetLineSpacing(float value)`

**Returns:** `void`

Sets the line spacing as percentage of line gap. A value of one will use the default state by the font, where as a value of two will leave a large gap between two lines. This will round the final result to the nearest pixel.

##### `GetLineSpacing(—)`

**Returns:** `float`

Returns the line spacing as percentage of line gap

##### `SetLetterSpacing(int value)`

**Returns:** `void`

Spacing between letters of the text, in pixels. This is in addition to the regular character spacing.

##### `GetLetterSpacing(—)`

**Returns:** `int`

Returns the spacing between the letters in pixels

##### `SetTabWidth(int value)`

**Returns:** `void`

Distance between tab stops. This value is in pixels. Default value is 8 * A width. Tabbing is only fully effective when text is left aligned.

##### `SetTabWidthInLetters(float value)`

**Returns:** `void`

Sets the tab width in digit widths.

##### `GetTabWidth(—)`

**Returns:** `int`

Returns tab width in pixels.

##### `SetParagraphSpacing(int value)`

**Returns:** `void`

Changes the additional space between paragraphs. A paragraph is stared by a manual line break. This distance is in pixels.

##### `GetParagraphSpacing(—)`

**Returns:** `int`

Get the space between paragraphs in pixels.

##### `print(target, text, location, defaultalign)`

**Returns:** ``

##### `printnowrap(target, text, location, defaultalign)`

**Returns:** ``

##### `print(TextureTarget &target, const std::string &text, Geometry::Pointf location, RGBAf color, RGBAf strikecolor, RGBAf underlinecolor)`

**Returns:** `void`

##### `print(TextureTarget &target, const std::string &text, Geometry::Rectanglef location, TextAlignment align, RGBAf color, RGBAf strikecolor, RGBAf underlinecolor)`

**Returns:** `void`


### `Font`

**Namespace:** `Gorgon`

#### Methods

##### `Font(—)`

**Returns:** ``

##### `Font(Graphics::GlyphRenderer &renderer)`

**Returns:** ``

Filling constructor, for now can only hold Graphics::BitmapFont. All images in the renderer should be bitmaps or their derivatives with data buffers still attached.

##### `HasRenderer(—)`

**Returns:** `bool`

This function will only prepare images loaded from a resource, does not work for images loaded later. Returns true if the resource has renderer.

##### `ASSERT(data, "Renderer is not set")`

**Returns:** ``

Returns the renderer stored in this resource.

##### `RemoveRenderer(—)`

**Returns:** `void`

Removes the renderer from this resource.

##### `SetRenderer(Graphics::GlyphRenderer &renderer)`

**Returns:** `void`

Changes the renderer to the given renderer

##### `AssumeRenderer(Graphics::GlyphRenderer &renderer)`

**Returns:** `void`

Changes the renderer to the given renderer and assumes ownership

##### `SetRenderer(renderer)`

**Returns:** ``


---

## Enums

### `NamedFont`

**Namespace:** `Gorgon`

Glyph is a symbol for a character. In Gorgon, glyphs are UTF32 chars. Constants for fonts.


### `HeaderLevel`

**Namespace:** `Gorgon`

Default font Default font Bold font First level heading Second level heading Third level heading Fourth level heading Italic font Smaller font, usually 75% of full size Bold and italic font Font style used to display information, usually smaller and uses different colors. Font style used to display information, usually smaller and uses different colors. Font style used to display information, usually smaller and uses different colors. Font style used to display information, usually smaller and uses different colors. A large font, usually 125% of the original size Small font that will be used in super and subscripts. Could also be used for other purposes. Small font that will be used in super and subscripts for fonts that is known to be bold. Could also be used for other purposes. Small font that will be used in super and subscripts. Could also be used for other purposes. This script font will be used for small, info and script fonts Fixed width font to be used in programming Fixed width font to be used in programming Fixed width font to be used in programming Fixed width font to be used in programming Constants for headings


### `ShadowType`

**Namespace:** `internal`


---

## Functions

### `decode(std::string::const_iterator &it, std::string::const_iterator end, bool skipcmd)`

**Returns:** `Glyph`



### `if(it == end)`

**Returns:** ``



### `if(g == 0x9a)`

**Returns:** ``



### `decode_impl(it, end)`

**Returns:** ``



### `if(it == end)`

**Returns:** ``



### `dodefaulttab(T_ s, T_ &x, T_ w)`

**Returns:** `void`



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``


helps with the simple layouts, decodes and executes unicode instructions. Offset parameter in render function is the offset that must be used after rendering the character. If g is 0, only offset should be processed


### `if(prev)`

**Returns:** ``



### `if(g == '\t')`

**Returns:** `else`



### `if(prev)`

**Returns:** ``



### `dotab()`

**Returns:** ``



### `donewline(g)`

**Returns:** ``



### `if(g > 32)`

**Returns:** `else`



### `if(prev)`

**Returns:** ``



### `if(ind != 0)`

**Returns:** ``



### `donewline(0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``


helps with the simple layouts, decodes and executes unicode instructions. Offset parameter in render function is the offset that must be used after rendering the character. If g is 0, only offset should be processed. This overload calls process function even for glyphs that are not normally rendered, and allows return value from the layout function to stop processing further.


### `if(prev)`

**Returns:** ``



### `if(g == '\t')`

**Returns:** `else`



### `if(prev)`

**Returns:** ``



### `dotab()`

**Returns:** ``



### `donewline(g)`

**Returns:** ``



### `if(g > 32)`

**Returns:** `else`



### `if(prev)`

**Returns:** ``



### `if(ind != 0)`

**Returns:** ``



### `donewline(0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(g == '\t')`

**Returns:** ``



### `dotab(x)`

**Returns:** ``



### `if(prev)`

**Returns:** ``



### `if(g > 32)`

**Returns:** `else`



### `if(prev)`

**Returns:** ``



### `if(width > 0 && x + cur_spacing + prev_gw > width)`

**Returns:** ``



### `if(lastbreak == 0)`

**Returns:** ``



### `if(ind == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(g == '\t')`

**Returns:** ``



### `dotab(x)`

**Returns:** ``



### `if(prev)`

**Returns:** ``



### `if(g > 32)`

**Returns:** `else`



### `if(prev)`

**Returns:** ``



### `if(width && x + cur_spacing + prev_gw > width)`

**Returns:** ``



### `if(lastbreak == 0)`

**Returns:** ``



### `if(ind == 0)`

**Returns:** ``



### `if(autobreak)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Center)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Right)`

**Returns:** `else`



### `if(location.X <= off || begin == end)`

**Returns:** ``



### `for(auto it = begin; it != end; ++it)`

**Returns:** ``



### `if(y > location.Y)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Center)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Right)`

**Returns:** `else`



### `for(auto it = begin; it != end; ++it)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(align == TextAlignment::Center)`

**Returns:** ``



### `if(align == TextAlignment::Right)`

**Returns:** `else`



### `for(auto it = begin; it != end; ++it)`

**Returns:** ``



### `if(shadow.type == TextShadow::Flat)`

**Returns:** ``



### `print(target, text, location, color, strikecolor, underlinecolor)`

**Returns:** ``



### `if(strike)`

**Returns:** ``



### `if(underline)`

**Returns:** ``



### `if(justify && eol == 0)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(justify && g == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(it->g == '\t')`

**Returns:** ``



### `if(letters && target/letters >= 1)`

**Returns:** ``



### `if(sps > 0)`

**Returns:** ``



### `if(target == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Center)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Right)`

**Returns:** `else`



### `if(location.X <= off || begin == end)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(y > location.Y)`

**Returns:** ``



### `if(justify && g == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(it->g == '\t')`

**Returns:** ``



### `if(letters && target/letters >= 1)`

**Returns:** ``



### `if(sps > 0)`

**Returns:** ``



### `if(target == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Center)`

**Returns:** ``



### `if(defaultalign == TextAlignment::Right)`

**Returns:** `else`



### `for(auto it = begin; it != end; ++it)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `if(shadow.type == TextShadow::Flat)`

**Returns:** ``



### `print(target, text, location, align_override, color, strikecolor, underlinecolor)`

**Returns:** ``



### `if(justify && g == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(it->g == '\t')`

**Returns:** ``



### `if(letters && target/letters >= 1)`

**Returns:** ``



### `if(sps > 0)`

**Returns:** ``



### `if(target == 0)`

**Returns:** ``



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(align == TextAlignment::Center)`

**Returns:** ``



### `if(align == TextAlignment::Right)`

**Returns:** `else`



### `for(auto it=begin; it!=end; ++it)`

**Returns:** ``



### `if(strike)`

**Returns:** ``



### `if(underline)`

**Returns:** ``



### `switch(align)`

**Returns:** ``



### `print(target, text, {location.X + location.Width / 2, location.Y, 0, location.Height}, align, color)`

**Returns:** ``



### `print(target, text, {location.X + location.Width, location.Y, 0, location.Height}, align, color)`

**Returns:** ``



### `switch(align)`

**Returns:** ``



### `print(target, text, {location.X + location.Width / 2, location.Y, 0, location.Height}, align)`

**Returns:** ``



### `print(target, text, {location.X + location.Width, location.Y, 0, location.Height}, align)`

**Returns:** ``



### `decode_impl(std::string::const_iterator &it, std::string::const_iterator end)`

**Returns:** `inline Glyph`



### `if(b <= 127)`

**Returns:** ``



### `if(b == '\r')`

**Returns:** ``



### `if(b == 255)`

**Returns:** ``



### `decode(std::string::const_iterator &it, std::string::const_iterator end, bool skipcmd = true)`

**Returns:** `Glyph`


Decodes a utf-8 character from the given iterator. If char is not valid 0xfffd is returned. \\r\\n is mapped to \\n, if skipcmd is true, this will skip advanced renderer commands


### `isnewline(Glyph g)`

**Returns:** `bool`



### `isspaced(Glyph g)`

**Returns:** `bool`



### `isspace(Glyph g)`

**Returns:** `bool`



### `isadjustablespace(Glyph g)`

**Returns:** `bool`



### `isbreaking(Glyph g)`

**Returns:** `bool`



### `ceildiv(int v, float f)`

**Returns:** `inline int`



### `rounddiv(int v, float f)`

**Returns:** `inline int`



### `isspaced(Glyph g)`

**Returns:** `inline bool`



### `isnewline(Glyph g)`

**Returns:** `inline bool`



### `switch(g)`

**Returns:** ``



### `isspace(Glyph g)`

**Returns:** `inline bool`



### `switch(g)`

**Returns:** ``



### `isadjustablespace(Glyph g)`

**Returns:** `inline bool`



### `switch(g)`

**Returns:** ``



### `isbreaking(Glyph g)`

**Returns:** `inline bool`



### `switch(g)`

**Returns:** ``



### `defaultspace(Glyph g, const GlyphRenderer &renderer)`

**Returns:** `inline float`



### `switch(g)`

**Returns:** ``



### `SetRenderer(renderer)`

**Returns:** ``



### `ASSERT(ok, "Font resource can only be a bitmapfont or freetype font")`

**Returns:** ``



### `if(br)`

**Returns:** ``



### `for(auto &p : *br)`

**Returns:** ``



### `if(bf)`

**Returns:** ``



### `for(auto &k : bf->kerning)`

**Returns:** ``



### `for(auto &p : *bf)`

**Returns:** ``



### `for(auto &p : *bf)`

**Returns:** ``



### `for(auto &i : bmps)`

**Returns:** ``



### `if(ft)`

**Returns:** `else`



### `if(data)`

**Returns:** `else`



### `while(!target)`

**Returns:** ``



### `if(gid == GID::Font_Props)`

**Returns:** ``



### `if(gid == GID::Font_FreeTypeData)`

**Returns:** `else`



### `if(sz)`

**Returns:** ``



### `if(gid == GID::Font_FreeTypeProps)`

**Returns:** `else`



### `if(gid == GID::Font_BitmapProps)`

**Returns:** `else`



### `if(gid == GID::Font_BitmapKerning)`

**Returns:** `else`



### `while(!kerntarget)`

**Returns:** ``



### `if(gid == GID::Font_Charmap)`

**Returns:** `else`



### `for(int i=0; i<256; i++)`

**Returns:** ``



### `if(gid == GID::Font_Charmap_II)`

**Returns:** `else`



### `for(unsigned i=0; i<size/20; i++)`

**Returns:** ``



### `if(gid == GID::Font_Image || gid == GID::Image)`

**Returns:** `else`



### `for(auto &p : descs)`

**Returns:** ``



### `if(bf)`

**Returns:** ``


