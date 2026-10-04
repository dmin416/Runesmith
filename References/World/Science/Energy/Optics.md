# Optics

Hub: `../Science.md`.

## Water-lens telescope (potential)

Concise gist for Mana Hands / ice-water optics or craft: a single lens only focuses; it does not magnify distant objects usefully on its own. Seeing far things up close needs two water lenses acting as a telescope: a large, gently curved front lens (objective) with a long focal length and a small, tightly curved back lens (eyepiece) with a short focal length. Magnification = f_objective / f_eyepiece.

### Objective lens (front, large)

Using lensmaker's equation for water (n = 1.33) with symmetric curvature, R = 2(n−1)f:

- Focal length: 1 m
- Radius of curvature: ≈ 0.66 m per surface
- Diameter: ≈ 0.5 m (bigger diameter = sharper resolution and more light but more mass to hold steady)
- Edge sag (how much the surface curves relative to flat, using sag ≈ D²/8R): ≈ 4.7 cm rise across that 0.5 m width, a shallow, gentle curve

### Eyepiece lens (back, small)

- Focal length: 0.1 m
- Radius of curvature: ≈ 0.066 m per surface
- Diameter: ≈ 5 cm
- Edge sag: ≈ 4.7 mm, a much tighter curve packed into a smaller width

### Result

That pairing gives 10× magnification (1 m ÷ 0.1 m). Spacing between the two lenses should sit close to f_objective + f_eyepiece ≈ 1.1 m for the image to focus properly.

### Scaling

Want more magnification: shrink the eyepiece's focal length rather than growing the objective, since that ratio drives everything. Want a wider field of view or more light-gathering: grow the objective's diameter; holding its focal length fixed makes the curve proportionally shallower and easier to hold steady.
