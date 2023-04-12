[![MFKDF](https://raw.githubusercontent.com/multifactor/MFKDF/master/site/logo.png "MFKDF")](https://mfkdf.com/ "MFKDF")

Browser Benchmarks for MFKDF

[![GitHub issues](https://img.shields.io/github/issues/multifactor/mfkdf-benchmark)](https://github.com/multifactor/mfkdf-benchmark/issues)
[![MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/multifactor/mfkdf-benchmark/blob/main/LICENSE)

[Run Benchmark](https://benchmark.mfkdf.com) |
[MFKDF Repo](https://github.com/multifactor/mfkdf) |
[MFKDF Site](https://mfkdf.com/) |
[MFKDF Docs](https://mfkdf.com/docs/) |
[Multifactor](https://github.com/multifactor) |
[Author](https://github.com/VCNinc)

This repository contains browser-based benchmarks for the MFKDF JavaScript library, including standard and threshold MFKDF variants along with all supported factors.

## Option A: Automatic Benchmark
The fastest and easiest way to run the browser-based benchmark is to simply visit [benchmark.mfkdf.com](https://benchmark.mfkdf.com) and click "Run Now." The benchmark usually takes just a few seconds to run, and the results will be immediately displayed within your browser upon completion.

## Option B: Manual Benchmark
Alternatively, you can manually run the benchmarking code by cloning this repository and opening "manual.html" in your browser of choice. Copy the resulting output into the "results.txt" file in the "figs" directory, and then run the python scripts in that directory to regenerate the graphs from the paper. The results can be used to verify the performance claims of §11 of the [USENIX paper](https://www.usenix.org/conference/usenixsecurity23/presentation/nair), particularly figures 7 and 8.

Copyright ©2023 Vivek Nair • [MIT](https://github.com/multifactor/mfkdf-benchmark/blob/main/LICENSE)
