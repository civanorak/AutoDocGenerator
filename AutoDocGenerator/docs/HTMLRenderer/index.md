# HTMLRenderer

&gt; Auto-generated documentation for the **HTMLRenderer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `FontFamily`

**Namespace:** `HTMLRendererInternal`


### `HashType`

**Namespace:** `HTMLRendererInternal`


### `HTMLRenderer`

**Namespace:** `HTMLRendererInternal`

#### Methods

##### `if(!initialized)`

**Returns:** ``

##### `initialize(—)`

**Returns:** ``

##### `Print(TextureTarget &target, const std::string &text, int x, int y)`

**Returns:** `void`

##### `parseandprint(target, text, x, y)`

**Returns:** ``


### `HashType`

**Namespace:** `HTMLRendererInternal`


---

## Functions

### `for(std::size_t i = 0; i < str.length()`

**Returns:** ``



### `if(current == '<')`

**Returns:** ``



### `HR_LOG_NOTICE("printing text: \"" + text + "\"")`

**Returns:** ``



### `print(target, text, xx, yy)`

**Returns:** ``



### `if(current == '>')`

**Returns:** `else`



### `HR_LOG_NOTICE("about to apply empty tag")`

**Returns:** ``



### `applytag(tagenum)`

**Returns:** ``



### `if(remove)`

**Returns:** `else`



### `removetag(tagenum)`

**Returns:** ``



### `clearattributes(tagenum)`

**Returns:** ``



### `HR_LOG_NOTICE("extracting accumulated attribute string before style application")`

**Returns:** ``



### `applytag(tagenum)`

**Returns:** ``



### `applyattributes(tagenum, attributes)`

**Returns:** ``



### `if(current == '/')`

**Returns:** `else`



### `if(current == '\"' || current == '\'')`

**Returns:** `else`



### `if(inquote)`

**Returns:** ``



### `if(intag)`

**Returns:** ``



### `if(parseattrbts)`

**Returns:** ``



### `if(current == '=')`

**Returns:** ``



### `if(inquote)`

**Returns:** ``



### `HR_LOG_NOTICE("about to print text")`

**Returns:** ``



### `print(target, text, xx, yy)`

**Returns:** ``



### `GetGlyphRenderer(Style style)`

**Returns:** `GlyphRenderer*`



### `HR_LOG_NOTICE("font style is found")`

**Returns:** ``



### `HR_LOG_NOTICE("could not find font style, will use the next available font")`

**Returns:** ``



### `for(unsigned int i = start; i < end; i++)`

**Returns:** ``



### `HR_LOG_ERROR("couldn't find any font, about to crash!!!")`

**Returns:** ``



### `ASSERT(false, "empty font family map")`

**Returns:** ``



### `AddFont(Style style, GlyphRenderer *renderer)`

**Returns:** `void`



### `RemoveFont(Style style)`

**Returns:** `void`



### `HasFont(Style style)`

**Returns:** `bool`



### `initialize()`

**Returns:** `static void`



### `string2tag(const std::string &tag)`

**Returns:** `static Tag`



### `if(tag == "u")`

**Returns:** ``



### `if(tag == "strike")`

**Returns:** `else`



### `if(tag == "b")`

**Returns:** `else`



### `if(tag == "strong")`

**Returns:** `else`



### `if(tag == "i")`

**Returns:** `else`



### `if(tag == "em")`

**Returns:** `else`



### `if(tag == "h1")`

**Returns:** `else`



### `if(tag == "br")`

**Returns:** `else`



### `string2attribute(const std::string &attribute)`

**Returns:** `static Attribute`



### `if(attribute == "color")`

**Returns:** ``



### `extractcolor(const std::string color)`

**Returns:** `static RGBAf`



### `if(color == "white")`

**Returns:** ``



### `if(color == "black")`

**Returns:** `else`



### `if(color == "green")`

**Returns:** `else`



### `HR_LOG_NOTICE("could not extract given color, using white")`

**Returns:** ``



### `RGBAf(1.f)`

**Returns:** `return`



### `parseandprint(TextureTarget &target, const std::string &str, int x, int y)`

**Returns:** `void`



### `applytag(Tag tag)`

**Returns:** `void`



### `switch(tag)`

**Returns:** ``



### `changeglyphrenderer(FontFamily::Style::Bold)`

**Returns:** ``



### `changeglyphrenderer(FontFamily::Style::Italic)`

**Returns:** ``



### `changeglyphrenderer(FontFamily::Style::Large)`

**Returns:** ``



### `if(drawunderlined)`

**Returns:** ``



### `if(drawstriked)`

**Returns:** ``



### `removetag(Tag tag)`

**Returns:** `void`



### `switch(tag)`

**Returns:** ``



### `drawline(LineType::Underline)`

**Returns:** ``



### `drawline(LineType::Strike)`

**Returns:** ``



### `changeglyphrenderer(FontFamily::Style::Normal)`

**Returns:** ``



### `applyattributes(Tag tag, const std::vector<std::pair<std::string, std::string>> &attributes)`

**Returns:** `void`



### `for(const auto &attstr: attributes)`

**Returns:** ``



### `switch(mappedval)`

**Returns:** ``



### `HR_LOG_NOTICE("changing underline color")`

**Returns:** ``



### `HR_LOG_NOTICE("changing strike color")`

**Returns:** ``



### `ASSERT(false, "unsupported attribute: " + attstr.first)`

**Returns:** ``



### `clearattributes(Tag tag)`

**Returns:** `void`



### `switch(tag)`

**Returns:** ``



### `HR_LOG_NOTICE("clearing underline attributes")`

**Returns:** ``



### `HR_LOG_NOTICE("clearing strike attributes")`

**Returns:** ``



### `drawline(LineType linetype)`

**Returns:** `void`



### `ASSERT(target, "texture target is null")`

**Returns:** ``



### `if(linetype == LineType::Underline)`

**Returns:** ``



### `HR_LOG_NOTICE("drawing underline")`

**Returns:** ``



### `if(linetype == LineType::Strike)`

**Returns:** `else`



### `HR_LOG_NOTICE("drawing strike")`

**Returns:** ``



### `ASSERT(false, "invalid line type")`

**Returns:** ``



### `changeglyphrenderer(FontFamily::Style newstyle)`

**Returns:** `void`



### `print(TextureTarget &target, const std::string &text, int x, int y)`

**Returns:** `void`


