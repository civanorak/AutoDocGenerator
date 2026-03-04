# URI

> Auto-generated documentation for the **URI** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `URIError`

**Namespace:** `Gorgon`

This error is thrown while URI decoding and building.


### `URI`

**Namespace:** `Gorgon`

Represents an unfolded URI. Can be used to parse a URI string or build one according to RFC 3986. @code #include <Gorgon/Network/HTTP.h> ... std::cout<<Gorgon::Network::HTTP::BlockingGetText(URI("http", "darkgaze.org", "path/to/data.php"))<<std::endl; @endcode

#### Methods

##### `URI(const std::string &scheme, const std::string &host, const std::string &path, const std::string &query = "", const std::string &fragment="")`

**Returns:** ``

Empty constructor. Does not set scheme thus would not be a valid URI Creates a new URI by filling in fields

##### `URI(const std::string &scheme, const std::string &host, int port, const std::string &path, const std::string &query = "", const std::string &fragment="")`

**Returns:** ``

Creates a new URI by filling in fields

##### `URI(const std::string &str, bool inpagelink = false)`

**Returns:** ``

Builds a new URI from the given string. May throw URIError. This constructor will not check if the URI is really valid. Use IsValid function for this purpose. If this URI is embedded inside another URI and possibly a relative link, set inpagelink to true. Otherwise, URIs without scheme will be treated having a host. For instance when inpagelink is false, in URI darkgaze.org/my/path darkgaze.org would be treated as host name.

##### `Convert(—)`

**Returns:** `std::string`

Builds a new URI from the given string. May throw URIError. This constructor will not check if the URI is really valid. Use IsValid function for this purpose. Converts this URI to a properly encoded string Converts this URI to a properly encoded string

##### `IsValid(—)`

**Returns:** `bool`

Returns if this URI is valid. This function checks if scheme is valid in format. Additionally, if the scheme is http, https and ftp, checks if the host is set.

##### `bool(—)`

**Returns:** `operator`

Returns if this URI is valid.

##### `IsValid(—)`

**Returns:** `return`

##### `Combine(const std::string &link)`

**Returns:** `void`

Compares two URIs in their simplest forms. Note that URIs with different fragments point to different places in the same resource and will not be used in comparison. This is also recommended by RFC 3986 Compares two URIs in their simplest forms. Note that URIs with different fragments point to different places in the same resource and will not be used in comparison. This is also recommended by RFC 3986 Combines a relative URI into this URI. Can be used to normalize links in a document. Care should be taken while using URIPath with this function as URIPath cannot represent relative paths.


### `HTTPQuery`

**Namespace:** `Gorgon`

Scheme of the URI, ex: http. Scheme cannot be encoded, thus should only start with an alpha character and should only contain Alphanumeric characters as well as +, - and . Host address, either IP/domain name or empty, ex: darkgaze.org User information. Use : to separate password. Use of password is no longer recommended by RFC unless it is empty. The port number, 0 means it is not defined. Path of the resource. Segments must be separated by /. You may use URIPath to construct a path Query for the resource, must be properly escaped and encoded, you may use HTTPQuery to build http query string. Fragment of the resource (anchor in HTML) Represents and HTTP query that might be send to page using POST or embedded in URI

#### Methods

##### `HTTPQuery(std::initializer_list<std::pair<const std::string, std::string>> init)`

**Returns:** ``

Empty constructor Creates a new HTTP query using the given pairs

##### `HTTPQuery(const std::string &query)`

**Returns:** ``

Parses the given query

##### `Convert(—)`

**Returns:** `std::string`

Converts this query system to string Converts this query system to string

##### `Get(const std::string &key)`

**Returns:** `std::string`

Returns the value that is stored within key. If key does not exist, an empty string will be returned.

##### `Exists(const std::string &key)`

**Returns:** `bool`

Returns the value that is stored within key. If key does not exist, an empty value with the given key is created. Returns if the given key exists


### `URIPath`

**Namespace:** `Gorgon`

Key-value pairs for this HTTP query Helps to manage URIPaths. Note that the URI paths are always absolute. Allows normalization as well as remapping, which would be useful to convert URI paths to file system paths.

#### Methods

##### `URIPath(std::initializer_list<std::string> init)`

**Returns:** ``

Empty constructor Initializes the path by the given segments

##### `URIPath(const std::string &path)`

**Returns:** ``

Parses the given path.

##### `GetSize(—)`

**Returns:** `int`

Parses the given path. Converts the path to string properly escaping for URI Compares two paths after normalization Compares two paths after normalization

##### `Get(int ind)`

**Returns:** `std::string`

Returns the segment at the given index Returns the segment at the given index. Index 0 will never cause an error, if does not exists, it will be empty string.

##### `StripFirst(—)`

**Returns:** `std::string`

Returns the first segment and removes it from the list of segments. This function will never fire error. If there are no segments it will return empty string

##### `Convert(—)`

**Returns:** `std::string`

Returns the segment at the given index Converts the path to string properly escaping for URI

##### `Combine(const URIPath &another)`

**Returns:** `void`

