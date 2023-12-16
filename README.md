# python-web-framework-performance

flask: https://github.com/pallets/flask

responder: https://github.com/kennethreitz/responder

## wrk testing results

Using wrk https://github.com/wg/wrk for http benchmarking

flask:

```
➜  ~ wrk -t12 -c400 -d30s http://127.0.0.1:5000/hello
Running 30s test @ http://127.0.0.1:5000/hello
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    69.53ms   46.60ms 614.33ms   97.09%
    Req/Sec   145.39     64.14   320.00     64.77%
  16604 requests in 30.11s, 2.64MB read
  Socket errors: connect 174, read 1113, write 8, timeout 0
Requests/sec:    551.53
Transfer/sec:     89.95KB
```

responder:

```
➜  ~ wrk -t12 -c400 -d30s http://127.0.0.1:5042/hello
Running 30s test @ http://127.0.0.1:5042/hello
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   149.27ms   30.32ms 215.54ms   80.00%
    Req/Sec   209.13     48.47   420.00     70.92%
  74991 requests in 30.10s, 10.08MB read
  Socket errors: connect 0, read 384, write 0, timeout 0
Requests/sec:   2491.70
Transfer/sec:    343.10KB
```