# Generator

> Auto-generated documentation for the **Generator** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `Generator`

**Namespace:** `Gorgon`

#### Methods

##### `virtual` `Button(—)`

**Returns:** `virtual UI::Template`

Generates a button template

##### `virtual` `IconButton(—)`

**Returns:** `virtual UI::Template`

Generates a button template with the given default size.

##### `virtual` `DialogButton(—)`

**Returns:** `virtual UI::Template`

Generates a button template

##### `virtual` `Checkbox(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `CheckboxButton(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `RadioButton(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Label(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `ErrorLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `BoldLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `TitleLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `SubtitleLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `LeadingLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `InfoLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `IconLabel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Panel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `TopPanel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `LeftPanel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `BottomPanel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `RightPanel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `BlankPanel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Inputbox(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Progressbar(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `HScrollbar(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `VScrollbar(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Layerbox(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `BlankLayerbox(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Listbox(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Dropdown(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Window(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `DialogWindow(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `ColorPlane(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `ColorPicker(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `TabPanel(—)`

**Returns:** `virtual UI::Template`

##### `virtual` `Textarea(—)`

**Returns:** `virtual UI::Template`

##### `switch(type)`

**Returns:** ``


### `SimpleGenerator`

**Namespace:** `Gorgon`


### `FocusInfo`

**Namespace:** `Gorgon`


### `BorderInfo`

**Namespace:** `Gorgon`


### `AssetID`

**Namespace:** `Gorgon`

Identifies and helps with the creation of assets used in a generator

#### Methods

##### `static` `HBorders(BorderSide b)`

**Returns:** `static int`

##### `switch(b)`

**Returns:** ``

##### `static` `VBorders(BorderSide b)`

**Returns:** `static int`

##### `switch(b)`

**Returns:** ``

##### `static` `TotalBorders(BorderSide b)`

**Returns:** `static int`

##### `switch(b)`

**Returns:** ``

##### `static` `HasLeft(BorderSide b)`

**Returns:** `static bool`

##### `switch(b)`

**Returns:** ``

##### `static` `HasTop(BorderSide b)`

**Returns:** `static bool`

##### `switch(b)`

**Returns:** ``

##### `static` `HasRight(BorderSide b)`

**Returns:** `static bool`

##### `switch(b)`

**Returns:** ``

##### `static` `HasBottom(BorderSide b)`

**Returns:** `static bool`

##### `switch(b)`

**Returns:** ``


---

## Enums

### `CornerStyle`

**Namespace:** `Gorgon`

Constants to control style of corners


### `AssetType`

**Namespace:** `Gorgon`


### `BorderSide`

**Namespace:** `Gorgon`


---

## Functions

### `disassemblevalue(const Value &value)`

**Returns:** `std::string`



### `switch(value.Type)`

**Returns:** ``



### `Disassemble(const Instruction *instruction)`

**Returns:** `std::string`



### `switch(instruction->Type)`

**Returns:** ``



### `disassemblevalue(instruction->RHS)`

**Returns:** ``



### `disassemblevalue(instruction->RHS)`

**Returns:** ``



### `disassemblevalue(instruction->RHS)`

**Returns:** ``



### `disassemblevalue(instruction->RHS)`

**Returns:** ``



### `if(instruction->Store)`

**Returns:** ``



### `for(auto &param : instruction->Parameters)`

**Returns:** ``



### `Disassemble(Scope &scope, std::ostream &out)`

**Returns:** `void`



### `FindDefaultFontFamily(bool mono, const std::vector<Gorgon::OS::FontFamily> &list)`

**Returns:** `std::string`



### `if(!os)`

**Returns:** ``



### `FcPatternDestroy(pat)`

**Returns:** ``



### `if(fs && fs->nfont > 0)`

**Returns:** ``



### `FcPatternGetString(font, FC_FAMILY, 0, &family)`

**Returns:** ``



### `FcPatternDestroy(pat)`

**Returns:** ``



### `FcObjectSetDestroy(os)`

**Returns:** ``



### `FcPatternDestroy(pat)`

**Returns:** ``



### `FcObjectSetDestroy(os)`

**Returns:** ``



### `for(auto r : l)`

**Returns:** ``



### `for(auto &f : list)`

