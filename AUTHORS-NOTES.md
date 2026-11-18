# Author list notes (updated 2026-11-18)

## Authorship criteria

Planned submission: mid-January 2027. An author must meet all of the following.

1. **Contribution history of about two months or more** by the submission date.
   A single PR or issue is not enough.
2. **Substantial contribution** to tenferro-rs or its upstream crates (strided,
   tcontract, tlinalg, threadteam, colmat/t4a-faer, t4a-gemm, t4a-gpu-backend,
   benchmark repositories): code, design, benchmarks, validation, or sustained
   real use of the tenferro ecosystem with feedback. Design direction counts
   (JOSS accepts non-code contributions).
3. **Commitment for about the next year** to put effort into developing the
   tenferro ecosystem and spreading it: using it in their own projects,
   feedback, teaching, talks, or bringing in users and groups.
4. **Consent and accountability.** Agree to be listed and to be accountable for
   the whole paper (JOSS policy).

Ask each candidate about (3) and (4) together with affiliation and ORCID.
People who do not meet the criteria are thanked in the Acknowledgements and can
become authors of later papers. AI agents and bots are never authors; they go in
the AI usage disclosure.

## Candidates

| Candidate | Contribution | History so far (as of 2026-11-18) |
| --- | --- | --- |
| Hiroshi Shinaoka | All repositories; overall design (corresponding) | since Feb 2026 |
| Jin-Guo Liu | Initial design with H.S. (tensor4all-meta); CUDA performance fixes | initial design (early 2026); yao-rs uses tenferro |
| Satoshi Terasaki | Benchmark infrastructure (tenferro-benchmark), strided, tcontract, colmat | since early 2026; mvmc-rs uses tenferro |
| Ryo Watanabe | CpuEngine, strided, tcontract, threadteam | since May 2026 |
| Lukas Devos | tcontract contraction engine (from his Rust prototype), Julia wrapper | tcontract commits Aug 2026; earlier Rust prototype. Confirm continued involvement |
| Martin Mikkelsen | colmat LAPACK numerical validation suite and numerical fixes; tlinalg | Julia libraries earlier; colmat/tlinalg/tenferro Oct–Nov 2026 |
| Yusheng Zhao | CUDA SVD driver selection (SvdOptions::driver, Xgesvdp), cuBLAS fixes | omeinsum-rs Jul 2026, tenferro Sep 2026 (issues Jul–Sep). Confirm continued involvement |
| Ning-Yuan Chen | tcontract-benchmark (qcbench, EPYC 9575F campaigns) | since Nov 11, 2026; reaches two months by mid-January if it continues |
| Guo Chen | CPU kernel collaboration; direction of benchmark work (write the concrete contribution) | collaboration starting; needs two months of actual contribution by submission |

Not authors: faer authors and contributors (cite faer); bots and AI agents.
Candidates for the tensor4all-rs paper (C): Ken Inayoshi, Lingrui Cheng, Samuel Badr.

To collect from each co-author: consent, affiliation, ORCID.
