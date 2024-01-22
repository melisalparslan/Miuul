import snakemake
from snakemake.shell import shell

fasta = snakemake.input.fasta
out = snakemake.output

shell(f"""orthofinder -f {fasta} -og""")

import subprocess

# BLAST'ın tam yolu
blast_path = "/usr/local/ncbi/blast/bin/blastn"

# BLAST'ı subprocess ile çağırma
result = subprocess.run([blast_path, '-help'], capture_output=True, text=True)
print(result.stdout)

