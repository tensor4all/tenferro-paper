#!/bin/sh
# Body word count excluding YAML front matter, the table, and figure captions.
awk 'BEGIN{fm=0} /^---$/{fm++; next} fm>=2' "$(dirname "$0")/../paper/paper.md" | grep -v '^|' | grep -v '^!\[' | wc -w
