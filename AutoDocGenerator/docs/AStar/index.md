# AStar

> Auto-generated documentation for the **AStar** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `GetHeuristic(Gorgon::Geometry::Point source_, Gorgon::Geometry::Point target_)`

**Returns:** `static Gorgon::Geometry::Point`



### `manhattan(Gorgon::Geometry::Point source_, Gorgon::Geometry::Point target_)`

**Returns:** `static uint`



### `euclidean(Gorgon::Geometry::Point source_, Gorgon::Geometry::Point target_)`

**Returns:** `static uint`



### `octagonal(Gorgon::Geometry::Point source_, Gorgon::Geometry::Point target_)`

**Returns:** `static uint`



### `DetectCollision(Gorgon::Geometry::Point coordinates_)`

**Returns:** `bool`



### `FindNodeOnList(NodeSet& nodes_, Gorgon::Geometry::Point coordinates_)`

**Returns:** `TileNode*`



### `for(auto node : nodes_)`

**Returns:** ``



### `if(node->coordinates == coordinates_)`

**Returns:** ``



### `ReleaseNodes(NodeSet& nodes_)`

**Returns:** `void`



### `for(auto it = nodes_.begin()`

**Returns:** ``



### `PathFinder()`

**Returns:** ``



### `SetDiagonalMovement(false)`

**Returns:** ``



### `SetHeuristic(&AStar::Heuristic::manhattan)`

**Returns:** ``



### `SetSize(Gorgon::Geometry::Size layer_size_)`

**Returns:** `void`



### `GetSize()`

**Returns:** `Geometry::Size`



### `SetDiagonalMovement(bool enable_)`

**Returns:** `void`



### `SetHeuristic(HeuristicFunction heuristic_)`

**Returns:** `void`



### `FindPath(Gorgon::Geometry::Point source_, Gorgon::Geometry::Point target_)`

**Returns:** `CoordinateList`



### `for(auto it = openSet.begin()`

**Returns:** ``



### `if(current->coordinates == target_)`

**Returns:** ``



### `for(uint i = 0; i < directions; ++i)`

**Returns:** ``



### `newCoordinates(current->coordinates + direction[i])`

**Returns:** `Gorgon::Geometry::Point`



### `if(successor == nullptr)`

**Returns:** ``



### `if(totalCost < successor->G)`

**Returns:** `else`



### `while(current != nullptr)`

**Returns:** ``



### `ReleaseNodes(openSet)`

**Returns:** ``



### `ReleaseNodes(closedSet)`

**Returns:** ``



### `AddBlock(Gorgon::Geometry::Point coordinates_)`

**Returns:** `void`



### `RemoveBlock(Gorgon::Geometry::Point coordinates_)`

**Returns:** `void`



### `ClearBlocks()`

**Returns:** `void`


