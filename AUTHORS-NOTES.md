# Author list notes (2026-11-15)

Authorship rule: people with substantive contributions to tenferro-rs or its
upstream crates (strided, tcontract, tlinalg, threadteam, colmat/t4a-faer,
t4a-gpu-backend, benchmark repositories), including non-code contributions
such as design direction (allowed by JOSS). All co-authors must agree before
submission. AI agents and bots are not authors; they go in the AI usage
disclosure.

| Author | Contribution |
| --- | --- |
| Hiroshi Shinaoka | All repositories; overall design (corresponding) |
| Jin-Guo Liu | Initial design with H.S. (tensor4all-meta); CUDA performance fixes |
| Satoshi Terasaki | Benchmark infrastructure (tenferro-benchmark), strided, tcontract, colmat |
| Ryo Watanabe | CpuEngine, strided, tcontract, threadteam |
| Lukas Devos | tcontract contraction engine (from his Rust prototype), Julia wrapper |
| Martin Mikkelsen | colmat LAPACK numerical validation suite and numerical fixes; tlinalg |
| Yusheng Zhao | CUDA SVD driver selection (SvdOptions::driver, Xgesvdp), cuBLAS fixes |
| Ning-Yuan Chen | tcontract-benchmark (qcbench, EPYC 9575F campaigns) |
| Guo Chen | CPU kernel collaboration; direction of benchmark work (write the concrete contribution) |

Not authors: faer authors and contributors (cite faer); bots and AI agents.
Candidates for the tensor4all-rs paper (C): Ken Inayoshi, Lingrui Cheng, Samuel Badr.

To collect from each co-author: consent, affiliation, ORCID.