**Returns:** ``



### `if(mono)`

**Returns:** ``



### `for(auto &f : list)`

**Returns:** ``



### `for(auto &face : f.Faces)`

**Returns:** ``



### `FindFontFile(std::string family, bool bold, bool italic, const std::vector<Gorgon::OS::FontFamily> &list, bool mono)`

**Returns:** `std::string`



### `for(auto &f : list)`

**Returns:** ``



### `for(auto &face : f.Faces)`

**Returns:** ``



### `for(auto &f : list)`

**Returns:** ``



### `for(auto &face : f.Faces)`

**Returns:** ``



### `if(fam != family)`

**Returns:** ``



### `if(italic)`

**Returns:** ``



### `if(bold)`

**Returns:** ``



### `for(auto &t : colors)`

**Returns:** ``



### `initfontrelated()`

**Returns:** ``


Loads the specified fonts, while using supplied or default family for monospaced fonts.


### `italicfnt(*italicrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `bolditalicfnt(*bolditalicrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `smallfnt(*smallrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `largerfnt(*largerrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `scriptfnt(*scriptrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `boldscriptfnt(*boldscriptrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `smallscriptfnt(*smallscriptrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `fixedwidthfnt(*fixedwidthrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `fixedwidthboldfnt(*fixedwidthboldrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `fixedwidthitalicfnt(*fixedwidthitalicrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `fixedwidthbolditalicfnt(*fixedwidthbolditalicrenderer, regcol)`

**Returns:** `Graphics::StyledPrinter`



### `if(bordersize == -1)`

**Returns:** ``



### `if(border.Width > 2)`

**Returns:** ``



### `if(border.Shape > 2.f)`

**Returns:** ``



### `switch(corners)`

**Returns:** ``



### `switch(corners)`

**Returns:** ``



### `switch(id.Type)`

**Returns:** ``



### `ASSERT(prov, "Unknown asset")`

**Returns:** ``



### `if(borders == AssetID::None)`

**Returns:** ``



### `if(border.A != 0)`

**Returns:** ``



### `switch(borders)`

**Returns:** ``



### `if(missingedge != -1)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `if(missingedge != -1)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `if(missingedge == -1)`

**Returns:** ``



### `if(missingedge == 0)`

**Returns:** ``



### `if(missingedge == 1)`

**Returns:** `else`



### `if(missingedge == 2)`

**Returns:** `else`



### `if(coff > 0)`

**Returns:** ``



### `if(r == 0)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `for(int i=0; i<=div; i++)`

**Returns:** ``



### `Rotate(border, rotation, {w/2.f, h/2.f})`

**Returns:** ``



### `if(size.Width - Border.Shape*4.6f < 3)`

**Returns:** ``



### `if(border)`

**Returns:** ``



### `makestate(Graphics::Color::Regular, UI::ComponentCondition::Always)`

**Returns:** ``



### `makestate(Graphics::Color::Hover, UI::ComponentCondition::Hover)`

**Returns:** ``



### `makestate(Graphics::Color::Down, UI::ComponentCondition::Down)`

**Returns:** ``



### `makestate(Graphics::Color::Disabled, UI::ComponentCondition::Disabled)`

**Returns:** ``



### `if(tabbutton == AssetID::None)`

**Returns:** ``



### `if(tabbutton == AssetID::None)`

**Returns:** ``



### `checkboxbutton(AssetID::None)`

**Returns:** `return`



### `makestate(Graphics::Color::Regular, UI::ComponentCondition::Always)`

**Returns:** ``



### `makestate(Graphics::Color::Hover, UI::ComponentCondition::Hover)`

**Returns:** ``



### `makestate(Graphics::Color::Down, UI::ComponentCondition::Down)`

**Returns:** ``



### `makestate(Graphics::Color::Disabled, UI::ComponentCondition::Disabled)`

**Returns:** ``



### `padding(spacing)`

**Returns:** `Geometry::Margin`



### `if(scrollers)`

**Returns:** ``



### `makepanel(AssetID::AllExceptTop, false)`

**Returns:** `return`



### `makepanel(AssetID::AllExceptLeft, true)`

**Returns:** `return`



### `makepanel(AssetID::AllExceptRight, true)`

