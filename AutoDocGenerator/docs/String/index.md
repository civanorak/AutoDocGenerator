# String

&gt; Auto-generated documentation for the **String** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Enums](#enums)
- [Functions](#functions)

---

## Classes

### `CaseInsensitiveLess`

**Namespace:** `String`

#### Methods

##### `for(unsigned i=0; i<len; i++)`

**Returns:** ``

##### `if(lc<rc)`

**Returns:** ``

##### `if(lc>rc)`

**Returns:** `else`


### `two`

**Namespace:** `String`


### `CanBeStringified`

**Namespace:** `String`

@endcond


---

## Enums

### `LineEnding`

**Namespace:** `String`

Line ending types


### `QuoteType`

**Namespace:** `String`


---

## Functions

### `FixLineEndings(const std::string &in, LineEnding type)`

**Returns:** `std::string`



### `for(auto it = in.begin()`

**Returns:** ``



### `if(*it == '\x0d')`

**Returns:** ``



### `if(*it >= '\x0a' && *it <= '\x0c')`

**Returns:** `else`



### `CaseInsensitiveCompare(const std::string &left, const std::string &right)`

**Returns:** `inline int`


Compares two strings case insensitive. Works similar to strcmp


### `for(unsigned i=0; i<len; i++)`

**Returns:** ``



### `if(lc<rc)`

**Returns:** ``



### `if(lc>rc)`

**Returns:** `else`



### `To(const std::string &value)`

**Returns:** `T_`


Converts a string to another type. Works for integral types and Gorgon classes including Point, Size, etc... There is no error handling. If conversion does not work, you may end up with uninitialized object. This system will be fixed at a later point.


### `T_()`

**Returns:** `return`



### `To(const std::string &value)`

**Returns:** ``


@cond


### `T_(value)`

**Returns:** `return`



### `To(const std::string &value)`

**Returns:** ``



### `ss(value)`

**Returns:** `std::stringstream`



### `To(const char *value)`

**Returns:** ``



### `T_(value)`

**Returns:** `return`



### `To(const char *value)`

**Returns:** ``



### `T_(value)`

**Returns:** `return`



### `To(const char *value)`

**Returns:** ``



### `ss(value)`

**Returns:** `std::stringstream`



### `HexTo(const std::string &value)`

**Returns:** `T_`


Converts a hexadecimal number stored in the string to a given integer type. If given string is not a valid number this function throws


### `PadStart(std::string str, std::size_t len, char pad = ' ')`

**Returns:** `inline std::string`


@endcond Pads the string to the given number of characters from the start. This function is not utf aware.


### `PadEnd(std::string str, std::size_t len, char pad = ' ')`

**Returns:** `inline std::string`


Pads the string to the given number of characters from the start. This function is not utf aware.


### `Replace(std::string str, const std::string &find, const std::string &replace)`

**Returns:** `inline std::string`


String replace that does not use regex. Works faster than regex variant. This function is not utf aware. @param  str is the string to process @param  find is the substrings to be replaced @param  replace is the string to place instead of find. Can be empty string.


### `Trim(std::string str, const std::string &chars=" \t\n\r")`

**Returns:** `inline std::string`


Strips whitespace around the given string both from start and end. This function is not utf aware. @param  str is the string to process @param  chars is the characters to be considered as whitespace


### `TrimStart(std::string str, const std::string &chars=" \t\n\r")`

**Returns:** `inline std::string`


Strips the whitespace from the start of a string. This function is not utf aware. @param  str is the string to process @param  chars is the characters to be considered as whitespace


### `TrimEnd(std::string str, const std::string &chars=" \t\n\r")`

**Returns:** `inline std::string`


Strips the whitespace at the end of a string. This function is not utf aware. @param  str is the string to process @param  chars is the characters to be considered as whitespace


### `ToLower(std::string str)`

**Returns:** `inline std::string`


Converts the given string to lowercase. This function is not utf aware.


### `for(auto it=str.begin()`

**Returns:** ``



### `ToUpper(std::string str)`

**Returns:** `inline std::string`


Converts the given string to uppercase. This function is not utf aware.


### `for(auto it=str.begin()`

**Returns:** ``



### `From(const char &value)`

**Returns:** `inline std::string`


@cond


### `From(const unsigned char &value)`

**Returns:** `inline std::string`



### `From(const int &value)`

**Returns:** `inline std::string`



### `From(const unsigned &value)`

**Returns:** `inline std::string`



### `From(const long &value)`

**Returns:** `inline std::string`



### `From(const unsigned long &value)`

**Returns:** `inline std::string`



### `From(const long long &value)`

**Returns:** `inline std::string`



### `From(const unsigned long long &value)`

**Returns:** `inline std::string`



### `From(const float &value)`

**Returns:** `inline std::string`



### `if(value > 1e7)`

**Returns:** ``



### `From(const double &value)`

**Returns:** `inline std::string`



### `if(value > 1e14)`

**Returns:** ``



### `From(const long double &value)`

**Returns:** `inline std::string`



### `if(value > 1e28l)`

**Returns:** ``



### `From(const std::string &value)`

**Returns:** `inline std::string`



### `From(const T_ &item)`

**Returns:** ``



### `From(const T_ &item)`

**Returns:** ``



### `test(...)`

**Returns:** `static two`



### `streamthis(std::stringstream &stream)`

**Returns:** `inline void`



### `streamthis(std::stringstream &stream, const T_ &first, const P_&... rest)`

**Returns:** `void`



### `streamthis(stream, rest...)`

**Returns:** ``



### `Concat(const P_&... rest)`

**Returns:** `std::string`


Streams the given parameters into a stringstream and returns the result, effectively concatinating all parameters.


### `streamthis(ss, rest...)`

**Returns:** ``



### `UTF8Bytes(char c)`

**Returns:** `inline int`


Returns the number of bytes used by the next UTF8 codepoint


### `UnicodeUTF8Bytes(Char c)`

**Returns:** `inline int`



### `UnicodeGlyphCount(const std::string &s)`

**Returns:** `inline int`



### `AppendUnicode(std::string &s, Char c)`

**Returns:** `inline bool`


Appends a unicode code point to the string. If the given char is valid, this function will return true. Otherwise, it will place a three byte long replacement character and returns false.


### `if(c > 0x10FFFF)`

**Returns:** ``



### `while(cur < bytes-1)`

**Returns:** ``



### `if(bytes == 1)`

**Returns:** ``



### `if(bytes == 2)`

**Returns:** `else`



### `if(bytes == 3)`

**Returns:** `else`



### `if(bytes == 4)`

**Returns:** `else`



### `InsertUnicode(std::string &s, std::size_t pos, Char c)`

**Returns:** `inline bool`


Appends a unicode code point to the string. If the given char is valid, this function will return true. Otherwise, it will place a three byte long replacement character and returns false. pos is the byte offset to insert the character.


### `if(c > 0x10FFFF)`

**Returns:** ``



### `while(cur < bytes-1)`

**Returns:** ``



### `if(bytes == 1)`

**Returns:** ``



### `if(bytes == 2)`

**Returns:** `else`



### `if(bytes == 3)`

**Returns:** `else`



### `if(bytes == 4)`

**Returns:** `else`



### `FixLineEndings(const std::string &in, LineEnding type = LineEnding::Standard)`

**Returns:** `std::string`


None, no line endings line feed \\x0a line feed \\x0a carriage return \\x0d carriage return \\x0d \\x0d\\x0a \\x0d\\x0a \\x0d\\x0a When there are multiple types of line endings present Fixes/changes line endings. If none is supplied, all line endings will be removed. If mixed is set, nothing will be done.


### `From(const T_ &item)`

**Returns:** `std::string`


Creates a string from the given data. Similar to to_string but allows conversion of a type if it can be casted or streamed to output. Also uses std::to_string where possible.


### `Join(const std::vector<T_> &vec, const std::string &glue = ", ")`

**Returns:** `std::string`


Joins a list of strings to a single string using the given glue text.


### `for(const auto &v : vec)`

**Returns:** ``



### `Join(const std::map<K_, V_> &map, const std::string &assignment = " = ", const std::string &glue = "\n")`

**Returns:** `std::string`



### `for(const auto &v : map)`

**Returns:** ``



### `Split(const std::string &str, const D_ &delimeter = '\n', bool nonempty = false)`

**Returns:** `std::vector<K_>`


Splits a string to a vector using either a single character or a list of characters as string. When nonempty is set to false, this function will only return entries that has some characters in.


### `while(true)`

**Returns:** ``



### `if(end > start || nonempty)`

**Returns:** ``



### `Map(const std::string &str, char assignment = '=', const D_ &delimeter = '\n', bool trimkey = true, bool lefttrimvalue = true, bool righttrimvalue = false, bool allowemptykey = false)`

**Returns:** `std::map<K_, V_>`


Splits a string to a map using one character for assignment and another (or a list of characters) for data endings. If a key occurs more than once, later one will be used.


### `while(start != std::string::npos)`

**Returns:** ``



### `if(end == std::string::npos)`

**Returns:** ``



### `if(end != std::string::npos && str[end] == assignment)`

**Returns:** ``



### `if(end == std::string::npos)`

**Returns:** ``



### `if(lefttrimvalue && righttrimvalue)`

**Returns:** ``



### `if(lefttrimvalue)`

**Returns:** `else`



### `if(righttrimvalue)`

**Returns:** `else`



### `if(allowemptykey || key != "")`

**Returns:** ``



### `Extract(std::string &original, const std::string &marker, bool trim = false)`

**Returns:** `inline std::string`


Extracts the part of the string up to the given marker. Extracted string and the marker is removed from the original string. If the given string does not contain marker, entire string will be extracted. It is possible to tokenize the given string using repeated calls to this function. However, its more convenient to use Tokenizer. @param  original string that will be processed. This string will be modified by the program @param  marker string that will be searched. @param  trim   if set, both extracted and the remaining part of the string @return Extracted string. Does not contain the marker.


### `if(pos==original.npos)`

**Returns:** ``



### `if(trim)`

**Returns:** ``



### `Extract(std::string &original, char marker, bool trim = false)`

**Returns:** `inline std::string`


Extracts the part of the string up to the given marker. Extracted string and the marker is removed from the original string. If the given string does not contain marker, entire string will be extracted. It is possible to tokenize the given string using repeated calls to this function. However, its more convenient to use Tokenizer. @param  original string that will be processed. This string will be modified by the program @param  marker character that will be searched. @param  trim   if set, both extracted and the remaining part of the string @return Extracted string. Does not contain the marker.


### `if(pos==original.npos)`

**Returns:** ``



### `if(trim)`

**Returns:** ``



### `Extract_UseQuotes(std::string &original, char marker, QuoteType quotetype=QuoteType::Both)`

**Returns:** `inline std::string`


Extracts the part of the string up to the given marker. This function will skipped quoted sections of the string. Both single and double quotes can be considered, however, double quotes should match with double quotes and single quotes should match with single quotes. A different quote type inside quote region is ignored. Extracted string and the marker is removed from the original string. If the given string does not contain marker outside the quotes, entire string will be extracted. It is possible to tokenize the given string using repeated calls to this function. Unbalanced quotes will be treated ending at the end of the string. @param  original string that will be processed. This string will be modified by the program @param  marker string that will be searched. It is possible to specify quote as a marker. @param  quotetype controls which type of quotes will be considered. @return Extracted string. Does not contain the marker. Quotes will not be removed


### `for(auto &c : original)`

**Returns:** ``



### `if(inquotes==1)`

**Returns:** ``



### `if(c=='\'')`

**Returns:** ``



### `if(inquotes==2)`

**Returns:** `else`



### `if(c=='"')`

**Returns:** ``



### `if(c==marker)`

**Returns:** `else`


