# CPU Benchmark Results

- Suite: `cpu/cpu_ops`
- Target profile: `mac-cpu`
- Timestamp: `20260812_212226`

Latest run: `./scripts/run_all.sh 4`.

This file is generated from one CPU ops run under `data/results/mac-cpu/cpu/einsum/20260812_212226`.

- tenferro-rs commit: `e57b00edd358df6421a436241041fc44b7e38db5`

## CPU Information

- Model: `Apple M5 Max`
- Vendor: `Apple`
- Logical CPUs: `18`
- Physical CPUs: `18`
- Sockets: `1`
- Cores per socket: `18`
- Threads per core: `1`
- NUMA nodes: `1`
- Performance levels: `Super: 6 physical / 6 logical (L1i 192 KiB, L1d 128 KiB, L2 16 MiB, 6 CPUs/L2); Performance: 12 physical / 12 logical (L1i 128 KiB, L1d 64 KiB, L2 8 MiB, 6 CPUs/L2)`
- Python platform: `macOS-26.5.1-arm64-arm-64bit`

## Thread Environment

- OMP_NUM_THREADS: `4`
- OMP_THREAD_LIMIT: `4`
- OMP_DYNAMIC: `FALSE`
- RAYON_NUM_THREADS: `4`
- OPENBLAS_NUM_THREADS: `4`
- GOTO_NUM_THREADS: `4`
- MKL_NUM_THREADS: `4`
- VECLIB_MAXIMUM_THREADS: `4`
- VECLIB_NUM_THREADS: `4`
- NUMEXPR_NUM_THREADS: `4`
- BLIS_NUM_THREADS: `4`
- XLA_FLAGS: `--xla_cpu_multi_thread_eigen=true intra_op_parallelism_threads=4`

## Python Backend Providers

- PyTorch: BLAS provider `accelerate`, version `2.12.0`, BLAS_INFO `accelerate`, LAPACK_INFO `accelerate`
  - linked BLAS/LAPACK libs: `/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate`; `@rpath/libomp.dylib`
- JAX: dot backend `xla_cpu`, version `0.10.1`, jaxlib `0.10.1`, default backend `cpu`, LAPACK provider `internal_lapack`
  - linked LAPACK libs: `bazel-out/darwin_arm64-opt/bin/jaxlib/cpu/_lapack.so`

## Threads: 4

- CSV: `data/results/mac-cpu/cpu/einsum/20260812_212226/cpu_ops_t4_20260812_212226.csv`
- Source table: `data/results/mac-cpu/cpu/einsum/20260812_212226/cpu_ops_t4_20260812_212226.md`

## CPU Benchmark Items

Median ± IQR (ms). Missing backends are shown as `-`.

