# BitmapFont

&gt; Auto-generated documentation for the **BitmapFont** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `glyphdata`

**Namespace:** `Gorgon`


### `BitmapFont`

**Namespace:** `Gorgon`


### `GlyphDescriptor`

**Namespace:** `Gorgon`

to be used internally.

#### Methods

##### `GlyphDescriptor(—)`

**Returns:** ``


### `ImportOptions`

**Namespace:** `Gorgon`

Use this structure to specify options for import operations


### `gtog`

**Namespace:** `Gorgon`


---

## Enums

### `ImportNamingTemplate`

**Namespace:** `Gorgon`


### `DeleteConstants`

**Namespace:** `Gorgon`

Filenames will be examined to determine the template. When this is set and prefix is empty, prefix is also tried to be determined Characters are the filenames, not recommended as some symbols will not be accepted as filename Decimal code of the character is used as filename Hexadecimal code of the character is used as filename


---

## Functions

### `swap(glyphmap, other.glyphmap)`

**Returns:** ``



### `swap(destroylist, other.destroylist)`

**Returns:** ``



### `swap(kerning, other.kerning)`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `if(maxwidth == 0)`

**Returns:** ``



### `if(baseline == 0)`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `for(; dir.IsValid()`

**Returns:** ``



### `if(prefix != "")`

**Returns:** ``



### `catch(...)`

**Returns:** ``



### `if(naming == Automatic)`

**Returns:** ``



### `for(auto p : files)`

**Returns:** ``



### `if(name[i] != prefix[i])`

**Returns:** ``



### `if(i == 0)`

**Returns:** ``



### `for(auto p : files)`

**Returns:** ``



### `for(auto c : name)`

**Returns:** ``



### `if(digitonly)`

**Returns:** ``



### `if(digitonly)`

**Returns:** ``



### `if(hexonly)`

**Returns:** `else`



### `if(!multichar)`

**Returns:** ``



### `if(digitonly)`

**Returns:** `else`



### `if(hexonly)`

**Returns:** `else`



### `for(auto p : files)`

**Returns:** ``



### `if(start == 0 && minval == 0)`

**Returns:** ``



### `if(options.converttoalpha == YesNoAuto::Auto)`

**Returns:** ``



### `for(auto p : files)`

**Returns:** ``



### `if(prevcolor.A == 0)`

**Returns:** ``



### `for(auto p : files)`

**Returns:** ``



### `if(naming == Alpha)`

**Returns:** ``



### `if(naming == Decimal)`

**Returns:** `else`



### `if(g == ' ')`

**Returns:** ``



### `if(options.trim)`

**Returns:** ``



### `if(g == '_')`

**Returns:** ``



### `if(options.baseline == -1)`

**Returns:** ``



### `if(bmp)`

**Returns:** ``



### `if(a != -1)`

**Returns:** ``



### `for(int x=0; x<bmp->GetWidth()`

**Returns:** ``



### `if(options.baseline == -1)`

**Returns:** ``



### `if(options.trim && spim && maxwidth == spw)`

**Returns:** ``



### `if(alphaloc != -1)`

**Returns:** ``



### `if(isempty)`

**Returns:** ``



### `if(options.prepare && !options.pack)`

**Returns:** ``



### `if(options.trim && uh)`

**Returns:** ``



### `if(options.trim && spacing==0)`

**Returns:** `else`



### `AutoKern(64, options.automatickerningreduction)`

**Returns:** ``



### `Pack()`

**Returns:** ``



### `for(int y=0; y<=searchsize.Height; y+= grid.Height)`

**Returns:** ``



### `for(int x=0; x<=searchsize.Width; x+= grid.Width)`

**Returns:** ``



### `for(int y=0; y<=bmp.GetHeight()`

**Returns:** ``



### `for(int x=0; x<bmp.GetWidth()`

**Returns:** ``



### `if(lastempty && !empty)`

**Returns:** ``



### `if(!lastempty && empty)`

**Returns:** `else`



### `for(auto row : rows)`

**Returns:** ``



### `for(int x=0; x<=bmp.GetWidth()`

**Returns:** ``



### `for(int y=row.first; y<row.second; y++)`

**Returns:** ``



### `if(lastempty && !empty)`

**Returns:** ``



