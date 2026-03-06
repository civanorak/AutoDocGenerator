# Enum

&gt; Auto-generated documentation for the **Enum** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `gorgon__no_enum_trait`

@cond INTERNAL


### `expandedenumtraits`

**Namespace:** `Gorgon`

Expands user declared enumtraits for additional capabilities

#### Methods

##### `expandedenumtraits(—)`

**Returns:** ``

##### `for(auto p : traits.mapping)`

**Returns:** ``

##### `if(p.first!=prev)`

**Returns:** ``

##### `lookupstring(T_ e, std::string &s)`

**Returns:** `bool`

##### `lookupvalue(std::string s, T_ &e)`

**Returns:** `bool`

##### `begin(—)`

**Returns:** ``

##### `end(—)`

**Returns:** ``

##### `getmin(—)`

**Returns:** `T_`

##### `getmax(—)`

**Returns:** `T_`


### `staticenumtraits`

**Namespace:** `Gorgon`

This class performs instanced member to static conversion

#### Methods

##### `static` `lookupstring(T_ e, std::string &s)`

**Returns:** `static bool`

##### `static` `lookupvalue(const std::string &s, T_ &e)`

**Returns:** `static bool`

##### `static` `begin(—)`

**Returns:** `static typename std::vector<T_>::const_iterator`

##### `static` `end(—)`

**Returns:** `static typename std::vector<T_>::const_iterator`


### `enum_type_id`

**Namespace:** `Gorgon`

#### Methods

##### `end(enum_type_id<T_>)`

**Returns:** `typename std::vector<T_>::const_iterator`

##### `To(const std::string &text)`

**Returns:** ``

##### `From(const T_ &e)`

**Returns:** ``

##### `Parse(const std::string &text)`

**Returns:** ``

##### `ParseError(20001, s)`

**Returns:** `throw`


---

## Functions

### `gorgon__enum_tr_loc(const T_ &)`

**Returns:** `gorgon__no_enum_trait`



### `catch(const Gorgon::String::ParseError &ex)`

**Returns:** `*`


