# Author list notes (updated 2026-11-19)

We want to give credit to the people who build the tenferro ecosystem. If you
contribute to tenferro-rs, its upstream crates, tenferro-sci-rs or
tenferro-examples, you can
become a co-author of the tenferro paper. See [How to apply](#how-to-apply).

## Authorship criteria

Planned submission: end of January 2027, so anyone who starts contributing by
the end of November 2026 can still qualify. The lead developer
(H. Shinaoka) makes the final decision on who is listed as an author, using
the following criteria.

1. **Contribution history of about two months or more** by the submission date.
   Two months is a guideline, not a hard cutoff: a significant contribution
   made in less than two months is also considered. A single small PR or issue
   is not enough.
2. **Substantial contribution** to tenferro-rs, its upstream crates (strided,
   tcontract, tlinalg, threadteam, colmat/t4a-faer, t4a-gemm, t4a-gpu-backend,
   benchmark repositories), [tenferro-sci-rs](https://github.com/tensor4all/tenferro-sci-rs)
   (the SciPy-like layer on tenferro, where tenferro-fft is also moving) or
   tenferro-examples: code, design, benchmarks, validation, or sustained
   real use of the tenferro ecosystem with feedback. Design direction counts
   (JOSS accepts non-code contributions).
   Contributions to tenferro-examples count only when the example is also
   compared in performance against Python (PyTorch/JAX) and Julia
   implementations, and what it finds is fed back to tenferro-rs as issues or
   PRs.
   Contributions to tensor4all-rs do not count here; they belong to the
   tensor4all-rs paper.
3. **Commitment for about the next year** to put effort into developing the
   tenferro ecosystem and spreading it: using it in their own projects,
   feedback, teaching, talks, or bringing in users and groups.
4. **Consent and accountability.** Agree to be listed and to be accountable for
   the whole paper (JOSS policy).
5. **Membership in the Matrix community.** Join the tenferro Matrix room,
   [#tenferro-tensor4all:matrix.org](https://matrix.to/#/#tenferro-tensor4all:matrix.org), in the tensor4all space, and take part in the
   discussion there. Design discussions and contributor coordination happen
   in this room. How to set up Matrix:
   <https://tensor4all.org/matrix>.

Ask each candidate about (3), (4) and (5) together with affiliation and ORCID.
People who are not listed as authors are thanked in the Acknowledgements and can
become authors of later papers. AI agents and bots are never authors; they go in
the AI usage disclosure.

## Future papers: when the contributor base grows

For this paper (tenferro v1.0) every contributor who meets the criteria above
is a named author, and each author's contribution is written out in Author
contributions. That works while the candidates number in the tens.

When contributors number in the many tens or hundreds, a later paper (for
example tenferro v2.0, or one covering tenferro-sci-rs as well) will follow the
model of the SciPy 1.0 paper ([arXiv:1907.10121](https://arxiv.org/abs/1907.10121);
Nature Methods 17, 261 (2020)), which uses three tiers:

1. **Named authors, chosen by role**: those who lead the design, the main
   maintainers, and those who write the manuscript.
2. **A consortium** ("tenferro Contributors") listing by name everyone who
   meets the criteria above; the criteria then decide consortium membership.
3. **Acknowledgements** for everyone else who contributed, down to a single
   issue or comment.

Before using a consortium, check that the target journal accepts one.

## How to apply

If you want to be an author, open a pull request to this repository that adds
or updates your row in the [Candidates](#candidates) table. In the pull request
description, state clearly:

- **What you have contributed so far**: the repositories, and links to your
  PRs, issues, commits, benchmarks, or design discussions. Say what each one
  achieved (for example a new feature, a performance gain with numbers, a bug
  fixed, a validation suite), not only that it was merged.
- **Since when** you have been contributing, and what you plan to contribute
  before submission.
- **Commitment** (criterion 3): how you intend to use, develop, or spread the
  tenferro ecosystem over about the next year.
- **Consent** (criterion 4), your affiliation, and your ORCID.
- **Your Matrix ID** (criterion 5), for example `@name:matrix.org`.

The lead developer reviews the pull request and decides. Opening one is welcome
at any time before submission; you can update it as your contribution grows.

## Candidates

| Candidate | Contribution | History so far (as of 2026-11-18) |
| --- | --- | --- |
| Hiroshi Shinaoka | All repositories; overall design (corresponding) | since Feb 2026 |
| Jin-Guo Liu | Initial design with H.S. (tensor4all-meta); CUDA performance fixes | initial design (early 2026); yao-rs uses tenferro |
| Satoshi Terasaki | Benchmark infrastructure (tenferro-benchmark), strided, tcontract, colmat | since early 2026; mvmc-rs uses tenferro |
| Ryo Watanabe | CpuEngine, strided, tcontract, threadteam | since May 2026 |
| Lukas Devos | tcontract contraction engine (from his Rust prototype), Julia wrapper | tcontract commits Aug 2026; earlier Rust prototype. Confirm continued involvement |
| Martin Mikkelsen | colmat LAPACK numerical validation suite and numerical fixes; tlinalg; tenferro-examples (nqs-rbm, kdv-pinn) | Julia libraries earlier; colmat/tlinalg/tenferro Oct–Nov 2026 |
| Yusheng Zhao | CUDA SVD driver selection (SvdOptions::driver, Xgesvdp), cuBLAS fixes | omeinsum-rs Jul 2026, tenferro Sep 2026 (issues Jul–Sep). Confirm continued involvement |
| Ning-Yuan Chen | tcontract-benchmark (qcbench, EPYC 9575F campaigns) | since Nov 11, 2026; reaches two months by the end of January if it continues |
| Guo Chen | CPU kernel collaboration; direction of benchmark work (write the concrete contribution) | collaboration starting; needs an actual contribution by submission |
| Samuel Badr | tenferro FFT AD rules (rfft/irfft), deep reverse-mode graph fix; colmat QL/RQ, polar/QDWH, range-limit fixes; tenferro-examples nonlinear-pinn | tenferro stack since Nov 17, 2026 (tensor4all-rs since Jul 2026 does not count); reaches two months by the end of January if it continues |
| Frank Ebel | tenferro `zeros`/`ones`/`full` constructors (PR open) | since Nov 18, 2026; reaches two months by the end of January if it continues |
| Ken Inayoshi | Sustained real use of tenferro through tensor4all-rs with feedback: tenferro-rs issues #2563 (Hermitian matrix functions with Daleckii–Krein AD), #2170 (BufferPool slowdown), #2049 (complex pinv), #2599 (single-tensor stack/concatenate); upstream bugs found from tensor4all-rs: t4a-faer SVD/QR panics with several threads (tensor4all-rs#1008, #1014), slowdowns after the tenferro migration (#328, #336), einsum label permutation (#281), mixed-dtype SVD and einsum plan-cache thrashing (#890, #891). No tenferro code; his tensor4all-rs code does not count here | feedback on the tenferro stack since Mar 2026; tensor4all-rs since Jan 2026. Write the feedback contribution explicitly in Author contributions |

Not authors: faer authors and contributors (cite faer); bots and AI agents.
Candidates for the tensor4all-rs paper (C): Ken Inayoshi (also a candidate here, by feedback), Lingrui Cheng, Samuel Badr.

To collect from each co-author: consent, affiliation, ORCID.