### `if(!lastempty && empty)`

**Returns:** `else`



### `if(options.spacing == -1)`

**Returns:** ``



### `if(options.converttoalpha == YesNoAuto::Auto)`

**Returns:** ``



### `if(c.A)`

**Returns:** ``



### `if(prevcolor.A == 0)`

**Returns:** ``



### `if(prevcolor != c)`

**Returns:** `else`



### `if(options.trim)`

**Returns:** ``



### `for(auto &b : bounds)`

**Returns:** ``



### `if(expand)`

**Returns:** ``



### `if(options.converttoalpha == YesNoAuto::Yes)`

**Returns:** ``



### `for(auto b : bounds)`

**Returns:** ``



### `if(start == '_')`

**Returns:** ``



### `if(options.converttoalpha == YesNoAuto::Yes)`

**Returns:** ``



### `for(auto b : bounds)`

**Returns:** ``



### `if(start == '_')`

**Returns:** ``



### `if(options.baseline == -1)`

**Returns:** ``



### `if(options.trim)`

**Returns:** ``



### `if(uh)`

**Returns:** ``



### `AutoKern(64, options.automatickerningreduction)`

**Returns:** ``



### `if(expand)`

**Returns:** ``



### `Pack()`

**Returns:** ``



### `if(capitaloffset == -1)`

**Returns:** ``



### `if(bmp)`

**Returns:** ``



### `for(int y=0; y<b.GetHeight()`

**Returns:** ``



### `for(int x=0; x<b.GetWidth()`

**Returns:** ``



### `if(!empty)`

**Returns:** ``



### `for(auto &g : glyphmap)`

**Returns:** ``



### `for(y=0; y<yoff; y++)`

**Returns:** ``



### `for(; y<yoff + h; y++)`

**Returns:** ``



### `for(; y<height; y++)`

**Returns:** ``



### `for(int y=std::max(0, -yoff)`

**Returns:** ``



### `for(x=0; x<w; x++)`

**Returns:** ``



### `for(x=0; x<w; x++)`

**Returns:** ``



### `for(y=0; y<yoff+h; y++)`

**Returns:** ``



### `for(auto &l : glyphmap)`

**Returns:** ``



### `for(auto &r : glyphmap)`

**Returns:** ``



### `for(int y=0; y<height; y++)`

**Returns:** ``



### `for(int yy = std::max(0, y-spacing)`

**Returns:** ``



### `for(auto &p : glyphmap)`

**Returns:** ``



### `if(bmp)`

**Returns:** ``



### `for(auto g : packing)`

**Returns:** ``



### `for(auto &p : glyphmap)`

**Returns:** ``



### `if(bmp)`

**Returns:** ``



### `swap(bounds, ret)`

**Returns:** ``



### `if(count == 1)`

**Returns:** ``



### `if(asciionly)`

**Returns:** ``



### `for(int i = 0; i<3; i++)`

**Returns:** ``



### `for(int i = 0; i<3; i++)`

**Returns:** ``



### `for(int y=0; y<bmp->GetHeight()`

**Returns:** ``



### `for(int x=0; x<bmp->GetWidth()`

**Returns:** ``



### `if(!foundfirst && !found)`

**Returns:** ``



### `if(found)`

**Returns:** ``



### `float(s + spacing)`

**Returns:** `return`



### `swap(glyphmap, other.glyphmap)`

**Returns:** ``



### `swap(destroylist, other.destroylist)`

**Returns:** ``



### `swap(kerning, other.kerning)`

**Returns:** ``



### `Duplicate()`

**Returns:** `BitmapFont`


Packs the bitmap font. This is optimal for rendering. However, packed fonts cannot be saved as resource. Set baseline to specific height. Use of non-integer values may caused blurriness in font rendering. Value of -1 means automatically detect according to estimatebaseline option. Whether to trim whitespace around the glyphs. This will also trigger automatic advance calculation. It is best to set this to true if using automatic kerning Whether to convert imported images to alpha only images. Conversion to alpha only is helpful to speed up text rendering, allows fonts that are represented with a different color than white to work properly. However, colored fonts will not work. Setting this to Auto will detect if conversion is safe by checking whether all pixels have the same color. However, this process is very slow. Prepares the loaded bitmaps. If pack option is set, this option is ignored. If baseline is set to -1 (auto), setting this to true will use cheap baseline calculation instead of searching it in letter A. If letter A does not exists, this option is enforced. Whether to apply automatic kerning after import is completed. If automatic kerning is applied, this value will be used to reduce the kerning amount. Removing kerning reduction will cause tighter kerning, increasing it will reduce the effect of kerning. Spaces between characters, -1 activates auto detection.


