# Filler

> Auto-generated documentation for the **Filler** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `any`

**Namespace:** `Internal`

#### Methods

##### `T_(—)`

**Returns:** `operator`


### `Get`

**Namespace:** `Internal`

#### Methods

##### `ByName_getif(const T_& obj, const std::string& name)`

**Returns:** `void`

##### `ByName_expand(Gorgon::TMP::Sequence<S_...>, const T_& obj, const std::string& name)`

**Returns:** `void`

##### `ByName(const T_& obj, const std::string& name)`

**Returns:** `any`

##### `ByName_expand(typename Gorgon::TMP::Generate<T_::ReflectionType::MemberCount>::Type{}, obj, name)`

**Returns:** ``

##### `ByName(obj, name)`

**Returns:** `return`

##### `To(const T_& obj, const std::string& name)`

**Returns:** `R_`


---

## Functions

### `count(const pugi::xml_node_iterator& parent_node, std::string keyword)`

**Returns:** `inline size_t`



### `for(auto child : children)`

**Returns:** ``



### `SetByName_setif(T_ &obj, const std::string &name, const std::string &value)`

**Returns:** `void`



### `SetByName_expand(Gorgon::TMP::Sequence<S_...>, T_ &obj, const std::string &name, const std::string &value)`

**Returns:** `void`



### `SetByName(T_ &obj, const std::string &name, const std::string &value)`

**Returns:** `void`



### `for(int i = 0; i < n; i++)`

**Returns:** ``



### `Fill(std::array<Struct, N>& obj_list, pugi::xml_node_iterator& first_child, pugi::xml_node_iterator& last_node)`

**Returns:** `constexpr void`



### `constexpr(Index < N)`

**Returns:** `if`



### `if(first_child == last_node)`

**Returns:** ``



### `constexpr(has_set<Struct>)`

**Returns:** `if`



### `Fill(std::array<Struct*, N>& obj_list, pugi::xml_node_iterator& first_node, pugi::xml_node_iterator& last_node)`

**Returns:** `constexpr void`



### `for(int i{}; i < N; i++)`

**Returns:** ``



### `for(int i{}; i < N; i++)`

**Returns:** ``



### `Fill(std::vector<Structure>& obj_list, pugi::xml_node_iterator first_child, pugi::xml_node_iterator last_node)`

**Returns:** `void`



### `for(auto i {0}; i < obj_list.size()`

**Returns:** ``



### `if(first_child == last_node)`

**Returns:** ``



### `constexpr(has_set<Structure>)`

**Returns:** `if`



### `Fill(std::vector<Structure>& obj_list, pugi::xml_object_range<pugi::xml_named_node_iterator> nodes)`

**Returns:** `void`



### `for(auto node : nodes)`

**Returns:** ``



### `constexpr(has_set<Structure>)`

**Returns:** `if`


