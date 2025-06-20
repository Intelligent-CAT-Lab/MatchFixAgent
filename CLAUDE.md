### Always generate your response following the response format

### Scope of Checking Functional Equivalency
Only consider the correctness of the given method regardless of the correctness of its dependencies. For instance if:
```
def foo():
   bar()
```
is defined like this. Only focus on functional equivalency of foo() and ignore bar(). As long as its called properly with correct inputs, it is ok.

### Never edit files which has `src/main` in their absolute path