Combines another URIPath using this one as the root

##### `Combine(another)`

**Returns:** ``

Combines this path with another, using this path as the root Combines another URIPath into this one, using this path as the root

##### `Normalize(—)`

**Returns:** `void`

Normalizes any relative references in the path. May throw URIError


---

## Functions

### `appendtoset(std::set<char> base, std::initializer_list<char> chars)`

**Returns:** `static std::set<char>`



### `appendtoset(std::set<char> base, std::set<char> second)`

**Returns:** `static std::set<char>`



### `URIDecode(const std::string &src)`

**Returns:** `std::string`



### `for(auto c : src)`

**Returns:** ``



### `if(pcte)`

**Returns:** ``



### `if(digit==-1)`

**Returns:** ``



### `if(--pcte==0)`

**Returns:** ``



### `if(pcte)`

**Returns:** ``



### `URIError("Unterminated escape sequence in URI")`

**Returns:** `throw`



### `PCTEncode(const std::string &src, const std::set<char> &allowed, bool allowalpha, bool allownum)`

**Returns:** `std::string`



### `for(auto c : src)`

**Returns:** ``



### `URIEncode(const std::string &src)`

**Returns:** `std::string`



### `PCTEncode(src, unreservedchars)`

**Returns:** `return`



### `if(hasscheme)`

**Returns:** ``



### `if(*it==':')`

**Returns:** ``



### `if(*it=='/')`

**Returns:** ``



### `if(*it=='/' || noslash)`

**Returns:** ``



### `if(first && c=='[')`

**Returns:** ``



### `if(doingipv6)`

**Returns:** `else`



### `if(c==']')`

**Returns:** ``



### `if(c==':')`

**Returns:** ``



### `if(c=='/' || c=='?' || c=='#')`

**Returns:** `else`



### `URIError("Scrap after IPv6.")`

**Returns:** `throw`



### `if(unknownipformat)`

**Returns:** ``



### `URIError("IPv6 format error")`

**Returns:** `throw`



### `if(c=='/' || c=='?' || c=='#')`

**Returns:** `else`



### `if(mustbeuserinfo)`

**Returns:** ``



### `URIError("Port number should be numeric")`

**Returns:** `throw`



### `if(doingport)`

**Returns:** ``



### `if(doingport)`

**Returns:** `else`



### `URIError("Port number should be numeric")`

**Returns:** `throw`



### `if(c == '@')`

**Returns:** `else`



### `URIError("Multiple userinfo in authority")`

**Returns:** `throw`



### `if(c==':' && !mustbeuserinfo)`

**Returns:** `else`



### `if(doingipv6 && !finishedipv6)`

**Returns:** ``



### `URIError("IPv6 is not finished with ]")`

**Returns:** `throw`



### `if(temp!="")`

**Returns:** ``



### `if(doingport)`

**Returns:** ``



### `if(c=='#' || c=='?')`

**Returns:** ``



### `if(*it=='?')`

**Returns:** ``



### `if(host!="" || userinfo!="")`

**Returns:** ``



### `if(path!="")`

**Returns:** ``



### `if(uriform.scheme!="")`

**Returns:** ``



### `if(uriform.host!="")`

**Returns:** `else`



### `if(uriform.path=="")`

**Returns:** ``



### `if(uriform.path[0]=='/')`

**Returns:** ``



### `if(relative)`

**Returns:** ``



### `if(scheme=="http")`

**Returns:** ``



### `if(scheme=="https")`

**Returns:** `else`



### `if(scheme=="ftp")`

**Returns:** `else`



### `if(scheme=="sftp" || scheme=="ssh")`

**Returns:** `else`



### `if(scheme=="ssh")`

**Returns:** `else`



### `for(auto p : data)`

**Returns:** ``



### `for(auto c : query)`

**Returns:** ``



### `if(c=='&' || c==';')`

**Returns:** ``



### `if(!invalue)`

**Returns:** ``



### `if(!invalue && c=='=')`

**Returns:** `else`



### `if(temp!="" || key!="")`

**Returns:** ``



### `if(!invalue)`

**Returns:** ``



### `for(auto c : path)`

**Returns:** ``



### `if(c=='/')`

**Returns:** ``



### `for(unsigned i = 0; i<segments.size()`

**Returns:** ``



### `if(seg==".")`

**Returns:** ``



### `if(seg=="..")`

**Returns:** `else`



### `if(i==0)`

**Returns:** ``



### `URIError("Parent directory directive at the top segment.")`

**Returns:** `throw`



### `for(auto seg : segments)`

**Returns:** ``



### `for(auto p : query.data)`

**Returns:** ``



### `URIDecode(const std::string &str)`

**Returns:** `std::string`


List of segments Decodes a given URI string according to RFC 3986. May throw URIError.


### `URIEncode(const std::string &str)`

**Returns:** `std::string`


Encodes a given URI string according to RFC 3986.


### `PCTEncode(const std::string &str, const std::set<char> &allowed, bool allowalpha=true, bool allownum=true)`

**Returns:** `std::string`


Customized percentage encoding. Some URI components have different characters that are allowed

