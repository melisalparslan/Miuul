rule all:
    input: "output/tRNA_scan_result.txt",
            "output/G_intestinalis.tRNA"

rule tRNAscan:
    input: "resource/G_intestinalis.fasta"
    output: "output/tRNA_scan_result.txt"
    shell: "bash scripts/tRNAscan.sh {input} {output}"

rule tRNAscan_stats:
    input:
            genome= "resource/G_intestinalis.fasta"
    output:
            stats = "output/G_intestinalis.stats",
            tRNA = "output/G_intestinalis.tRNA"
    params:
            threads=2
    conda:
            "env/env.yaml"
    script:
            "scripts/tRNAscan_stats.py"

