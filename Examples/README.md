# Examples

This folder contains some examples of l-systems.

These where found on:
- [Wikipedia](https://en.wikipedia.org/wiki/L-system) 
- [Paul Bourke's website](http://paulbourke.net/fractals/lsys/)


## Assignment

This l-system was given on our assignment:

```json
{
    "axiom": "A",
    "rules": {
        "A": "AA+[+A-A-A]-[-A+A+A]"
	},
	"translations" : {
        "A": ["draw", 10],
        "+": ["angle", 22.5],
        "-": ["angle", -22.5],
        "[": ["push"],
        "]": ["pop"]
	}
}
```

This produces the following drawing for 5 iterations:

<img src="Assignment_5.svg">

## Sierpinski triangle

Config:

```json
{
    "axiom": "F−G−G",
    "rules": {
        "F": "F−G+F+G−F",
        "G": "GG"
    },
    "translations": {
        "F": ["draw", 10],
        "G": ["draw", 10],
        "+": ["angle", 120],
        "−": ["angle", -120]
    }
}
```

This produces the following drawing for 5 iterations:

<img src="SierpinskiTriangle_5.svg">

## Fractal plant

Config:

```json
{
    "axiom": "X",
    "rules": {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF"
    },
    "translations": {
        "F": ["draw", 10],
        "X": ["draw", 10],
        "+": ["angle", 25],
        "-": ["angle", -25],
        "[": ["push"],
        "]": ["pop"]
    }
}
```

This produces the following drawing for 5 iterations:

<img src="FractalPlant_5.svg">

## Bush: Saupe


```json
{
    "axiom": "VZFFF",
    "rules": {
        "V": "[+++W][---W]YV",
        "W": "+X[-W]Z",
        "X": "-W[+X]Z",
        "Y": "YZ",
        "Z": "[-FFF][+FFF]F"
    },
    "translations": {
        "F": ["draw", 10],
        "V": ["draw", 10],
        "W": ["draw", 10],
        "X": ["draw", 10],
        "Y": ["draw", 10],
        "Z": ["draw", 10],
        "+": ["angle", 20],
        "-": ["angle", -20],
        "[": ["push"],
        "]": ["pop"]
    }
}
```

This produces the following drawing for 7 iterations:

<img src="BushSaupe_7.svg">

## Quadratic Snowflake

Variation by Hasan Hosam.
Config:

```json
{
    "axiom": "FF+FF+FF+FF",
    "rules": {
        "F": "F+F-F-F+F"
    },
    "translations": {
        "F": ["draw", 10],
        "+": ["angle", 90],
        "-": ["angle", -90]
    }
}
```

This produces the following drawing for 4 iterations:

<img src="QuadraticSnowflake_4.svg">

## Triangle

Variation by Paul Bourke

```json
{
    "variables": ["F"],
    "constants": ["+", "-"],
    "axiom": "F+F+F",
    "rules": {
        "F": "F-F+F"
	},
	"translations" : {
        "F": ["draw", 10],
        "+": ["angle", 120],
        "-": ["angle", -120]
	}
}
```

This produces the following drawing for 5 iterations:
<img src="Triangle_5.svg">

