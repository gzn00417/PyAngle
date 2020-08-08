# PyAngle

> A simple package for angle calculation

## Use

```
pip install PyAngle
```

# class Angle

> Designed especially for angle in the form of DMS(Degree, Minute and Second)
>
> immutable object
>
> default: public, non-static

## APIs

### Creators

- [x] `from_dms()`
- [x] `from_degrees()`
- [x] `from_rad()`
- [x] `from_atan2()`

### Operators

- [x] `__add__(self, other)`: "+"
- [x] `__sub__(self, other)`: "-"
- [x] `__mul__(self, n)`: "\*"
- [x] `__truediv__(self, n)`: "/"
- [x] `__floordiv__(self, n)`: "//"
- [x] `__mod__(self, other)`: "%
- [x] `__str__(self)`
- [x] `__cmp__(self, other)`
- [x] `__eq__(self, other)`: "=="
- [x] `__ne__(self, other)`: "!="
- [x] `__le__(self, other)`: "<="
- [x] `__lt__(self, other)`: "<"
- [x] `__ge__(self, other)`: ">="
- [x] `__gt__(self, other)`: ">"

### Calculators

- [x] `float sin()`
- [x] `float cos()`
- [x] `float tan()`

### Getters

- [x] `int get_deg()`
- [x] `int get_min()`
- [x] `float get_sec()`

### Switchers

- [x] `float to_degrees()`
- [x] `float to_rad()`
- [x] `(float, float) to_atan2(x=None, y=None)`
- [x] `String to_fmt_str(fmt="xxx°xxx′xxx″", decimal=2)`

### Judges

- [x] `bool is_zero_angle()`: 零角
- [x] `bool is_acute_angle()`: 锐角
- [x] `bool is_right_angle()`: 直角
- [x] `bool is_obtuse_angle()`: 钝角
- [x] `bool is_straight_angle()`: 平角
- [x] `bool is_major_angle()`: 优角
- [x] `bool is_minor_angle()`: 劣角

## Future Features

- [ ] `Angle[] toAnglesFromXYs((float, float)[] angles)`: 参数为(x, y)元组的列表
- [ ] `Angle[] toAnglesFromDegrees(float[] angles)`: 参数为 degree 元组的列表
- [ ] `Angle[] toAnglesFromRads(float[] angles)`: 参数为 rad 元组的列表
- [ ] `(float, float)[] toXYsFromAngles(Angle[] angles)`
- [ ] `float[] toDegreesFromAngles(Angle[] angles)`
- [ ] `float[] toRadsFromAngles(Angle[] angles)`
- [ ] `Angle getNearestAngle(Angle angle, Angle[] angles)`: 在`angles`中找到与`angle`最近的角
- [ ] `Angle getFurthestAngle(Angle angle, Angle[] angles)`: 在`angles`中找到与`angle`最远的角
