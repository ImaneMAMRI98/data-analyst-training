#!/bin/bash

for fichier in WDGAS/RH; do
    echo "$fichier" | tr "_" "\n"

    #mv "$fichier" "${fichier/\d/ }"
done