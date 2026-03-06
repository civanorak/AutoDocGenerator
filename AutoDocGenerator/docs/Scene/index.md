# Scene

&gt; Auto-generated documentation for the **Scene** module of the Gorgon C++ Game Engine.


## Contents

- [Classes](#classes)
- [Functions](#functions)

---

## Classes

### `None`

Used to denote there is no explicit scene id given to a scene.


### `Scene`

#### Methods

##### `Scene(SceneID id = NoSceneID, bool mouseinput = true)`

**Returns:** `explicit`

Empty constructor. After this constructor, the scene cannot be activated.

##### `Scene(SceneManager &parent, SceneID id = NoSceneID, bool mouseinput = true)`

**Returns:** `explicit`

Sets the parent layer so that the scene can be activated.

##### `virtual` `RequiresKeyInput(—)`

**Returns:** `virtual bool`

Whether this scene requires keyboard input.

##### `GetID(—)`

**Returns:** `SceneID`

Activates the current scene Returns the ID of the current scene

##### `virtual` `KeyEvent(Gorgon::Input::Key, float)`

**Returns:** `virtual void`

Called when the scene receives a key

##### `virtual` `first_activation(—)`

**Returns:** `virtual void`

Fires whenever activation of this layer is completed. Will not be fired if the layer is already active and Activate function is called. Fires whenever deactivation of this layer is completed. Will not be fired if the layer is already inactive and Deactivate function is called. Called only for the first time this scene is activated. Allocate your resources here.

##### `virtual` `activate(—)`

**Returns:** `virtual void`

Called after very activation. first_activation will be called before activate.

##### `virtual` `deactivate(—)`

**Returns:** `virtual void`

Called *before* deactivation

##### `virtual` `doframe(unsigned int delta)`

**Returns:** `virtual void`

Scene should perform its frame based operations in this function

##### `virtual` `render(—)`

**Returns:** `virtual void`

This is called after doframe to perform rendering operation. It is possible to receive render without receiving doframe, thus they should not be co-dependent.

##### `setlayerbounds(const Geometry::Bounds &bounds)`

**Returns:** `void`

Changes the boundaries of the main layer

##### `activate_scene(—)`

**Returns:** `void`

ID of the current scene Graphics layer that can be drawn on Mouse layer that can be used to receive mouse events. If the mouseinput parameter of the constructor is set to true, this layer will be attached, otherwise it will not be functional. The parent window for the scene. Unless you are explicitly requesting a parent, this member could be nullptr. This panel covers the entire area of the window. You may place your widgets on top of this panel. They will be displayed above drawing layer

##### `deactivate_scene(—)`

**Returns:** `void`


### `SceneManager`

#### Methods

##### `SwitchScene(SceneID scene)`

**Returns:** `void`

Switches the current scene to the scene with the given id. Will throw std::runtime_error if scene is not found. If given id is NoSceneID, all scenes will be deactivated.

##### `Deactivate(—)`

**Returns:** `void`

Deactivates all scenes

##### `ActivateKeyboard(—)`

**Returns:** `void`

Moves keyboard input event to the top if there is a layer that accepts keyboard input.

##### `if(active)`

**Returns:** ``

Runs the application by running the active scene, progressing OS events and rendering mechanism. This function will run until Quit is called. Steps the application by running the active scene, progressing OS events and rendering mechanism.

##### `GetSceneCount(—)`

**Returns:** `int`

Returns the number of scenes registered

##### `SceneExists(SceneID id)`

**Returns:** `bool`

Returns if the given scene exists

##### `DeleteScene(SceneID scene)`

**Returns:** `void`

Returns the requested scene. If it does not exist, this function will throw runtime error. Deletes the given scene, nothing is done if the scene is not found

##### `Assume(Scene<> &scene)`

**Returns:** `void`

Releases the ownership of the scene with the given ID, removing it from the manager. Using scene while it does not have parent might cause problems. Assumes the ownership of the the given scene, adding it to the list of scenes.

##### `begin(—)`

**Returns:** `auto`

Returns iterator to the first scene.

##### `begin(—)`

**Returns:** `auto`

Returns iterator to the first scene.

##### `end(—)`

**Returns:** `auto`

Returns iterator to the end of scenes.

##### `end(—)`

**Returns:** `auto`

Returns iterator to the end of scenes.

##### `init(—)`

**Returns:** `EventToken`

Quits the scene manager, returning the execution to the point where Run function is called. It allows current frame to be completed before quiting. It also deactives the current scene. Creates a new scene using the given type and parameters. Scene class should always take parent layer first, then id and then the other parameters if they exists. When using this function, only specify the class as template parameter, the others will be resolved. If a scene with the same id exists, it will be deleted. It is advisable to add new scenes at the start without activating any scene.  @code enum SceneIDs { SCENE_MENU, SCENE_GAME };  //...  class GameScene : public Scene { public: GameScene(Gorgon::SceneManager &parent, SceneID id, int players);  //... };  //...  //Create the game scene with a single player. manager.NewScene&lt;GameScene&gt;(SCENE_GAME, 1);  manager.SwitchScene(SCENE_GAME);  @endcode This event will be fired whenever a scene is activated.


### `Scene`

**Namespace:** `Gorgon`

#### Methods

##### `Scene(SceneID id = NoSceneID, bool mouseinput = true)`

**Returns:** `explicit`

Empty constructor. After this constructor, the scene cannot be activated.

##### `Scene(SceneManager &parent, SceneID id = NoSceneID, bool mouseinput = true)`

**Returns:** `explicit`

Sets the parent layer so that the scene can be activated.

##### `virtual` `RequiresKeyInput(—)`

**Returns:** `virtual bool`

Whether this scene requires keyboard input.

##### `GetID(—)`

**Returns:** `SceneID`

Activates the current scene Returns the ID of the current scene

##### `virtual` `KeyEvent(Gorgon::Input::Key, float)`

**Returns:** `virtual void`

Called when the scene receives a key

##### `virtual` `first_activation(—)`

**Returns:** `virtual void`

Fires whenever activation of this layer is completed. Will not be fired if the layer is already active and Activate function is called. Fires whenever deactivation of this layer is completed. Will not be fired if the layer is already inactive and Deactivate function is called. Called only for the first time this scene is activated. Allocate your resources here.

##### `virtual` `activate(—)`

**Returns:** `virtual void`

Called after very activation. first_activation will be called before activate.

##### `virtual` `deactivate(—)`

**Returns:** `virtual void`

Called *before* deactivation

##### `virtual` `doframe(unsigned int delta)`

**Returns:** `virtual void`

Scene should perform its frame based operations in this function

##### `virtual` `render(—)`

**Returns:** `virtual void`

This is called after doframe to perform rendering operation. It is possible to receive render without receiving doframe, thus they should not be co-dependent.

##### `setlayerbounds(const Geometry::Bounds &bounds)`

**Returns:** `void`

Changes the boundaries of the main layer

##### `activate_scene(—)`

**Returns:** `void`

ID of the current scene Graphics layer that can be drawn on Mouse layer that can be used to receive mouse events. If the mouseinput parameter of the constructor is set to true, this layer will be attached, otherwise it will not be functional. The parent window for the scene. Unless you are explicitly requesting a parent, this member could be nullptr. This panel covers the entire area of the window. You may place your widgets on top of this panel. They will be displayed above drawing layer

##### `deactivate_scene(—)`

**Returns:** `void`


### `SceneManager`

**Namespace:** `Gorgon`

#### Methods

##### `SwitchScene(SceneID scene)`

**Returns:** `void`

Switches the current scene to the scene with the given id. Will throw std::runtime_error if scene is not found. If given id is NoSceneID, all scenes will be deactivated.

##### `Deactivate(—)`

**Returns:** `void`

Deactivates all scenes

##### `ActivateKeyboard(—)`

**Returns:** `void`

Moves keyboard input event to the top if there is a layer that accepts keyboard input.

##### `if(active)`

**Returns:** ``

Runs the application by running the active scene, progressing OS events and rendering mechanism. This function will run until Quit is called. Steps the application by running the active scene, progressing OS events and rendering mechanism.

##### `GetSceneCount(—)`

**Returns:** `int`

Returns the number of scenes registered

##### `SceneExists(SceneID id)`

**Returns:** `bool`

Returns if the given scene exists

##### `DeleteScene(SceneID scene)`

**Returns:** `void`

Returns the requested scene. If it does not exist, this function will throw runtime error. Deletes the given scene, nothing is done if the scene is not found

##### `Assume(Scene &scene)`

**Returns:** `void`

Releases the ownership of the scene with the given ID, removing it from the manager. Using scene while it does not have parent might cause problems. Assumes the ownership of the the given scene, adding it to the list of scenes.

##### `begin(—)`

**Returns:** `auto`

Returns iterator to the first scene.

##### `begin(—)`

**Returns:** `auto`

Returns iterator to the first scene.

##### `end(—)`

**Returns:** `auto`

Returns iterator to the end of scenes.

##### `end(—)`

**Returns:** `auto`

Returns iterator to the end of scenes.

##### `init(—)`

**Returns:** `EventToken`

Quits the scene manager, returning the execution to the point where Run function is called. It allows current frame to be completed before quiting. It also deactives the current scene. Creates a new scene using the given type and parameters. Scene class should always take parent layer first, then id and then the other parameters if they exists. When using this function, only specify the class as template parameter, the others will be resolved. If a scene with the same id exists, it will be deleted. It is advisable to add new scenes at the start without activating any scene.  @code enum SceneIDs { SCENE_MENU, SCENE_GAME };  //...  class GameScene : public Scene { public: GameScene(Gorgon::SceneManager &parent, SceneID id, int players);  //... };  //...  //Create the game scene with a single player. manager.NewScene&lt;GameScene&gt;(SCENE_GAME, 1);  manager.SwitchScene(SCENE_GAME);  @endcode This event will be fired whenever a scene is activated.


---

## Functions

### `if(first)`

**Returns:** ``



### `first_activation()`

**Returns:** ``



### `activate()`

**Returns:** ``



### `ActivatedEvent()`

**Returns:** ``



### `deactivate()`

**Returns:** ``



### `DeactivatedEvent()`

**Returns:** ``



### `Deactivate()`

**Returns:** ``



### `if(scene == NoSceneID)`

**Returns:** ``



### `ActivatedEvent(*active)`

**Returns:** ``



### `if(active)`

**Returns:** ``



### `while(!quiting)`

**Returns:** ``



### `if(active)`

**Returns:** ``



### `SwitchScene(NoSceneID)`

**Returns:** ``



### `SetFocusStrategy(Strict)`

**Returns:** ``