| suite | benchmark | dtype | threads | shape | tenferro-rs eager mode (ms) | tenferro-rs trace mode (ms) | PyTorch Python (ms) | JAX Python (XLA CPU) (ms) |
|---|---|---:|---:|---|---:|---:|---:|---:|
| batched | `batched_eigh` | f64 | 4 | `2x2xbatch16 (native batch layout)` | 0.071 ± 0.024 | 0.065 ± 0.005 | 0.008 ± 0.001 | 0.015 ± 0.002 |
| batched | `batched_eigh` | f64 | 4 | `2x2xbatch64 (native batch layout)` | 0.128 ± 0.003 | 0.136 ± 0.006 | 0.017 ± 0.000 | 0.049 ± 0.003 |
| batched | `batched_eigh` | f64 | 4 | `4x4xbatch16 (native batch layout)` | 0.074 ± 0.003 | 0.077 ± 0.004 | 0.021 ± 0.000 | 0.030 ± 0.002 |
| batched | `batched_eigh` | f64 | 4 | `4x4xbatch64 (native batch layout)` | 0.182 ± 0.006 | 0.189 ± 0.004 | 0.069 ± 0.000 | 0.106 ± 0.007 |
| batched | `batched_matmul_ikb_kjb_ijb` | f64 | 4 | `2x2xbatch16 (native batch layout)` | 0.064 ± 0.029 | 0.063 ± 0.005 | 0.008 ± 0.001 | 0.075 ± 0.006 |
| batched | `batched_matmul_ikb_kjb_ijb` | f64 | 4 | `2x2xbatch64 (native batch layout)` | 0.050 ± 0.003 | 0.072 ± 0.053 | 0.008 ± 0.000 | 0.090 ± 0.005 |
| batched | `batched_matmul_ikb_kjb_ijb` | f64 | 4 | `4x4xbatch16 (native batch layout)` | 0.050 ± 0.003 | 0.066 ± 0.006 | 0.008 ± 0.000 | 0.100 ± 0.023 |
| batched | `batched_matmul_ikb_kjb_ijb` | f64 | 4 | `4x4xbatch64 (native batch layout)` | 0.055 ± 0.005 | 0.068 ± 0.008 | 0.009 ± 0.000 | 0.113 ± 0.017 |
| batched | `batched_qr` | f64 | 4 | `2x2xbatch16 (native batch layout)` | 0.070 ± 0.013 | 0.069 ± 0.002 | 0.027 ± 0.007 | 0.013 ± 0.001 |
| batched | `batched_qr` | f64 | 4 | `2x2xbatch64 (native batch layout)` | 0.131 ± 0.004 | 0.139 ± 0.005 | 0.034 ± 0.003 | 0.024 ± 0.001 |
| batched | `batched_qr` | f64 | 4 | `4x4xbatch16 (native batch layout)` | 0.063 ± 0.004 | 0.073 ± 0.006 | 0.030 ± 0.003 | 0.017 ± 0.001 |
| batched | `batched_qr` | f64 | 4 | `4x4xbatch64 (native batch layout)` | 0.153 ± 0.004 | 0.157 ± 0.005 | 0.049 ± 0.002 | 0.056 ± 0.005 |
| batched | `batched_solve` | f64 | 4 | `2x2xbatch16 (native batch layout),rhs=1` | 0.197 ± 0.024 | 0.160 ± 0.016 | 0.030 ± 0.003 | 0.011 ± 0.002 |
| batched | `batched_solve` | f64 | 4 | `2x2xbatch64 (native batch layout),rhs=1` | 0.330 ± 0.077 | 0.294 ± 0.008 | 0.034 ± 0.003 | 0.036 ± 0.004 |
| batched | `batched_solve` | f64 | 4 | `4x4xbatch16 (native batch layout),rhs=1` | 0.184 ± 0.003 | 0.161 ± 0.006 | 0.032 ± 0.006 | 0.013 ± 0.001 |
| batched | `batched_solve` | f64 | 4 | `4x4xbatch64 (native batch layout),rhs=1` | 0.327 ± 0.009 | 0.303 ± 0.004 | 0.038 ± 0.006 | 0.043 ± 0.010 |
| batched | `batched_svd` | f64 | 4 | `2x2xbatch16 (native batch layout)` | 0.102 ± 0.015 | 0.088 ± 0.004 | 0.013 ± 0.001 | 0.037 ± 0.002 |
| batched | `batched_svd` | f64 | 4 | `2x2xbatch64 (native batch layout)` | 0.192 ± 0.005 | 0.197 ± 0.007 | 0.035 ± 0.001 | 0.111 ± 0.005 |
| batched | `batched_svd` | f64 | 4 | `4x4xbatch16 (native batch layout)` | 0.106 ± 0.005 | 0.117 ± 0.005 | 0.039 ± 0.001 | 0.061 ± 0.003 |
| batched | `batched_svd` | f64 | 4 | `4x4xbatch64 (native batch layout)` | 0.298 ± 0.004 | 0.303 ± 0.006 | 0.135 ± 0.001 | 0.221 ± 0.003 |
| batched | `grad_sum_batched_matmul_backward` | f64 | 4 | `2x2xbatch16 (native batch layout)` | 0.329 ± 0.031 | 0.155 ± 0.004 | 0.043 ± 0.003 | 0.705 ± 0.118 |
| batched | `grad_sum_batched_matmul_backward` | f64 | 4 | `2x2xbatch64 (native batch layout)` | 0.286 ± 0.011 | 0.159 ± 0.004 | 0.044 ± 0.002 | 0.582 ± 0.058 |
| batched | `grad_sum_batched_matmul_backward` | f64 | 4 | `4x4xbatch16 (native batch layout)` | 0.292 ± 0.011 | 0.175 ± 0.028 | 0.046 ± 0.004 | 0.595 ± 0.050 |
| batched | `grad_sum_batched_matmul_backward` | f64 | 4 | `4x4xbatch64 (native batch layout)` | 0.325 ± 0.056 | 0.163 ± 0.005 | 0.047 ± 0.001 | 0.599 ± 0.043 |
| batched | `grad_sum_batched_solve_backward` | f64 | 4 | `2x2xbatch16 (native batch layout),rhs=1` | 0.751 ± 0.010 | 0.435 ± 0.013 | 0.060 ± 0.013 | 0.494 ± 0.028 |
| batched | `grad_sum_batched_solve_backward` | f64 | 4 | `2x2xbatch64 (native batch layout),rhs=1` | 1.245 ± 0.022 | 0.669 ± 0.007 | 0.069 ± 0.013 | 0.482 ± 0.033 |
| batched | `grad_sum_batched_solve_backward` | f64 | 4 | `4x4xbatch16 (native batch layout),rhs=1` | 0.779 ± 0.031 | 0.464 ± 0.080 | 0.060 ± 0.003 | 0.489 ± 0.024 |
| batched | `grad_sum_batched_solve_backward` | f64 | 4 | `4x4xbatch64 (native batch layout),rhs=1` | 1.282 ± 0.043 | 0.746 ± 0.215 | 0.071 ± 0.005 | 0.503 ± 0.021 |
| large | `eigh` | f64 | 4 | `64x64` | 0.344 ± 0.022 | 0.358 ± 0.030 | 0.295 ± 0.012 | 0.338 ± 0.015 |
| large | `grad_sum_matmul` | f64 | 4 | `64x64` | 0.060 ± 0.007 | 0.098 ± 0.032 | 0.009 ± 0.001 | 0.061 ± 0.009 |
| large | `grad_sum_matmul_backward` | f64 | 4 | `64x64` | 0.294 ± 0.013 | 0.177 ± 0.024 | 0.039 ± 0.012 | 0.531 ± 0.179 |
| large | `grad_sum_solve_backward` | f64 | 4 | `64x64,rhs=1` | 0.904 ± 0.199 | 0.364 ± 0.003 | 0.058 ± 0.002 | 0.502 ± 0.022 |
| large | `grad_sum_svd_s_backward` | f64 | 4 | `64x64` | 1.081 ± 0.047 | 0.572 ± 0.004 | 0.454 ± 0.044 | 0.673 ± 0.181 |
| large | `matmul` | f64 | 4 | `128x128` | 0.079 ± 0.059 | 0.082 ± 0.004 | 0.023 ± 0.002 | 0.129 ± 0.002 |
| large | `matmul` | f64 | 4 | `256x256` | 0.210 ± 0.033 | 0.216 ± 0.003 | 0.132 ± 0.011 | 0.274 ± 0.031 |
| large | `matmul_rect` | f64 | 4 | `256x1024 * 1024x256` | 0.612 ± 0.019 | 0.612 ± 0.027 | 0.543 ± 0.020 | 0.537 ± 0.077 |
| large | `qr` | f64 | 4 | `64x64` | 0.141 ± 0.018 | 0.146 ± 0.007 | 0.127 ± 0.008 | 0.141 ± 0.027 |
| large | `solve` | f64 | 4 | `64x64,rhs=1` | 0.151 ± 0.006 | 0.190 ± 0.029 | 0.027 ± 0.002 | 0.052 ± 0.005 |
| large | `solve` | f64 | 4 | `64x64,rhs=16` | 0.149 ± 0.009 | 0.186 ± 0.006 | 0.031 ± 0.006 | 0.064 ± 0.006 |
| large | `solve` | f64 | 4 | `64x64,rhs=64` | 0.159 ± 0.011 | 0.202 ± 0.024 | 0.038 ± 0.001 | 0.085 ± 0.019 |
| large | `svd` | f64 | 4 | `64x64` | 0.469 ± 0.023 | 0.473 ± 0.011 | 0.422 ± 0.034 | 0.456 ± 0.004 |
| small | `eigh` | f64 | 4 | `2x2` | 0.050 ± 0.008 | 0.051 ± 0.004 | 0.004 ± 0.001 | 0.009 ± 0.001 |
| small | `eigh` | f64 | 4 | `4x4` | 0.051 ± 0.038 | 0.049 ± 0.006 | 0.005 ± 0.001 | 0.010 ± 0.001 |
| small | `eigh` | f64 | 4 | `8x8` | 0.055 ± 0.003 | 0.053 ± 0.004 | 0.008 ± 0.001 | 0.014 ± 0.002 |
| small | `einsum_ij_jk_ik` | f64 | 4 | `2x2` | 0.067 ± 0.006 | 0.062 ± 0.009 | 0.007 ± 0.001 | 0.074 ± 0.005 |
| small | `einsum_ij_jk_ik` | f64 | 4 | `4x4` | 0.055 ± 0.004 | 0.061 ± 0.006 | 0.007 ± 0.000 | 0.078 ± 0.004 |
| small | `einsum_ij_jk_ik` | f64 | 4 | `8x8` | 0.063 ± 0.018 | 0.061 ± 0.004 | 0.008 ± 0.000 | 0.085 ± 0.006 |
| small | `grad_sum_matmul_backward` | f64 | 4 | `2x2` | 0.323 ± 0.027 | 0.151 ± 0.009 | 0.020 ± 0.003 | 0.440 ± 0.031 |
| small | `grad_sum_matmul_backward` | f64 | 4 | `4x4` | 0.391 ± 0.046 | 0.156 ± 0.010 | 0.019 ± 0.001 | 0.435 ± 0.035 |
| small | `grad_sum_matmul_backward` | f64 | 4 | `8x8` | 0.303 ± 0.013 | 0.158 ± 0.003 | 0.028 ± 0.050 | 0.451 ± 0.018 |
| small | `grad_sum_solve_backward` | f64 | 4 | `2x2,rhs=1` | 0.707 ± 0.096 | 0.352 ± 0.013 | 0.030 ± 0.001 | 0.487 ± 0.023 |
| small | `grad_sum_solve_backward` | f64 | 4 | `4x4,rhs=1` | 0.701 ± 0.089 | 0.341 ± 0.007 | 0.030 ± 0.002 | 0.477 ± 0.026 |
| small | `grad_sum_solve_backward` | f64 | 4 | `8x8,rhs=1` | 0.691 ± 0.207 | 0.347 ± 0.011 | 0.032 ± 0.001 | 0.479 ± 0.029 |
| small | `grad_sum_svd_s_backward` | f64 | 4 | `2x2` | 0.283 ± 0.015 | 0.161 ± 0.010 | 0.023 ± 0.001 | 0.521 ± 0.027 |
| small | `grad_sum_svd_s_backward` | f64 | 4 | `4x4` | 0.335 ± 0.071 | 0.161 ± 0.007 | 0.024 ± 0.000 | 0.534 ± 0.027 |
| small | `grad_sum_svd_s_backward` | f64 | 4 | `8x8` | 0.304 ± 0.090 | 0.169 ± 0.012 | 0.043 ± 0.023 | 0.549 ± 0.049 |
| small | `matmul` | f64 | 4 | `2x2` | 0.092 ± 0.008 | 0.066 ± 0.055 | 0.001 ± 0.000 | 0.007 ± 0.002 |
| small | `matmul` | f64 | 4 | `4x4` | 0.054 ± 0.003 | 0.062 ± 0.004 | 0.001 ± 0.000 | 0.007 ± 0.001 |
| small | `matmul` | f64 | 4 | `8x8` | 0.080 ± 0.033 | 0.067 ± 0.007 | 0.001 ± 0.000 | 0.023 ± 0.003 |
| small | `qr` | f64 | 4 | `2x2` | 0.060 ± 0.006 | 0.051 ± 0.009 | 0.025 ± 0.009 | 0.009 ± 0.002 |
| small | `qr` | f64 | 4 | `4x4` | 0.050 ± 0.022 | 0.049 ± 0.002 | 0.027 ± 0.010 | 0.009 ± 0.002 |
| small | `qr` | f64 | 4 | `8x8` | 0.057 ± 0.011 | 0.051 ± 0.004 | 0.025 ± 0.013 | 0.010 ± 0.001 |
| small | `solve` | f64 | 4 | `2x2,rhs=1` | 0.169 ± 0.018 | 0.127 ± 0.022 | 0.008 ± 0.000 | 0.009 ± 0.001 |
| small | `solve` | f64 | 4 | `2x2,rhs=4` | 0.163 ± 0.008 | 0.119 ± 0.010 | 0.008 ± 0.000 | 0.008 ± 0.002 |
| small | `solve` | f64 | 4 | `4x4,rhs=1` | 0.239 ± 0.146 | 0.136 ± 0.013 | 0.008 ± 0.000 | 0.009 ± 0.001 |
| small | `solve` | f64 | 4 | `4x4,rhs=4` | 0.142 ± 0.021 | 0.116 ± 0.003 | 0.008 ± 0.000 | 0.009 ± 0.002 |
| small | `solve` | f64 | 4 | `8x8,rhs=1` | 0.208 ± 0.027 | 0.118 ± 0.004 | 0.008 ± 0.000 | 0.009 ± 0.001 |
| small | `solve` | f64 | 4 | `8x8,rhs=4` | 0.176 ± 0.018 | 0.126 ± 0.010 | 0.008 ± 0.000 | 0.009 ± 0.001 |
| small | `svd` | f64 | 4 | `2x2` | 0.067 ± 0.009 | 0.060 ± 0.003 | 0.005 ± 0.001 | 0.012 ± 0.002 |
| small | `svd` | f64 | 4 | `4x4` | 0.050 ± 0.002 | 0.055 ± 0.004 | 0.007 ± 0.000 | 0.014 ± 0.001 |
| small | `svd` | f64 | 4 | `8x8` | 0.058 ± 0.010 | 0.064 ± 0.003 | 0.012 ± 0.001 | 0.020 ± 0.002 |
