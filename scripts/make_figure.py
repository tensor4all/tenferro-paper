"""Build paper/figure_benchmark.png from the markdown tables under data/.

Both panels show wall time relative to tenferro-rs trace mode (value 1 means
same speed, above 1 means slower than tenferro trace). Sources are the latest
published tenferro-benchmark reports copied verbatim into data/.
"""
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "paper" / "figure_benchmark.png"

CELL = re.compile(r"\*?\*?([0-9.]+)")


def parse_table(path, header_prefix="| Instance"):
    rows = {}
    header = None
    for line in path.read_text().splitlines():
        if line.startswith(header_prefix):
            header = [h.strip() for h in line.strip("|").split("|")]
            continue
        if header and line.startswith("|") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != len(header):
                continue
            name = cells[0].strip("`")
            vals = {}
            for h, c in zip(header[1:], cells[1:]):
                m = CELL.match(c)
                vals[h] = float(m.group(1)) if m else np.nan
            rows[name] = vals
        elif header and not line.startswith("|"):
            header = None
    return rows


def short(name):
    name = re.sub(r"^(bin_|str_|lm_|gm_|nary_)", "", name)
    name = name.replace("batch_likelihood_", "lm_").replace("tensornetwork_permutation_", "tn_perm_")
    return name[:34]


# Panel (a): mac CPU einsum, opt_flops.
cpu = parse_table(DATA / "mac-cpu_einsum_opt_flops_20260812.md")
cpu_cols = {
    "tenferro-rs eager mode (ms)": "tenferro eager",
    "PyTorch Python (ms)": "PyTorch 2.12 (Accelerate)",
    "JAX Python (XLA CPU dot) (ms)": "JAX 0.10 (XLA CPU)",
}
cpu_ref = "tenferro-rs trace mode (ms)"

# Panel (b): NVIDIA GPU, dense + einsum + tensornetwork + AD (large 512 rows).
gpu = {}
for f in ["nvidia-gpu_dense_20260822.md", "nvidia-gpu_einsum_20260822.md", "nvidia-gpu_tensornetwork_20260822.md"]:
    gpu.update(parse_table(DATA / f, header_prefix="| Problem"))
ad = parse_table(DATA / "nvidia-gpu_linalg_jvp_vjp_20260822.md", header_prefix="| suite")
# parse_table keyed by 'suite' column; rebuild keyed by benchmark+shape for large 512.
ad_rows = {}
for line in (DATA / "nvidia-gpu_linalg_jvp_vjp_20260822.md").read_text().splitlines():
    if line.startswith("| large"):
        c = [x.strip() for x in line.strip("|").split("|")]
        if "512" in c[3]:
            ad_rows[c[1].strip("`").replace("grad_sum_", "ad_")] = {
                "tenferro-rs CUDA trace": float(CELL.match(c[4]).group(1)),
                "PyTorch CUDA": float(CELL.match(c[5]).group(1)),
            }
gpu.update(ad_rows)
gpu_cols = {
    "tenferro-rs CUDA eager": "tenferro eager",
    "PyTorch CUDA": "PyTorch 2.12 CUDA",
}
gpu_ref = "tenferro-rs CUDA trace"

fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1.15, 1]})
colors = ["#7f7f7f", "#d62728", "#1f77b4"]

for ax, table, cols, ref, title in [
    (axes[0], cpu, cpu_cols, cpu_ref, "(a) CPU einsum suite, Apple M5 Max, 4 threads"),
    (axes[1], gpu, gpu_cols, gpu_ref, "(b) NVIDIA RTX 3060, f64 dense, einsum and AD"),
]:
    names = list(table)
    y = np.arange(len(names))
    n = len(cols)
    h = 0.8 / n
    for i, (col, label) in enumerate(cols.items()):
        rel = np.array([table[k].get(col, np.nan) / table[k][ref] for k in names])
        ax.barh(y + (i - (n - 1) / 2) * h, rel, height=h, label=label, color=colors[i if n == 3 else i * 2 % 3 if False else [0, 1][i] if n == 2 else i])
    ax.axvline(1.0, color="k", lw=1)
    ax.set_yticks(y)
    ax.set_yticklabels([short(k) for k in names], fontsize=8)
    ax.set_xscale("log")
    ax.set_xlabel("time / tenferro-rs trace mode time")
    ax.set_title(title, fontsize=10)
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3)
    ax.legend(fontsize=8, loc="lower right")

fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("wrote", OUT)
