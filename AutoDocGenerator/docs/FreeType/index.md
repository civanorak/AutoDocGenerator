# FreeType

> Auto-generated documentation for the **FreeType** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `ftlib`

**Namespace:** `Gorgon`

#### Methods

##### `ftlib(—)`

**Returns:** ``

##### `FT_Init_FreeType(&library)`

**Returns:** ``

##### `destroyface(—)`

**Returns:** `void`

##### `FT_Done_Face(face)`

**Returns:** ``

##### `FT_Done_FreeType(library)`

**Returns:** ``


### `FreeType`

**Namespace:** `Gorgon`

@cond internal @endcond


### `GlyphDescriptor`

**Namespace:** `Gorgon`

to be used internally.


### `Images`

**Namespace:** `Gorgon`


---

## Functions

### `FT_Set_Transform(face, matrix, delta)`

**Returns:** ``



### `if(ftbmp.pitch < 0)`

**Returns:** ``



### `if(ftbmp.pixel_mode == FT_PIXEL_MODE_MONO)`

**Returns:** ``



### `for(unsigned y=0; y<ftbmp.rows; y++)`

**Returns:** ``



### `for(unsigned x=0; x<ftbmp.width; x++)`

**Returns:** ``



### `if(b<0)`

**Returns:** ``



### `for(unsigned y=0; y<ftbmp.rows; y++)`

**Returns:** ``



### `for(unsigned x=0; x<ftbmp.width; x++)`

**Returns:** ``



### `if(ftbmp.pixel_mode == FT_PIXEL_MODE_MONO)`

**Returns:** ``



### `for(unsigned y=0; y<ftbmp.rows; y++)`

**Returns:** ``



### `for(unsigned x=0; x<ftbmp.width; x++)`

**Returns:** ``



### `if(b<0)`

**Returns:** ``



### `for(unsigned y=0; y<ftbmp.rows; y++)`

**Returns:** ``



### `for(unsigned x=0; x<ftbmp.width; x++)`

**Returns:** ``



### `if(lib->face->charmap == nullptr)`

**Returns:** ``



### `if(error == FT_Err_Ok)`

**Returns:** ``



### `if(error == FT_Err_Ok)`

**Returns:** ``



### `if(lib->face->num_charmaps > 0)`

**Returns:** ``



### `if(error != FT_Err_Ok)`

**Returns:** ``



### `LoadGlyphs({0, {0x20, 0x7f}})`

**Returns:** `return`



### `file(filename, std::ios::binary)`

**Returns:** `std::ifstream`



### `for(int i=0; i<lib->face->num_fixed_sizes; i++)`

**Returns:** ``



### `if(diff < mindiff)`

**Returns:** ``



### `for(Glyph g = range.Start; g <= range.End; g++)`

**Returns:** ``



### `if(index == 0)`

**Returns:** ``



### `for(int i=0; i<lib->face->num_charmaps; i++)`

**Returns:** ``



### `FT_Set_Charmap(lib->face, lib->face->charmaps[i])`

**Returns:** ``



### `if(!bmp || !withoffset)`

**Returns:** ``



### `if(prepare)`

**Returns:** ``



### `for(int i=0; i<lib->face->num_fixed_sizes; i++)`

**Returns:** ``



### `float(height / 4)`

**Returns:** `return`



### `LoadGlyphs(chr)`

**Returns:** ``



### `for(auto it=text.begin()`

**Returns:** ``



### `loadglyphs(range, true)`

**Returns:** ``



### `pack()`

**Returns:** ``



### `if(haskerning)`

**Returns:** ``



### `for(auto &l : glyphmap)`

**Returns:** ``



### `for(auto &r : glyphmap)`

**Returns:** ``



### `if(p.X != 0 || p.Y != 0)`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `if(haskerning)`

**Returns:** ``



### `for(auto &l : glyphmap)`

**Returns:** ``



### `for(auto &r : glyphmap)`

**Returns:** ``



### `if(p.X != 0 || p.Y != 0)`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `for(const auto &i : destroylist)`

**Returns:** ``



### `Clear()`

**Returns:** ``



### `nu(w*h)`

**Returns:** `std::vector<bool>`



### `for(auto &g : glyphmap)`

**Returns:** ``



### `ni({w, h}, ColorMode::Alpha)`

**Returns:** `Containers::Image`



### `for(auto &g : glyphmap)`

**Returns:** ``



### `for(auto &i : images)`

**Returns:** ``



### `setatlassize(cursize)`

**Returns:** ``



### `setatlassize(cursize)`

**Returns:** ``



### `for(auto &b : images)`

**Returns:** ``



### `if(!tightpack)`

**Returns:** ``



### `while(!found)`

**Returns:** ``



### `if(cur.X + w > aw)`

**Returns:** ``



### `if(cur.Y + h > ah)`

**Returns:** ``



### `setatlassize(cursize)`

**Returns:** ``



### `for(auto &img : replacements)`

**Returns:** ``



### `for(int x=cur.X; x<cur.X+w; x++)`

**Returns:** ``