### `BitmapFont(BitmapFont &&other)`

**Returns:** ``



### `AddGlyph(Glyph glyph, const RectangularDrawable &bitmap, int baseline = 0)`

**Returns:** `void`


Moves another bitmap font into this one. This font will be destroyed in this process Adds a new glyph bitmap to the list. If a previous one exists, it will be replaced. Ownership of bitmap is not transferred. TODO: better baseline handling


### `AddGlyph(Glyph glyph, const RectangularDrawable &bitmap, Geometry::Pointf offset, float advance)`

**Returns:** `void`


Adds a new glyph bitmap to the list. If a previous one exists, it will be replaced. Ownership of bitmap is not transferred.


### `AssumeGlyph(Glyph glyph, const RectangularDrawable &bitmap, int baseline = 0)`

**Returns:** `void`


Adds a new glyph bitmap to the list. If a previous one exists, it will be replaced. Ownership of bitmap is not transferred.


### `AddGlyph(glyph, bitmap, baseline)`

**Returns:** ``



### `AssumeGlyph(Glyph glyph, const RectangularDrawable &bitmap, Geometry::Pointf offset, float advance)`

**Returns:** `void`


Adds a new glyph bitmap to the list. If a previous one exists, it will be replaced. Ownership of bitmap is not transferred.


### `AddGlyph(glyph, bitmap, offset, advance)`

**Returns:** ``



### `SetKerning(Glyph left, Glyph right, Geometry::Pointf kern)`

**Returns:** `void`



### `SetKerning(Glyph left, Glyph right, float x)`

**Returns:** `void`



### `Pack(bool tight = false, DeleteConstants del = Owned)`

**Returns:** `void`


Converts individual glyphs to a single atlas. Only the glyphs that are registered as bitmaps can be packed. This function will automatically detect types and act accordingly. If the ownership of the packed images belong to the font and del parameter is set to owned, owned images that are created either by import or a previous pack will be destroyed. If it is set to all, all images that took part in packing will be destroyed If tight packing is set, glyphs will be placed next to each other, saving space. However, if resized, they will have artifacts.


### `CreateAtlas(std::vector<Geometry::Bounds> &bounds, bool tight = false)`

**Returns:** `Graphics::Bitmap`


Performs packing without changing the font itself


### `SetHeight(int value)`

**Returns:** `void`


Changes the line height of the font. Adding glyphs may override this value.


### `SetMaxWidth(int value)`

**Returns:** `void`


Changes the maximum width for a character. Adding glyphs may override this value.


### `DetermineDimensions()`

**Returns:** `void`


Searches through the currently registered glyphs to determine dimensions. This function will calculate following values: height, max width, underline offset. Baseline is set to 0.7 * height if it is 0.


### `SetGlyphSpacing(int value)`

**Returns:** `void`


Changes the spacing between glyphs


### `GetGlyphSpacing()`

**Returns:** `int`


Returns the spacing between glyphs


### `SetLineThickness(int value)`

**Returns:** `void`


Changes the line thickness to the specified value.


### `SetUnderlineOffset(int value)`

**Returns:** `void`


Changes the underline position to the specified value.


### `SetBaseline(float value)`

**Returns:** `void`


Changes the baseline. Might cause problems if the font already has glyphs in it.


### `SetLineGap(float value)`

**Returns:** `void`


Changes the distance between two lines. Non-integer values are not recommended.


### `ImportAtlas(Bitmap &&bmp, Geometry::Size grid = {0, 0}, Glyph start = 0x20, bool expand = false, ImportOptions options = ImportOptions{})`

**Returns:** `int`


