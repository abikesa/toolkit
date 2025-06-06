#!/bin/bash
# move-from-list.sh

src="/Users/apollo/Documents/ukuzula/kitabo/ensi"
dest="/Users/apollo/Documents/internship/ukb/dolce"
list="/Users/apollo/Documents/internship/list.txt"

cd "$src" || { echo "❌ Could not cd into $src"; exit 1; }

while IFS= read -r pattern; do
  # Expand the glob pattern *in the shell*
  eval matches=( $pattern )

  if [[ ${#matches[@]} -eq 0 ]]; then
    echo "⚠️  No match for pattern: $pattern"
  else
    for item in "${matches[@]}"; do
      echo "🚚 Moving $item → $dest/"
      mv "$item" "$dest/"
    done
  fi
done < "$list"