### `if(used[x + cur.Y * aw])`

**Returns:** ``



### `if(full)`

**Returns:** ``



### `for(int y=cur.Y; y<cur.Y+h; y++)`

**Returns:** ``



### `if(used[cur.X + y * aw])`

**Returns:** ``



### `if(full)`

**Returns:** ``



### `for(int y=cur.Y; y<cur.Y+h; y++)`

**Returns:** ``



### `for(int x=cur.X; x<cur.X+w; x++)`

**Returns:** ``



### `if(cpeach)`

**Returns:** ``



### `if(!cpeach)`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `for(auto &im : images)`

**Returns:** ``



### `for(auto r : ranges)`

**Returns:** ``



### `pack()`

**Returns:** ``



### `pack()`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `if(asciionly)`

**Returns:** ``



### `loadglyphs('A', true)`

**Returns:** ``



### `loadglyphs('f', true)`

**Returns:** ``



### `loadglyphs('j', true)`

**Returns:** ``



### `loadglyphs('A', true)`

**Returns:** ``



### `loadglyphs(0xc2, true)`

**Returns:** ``



### `loadglyphs('f', true)`

**Returns:** ``



### `loadglyphs('j', true)`

**Returns:** ``



### `for(int i = 0; i<3; i++)`

**Returns:** ``



### `for(int i = 0; i<3; i++)`

**Returns:** ``



### `GlyphDescriptor()`

**Returns:** ``



### `FreeType()`

**Returns:** ``


holds two bitmaps, a regular and one rendered with 0.5 pixel offset Initializes the class without loading any glyphs or files. Any calls to render or get size attempts will not perform any operation or returns 0. Use this constructor to font data from memory.


### `LoadFile(filename)`

**Returns:** ``


Initializes the class by loading the given file. After this step only generic information about the font file will be provided. You may continue loading by LoadMetrics function.


### `LoadFile(filename, size, loadascii)`

**Returns:** ``


Initializes the class by loading the given file.


### `LoadFile(const std::string &filename)`

**Returns:** `bool`


No copy constructor No copy assignment Destructor Loads the given file. Unloads the previous file, if it exists. This operation will not unload loaded glyphs. Use Clear function to unload already loaded glyphs. After this step only generic information about the font file will be provided. You may continue loading by LoadMetrics function.


### `LoadFile(const std::string &filename, int size, bool loadascii = true)`

**Returns:** `bool`


Loads the given file. Unloads the previous file, if it exists. This operation will not unload loaded glyphs. Use Clear function to unload already loaded glyphs.


### `Load(const std::vector<Byte> &data)`

**Returns:** `bool`


Loads the given data. Unloads the previous file, if it exists. This operation will not unload loaded glyphs. Use Clear function to unload already loaded glyphs. After this step only generic information about the font file will be provided. You may continue loading by LoadMetrics function. Data will be required for the life time of this object. See assume for transferring ownership of the data.


### `Load(const Byte *data, long datasize)`

**Returns:** `bool`


Loads the given data. Unloads the previous file, if it exists. This operation will not unload loaded glyphs. Use Clear function to unload already loaded glyphs. After this step only generic information about the font file will be provided. You may continue loading by LoadMetrics function.


### `Assume(std::vector<Byte> &data)`

**Returns:** `bool`


Loads the given data. Unloads the previous file, if it exists. This operation will not unload loaded glyphs. Use Clear function to unload already loaded glyphs. After this step only generic information about the font file will be provided. You may continue loading by LoadMetrics function. This function will keep the copy of the data for further operations. The data of the vector given to this function will be moved out of it.


### `Assume(const Byte *data, long datasize)`

**Returns:** `bool`


Loads the given data. Unloads the previous file, if it exists. This operation will not unload loaded glyphs. Use Clear function to unload already loaded glyphs. After this step only generic information about the font file will be provided. You may continue loading by LoadMetrics function. After this object is done with the data, it will destroy it.


### `LoadMetrics(int size)`

**Returns:** `bool`


Continues loading a file by setting font size and obtaining necessary information. If the given size is invalid, this function will return 0. Use GetPresetSizes function to get list of sizes that the font supports. You may also check IsScalable return to check whether using an arbitrary size is allowed.


### `LoadGlyphs(GlyphRange range, bool prepare = true)`

**Returns:** `bool`


Loads the glyphs in the given range. It is possible to LoadGlyphs functions multiple times. If a glyph in the given range is already loaded, it will not be loaded again.


### `LoadGlyphs(Glyph start, Glyph end, bool prepare = true)`

**Returns:** `bool`


Loads the glyphs in the given range. It is possible to LoadGlyphs functions multiple times. If a glyph in the given range is already loaded, it will not be loaded again.


### `LoadGlyphs(const std::vector<GlyphRange> &ranges, bool prepare = true)`

**Returns:** `bool`


Loads the glyphs in the given range. It is possible to LoadGlyphs functions multiple times. If a glyph in the given range is already loaded, it will not be loaded again. This overload will load all ranges given in the vector. It terminates at first error.


