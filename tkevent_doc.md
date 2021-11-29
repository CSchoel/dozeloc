## Observation: Error vanishes when disabling all lines that set the state of the widget to "disabled"

`state="disabled"` in constructor is not relevant, since it is overwritten in `select()` and `show_result()` respectively.

`.config(state="diabled")` however does activate/inactivate key events both in the result and in the exercise text widget.

## Stackoverflow-Post points to problem with focus

Link: https://stackoverflow.com/a/10817982

The thing that is platform independent seems to be that on some platforms (e.g. Mac OSX) the disabled widget does not get the focus when it is clicked and on others (windows, linux) it does. This can be remedied by adding the following line:

```python
self.result.bind("<Button-1>", lambda event: self.result.focus_set())
```