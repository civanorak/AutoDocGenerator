# AdvancedTextBuilder

> Auto-generated documentation for the **AdvancedTextBuilder** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `AdvancedTextBuilder`

**Namespace:** `Gorgon`


### `TableColumn`

**Namespace:** `Gorgon`

Defines a table column. If both pixel width and relative width are 0, the column is automatically sized.


---

## Enums

### `ImageAlign`

**Namespace:** `Gorgon`

Defines how an image will be aligned


---

## Functions

### `switch(align)`

**Returns:** ``


Alignment of text in the column Width in pixels Width in percentage Constructor, optionally initial string can be supplied. Appends the given data to the builder Appends the given data to the builder Returns the string built by this builder. Returns the string built by this builder. Returns the string built by this builder. You may change it. Returns the string built by this builder. Appends a line break that does not start a new paragraph. Appends a zero width breaking space. Resets all formatting instructions. @name Font style switching Use to change the current font. Bold and italic are exclusive and may not be available. Unless overridden, all styles can modify color, underline, strikethrough and paragraph and line spacing. @{ BEGIN Switch to superscript, use ScriptOff to switch off Switch to subscript, use ScriptOff to switch off Switches sub and superscript off Switches to the given font index. If it doesn't exist, default font will be used. Switches to the given font index. If it doesn't exist, default font will be used. END @} @name Color control These functions control the color of different parts of the system. Default color for text and border is set by font style. Default color for background is transparent. @{ BEGIN Sets the forecolor to the given 7-bit index. Sets the forecolor to the given index name. Sets the forecolor to the given color. Removes tint color that is used for images. Sets the tint color that is used for images to the given 7-bit index. Sets the tint color that is used for images to the given index name. Sets the tint color that is used for images to the given color. Sets the alpha that is used for images to the given color. Sets the background color to the given 7-bit index. Sets the background color to the given index name. Sets the background color to the given color. Sets the border color to the given 7-bit index. Sets the border color to the given index name. Sets the border color to the given color. Sets the underline color to the given 7-bit index. Sets the underline color to the given index name. Sets the underline color to the given color. Sets the strikethrough color to the given 7-bit index. Sets the strikethrough color to the given index name. Sets the strikethrough collor to the given color. Sets the text color of the selection. Default is NamedFontColors::Selection Sets the text color of the selection. Default is NamedFontColors::Selection Sets the text color of the selection. Default is NamedFontColors::Selection Sets the background color of the selection. Default is NamedFontColors::Selection. Disables selection image Sets the background color of the selection. Default is NamedFontColors::Selection. Disables selection image Sets the background color of the selection. Default is NamedFontColors::Selection. Disables selection image Uses default background color if no image is set. END @} @name Alignment These functions modify alignment of text and images. Default horizontal alignment is dictated by the font style. Default vertical alignment is baseline. @{ BEGIN Disables horizontal alignment and justify override. Aligns text to left. Disables justify. Aligns text to center. Disables justify. Aligns text to right. Disables justify. Aligns text to left. Enables justify. Aligns text to center. Enables justify. Aligns text to right. Enables justify. Sets the text alignment without changing justify.


### `SCI(Graphics::internal::SCI_ALIGN_LEFT)`

**Returns:** `case Graphics::TextAlignment::Left: return`



### `SCI(Graphics::internal::SCI_ALIGN_RIGHT)`

**Returns:** `case Graphics::TextAlignment::Right: return`



### `SCI(Graphics::internal::SCI_ALIGN_CENTER)`

**Returns:** `case Graphics::TextAlignment::Center: return`



### `CSI(Graphics::internal::CSI_SET_LETTER_OFFSET)`

**Returns:** ``


Turns justify on/off Modifies vertical alignment Modifies vertical alignment Modifies vertical alignment Modifies vertical alignment. This is the default alignment. END @} @name Marking @{ BEGIN Uses the style default for underline on/off state Uses the style default for strikethrough on/off state END @} @name Positioning @{ BEGIN Sets the width that the words will wrap from. Pixel and em widths will be added together. rel is relative to em size. Changes the offset that will be added to each letter. Relative sizing is relative to character width and line height, the value is in percentage.


### `ValAndRel(pixels.X, rel.X)`

**Returns:** ``



### `ValAndRel(pixels.Y, rel.Y)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_SET_UNDERLINE_SETTINGS)`

**Returns:** ``


Changes the offset of underline. rel is relative to line height and in percentage. Changes underline settings. Thickness will be set to default. If no parameters are given, will set all of them to defaults.


### `Index(1 | descenders<<2 | spaces<<3 | tabs<<4 | gaps<<5 | placeholders<<6)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_SET_UNDERLINE_SETTINGS)`

**Returns:** ``


Changes underline thickness. rel is relative to line thickness and is in percentage


### `Index(0b10)`

**Returns:** ``



### `ValAndRel(pixels, rel)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_SET_STRIKETHROUGH_SETTINGS)`

**Returns:** ``


Changes the offset of strike. rel is relative to line height and in percentage. Changes strike settings. If no parameters are given, will set them to defaults.


### `Index(1 | 1<<2 | spaces<<3 | tabs<<4 | gaps<<5 | placeholders<<6)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_SET_STRIKETHROUGH_SETTINGS)`

**Returns:** ``


Changes strike thickness. rel is relative to line thickness and is in percentage


### `Index(0b10)`

**Returns:** ``



### `ValAndRel(pixels, rel)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_ADD_BREAKING_LETTERS)`

**Returns:** ``


Add letters that will be used to break text from. Useful for code views.


### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_REMOVE_BREAKING_LETTERS)`

**Returns:** ``


Removes letters that will be used to break text from. Useful for code views.


### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_SET_BORDER_PADDING)`

**Returns:** ``


END @} @name Spacing @{ BEGIN Changes the spacing between paragraphs. rel is relative to line height and in percentage. This value is applied after line spacing. Changes the spacing between lines. rel is relative to line height and in percentage. Changes the spacing between the letters. rel is relative to em width and in percentage. Changes the indent. rel is relative to em width and in percentage. Changes the indent of the start of paragraphs. rel is relative to em width and in percentage. Place the requested amount of space horizontally. rel is relative to em width and in percentage. per is relative to wrap width and in basis points (1/10000). This space will not be breaking. If breaking is desired, you may insert zero width space. Place the requested amount of space vertically. rel is relative to line height and in percentage. Changes the spacing between the tab stops. rel is in em width and is in percentage. per is basis points of wrap width Uses default tab width Adds a tabstop. The tabstop with the given index will be located at the specified location. It replaces nearest tabstop. rel is in space widths. per is basis point of wrap width Removes the tabstop at the given index. END @} @name Box Controls box features such as background and border. Default background color is transparent, it must be changed if background is to be used. Default border thickness is set to underline thickness of the default font. Border and background are off by default. They will be turned on and used for tables. @{ BEGIN Sets the border thickness. rel is relative to underline thickness and is in percentage. Default thickness is pixels = 0, rel = 100 Sets the padding of the text from the border. rel is relative to underline thickness and is in percentage. Default padding is pixels = 0, rel = 100


### `ValAndRel(pixels.Left, rel.Left)`

**Returns:** ``



### `ValAndRel(pixels.Top, rel.Top)`

**Returns:** ``



### `ValAndRel(pixels.Right, rel.Right)`

**Returns:** ``



### `ValAndRel(pixels.Bottom, rel.Bottom)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_SET_SELECTION_PADDING)`

**Returns:** ``


Sets the padding of the selected text from the selected image border. This includes the width of the border. rel is relative to line thickness and is in percentage. Default is pixels = 0, rel = 0.


### `ValAndRel(pixels.Left, rel.Left)`

**Returns:** ``



### `ValAndRel(pixels.Top, rel.Top)`

**Returns:** ``



### `ValAndRel(pixels.Right, rel.Right)`

**Returns:** ``



### `ValAndRel(pixels.Bottom, rel.Bottom)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_DISPLAY_IMAGE)`

**Returns:** ``


END @} @name Image @{ BEGIN Displays the image with the given ID aIf the image is larger than the wrap width


### `Index(index)`

**Returns:** ``



### `Index(0)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_DISPLAY_IMAGE)`

**Returns:** ``


Displays the image with the given ID and offset. If the image is larger than the wrap width, it will be shrunk.


### `Index(index)`

**Returns:** ``



### `Index(0b100)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_DISPLAY_IMAGE)`

**Returns:** ``


Displays the image with the given ID and size. Image will be scale proportionally to this area. If any dimension is 0, it will be ignored. relsize is relative to wrap width and line height and is in percentage.


### `Index(index)`

**Returns:** ``



### `Index(0b1000)`

**Returns:** ``



### `Index(0b1100)`

**Returns:** ``



### `ValAndRel(pixelsize.Width, relsize.Width)`

**Returns:** ``



### `ValAndRel(pixelsize.Height, relsize.Height)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `CSI(Graphics::internal::CSI_DISPLAY_IMAGE)`

**Returns:** ``


Displays the image with the given ID, side and margin. If the image is larger than the wrap width, it will be shrunk.


### `Index(index)`

**Returns:** ``



### `if(margintype == 1)`

**Returns:** ``



### `if(margintype == 2)`

**Returns:** `else`



### `ST()`

**Returns:** `return`



### `AlignedImage(index, side, Geometry::Point{0, 0}, margins)`

**Returns:** `return`


Displays the image with the given ID and offset. If the image is larger than the wrap width, it will be shrunk.


### `CSI(Graphics::internal::CSI_DISPLAY_IMAGE)`

**Returns:** ``


Displays the image with the given ID, side and margin. If the image is larger than the wrap width, it will be shrunk. If any dimension of the size is zero, it will be ignored.


### `Index(index)`

**Returns:** ``



### `ValAndRel(pixelsize.Width, relsize.Width)`

**Returns:** ``



### `ValAndRel(pixelsize.Height, relsize.Height)`

**Returns:** ``



### `if(margintype == 1)`

**Returns:** ``



### `if(margintype == 2)`

**Returns:** `else`



### `ST()`

**Returns:** `return`



### `AlignedImage(index, side, pixelsize, relsize, {0, 0}, margins)`

**Returns:** `return`


Displays the image with the given ID and offset. If the image is larger than the wrap width, it will be shrunk. If any dimension of the size is zero, it will be ignored.


### `CSI(Graphics::internal::CSI_BEGIN_TABLE)`

**Returns:** ``


END @} @name Table These functions allow generation of tables @{ BEGIN Starts a table. Tables use background and border settings. Set border thickness to 0 to disable table border. relwidth is relative to wrap width and in percentage.


### `Index(drawouterborder)`

**Returns:** ``



### `ValAndRel(pixelwidth, relwidth)`

**Returns:** ``



### `for(auto c : columns)`

**Returns:** ``



### `RS()`

**Returns:** ``



### `ValAndRel(c.Width, c.RelWidth)`

**Returns:** ``



### `ST()`

**Returns:** `return`



### `if(colspan > 1)`

**Returns:** ``


Go to next cell. If colspan is set, span align is used to align the new joined column


### `CSI(Graphics::internal::CSI_COL_SPAN)`

**Returns:** ``



### `Index(colspan)`

**Returns:** ``



### `ST()`

**Returns:** ``



### `if(rowspan > 1)`

**Returns:** ``



### `CSI(Graphics::internal::CSI_ROW_SPAN)`

**Returns:** ``



### `Index(rowspan)`

**Returns:** ``



### `ST()`

**Returns:** ``



### `US()`

**Returns:** ``



### `CSI(Graphics::internal::CSI_PLACEHOLDER)`

**Returns:** ``


END @} @name Selection These functions help to display selection marker @{ Sets the selection image, disables selection background color. Removes the selection image and color. Calling this function will effectively remove all background from the selected text. @} @name Regions Regions are ranges of text. AdvancedPrint function will return a list of region boundaries. Each region will have one or more boundaries. Multiple boundaries are returned if a region spans multiple lines. You may use same region id multiple times. Regions can overlap. @{ Places a placeholder space. Placeholder will be wrapped as if it is a single glyph. Relative is relative to wrap width and line height and is in percentage.


### `ValAndRel(pixels.Width, rel.Width)`

**Returns:** ``



### `ValAndRel(pixels.Height, rel.Height)`

**Returns:** ``



### `ST()`

**Returns:** ``



### `Int(int16_t val)`

**Returns:** `void`


Places a placeholder space. Placeholder will be wrapped as if it is a single glyph. This overload will have the same size as the previous placeholder. @}


### `Index(Byte ind)`

**Returns:** `void`



### `Alpha(Byte alpha)`

**Returns:** `void`



### `Color(Graphics::RGBA color)`

**Returns:** `void`



### `ValAndRel()`

**Returns:** `void`



### `Index(127)`

**Returns:** ``



### `ValAndRel(short value, short rel)`

**Returns:** `void`



### `Int(value)`

**Returns:** ``



### `Int(rel)`

**Returns:** ``



### `ValRelAndPer()`

**Returns:** `void`



### `Index(127)`

**Returns:** ``



### `ValRelAndPer(short value, short rel, short per)`

**Returns:** `void`



### `Int(value)`

**Returns:** ``



### `Int(rel)`

**Returns:** ``



### `Int(per)`

**Returns:** ``



### `CSI(char cmd)`

**Returns:** `void`



### `RS()`

**Returns:** `void`



### `US()`

**Returns:** `void`


