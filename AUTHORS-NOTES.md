# Author list notes (updated 2026-11-26)

We want to give credit to the people who build the tenferro ecosystem. If you
contribute to tenferro-rs, its upstream crates, tenferro-sci-rs or
tenferro-examples, you can
become a co-author of the tenferro paper. See [How to apply](#how-to-apply).

## Authorship criteria

Planned submission: end of March 2027 (see [Submission plan](#submission-plan)),
so anyone who starts contributing by the end of January 2027 can still qualify. The lead developer
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
   (non-code contributions are accepted).
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
   the whole paper.
5. **Membership in the Matrix community.** Join the tenferro Matrix room,
   [#tenferro-tensor4all:matrix.org](https://matrix.to/#/#tenferro-tensor4all:matrix.org), in the tensor4all space, and take part in the
   discussion there. Design discussions and contributor coordination happen
   in this room. How to set up Matrix:
   <https://tensor4all.org/matrix>.

Ask each candidate about (3), (4) and (5) together with affiliation and ORCID.
People who are not listed as authors are thanked in the Acknowledgements and can
become authors of later papers. AI agents and bots are never authors; they go in
the AI usage disclosure.

## Submission plan

- **Journal: [SciPost Physics Codebases](https://scipost.org/SciPostPhysCodeb/about),
  submission at the end of March 2027.** If it is rejected, we revise using the
  public referee reports and submit to Computer Physics Communications (CPC),
  which asks for nearly the same material. SoftwareX (3000-word limit) and JOSS
  are kept as further fallbacks.
- **Scope: tenferro-rs only.** [tenferro-sci-rs](https://github.com/tensor4all/tenferro-sci-rs)
  is described as the dogfooding ground, still in development: a downstream
  library written against tenferro's public API only. The gaps it exposed in
  tenferro (control flow in traced programs, core operations, DCT/DST, the
  public API) and how they were fixed are evidence that the design is
  extensible. Claims about tenferro-sci-rs are limited to what exists at
  submission; it gets its own paper once it matures.
- **What the manuscript says: only what does not go stale.** The problem
  tenferro solves, the design decisions and why (eager and traced execution,
  extensions through ExtensionOp, the engine passed on every call, pure Rust,
  downstream code on the public API only), and how correctness is checked.
  API usage, feature and hardware tables stay in the documentation, README and
  tenferro-examples, linked from the paper. Benchmark numbers name the release
  tag they were measured on and come with scripts that reproduce them.
- **What Codebases requires** (acceptance criteria on the journal's About
  page): benchmarking tests, at least one example application presented in
  detail, high programming standards, the added value over existing software,
  a demonstrable need, and complete documentation for installing and running.
  The userguide and the code release each get a DOI; later code releases go
  through a short refereeing round, which suits a library that keeps
  changing. Referee reports are public.
- **Use of AI** ([SciPost Terms and Conditions](https://scipost.org/journals/journals_terms_and_conditions#GenAI),
  "Use of Generative Artificial Intelligence", added in March 2026):
  - The manuscript is written by the human authors. AI is used at most for
    text polishing and light editing; the rules say that use beyond that is
    likely impermissible.
  - AI use in writing the code (coding agents under human design, review and
    validation) is disclosed in detail in the Acknowledgements: which tools,
    how, and for what. The rules ask for that disclosure and forbid blanket
    delegation, so the disclosure describes how humans direct and check the
    work.
  - Where "light editing" ends is not defined. Before submission we ask the
    SciPost editorial office with a concrete description of our workflow, and
    keep the answer.
- **Format:** the current draft in `paper/` is in JOSS format and moves to the
  SciPost LaTeX template.

## Arguments for the manuscript

Points that answer "what does tenferro do that the alternatives do not". Each
needs evidence in the repository before it goes into the text.

- **One code base from a laptop to an HPC system.** tenferro builds with
  `cargo` alone. The libraries that only a site or a vendor can provide (MPI,
  HDF5, CUDA) are loaded at run time instead of linked at build time
  ([rsmpi-rt](https://github.com/tensor4all/rsmpi-rt) through MPItrampoline's
  MPIABI, [hdf5-rt](https://github.com/tensor4all/hdf5-rt) through dlopen). The
  same build runs on a laptop and on a cluster, where it uses the site's MPI and
  HDF5. Nothing is rebuilt per machine, and no MPI headers, C compiler or
  libclang are needed to build it.
- **It lives inside a Julia or Python process.** Because MPI and HDF5 are found
  at run time, tenferro can use the libraries that MPI.jl or mpi4py and HDF5.jl
  or h5py have already loaded, instead of bringing a second copy that conflicts
  with them. The MPI adapter never calls `MPI_Init` or `MPI_Finalize` and does
  not own communicators, so a host language can hand it the communicator it
  already uses. PyTorch and JAX bring their own runtime; ITensors and OMEinsum
  need the Julia runtime. tenferro is the one in this comparison that a Julia
  or Python code can call as an ordinary library and share MPI and HDF5 with.
- **Evidence we have now** (tenferro-rs main, 2026-11-26):
  - `tenferro-mpi` has a `runtime` feature (rsmpi-rt `mpi-rt-sys-backend`) with
    its own point-to-point test (`mpi_p2p_runtime`). It needs MPIwrapper built
    against the system MPI, so it runs locally only, not in hosted CI.
  - `tenferro-hdf5` round-trips files with h5py in a gated interoperability
    test; Tensor4all.jl calls HDF5 through the C API next to HDF5.jl.
- **Evidence still missing:** (tracked in
  [tenferro-rs#2735](https://github.com/tensor4all/tenferro-rs/issues/2735))
  - the same build run on a laptop and on at least one cluster with the site
    MPI, recorded with versions;
  - one Julia process that runs MPI.jl and tenferro on the same communicator,
    and the same for mpi4py;
  - a hosted or scheduled CI lane for the runtime MPI backend.
- rsmpi-rt is marked experimental and MPIwrapper is an extra build step on
  each site. The paper states both.

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
| Ning-Yuan Chen | tcontract-benchmark (qcbench, EPYC 9575F campaigns) | since Nov 11, 2026; reaches two months well before submission if it continues |
| Guo Chen | CPU kernel collaboration; direction of benchmark work (write the concrete contribution) | collaboration starting; needs an actual contribution by submission |
| Samuel Badr | tenferro FFT AD rules (rfft/irfft), deep reverse-mode graph fix; colmat QL/RQ, polar/QDWH, range-limit fixes; tenferro-examples nonlinear-pinn | tenferro stack since Nov 17, 2026 (tensor4all-rs since Jul 2026 does not count); reaches two months well before submission if it continues |
| Frank Ebel | tenferro `zeros`/`ones`/`full` constructors (PR open) | since Nov 18, 2026; reaches two months well before submission if it continues |
| Ken Inayoshi | Sustained real use of tenferro through tensor4all-rs with feedback: tenferro-rs issues #2563 (Hermitian matrix functions with Daleckii–Krein AD), #2170 (BufferPool slowdown), #2049 (complex pinv), #2599 (single-tensor stack/concatenate); upstream bugs found from tensor4all-rs: t4a-faer SVD/QR panics with several threads (tensor4all-rs#1008, #1014), slowdowns after the tenferro migration (#328, #336), einsum label permutation (#281), mixed-dtype SVD and einsum plan-cache thrashing (#890, #891). No tenferro code; his tensor4all-rs code does not count here | feedback on the tenferro stack since Mar 2026; tensor4all-rs since Jan 2026. Write the feedback contribution explicitly in Author contributions |

Not authors: faer authors and contributors (cite faer); bots and AI agents.
Candidates for the tensor4all-rs paper (C): Ken Inayoshi (also a candidate here, by feedback), Lingrui Cheng, Samuel Badr.

To collect from each co-author: consent, affiliation, ORCID.
