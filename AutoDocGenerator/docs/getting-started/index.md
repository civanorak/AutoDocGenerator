# Getting Started with Gorgon

&gt; This guide will walk you through creating your first game using the Gorgon C++ Game Engine. In about 50 lines of code, you'll have a working window with graphics and mouse input.

## Prerequisites

- A C++ compiler (MSVC on Windows, GCC/Clang on Linux)
- CMake 3.16+
- Gorgon library built and linked to your project

---

## Essential Header Files

Every Gorgon game is built around a small set of core includes. Here's what each one does:

| Header | Purpose |
|---|---|
| `<Gorgon/Main.h>` | **Engine core** — `Initialize()`, `NextFrame()`, `Tick()` |
| `<Gorgon/Window.h>` | **Window creation** — opens the OS window |
| `<Gorgon/WindowManager.h>` | **OS integration** — icons, monitor info |
| `<Gorgon/Graphics/Layer.h>` | **Rendering** — draw surfaces (like canvas layers in Photoshop) |
| `<Gorgon/Graphics/BlankImage.h>` | **Solid color shapes** — rectangles, backgrounds |
| `<Gorgon/Graphics/FreeType.h>` | **Text rendering** — load TTF fonts and print text |
| `<Gorgon/Graphics/Bitmap.h>` | **Image loading** — PNG/JPG textures |
| `<Gorgon/Input/Mouse.h>` | **Mouse input** — click, move, scroll events |
| `<Gorgon/Input/Layer.h>` | **Input regions** — bind mouse input to a specific area |
| `<Gorgon/Time.h>` | **Delta time** — frame-accurate time for smooth movement |
| `<Gorgon/Geometry/Point.h>` | **2D position** — `Point{x, y}` |
| `<Gorgon/Geometry/Size.h>` | **Dimensions** — `Size{width, height}` |
| `<Gorgon/Geometry/Bounds.h>` | **Collision boxes** — rectangle-point intersection |

---

## The Game Loop Pattern

Every Gorgon game follows the same three-step loop:

```cpp
// Step 1: Initialize the engine once
Gorgon::Initialize("MyGame");

// Step 2: Create a window
Gorgon::Window window({800, 600}, "My First Game");

// Step 3: Run the game loop
while(true) {
    // --- UPDATE ---
    auto delta = Gorgon::Time::DeltaTime();  // ms since last frame
    // move your objects using delta...

    // --- RENDER ---
    gameLayer.Clear();
    // draw your objects...

    // --- NEXT FRAME (handles OS events, limits to ~60 FPS) ---
    Gorgon::NextFrame();
}
```

---

## Table of Contents

