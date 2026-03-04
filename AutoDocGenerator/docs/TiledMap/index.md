# TiledMap

> Auto-generated documentation for the **TiledMap** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `GridTile`

#### Methods

##### `is_passable(—)`

**Returns:** `bool`


### `Object`

#### Methods

##### `DefineStructMembers(Object, id, gid, x, y, width, height)`

**Returns:** ``


### `ObjectGroup`

#### Methods

##### `Set(const pugi::xml_node_iterator& in)`

**Returns:** `void`

##### `DefineStructMembers(ObjectGroup, id, name)`

**Returns:** ``

##### `GetObject(size_t index)`

**Returns:** `Object`

##### `GetObjects(—)`

**Returns:** `std::vector<Object>`

##### `for(auto obj : obj_list)`

**Returns:** ``

##### `fp(obj)`

**Returns:** ``


### `TileSet`

#### Methods

##### `Set(const pugi::xml_node_iterator& in)`

**Returns:** `void`


### `Image`


### `Layer`

#### Methods

##### `Set(const pugi::xml_node_iterator& in)`

**Returns:** `void`

##### `DefineStructMembers(Layer, id, width, height, name)`

**Returns:** ``

##### `map_data_2d_string(—)`

**Returns:** `std::vector<std::vector<std::string>>`

##### `for(std::string line; getline(ss, line)`

**Returns:** ``

##### `for(std::string gid; getline(cs, gid, ', ')`

**Returns:** ``

##### `map_data_2d(—)`

**Returns:** `std::vector<std::vector<int>>`

##### `for(std::string line; getline(ss, line)`

**Returns:** ``

##### `for(std::string gid; getline(cs, gid, ', ')`

**Returns:** ``

##### `map_data(—)`

**Returns:** `std::vector<int>`

##### `for(std::string line; getline(ss, line)`

**Returns:** ``

##### `for(std::string gid; getline(cs, gid, ', ')`

**Returns:** ``

##### `data_to_grid(—)`

**Returns:** `std::vector<GridTile>`

##### `for(int y{}; y < height; y++)`

**Returns:** ``

##### `for(int x{}; x < width; x++)`

**Returns:** ``

##### `Size(—)`

**Returns:** `Geometry::Size`

##### `is_passability_layer(—)`

**Returns:** `bool`


### `Map`

#### Methods

##### `DefineStructMembers(Map, width, height, tilewidth, tileheight)`

**Returns:** ``

##### `Fill(TileSets, first_node, last_node)`

**Returns:** ``

##### `Fill(Layers, first_node, last_node)`

**Returns:** ``

##### `Fill(ObjectGroups, first_node, last_node)`

**Returns:** ``

##### `Fill(TileSets, first_node, last_node)`

**Returns:** ``

##### `Fill(Layers, first_node, last_node)`

**Returns:** ``

##### `Map(const std::string& file_name)`

**Returns:** ``

##### `Fill(TileSets, TileSetNodes)`

**Returns:** ``

##### `Fill(Layers, LayerNodes)`

**Returns:** ``

##### `Fill(ObjectGroups, OgNodes)`

**Returns:** ``

##### `Map(—)`

**Returns:** ``

##### `GetTileSet(—)`

**Returns:** `template<size_t Index> const struct TileSet&`

##### `GetTileSet(—)`

**Returns:** `template<size_t Index> const struct TileSet`

##### `GetTileSet(size_t Index)`

**Returns:** `struct TileSet&`

##### `GetTileSet(size_t Index)`

**Returns:** `struct TileSet`

##### `GetTileSets(—)`

**Returns:** `std::vector<TileSet>&`

##### `GetTileSets(—)`

**Returns:** `std::vector<TileSet>`

##### `GetLayer(—)`

**Returns:** `template<size_t Index> const struct Layer&`

##### `GetLayer(—)`

**Returns:** `template<size_t Index> const struct Layer`

##### `GetLayer(int Index)`

**Returns:** `struct Layer&`

##### `GetLayer(int Index)`

**Returns:** `struct Layer`

##### `GetLayers(—)`

**Returns:** `std::vector<Layer>&`

##### `GetLayers(—)`

**Returns:** `std::vector<Layer>`

##### `GetObjectGroup(size_t index)`

**Returns:** `ObjectGroup&`

##### `GetObjectGroup(size_t index)`

**Returns:** `ObjectGroup`

##### `GetObjectGroupMap(—)`

**Returns:** `std::unordered_map<int, ObjectGroup>`

##### `for(auto group : ObjectGroups)`

**Returns:** ``

##### `GetObjectGroups(—)`

**Returns:** `std::vector<ObjectGroup>&`

##### `GetObjectGroups(—)`

**Returns:** `std::vector<ObjectGroup>`

##### `ObjectLayerOrder(—)`

**Returns:** `std::unordered_map<int, int>`

##### `for(auto group : ObjectGroups)`

**Returns:** ``

##### `GetPassabilityLayer(—)`

**Returns:** `Layer&`


---

## Functions

### `TileSet()`

**Returns:** ``



### `DefineStructMembers(TileSet, firstgid, tilewidth, tileheight, tilecount, columns, name)`

**Returns:** ``


