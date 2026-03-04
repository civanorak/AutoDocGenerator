# Threading

> Auto-generated documentation for the **Threading** module of the Gorgon C++ Game Engine.


## Contents

- [Functions](#functions)

---

## Functions

### `t(fn)`

**Returns:** `std::thread`


Executes a function asynchronously. This function starts the thread immediately. There is no way to wait for the thread, stop or query its execution. @param fn the function to be executed.


### `for(int id=0;id<threads;id++)`

**Returns:** ``


Runs a function specified amount of times in parallel. threads parameter controls the amount of parallel executions. This function will return when all threads it controls finishes. The following example performs an operation over the data vector using 4 threads. If the threads parameter is omitted, the number of threads supported by hardware is used. @code std::vector<int> data(1000); RunInParallel([&data](int threadid, int threads) { for(int i=threadid;i<data.size();i+=threads) { //... do something with data[i] } }, 4); @endcode @param fn is the function to be executed. First parameter of the function should be thread id, second is the number of threads. See the example. @param threads the number of threads to be executed.


### `for(int id=0;id<threads;id++)`

**Returns:** ``