**Returns:** `return`



### `makepanel(AssetID::AllExceptBottom, false)`

**Returns:** `return`



### `switch(icon)`

**Returns:** ``



### `makebutton(Graphics::Color::Regular, 0, UI::ComponentCondition::Always)`

**Returns:** ``



### `makebutton(Graphics::Color::Regular, 1, UI::ComponentCondition::Reversed)`

**Returns:** ``



### `makebutton(Graphics::Color::Regular, 2, UI::ComponentCondition::Opened)`

**Returns:** ``



### `for(auto &c : temp)`

**Returns:** ``



### `for(auto &c : temp)`

**Returns:** ``



### `if(rootp)`

**Returns:** ``



### `SetColor(Graphics::Color::Designation designation, Graphics::Color::Triplet<> color)`

**Returns:** `void`


Creates a non-working simple generator. Calls to any function other than Init is undefined behaviour. Updates a single color. All setup should be performed before any templates are generated


### `SetColors(Graphics::Color::TripletPack pack)`

**Returns:** `void`


Replaces the list of colors with the given list. All setup should be performed before any templates are generated


### `InitFonts(int size, std::string family = "", std::string mono = "")`

**Returns:** `void`


Finds the requested typeface from the installed fonts. You may query installed fonts using OS::GetFontFamilies. Leaving family empty will trigger internal mechanism to find an ideal font for the task. On Linux, the font is requested from FontConfig, on Windows, we have a list of fonts that will be tried in order.


### `InitFonts(family, mono, density)`

**Returns:** ``


Loads the specified fonts, while using supplied or default family for monospaced fonts. Loads the specified fonts. Finds the requested typeface from the installed fonts. You may query installed fonts using OS::GetFontFamilies. Leaving family empty will trigger internal mechanism to find an ideal font for UI. On Linux, the font is requested from FontConfig, on Windows, we have a list of fonts that will be tried in order. Font size will be calculated from the monitor size and density Loads the specified fonts, while using supplied or default family for monospaced fonts. Loads the specified fonts. Initializes the dimensions that will be used by the generator. Call after font setup is completed. Density controls how dense the widgets will be packed together, effecting their spacing. bordersize controls the border of individual widgets. If -1 is supplied for border, line thickness from the regular font will be used. Fully initializes the generator with default colors


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(size, family, mono)`

**Returns:** ``


Fully initializes the generator with default colors


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(family, mono, density)`

**Returns:** ``


Fully initializes the generator


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(size, family, mono)`

**Returns:** ``


Fully initializes the generator


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(regular, bold, italic, bolditalic, mono, density)`

**Returns:** ``


Fully initializes the generator


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(size, regular, bold, italic, bolditalic, mono)`

**Returns:** ``


Fully initializes the generator


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(regular, bold, italic, bolditalic, mono, monobold, monoitalic, monobolditalic, density)`

**Returns:** ``


Fully initializes the generator


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `InitFonts(size, regular, bold, italic, bolditalic, mono, monobold, monoitalic, monobolditalic)`

**Returns:** ``


Fully initializes the generator


### `InitDimensions(density, bordersize, corners)`

**Returns:** ``



### `Button(bool border)`

**Returns:** `UI::Template`



### `makeborder(Graphics::RGBA border, Graphics::RGBA bg, SimpleGenerator::AssetID::BorderSide borders, int w = -1, int r = -1)`

**Returns:** `Graphics::RectangularAnimationProvider*`


Returns the foreground color for the requested designation. Returns the background for the requested designation. Returns an printer instance that will render the requested text style Returns an advanced printer instance that will be able to render any text style


### `makepanel(SimpleGenerator::AssetID::BorderSide edge, bool scrollers, bool spacing = true, bool nobg = false)`

**Returns:** `UI::Template`



### `checkboxbutton(AssetID::BorderSide tabbutton)`

**Returns:** `UI::Template`



### `initfontrelated()`

**Returns:** `void`


This is the height of a bordered widget This is the height of a non-bordered widget


### `expandedradius(float pixels)`

**Returns:** `float`



### `maketemplate()`

**Returns:** `UI::Template`



### `setupfocus(UI::GraphicsTemplate &focus)`

**Returns:** `void`


