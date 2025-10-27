# pikahttp Documentation

```{toctree}
:maxdepth: 2
:caption: Contents:

installation
quickstart
api
examples
```

## About pikahttp

pikahttp is a fast HTTP client for Python powered by Rust. It combines Python's ease of use with Rust's performance and safety.

## Features

- Fast: Written in Rust using the high-performance Hyper HTTP library
- Simple: Clean Python API that's easy to use
- Reliable: Built on battle-tested Rust libraries
- Memory efficient: Minimizes allocations and copies

## Performance

Based on benchmarks making 100 HTTP requests to api.ipify.org:

```
Library         Mean (s)     Median (s)   Min (s)      Max (s)      StdDev (s)  
--------------------------------------------------------------------------------
urllib         0.2389       0.2351       0.2291       0.6488       0.0415      
requests       0.2590       0.2575       0.2524       0.3014       0.0071      
pikahttp       0.2193       0.2202       0.2162       0.2252       0.0021      
```

Key findings:
- 8.9% faster than urllib
- 18.1% faster than requests
- More consistent performance (lower standard deviation)

## Indices and tables

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`