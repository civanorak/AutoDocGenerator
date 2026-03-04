# Renderer

> Auto-generated documentation for the **Renderer** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `has_bounds`

#### Methods

##### `static` `test(...)`

**Returns:** `static NoType&`


### `has_bounds_on`

#### Methods

##### `static` `test(...)`

**Returns:** `static NoType&`


### `has_pass_layer`

#### Methods

##### `static` `test(...)`

**Returns:** `static NoType&`


### `has_zoomed_prepare`

#### Methods

##### `static` `test(...)`

**Returns:** `static NoType&`


### `has_zoomed_generate`

#### Methods

##### `static` `test(...)`

**Returns:** `static NoType&`


### `abstract_base_renderer`

#### Methods

##### `virtual` `Render(int, int)`

**Returns:** `virtual void`

##### `virtual` `Render(Geometry::Point)`

**Returns:** `virtual void`

##### `virtual` `BoundsOfTiles(Geometry::Point)`

**Returns:** `virtual void`

##### `virtual` `BoundsOfTiles(CGI::StrokeSettings, CGI::SolidFill<>, Geometry::Point)`

**Returns:** `virtual void`

##### `virtual` `BoundsOnPoint(Geometry::Point, Geometry::Point)`

**Returns:** `virtual Geometry::Point`

##### `virtual` `BoundsOnPoint(Geometry::Point, CGI::StrokeSettings, CGI::SolidFill<>, Geometry::Point)`

**Returns:** `virtual Geometry::Point`

##### `virtual` `GetImageByID(int)`

**Returns:** `virtual std::shared_ptr<Graphics::TextureImage>`

##### `virtual` `PassabilityLayer(—)`

**Returns:** `virtual void`

##### `virtual` `TileCoordinateOnPoint(Geometry::Point)`

**Returns:** `virtual Geometry::Point`

##### `virtual` `Prepare(—)`

**Returns:** `virtual void`

##### `virtual` `PrepareZoomed(int)`

**Returns:** `virtual void`

##### `virtual` `Unprepare(—)`

**Returns:** `virtual void`

##### `virtual` `SetActiveMap(int, bool)`

**Returns:** `virtual void`

##### `virtual` `SetLayer(Graphics::Layer&)`

**Returns:** `virtual void`


### `base_tile_renderer`

#### Methods

##### `Render(int offset_x = 0, int offset_y = 0)`

**Returns:** `void`

##### `ASSERT(target_layer != nullptr, "Layer is not set, you must set it first.")`

**Returns:** ``

##### `Render(Geometry::Point offset)`

**Returns:** `void`

##### `ASSERT(target_layer != nullptr, "Layer is not set, you must set it first.")`

**Returns:** ``

##### `BoundsOfTiles(Geometry::Point offset = {0, 0})`

**Returns:** `void`

##### `ASSERT(false, "This function does not exist!")`

**Returns:** ``

##### `BoundsOfTiles(CGI::StrokeSettings stroke, CGI::SolidFill<> color, Geometry::Point offset = {0, 0})`

**Returns:** `void`

##### `ASSERT(false, "This function does not exist!")`

**Returns:** ``

##### `BoundsOnPoint(Geometry::Point location, Geometry::Point offset = {0, 0})`

**Returns:** `Geometry::Point`

##### `ASSERT(false, "This function does not exist!")`

**Returns:** ``

##### `BoundsOnPoint(Geometry::Point location, CGI::StrokeSettings stroke, CGI::SolidFill<> color, Geometry::Point offset = {0, 0})`

**Returns:** `Geometry::Point`

##### `ASSERT(false, "This function does not exist!")`

**Returns:** ``

##### `GetImageByID(int id)`

**Returns:** `std::shared_ptr<Graphics::TextureImage>`

##### `PassabilityLayer(—)`

**Returns:** `void`

##### `ASSERT(false, "This function does not exist!")`

**Returns:** ``

##### `Prepare(—)`

**Returns:** `void`

##### `Unprepare(—)`

**Returns:** `void`

##### `PrepareZoomed(int factor)`

**Returns:** `void`

##### `ASSERT(false, "This function does not exist!")`

**Returns:** ``

##### `GetMap(—)`

**Returns:** `std::vector<map_type>`

##### `SetActiveMap(int ID, bool prepare = false)`

**Returns:** `void`

