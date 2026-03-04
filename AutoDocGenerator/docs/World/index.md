# World

> Auto-generated documentation for the **World** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)

---

## Classes

### `Scene`

#### Methods

##### `OnUpdate(delta)`

**Returns:** ``

##### `OnRender(graphics)`

**Returns:** ``

##### `MouseMove(Geometry::Point location)`

**Returns:** `void`

##### `OnMouseMove(location)`

**Returns:** ``

##### `OnKeyEvent(k_, f_)`

**Returns:** ``

##### `InitFunctionBinds(—)`

**Returns:** `void`

##### `RemoveUI(—)`

**Returns:** `void`

##### `InitPathfinder(—)`

**Returns:** `void`

##### `Init(bool remove_ui, bool prepare, bool path_find)`

**Returns:** `void`

##### `RemoveUI(—)`

**Returns:** ``

##### `Prepare(—)`

**Returns:** ``

##### `if(path_find)`

**Returns:** ``

##### `InitPathfinder(—)`

**Returns:** ``

##### `InitFunctionBinds(—)`

**Returns:** ``

##### `InitZoomed(int factor, bool remove_ui, bool path_find)`

**Returns:** `void`

##### `RemoveUI(—)`

**Returns:** ``

##### `PrepareZoomed(factor)`

**Returns:** ``

##### `if(path_find)`

**Returns:** ``

##### `InitPathfinder(—)`

**Returns:** ``

##### `InitFunctionBinds(—)`

**Returns:** ``

##### `Init(false, true, true)`

**Returns:** ``

##### `Init(remove_ui, prepare, set_pathfinder)`

**Returns:** ``

##### `Init(remove_ui, true, true)`

**Returns:** ``

##### `InitZoomed(zoom_factor, remove_ui, true)`

**Returns:** ``

##### `InitZoomed(zoom_factor, false, true)`

**Returns:** ``

##### `ReinitPathfinder(—)`

**Returns:** `void`

##### `InitPathfinder(—)`

**Returns:** ``

##### `GetTargetSize(—)`

**Returns:** `Geometry::Size`

##### `Prepare(—)`

**Returns:** `void`

##### `PrepareZoomed(int factor)`

**Returns:** `void`

##### `GetUI(—)`

**Returns:** `Widgets::Panel&`

##### `SetBackgroundRender(bool status)`

**Returns:** `void`

##### `GetBackgroundRender(—)`

**Returns:** `bool`

##### `GetRenderer(—)`

**Returns:** `Rendering::base_tile_renderer<Map::Tiled::Map, class derived>&`

##### `GetPathFinder(—)`

**Returns:** `Pathfinding::base_pathfinder&`


### `World`

#### Methods

##### `for(auto  r : {renderers...})`

**Returns:** ``

##### `exit(0)`

**Returns:** ``

##### `for(auto  r : {renderers...})`

**Returns:** ``

##### `exit(0)`

**Returns:** ``

##### `NewScene(SceneID id, Renderer_&& class_, Args_&&... args)`

**Returns:** `void`

##### `Run(—)`

**Returns:** `void`


### `has_passability_layer`

#### Methods

##### `static` `test(...)`

**Returns:** `static NoType&`


### `Scene`

#### Methods

##### `OnUpdate(delta)`

**Returns:** ``

##### `OnRender(graphics)`

**Returns:** ``

##### `MouseMove(Geometry::Point location)`

**Returns:** `void`

##### `OnMouseMove(location)`

**Returns:** ``

##### `OnKeyEvent(k_, f_)`

**Returns:** ``

##### `InitFunctionBinds(—)`

**Returns:** `void`

##### `RemoveUI(—)`

**Returns:** `void`

##### `InitPathfinder(—)`

**Returns:** `void`

##### `ASSERT(false, "Your class needs to have an information on passability layer.")`

**Returns:** ``

##### `Init(bool remove_ui, bool prepare, bool path_find)`

**Returns:** `void`

##### `RemoveUI(—)`

**Returns:** ``

##### `Prepare(—)`

**Returns:** ``

##### `if(path_find)`

**Returns:** ``

##### `InitPathfinder(—)`

**Returns:** ``

##### `InitFunctionBinds(—)`

**Returns:** ``

##### `InitZoomed(int factor, bool remove_ui, bool path_find)`

**Returns:** `void`

##### `RemoveUI(—)`

**Returns:** ``

##### `PrepareZoomed(factor)`

**Returns:** ``

##### `if(path_find)`

**Returns:** ``

##### `InitPathfinder(—)`

**Returns:** ``

##### `InitFunctionBinds(—)`

**Returns:** ``

##### `Init(false, true, true)`

**Returns:** ``

##### `Init(remove_ui, prepare, set_pathfinder)`

**Returns:** ``

##### `Init(remove_ui, true, true)`

**Returns:** ``

##### `InitZoomed(zoom_factor, remove_ui, true)`

**Returns:** ``

##### `InitZoomed(zoom_factor, false, true)`

**Returns:** ``

##### `ReinitPathfinder(—)`

**Returns:** `void`

##### `InitPathfinder(—)`

**Returns:** ``

##### `GetTargetSize(—)`

**Returns:** `Geometry::Size`

##### `Prepare(—)`

**Returns:** `void`

##### `PrepareZoomed(int factor)`

**Returns:** `void`

##### `GetUI(—)`

**Returns:** `Widgets::Panel&`

##### `SetBackgroundRender(bool status)`

**Returns:** `void`

##### `GetBackgroundRender(—)`

**Returns:** `bool`

##### `GetRenderer(—)`

**Returns:** `renderer&`

##### `GetPathFinder(—)`

**Returns:** `generator&`


### `EmptyInitializer`


### `World`

#### Methods

##### `for(auto r : {renderer...})`

**Returns:** ``

##### `exit(0)`

**Returns:** ``

##### `for(auto r : {renderer...})`

**Returns:** ``

##### `exit(0)`

**Returns:** ``

##### `GetScene(const int& ID)`

**Returns:** `Scene<renderer_type>&`

##### `GetActiveScene(—)`

**Returns:** `Scene<renderer_type>&`

##### `ASSERT(active_scene != NoSceneID, "No active scene is set.")`

**Returns:** ``

##### `NewScene(SceneID id, Renderer_&& class_, Args_&&... args)`

**Returns:** `void`

##### `DeleteScene(SceneID id)`

**Returns:** `void`

##### `SwitchScene(SceneID id)`

**Returns:** `void`

##### `Run(—)`

**Returns:** `void`

