#!/bin/bash

# creation des dossiers
if ! [ -d "WDGAS/BU" ]; then
  mkdir WDGAS/BU
fi

if ! [ -d "WDGAS/IT" ]; then
  mkdir WDGAS/IT
fi

if ! [ -d "WDGAS/RH" ]; then
  mkdir WDGAS/RH
fi



# deplacer les fichiers
for fichier in WDGAS/*; do
    if [ -f "$fichier" ]; then
        if echo "$fichier" | grep -q "HR"; then
            mv "$fichier" WDGAS/RH
        fi
        if echo "$fichier" | grep -q "IT"; then
            mv "$fichier" WDGAS/IT
        fi
        if echo "$fichier" | grep -q "BU"; then
            mv "$fichier" WDGAS/BU
        fi
    fi
done 


#renommer les fichiers

for fichier in WDGAS/RH/*.data; do
    if [ -f "$fichier" ]; then
        base=$(basename "$fichier" .data)
        base=$(echo "$base" | sed 's/[0-9]//g')
        base=$(echo "$base" | sed 's/_*\(RH\|HR\)_*//g')
        base=$(echo "$base" | sed 's/-//g')
        f="WDGAS/RH/${base}.data"
        mv "$fichier" "$f"
    fi
done

for fichier in WDGAS/IT/*.data; do
    if [ -f "$fichier" ]; then
        base=$(basename "$fichier" .data)
        base=$(echo "$base" | sed 's/[0-9]//g')
        base=$(echo "$base" | sed 's/_*\(IT\)_*//g')
        base=$(echo "$base" | sed 's/-//g')
        f="WDGAS/IT/${base}.data"
        mv "$fichier" "$f"
    fi
done

for fichier in WDGAS/BU/*.data; do
    if [ -f "$fichier" ]; then
        base=$(basename "$fichier" .data)
        base=$(echo "$base" | sed 's/[0-9]//g')
        base=$(echo "$base" | sed 's/_*\(BU\)_*//g')
        base=$(echo "$base" | sed 's/-//g')
        f="WDGAS/BU/${base}.data"
        mv "$fichier" "$f"
    fi
done