- [Tutorial: Your First Game — Green Shooter](#tutorial-your-first-game-green-shooter)
- [Tutorial: Space Shooter — Keyboard & Physics](#tutorial-space-shooter-keyboard-physics)
- [Core Concepts Reference](#core-concepts-reference)
- [What to Build Next](#what-to-build-next)

---

## Tutorial: Your First Game — Green Shooter

This tutorial recreates the bundled **Green Shooter** example step by step. The game spawns colored squares on screen; click the green ones to score points.

### Step 1 — Includes and Setup

```cpp
#include <Gorgon/Main.h>
#include <Gorgon/Window.h>
#include <Gorgon/WindowManager.h>
#include <Gorgon/Graphics/Layer.h>
#include <Gorgon/Graphics/FreeType.h>
#include <Gorgon/Graphics/BlankImage.h>
#include <Gorgon/Input/Mouse.h>
#include <Gorgon/Input/Layer.h>

// Game state
int score = 0;
int lives = 3;
```

### Step 2 — Creating a Window and Layers

Gorgon uses **Layers** as rendering surfaces. Think of them like layers in an image editor — they stack on top of each other.

```cpp
// Initialize the engine with a system name
Gorgon::Initialize("GreenShooter");

// Create the window (size, title)
Gorgon::Window window({404, 444}, "Green Shooter");

// Create rendering layers
Gorgon::Graphics::Layer backgroundLayer; // bottom: static background
Gorgon::Graphics::Layer uiLayer;         // middle: score / UI text
Gorgon::Graphics::Layer gameLayer;       // top: game objects

// Add layers to the window (order = draw order, last is on top)
window.Add(backgroundLayer);

uiLayer.Move(2, 2);
uiLayer.Resize(400, 38);
window.Add(uiLayer);

gameLayer.EnableClipping();   // prevents drawing outside the area
gameLayer.Move(2, 42);
gameLayer.Resize(400, 400);
window.Add(gameLayer);
```

### Step 3 — Drawing Backgrounds

`BlankImage` is a solid-color rectangle — the simplest drawable in Gorgon.

```cpp
// Create solid-color backgrounds (float = lightness 0.0–1.0)
Gorgon::Graphics::BlankImage appBg(0.22f);  // dark gray
Gorgon::Graphics::BlankImage gameBg(0.85f); // light gray
Gorgon::Graphics::BlankImage uiBg(0.32f);   // medium gray

// DrawIn fills the entire layer (drawn once — no need to redraw)
appBg.DrawIn(backgroundLayer);
gameBg.DrawIn(backgroundLayer, 2, 42, 400, 400);
uiBg.DrawIn(backgroundLayer, 2, 2, 400, 38);
```

### Step 4 — Loading a Font

```cpp
Gorgon::Graphics::FreeType font;
font.DisableAntiAliasing();       // pixel-art style
font.LoadFile("Boxy-Bold.ttf", 20); // filename, size in px
```

### Step 5 — Handling Mouse Clicks

`Input::Layer` binds mouse events to a region. Register a lambda to handle clicks:

```cpp
Gorgon::Input::Layer inputLayer;
gameLayer.Add(inputLayer);  // attach to game area

inputLayer.SetClick([](Gorgon::Geometry::Point location) {
    for(auto &obj : objects) {
        // Check if click is inside this object's bounding box
        Gorgon::Geometry::Bounds bounds(obj.location, {40, 40});
        if(IsInside(bounds, location)) {
            obj.Hit();
            return;
        }
    }
    score--;  // missed, penalty
});
```

### Step 6 — The Game Loop

```cpp
// Close window → quit app
window.DestroyedEvent.Register([]() { exit(0); });

while(true) {
    // Delta time in milliseconds since last frame
    auto delta = Gorgon::Time::DeltaTime();

    // Update all game objects
    for(auto &obj : objects) {
        obj.Elapsed(delta);
    }

    // Remove expired objects
    objects.erase(
        std::remove_if(objects.begin(), objects.end(),
            [](const Object &o) { return o.lifetime <= 0; }),
        objects.end()
    );

    // Render frame
    gameLayer.Clear();
    for(auto &obj : objects) {
        obj.Draw(gameLayer);
    }

    // Draw UI text
    ui_layer.Clear();
    font.Print(uiLayer, Gorgon::String::Concat("Score: ", score), 11, 11, 378, 0.0f);
    font.Print(uiLayer, Gorgon::String::Concat("Lives: ", lives), 11, 11, 378,
               Gorgon::Graphics::TextAlignment::Right, 0.0f);

    // End frame (render + ~60 FPS cap + OS events)
    Gorgon::NextFrame();
}
```

---

---

## Tutorial: Space Shooter — Full-scale Game

In this expanded tutorial, we create a complete **Space Shooter** with parallax backgrounds, sprite animations, and explosion effects.

### Step 1 — Advanced Initialization & Layers

For a full-scale game, we need separate layers for depth.

```cpp
#include <Gorgon/Main.h>
#include <Gorgon/Graphics/Layer.h>
#include <Gorgon/Graphics/TextureAnimation.h>

Gorgon::Window window({800, 600}, "Space Shooter Pro");

Gorgon::Graphics::Layer starfieldLayer; // Background
Gorgon::Graphics::Layer gameLayer;      // Ships and Bullets
Gorgon::Graphics::Layer fxLayer;        // Explosions and particles
Gorgon::Graphics::Layer uiLayer;        // Score and UI

window.Add(starfieldLayer);
window.Add(gameLayer);
window.Add(fxLayer);
window.Add(uiLayer);
```

### Step 2 — Animated Sprites & Background

We use `TextureAnimation` to handle multiple frames for the ship and the starfield.

```cpp
// 1. Loading an animated ship
Gorgon::Graphics::TextureAnimation shipAnim;
shipAnim.LoadFile("ship_spritesheet.png", 64, 64); // sprite size
shipAnim.SetSpeed(100); // 100ms per frame

// 2. Scrolling Background (Parallax)
float bgOffset = 0;
void DrawBackground(float delta) {
    bgOffset += 0.05f * delta;
    if (bgOffset > 600) bgOffset = 0;
    
    starfieldLayer.Clear();
    starTexture.Draw(starfieldLayer, {0, bgOffset});
    starTexture.Draw(starfieldLayer, {0, bgOffset - 600});
}
```

### Step 3 — Full Ship Control (2D Movement)

We check for WASD or Arrow keys to move the ship in any direction.

```cpp
Gorgon::Geometry::Pointf shipPos = {400, 500};
float speed = 0.4f;

void UpdateInput(float delta) {
    using namespace Gorgon::Input;
    if (Keyboard::IsDown(Keyboard::Key::W)) shipPos.y -= speed * delta;
    if (Keyboard::IsDown(Keyboard::Key::S)) shipPos.y += speed * delta;
    if (Keyboard::IsDown(Keyboard::Key::A)) shipPos.x -= speed * delta;
    if (Keyboard::IsDown(Keyboard::Key::D)) shipPos.x += speed * delta;
    
    // Fire weapon
    if (Keyboard::IsDown(Keyboard::Key::Space)) {
        Shoot();
    }
}
```

### Step 4 — Explosions & Enemy Animations

When an enemy is hit, we spawn an explosion object that plays its animation once and then disappears.

```cpp
struct Explosion {
    Gorgon::Geometry::Pointf pos;
    Gorgon::Graphics::TextureAnimation anim;
    bool finished = false;

    Explosion(Gorgon::Geometry::Pointf p) : pos(p) {
        anim.LoadFile("explosion.png", 32, 32);
        anim.SetLoop(false); // plays once
    }

    void Update(float delta) {
        anim.Elapsed(delta);
        if (anim.IsFinished()) finished = true;
    }

    void Draw(Gorgon::Graphics::Layer &l) {
        anim.Draw(l, pos);
    }
};

// Global list for FX
std::vector<Explosion> effects;

// Inside collision detection:
if (HitDetection(bullet, enemy)) {
    effects.emplace_back(enemy.pos); // Create explosion
    Destroy(enemy);
}
```

### Step 5 — The Main Loop

Everything comes together in the loop.

```cpp
while(true) {
    auto delta = Gorgon::Time::DeltaTime();

    UpdateInput(delta);
    DrawBackground(delta);

    gameLayer.Clear();
    fxLayer.Clear();

    // Draw Ship
    shipAnim.Elapsed(delta);
    shipAnim.Draw(gameLayer, shipPos);

    // Update & Draw FX
    for(auto &fx : effects) {
        fx.Update(delta);
        fx.Draw(fxLayer);
    }

    // Cleanup finished FX
    effects.erase(std::remove_if(effects.begin(), effects.end(), 
        [](auto &fx){ return fx.finished; }), effects.end());

    Gorgon::NextFrame();
}
```

---

## Core Concepts Reference

### Geometry Types

```cpp
Gorgon::Geometry::Point  p  = {100, 200};     // x, y position
Gorgon::Geometry::Size   sz = {400, 300};     // width, height
Gorgon::Geometry::Bounds b  = {p, sz};        // rectangle starting at p

bool hit = Gorgon::Geometry::IsInside(b, clickPoint); // collision check
```

### Drawing Images

```cpp
// BlankImage: solid-color rectangle
Gorgon::Graphics::BlankImage rect(40, 40, 0xff193d19); // w, h, ARGB color

// Draw at position on a layer
rect.Draw(layer, {x, y});

// Draw with alpha fade (lightness, alpha)
rect.Draw(layer, {x, y}, {1.0f, 0.5f});  // 50% transparent
```

### Time and Delta Time

```cpp
// Returns milliseconds elapsed since last frame
auto delta = Gorgon::Time::DeltaTime();

// Move an object at 200 pixels/second
object.x += 200.0f * (delta / 1000.0f);
```

### Text Rendering

```cpp
// Print text at position (layer, text, x, y, maxWidth, color)
font.Print(layer, "Hello World!", 10, 10, 300, 0.0f);  // 0.0f = black

// Right-aligned
font.Print(layer, "Score: 42", 10, 10, 300,
           Gorgon::Graphics::TextAlignment::Right, 0.0f);
```

---

## What to Build Next

| Idea | New Concepts |
|---|---|
| Moving character | `Input::Keyboard`, frame-based position update |
| Platformer physics | `Geometry::Bounds` collision, gravity via delta time |
| Sound effects | `Audio::Source`, `Encoding::FLAC` / `Vorbis` |
| Tiled map | `Game::Map::TiledMap` |
| A\* pathfinding | `Game::Pathfinding::AStar` |
| Animated sprites | `Animation`, `Graphics::TextureAnimation` |

See the sidebar for the full API reference of each module. Good luck! 🎮