### `IsScalable()`

**Returns:** `bool`


Returns if the loaded font is scalable. This information is not very useful once the glyphs are loaded, however, you may check this information to ensure LoadMetrics function is presented with a valid size. Will return false if no file is loaded.


### `GetPresetSizes()`

**Returns:** `std::vector<int>`


Returns the preset sizes in the font file. If the font is not scalable, these are the only sizes that will work. Will return empty vector if no file is loaded.


### `IsFileLoaded()`

**Returns:** `bool`


Returns whether the file is loaded. Check IsReady


### `IsSymbolOnly()`

**Returns:** `bool`


Returns if the FreeType is ready to work. If the metrics are set and either the file is loaded or there are loaded glyphs this function will return true. Returns whether the font is a symbol only font


### `HasKerning()`

**Returns:** `bool`


Returns whether this font contains kerning table


### `DisableAntiAliasing()`

**Returns:** `void`


Disables anti aliasing. Does not affect already loaded glyphs. If necessary call Clear before calling this function.


### `EnableAntiAliasing()`

**Returns:** `void`


Enables anti aliasing. Does not affect already loaded glyphs. If necessary call Clear before calling this function.


### `GetFamilyName()`

**Returns:** `std::string`


Returns the name of the font


### `GetStyleName()`

**Returns:** `std::string`


Returns the style name of the font


### `Clear()`

**Returns:** `void`


Clears the glyphs that are loaded


### `CopyToBitmap(bool prepare = true)`

**Returns:** `BitmapFont`


Copy the loaded glyphs into a new bitmap font. Only the glyphs that are already loaded will be copied into the bitmap font. This object will keep its loaded glyphs after a call to this function. Use MoveOutBitmap to convert this font to bitmap to move out bitmaps, avoiding copying. This function will automatically unpack glyphs if discard is not called.


### `MoveOutBitmap(bool unpack = false, bool prepare = true)`

**Returns:** `BitmapFont`


Moves the loaded glyphs into a new bitmap font. Only the glyphs that are already loaded will be copied into the bitmap font. This object will loose its glyphs but will be able to reload them if requested. Use CopyToBitmap to convert this font to bitmap with the copies of glyphs. If requested this function can unpack glyphs to create a bitmap font with bitmaps as glyphs, which then can be saved. However, this functionality will not work if discard is called. Prepare parameter is used if the font is unpacked.


### `Pack(bool keeppacked = true, bool tight = true, float extrasize = 0.2)`

**Returns:** `void`


Packs current glyphs into a single atlas. If keeppacked is selected, any call to LoadGlyph function pack the loaded asset immediately.


### `pack(extrasize)`

**Returns:** ``



### `StopPacking()`

**Returns:** `void`


Stops packing new glyphs. This will not unpack already packed glyphs. Use Pack function to pack all glyphs and set packing for future glyphs.


### `Available(Glyph g)`

**Returns:** `bool`


This function should render the given character to the target at the specified location and color. If chr does not exists, this function should perform no action. location and color can be modified as per the needs of renderer. If the kerning returns integers location will always be an integer. Additionally, text renderers will place glyphs on 0 y position from the top. It is glyph renderer's task to ensure baseline of glyphs to line up. This function will return the drawable that is used to render the given glyph. This function will load the glyph if necessary. If glyph is not found, this function will return nullptr or not found character. This function should return the size of the requested glyph. If it does not exists, 0x0 should be returned This function should return the number of pixels the cursor should advance after this glyph. This value will be added to kerning distance. Returns true if the glyph exists Returns true if the glyph is available in the font. Exists will return true if it is already loaded.


### `Discard()`

**Returns:** `void`


This function should return true if this font renderer supports only 7-bit ASCII This function should return true if this font is fixed width. This will suppress calls to GetSize function. This function should return the additional distance between given glyphs. Returned value could be (in most cases it is) negative. Returns the size of the EM dash Returns the advance the of widest glyph. Height of glyphs, actual size could be smaller but all glyphs should have the same virtual height. When drawn on the same y position, all glyphs should line up. Renderer can change actual draw location to compensate. Width of a digit, if digits do not have the same width, maximum should be returned. For practical reasons, this function is expected to consider arabic numerals. Baseline point of glyphs from the top. Returns the spacing between the lines. Should return the average thickness of a line. This information can be used to construct underline and strike through. The position of the underline, if it is to be drawn. Should return if the glyph renderer requires preparation regarding the text given. Notifies glyph renderer about a text to be rendered. If renderers require modification to their internal structures, they should mark them Discards intermediate files. Font will continue to work and will take less resources, however, new glyphs cannot be loaded and packed after this function is issued. Additionally, bitmap font copying and unpacking option in moving out will not work.


### `pack(float extrasize = 0.2)`

**Returns:** `void`



### `loadglyphs(GlyphRange range, bool prepare)`

**Returns:** `bool`



### `finalizeload()`

**Returns:** `bool`



### `savedata(std::ostream &stream)`

**Returns:** `bool`



### `setatlassize(unsigned size)`

**Returns:** `void`


