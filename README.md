# PyAngle

> A simple package for angle calculation

## Use

install

```shell
pip install PyAngle
```

import

```python
from PyAngle import *
```

# class `Angle`

> Designed especially for angle in the form of DMS(Degree, Minute and Second)
>
> immutable object
>
> default: public, non-static

import

```python
from PyAngle.Angle import Angle
```

## APIs

### Creators

```python
>>> a1 = Angle.from_dms(deg=30, min=20, sec=10)
>>> a2 = Angle.from_degrees(degrees=60)
>>> a3 = Angle.from_rad(rad=1.23)
>>> a4 = Angle.from_atan2(x=0.7, y=0.8)
>>> a5 = Angle.from_fmt_str(angle_str="1°2′3″", fmt="aaa°bbb′ccc″")
>>> a6 = Angle(a5)
```

- [x] `from_dms(deg, min=0, sec=0) -> Angle`
- [x] `from_degrees(degrees) -> Angle`
- [x] `from_rad(rad) -> Angle`
- [x] `from_atan2(x, y) -> Angle`
- [x] `from_fmt_str(angle_str, fmt)`

### Operators

```python
>>> str(a1 + a2)
'90 20 10.00'
>>> str(a3 % a4)
'21 39 35.04'
>>> angle_list = [a1, a2, a3, a4]
>>> angle_list.sort(reverse=True)
>>> angle_list
[<PyAngle.Angle.Angle object at 0x0000020C195FD0F0>, <PyAngle.Angle.Angle object at 0x0000020C19521B38>, <PyAngle.Angle.Angle object at 0x0000020C195FD860>, <PyAngle.Angle.Angle object at 0x0000020C195D6EF0>]
>>> a3 > a4
True
```

- [x] `__add__(self, other)`: "+"
- [x] `__sub__(self, other)`: "-"
- [x] `__mul__(self, n)`: "\*"
- [x] `__truediv__(self, n)`: "/"
- [x] `__floordiv__(self, n)`: "//"
- [x] `__mod__(self, other)`: "%"
- [x] `__str__(self)`
- [x] `__cmp__(self, other)`
- [x] `__eq__(self, other)`: "=="
- [x] `__ne__(self, other)`: "!="
- [x] `__le__(self, other)`: "<="
- [x] `__lt__(self, other)`: "<"
- [x] `__ge__(self, other)`: ">="
- [x] `__gt__(self, other)`: ">"
- [x] `__hash__(self)`

### Calculators

```python
>>> a2.sin()
0.8660254037844386
```

- [x] `sin() -> float`
- [x] `cos() -> float`
- [x] `tan() -> float`

### Getters

```python
>>> a4.get_deg()
48
>>> a4.get_sec()
50.66940344529314
```

- [x] `get_deg() -> int`
- [x] `get_min() -> int`
- [x] `get_sec() -> float`

### Switchers

```python
>>> [x.to_degrees() for x in angle_list]
[70.47380880109125, 60.0, 48.81407483429036, 30.336111111111112]
>>> a1.to_atan2(x=1)
(1, 0.5851986012863108)
>>> a3.to_fmt_str()
'70°28′25.71″'
```

- [x] `to_degrees() -> float`
- [x] `to_rad() -> float`
- [x] `to_atan2(x=None, y=None) -> (float, float)`
- [x] `to_fmt_str(fmt="xxx°xxx′xxx″", decimal=2) -> str`

### Judges

```python
>>> a3.is_acute_angle()
True
```

- [x] `is_zero_angle() -> bool`: 零角
- [x] `is_acute_angle() -> bool`: 锐角
- [x] `is_right_angle() -> bool`: 直角
- [x] `is_obtuse_angle() -> bool`: 钝角
- [x] `is_straight_angle() -> bool`: 平角
- [x] `is_major_angle() -> bool`: 优角
- [x] `is_minor_angle() -> bool`: 劣角
- [x] `is_complementary_angle_with(other) -> bool`: 余角
- [x] `is_supplementary_angle_with(other) -> bool`: 补角

# module `AngleListAPIs`

import

```python
from PyAngle.AngleListAPIs import *
```

## APIs

```python
>>> AngleListAPIs.from_angle_list_to_atan2_list(angle_list)
[(0.3342377271245026, 0.9424888019316975), (0.5000000000000001, 0.8660254037844386), (0.658504607868518, 0.7525766947068778), (0.8630773966838536, 0.5050716853412216)]
>>> AngleListAPIs.from_rad_list_to_angle_list([1.23, 1.0471975511965976, 0.8519663271732721, 0.5294650211397243])
[<PyAngle.Angle.Angle object at 0x0000028ED1910DD8>, <PyAngle.Angle.Angle object at 0x0000028ED1910E48>, <PyAngle.Angle.Angle object at 0x0000028ED1910EB8>, <PyAngle.Angle.Angle object at 0x0000028ED1910F28>]
```

- [x] `from_atan2_list_to_angle_list(angles: [(float, float)]) -> ["Angle"]`
- [x] `from_degrees_list_to_angle_list(angles: [float]) -> ["Angle"]`
- [x] `from_rad_list_to_angle_list(angles: [float]) -> ["Angle"]`
- [x] `from_angle_list_to_atan2_list(angles: ["Angle"]) -> [(float, float)]`
- [x] `from_angle_list_to_degrees_list(angles: ["Angle"]) -> [float]`
- [x] `from_angle_list_to_rad_list(angles: ["Angle"]) -> [float]`

```python
# When needed to switch within atan2, degrees and rad, switch via angle list
>>> degrees_list = [1.2, 3.4, 5.6, 7.8, 9.0]
>>> atan2_list = AngleListAPIs.from_angle_list_to_atan2_list(AngleListAPIs.from_degrees_list_to_angle_list(degrees_list))
>>> atan2_list
[(0.9997806834748455, 0.020942419883356957), (0.9982398279237653, 0.05930637357596162), (0.9952273999818312, 0.09758289975914947), (0.9907478404714436, 0.13571557243430438), (0.9876883405951378, 0.15643446504023087)]
```

- [x] `get_nearest_angle(angle: "Angle", angles: ["Angle"]) -> "Angle"`: 在`angles`中找到与`angle`最近的角
- [x] `get_furthest_angle(angle: "Angle", angles: ["Angle"]) -> "Angle"`: 在`angles`中找到与`angle`最远的角

```python
>>> nearest_angle = get_nearest_angle(angle, angles)
```

# class `UnlimitedAngle`

> degrees ranges [-∞, +∞] (without restrict)

import

```python
from PyAngle.UnlimitedAngle import UnlimitedAngle
```

- [x] `to_Angle()`: switch `UnlimitedAngle` into `Angle`

```python
>>> ua1 = UnlimitedAngle.from_degrees(degrees=1000)
>>> ua2 = UnlimitedAngle.from_degrees(degrees=-1000)
>>> ua3 = UnlimitedAngle(ua1)
>>> ua4 = UnlimitedAngle(Angle(UnlimitedAngle(ua2)))
```

# Future Features

## 2.7

> convert relation between `Angle` & `UnlimitedAngle`

- `UnlimitedAngle` to be base class
- `Angle` to be derived class

> Rename `UnlimitedAngle` as `BaseAngle`, features remained

- Provide `__adjust()` for derived class (empty at first)

## 3.0 Beta

- Modify `import PyAngle` as `import pyangle`

## Global Coordinates

## Plot

> Draw Angle on Axis

- [ ] `plot(length, origin=(0, 0), base_angle=Angle.from_degrees(degrees=0), counter_clock_wise=True)`
