# eval_expr
A TI-Nspire CX II python library to evaluate arbitrary TI-Basic expressions.

## Context
TI provides useful functions in their [ti_system module](https://education.ti.com/html/webhelp/EG_TINspire/EN/Subsystems/EG_Python/Content/m_menumap/mm_tisystem.HTML).
Among those, there is `eval_function("name",value)` which "evaluates a predefined OS function at the specified value".

That's good but not good enough to evaluate any function that takes more than a single argument, for instance... And it seems to be restricted to numerical stuff only, too.
How are we supposed to do fancy math stuff from Python? :(

In fact, people have started asking this question on TI-Planet for instance, where [someone wanted](https://tiplanet.org/forum/viewtopic.php?f=116&t=24279#p256279) to have access to specfunc for Laplace transforms. That's when I started to dig in and see if there was any way to do more than just `eval_function`...


## How does this library work?
Well, it turns out that the `ti_system` module also has some internal/lower-level functions exposed (but not listed in the menus), like `writeST` and `readST` (which I guess is used by other higher-level functions like `store_value` and `recall_value`), which interact with the *Symbol Table* which is basically where variables are stored and shared.

Interestingly, `recall_value` seems to be able to evaluate the input and return the output, with much less restrictions!

So, the library leverages that, with some pre- and post-processing to work around some quirks, but it seems to work relatively well.


## Installation
1. Download the .tns file from the [latest release page](https://github.com/TI-Planet/eval_expr/releases/latest).
2. Transfer it to your calculator, in the **PyLib** folder.
3. Enjoy!


## Usage
Just import the module and use the functions it provides: `eval_expr` and `call_func`.

If you just need the `eval_expr` function, you can just do this: `from eval_expr import eval_expr`.

*Aliases (`caseval`, `eval_native`) to `eval_expr` are provided for convenience, for compatibility purposes, if you import the whole module.*


## Documentation
### `eval_expr(expr, trypyeval=False)`:
This is the main function of the library. Pass a TI-Basic expression *(you'll probably want to make that a string)* in the first argument and it will try to evaluate it and return the result as a native Python type, otherwise a string.

If you pass `True` as the 2nd argument (optional, it's `False` by default), it will try to actually evaluate the output in Python. This can be useful for numerical results.
For instance, on an exact-math Nspire (CX II-T) or a CAS model, `eval_expr("sqrt(90)")` would give you `'3*sqrt(10)'`. But `eval_expr("sqrt(90)", True)` returns `9.486832980505138`.

Notes: complex numbers uses the `i` math symbol (looks like `𝒊`) but in Python it's just the letter `j`. Substitution from Basic to Python is handled automatically, just like for other symbols (`√`, `π`, `𝒆`).


### `call_func(funcname, *pyargs)`:
This builds on top of `eval_expr` in order to provide a more powerful `eval_function` that the `ti_system` module offers.

This is a *variadic* function, meaning you can pass any number of arguments you want, for instance `call_func("log", 2, 3.0)` which will give `0.63093`.

The function returns `None` if the output is the same as the input, meaning it couldn't be evaluated. This allows you to easily handle this case in your scripts.


## Caveats
* TI-Basic lists (`{...}`) aren't automatically converted to/from Python lists `[...]`. In a next version?
* No automatic substitution is done from Python to Basic. In a next version?

If you find a bug, a weird behavior, or if you want to submit feedback or give ideas in general, please [open an issue here](https://github.com/TI-Planet/eval_expr/issues/new) :)


## Examples
Here's a screenshot with a few expressions: *(note that `@i` is a way on the Nspire software to quickly get the complex i symbol)*

![Screenshot](https://i.imgur.com/zNZnSf6m.png)


## In the future...
Well, I've contacted TI to see if they could add this kind of feature natively so that we don't need to resort to weird tricks, and they've replied that they're analyzing my feedback, so *there's hope* for a future update :)