Imports bitmap font images from a folder with the specified file naming template. Automatic detection will only work if there is a single bitmap font set in the folder. If baseline is set to a negative value, it would be calculated as 70% of the font height. Only png files are considered for import. If converttoalpha is set, then the images read will be converted to alpha only images. Import will import separate images, you may use Pack function to pack them to an image atlas. If prepare is set, the imported images will be prepared and font will be ready to be used. As of now, this function cannot deal with animated fonts. start parameter can be used for adjusting numeric offset. If template naming is automatic and the value is left as 0, it will be determined automatically so that the imported images will be matched with printable characters. Any files that start with . and _ is ignored, unless it is the name of the file. This function will return the number of images imported. Imported images will be destroyed by this object. Automatic conversion can cause issues with suffixes, however, if naming is set, any additional text after the number or character is ignored. This function calculates the line thickness using trimmed height of the underscore. If trimming is not set, this functionality will not work. Additionally, this function will set underline position to halfway between baseline and bottom. If estimatebaseline is set, then the baseline position is a simple estimate instead of a search. The search will look at A to find the lowest pixel to declare it baseline. Returns number of glyphs that are imported. Imports the given bitmap as atlas image. The bitmap data will be copied out of the given bitmap. If grid is not specified or specified as zero size, glyph locations will be determined automatically. This automatic detection requires glyphs to be arranged in lines and there must be at least 1px space between the lines and the glyphs. If saved, atlas images packed loosely by bitmap font will work with ImportAtlas function. However, packing algorithm of FreeType produces atlases with variable line height, making it impossible to determine glyph locations. packing options can be used to control the final result of glyphs. If you intend to save this font as a resource, you need to set expand to true. Space characters cannot be detected in automatic mode, thus they will be skipped. However, renderer has default space widths generated from font height.  Automatic detection can fail for double quotes and any other glyphs that are horizontally separate. Using ImportAtlas with automatic detection is difficult. you may need to modify atlas images to suit the function. Make sure there is at least 1px space between rows and glyphs are ordered as they should.


### `ImportAtlas(const Bitmap &bmp, Geometry::Size grid = {0, 0}, Glyph start = 0x20, bool expand = false, ImportOptions options = ImportOptions{})`

**Returns:** `int`


Imports the given bitmap as atlas image. The given bitmap will be duplicated. See ImportAtlas(Bitmap &&) for details.


### `ImportAtlas(const std::string &filename, Geometry::Size grid = {0, 0}, Glyph start = 0x20, bool expand = false, ImportOptions options = ImportOptions{})`

**Returns:** `int`


Imports the given file as atlas image. See ImportAtlas(Bitmap &&) for details.


### `AutoKern(Byte opaquelevel = 64, int reduce = 1, int capitaloffset = -1)`

**Returns:** `void`


Automatically calculates kerning distances between glyphs. This operation might take a while depending on the number of glyphs that are loaded. This function uses glyph spacing. This function is optimized for pixel fonts without fractional alpha. Glyphs should be bitmaps for this function to work properly. Additionally, this function either needs the Y-offset of capital letters, or the letter A should be present. This data will be used to determine accent symbols which should not be kerned. A value of -1 means use A to determine. If A is not present or the value is 0, this feature is disabled. The function takes glyph offsets into account. However, x offsets can cause issues.


### `Remove(Glyph g)`

**Returns:** `void`


Returns the image that represents a glyph Removes a glyph from the bitmap font. If this glyph is created by font object and this glyph is the last user of that resource, it will be destroyed. Use Release to prevent this from happening.


### `Release(RectangularDrawable &img)`

**Returns:** `bool`


If the given resource is owned by this bitmap font, its ownership will be released.


### `IsOwned(const RectangularDrawable &img)`

**Returns:** `bool`


Returns if the given image is owned by this bitmap font.


### `Adopt(const RectangularDrawable &img)`

**Returns:** `void`


This will add the given image to the list of images that will be destroyed with this object.


### `begin()`

**Returns:** `std::map<Glyph, GlyphDescriptor>::iterator`


@see Gorgon::Graphics::GlyphRenderer::GetLetterHeight. This function may produce incorrect values if the bitmap data for the used letters are not present.


### `end()`

**Returns:** `std::map<Glyph, GlyphDescriptor>::iterator`



### `begin()`

**Returns:** `std::map<Glyph, GlyphDescriptor>::const_iterator`



### `end()`

**Returns:** `std::map<Glyph, GlyphDescriptor>::const_iterator`