##### `Unprepare(—)`

**Returns:** ``

##### `if(prepare)`

**Returns:** ``

##### `SetActiveMap(map_type& map, bool prepare = false)`

**Returns:** `void`

##### `if(prepare)`

**Returns:** ``

##### `GetActiveMap(—)`

**Returns:** `map_type&`

##### `SetLayer(Graphics::Layer& layer)`

**Returns:** `void`

##### `for(int i{}; i < outer; i++)`

**Returns:** ``

##### `for(int j{}; j < inner; j++)`

**Returns:** ``

##### `Fp(i, j)`

**Returns:** ``


### `StandardTileRenderer`

#### Methods

##### `pass_layer_impl(—)`

**Returns:** `void`

##### `prepare_zoomed_resources(int factor)`

**Returns:** `void`

##### `for(const auto& tileset : tilesets)`

**Returns:** ``

##### `prepare_resources(—)`

**Returns:** `void`

##### `for(const auto& tileset : tilesets)`

**Returns:** ``

##### `generate_zoomed_drawables(int factor)`

**Returns:** `void`

##### `for(int i{}; i < Base::resources.size()`

**Returns:** ``

##### `for(auto j : item)`

**Returns:** ``

##### `generate_drawables(—)`

**Returns:** `void`

##### `for(int i{}; i < Base::resources.size()`

**Returns:** ``

##### `for(auto j: item)`

**Returns:** ``

##### `render_impl(int off_x = 0, int off_y = 0)`

**Returns:** `void`

##### `for(const auto& layer : layers)`

**Returns:** ``

##### `render_object(obj_it->second, off_x, off_y)`

**Returns:** ``

##### `render_object(int id, int off_x, int off_y)`

**Returns:** `void`

##### `for(auto [key, val] : group)`

**Returns:** ``

##### `if(val.previous_object_group_index == id)`

**Returns:** ``

##### `render_object(val.id, off_x, off_y)`

**Returns:** ``

##### `bound_impl(CGI::StrokeSettings stroke, CGI::SolidFill<> color, int offset_x, int offset_y)`

**Returns:** `void`

##### `if(first_time_all)`

**Returns:** ``

##### `bounds_on_impl(Geometry::Point location, CGI::StrokeSettings stroke, CGI::SolidFill<> color, int offset_x, int offset_y)`

**Returns:** `Geometry::Point`

##### `if(first_time)`

**Returns:** ``


### `IsometricTileRenderer`

#### Methods

##### `pass_layer_impl(—)`

**Returns:** `void`

##### `prepare_zoomed_resources(float factor)`

**Returns:** `void`

##### `for(const auto& tileset : tilesets)`

**Returns:** ``

##### `prepare_resources(—)`

**Returns:** `void`

##### `for(const auto& tileset : tilesets)`

**Returns:** ``

##### `generate_zoomed_drawables(float factor)`

**Returns:** `void`

##### `for(int i{}; i < Base::resources.size()`

**Returns:** ``

##### `for(auto j : item)`

**Returns:** ``

##### `generate_drawables(—)`

**Returns:** `void`

##### `for(int i{}; i < Base::resources.size()`

**Returns:** ``

##### `for(auto i : item)`

**Returns:** ``

##### `render_impl(int off_x = 0, int off_y = 0)`

**Returns:** `void`

##### `for(const auto& layer: layers)`

**Returns:** ``

##### `render_object(obj_it->second, off_x, off_y)`

**Returns:** ``

##### `render_object(int id, int off_x, int off_y)`

**Returns:** `void`

##### `for(auto [key, val] : group)`

**Returns:** ``

##### `if(val.previous_object_group_index == id)`

**Returns:** ``

##### `render_object(val.id, off_x, off_y)`

**Returns:** ``

##### `bound_impl(CGI::StrokeSettings stroke, CGI::SolidFill<> color, int offset_x, int offset_y)`

**Returns:** `void`

##### `if(first_time_all)`

**Returns:** ``

##### `bounds_on_impl(Geometry::Point location, CGI::StrokeSettings stroke, CGI::SolidFill<> color, int offset_x, int offset_y)`

**Returns:** `Geometry::Point`

##### `if(first_time)`

**Returns:** ``

##### `if(x < 0 or x > MW - 1 or y < 0 or y > MH - 1)`

**Returns:** ``

