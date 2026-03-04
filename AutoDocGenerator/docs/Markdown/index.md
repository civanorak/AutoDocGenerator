# Markdown

> Auto-generated documentation for the **Markdown** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `MarkdownLink`

**Namespace:** `Gorgon`


---

## Functions

### `readuntilornewline(Graphics::Glyph c, std::string::const_iterator &it, const std::string::const_iterator &end)`

**Returns:** `std::string`



### `for(; it != end; it++)`

**Returns:** ``



### `ParseMarkdown(const std::string &text, bool useinfofont)`

**Returns:** `std::pair<std::string, std::vector<MarkdownLink>>`



### `for(auto it = text.begin()`

**Returns:** ``



### `if(eatnext)`

**Returns:** ``



### `if(header)`

**Returns:** ``



### `if(linecount > 0 || pre)`

**Returns:** `else`



### `if(spacecount > 1)`

**Returns:** `else`



### `if(prev == '\\')`

**Returns:** `else`



### `if(emcnt > 0 && g != '*')`

**Returns:** ``



### `if(emcnt >= 2)`

**Returns:** ``



### `if(bold && prev != ' ')`

**Returns:** ``



### `if(!bold && g != ' ' && !disallow && !newline)`

**Returns:** `else`



### `if(emcnt >= 1)`

**Returns:** ``



### `if(italic && prev != ' ')`

**Returns:** ``



### `if(!italic && g != ' ' && !disallow && !newline)`

**Returns:** `else`



### `if(changed)`

**Returns:** ``



### `if(bold)`

**Returns:** ``



### `while(emcnt)`

**Returns:** ``



### `if(tildecnt > 0 && g != '~')`

**Returns:** ``



### `if(tildecnt >= 2)`

**Returns:** ``



### `if(strike && prev != ' ')`

**Returns:** ``



### `if(!strike && g != ' ' && !disallow && !newline)`

**Returns:** `else`



### `while(tildecnt)`

**Returns:** ``



### `if(spacecount > 4 && pre)`

**Returns:** `else`



### `if(spacecount == 4 && newpar && !pre)`

**Returns:** `else`



### `if(newline)`

**Returns:** ``



### `if(it != end)`

**Returns:** ``



### `if(!done)`

**Returns:** ``



### `if(!bullet)`

**Returns:** ``



### `if(tlevel != bullet)`

**Returns:** ``



### `switch(bullet)`

**Returns:** ``



### `if(bullet && newpar)`

**Returns:** ``



### `if(!pre && g == '#')`

**Returns:** ``



### `if(pre && spacecount < 4)`

**Returns:** `else`



### `if(!newpar && linecount > 0 && outchars != 0 && spaceadded == 0 && !pre)`

**Returns:** `else`



### `if(header && header != currentheader)`

**Returns:** ``



### `if(!pre && g == '[')`

**Returns:** ``



### `if(nit != end)`

**Returns:** ``



### `if(final == ']' && next == ':' && newpar)`

**Returns:** ``



### `if(it != end && *it == ' ')`

**Returns:** ``



### `if(next != ' ')`

**Returns:** ``



### `if(it == end || *it != ']')`

**Returns:** ``



### `renderlink(p1)`

**Returns:** ``



### `if(final == ']' && next == '(')`

**Returns:** `else`



### `renderlink(p1)`

**Returns:** ``



### `if(!pre && g == '<')`

**Returns:** ``



### `if(nit != end)`

**Returns:** ``



### `if(next != ' ')`

**Returns:** ``



### `if(loc != p1.npos)`

**Returns:** ``



### `renderlink(p1)`

**Returns:** ``



### `if(g == '`')`

**Returns:** ``



### `if(!pre)`

**Returns:** ``



### `if(preinline)`

**Returns:** `else`



### `if(!pre)`

**Returns:** ``



### `if(g == '*' && emcnt < 3)`

**Returns:** ``



### `if(g == '~' && tildecnt < 2)`

**Returns:** ``



### `ParseMarkdown(const std::string &markdown, bool useinfofont = false)`

**Returns:** `std::pair<std::string, std::vector<MarkdownLink>>`


