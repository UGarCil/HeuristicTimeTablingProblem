# HeuristicTimeTablingProblem
A heuristic approach to the timetabling problem.

```python
# The algorithm

# FOR 1000 iterations:
    # create copy of STUDENT_LIST and shuffle it
    # While tries are less than 100:
        # pick a student at random from STUDENT_LIST:
            # create random copy of this STUDENT times
            # for every time available:
                # is time available?
                #   T: assign time, then append student and its time to finalLIst.
                #      erase student from clone students LIST once it's done
                #      stop looking for more STUDENT times
        # tries += 1
```

Here is an introduction and video tutorial:  
[![Video Tutorial](http://img.youtube.com/vi/2OtvSYY6bZw/0.jpg)](https://www.youtube.com/watch?v=2OtvSYY6bZw)
