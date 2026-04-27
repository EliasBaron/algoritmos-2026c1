#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Uso: $0 <extension> <timeout_segundos>"
    exit 1
fi

EXT=$1
T_LIMIT=$2

g++ -O3 -std=c++11 maxclique.cpp -o maxclique

echo "Triple-Benchmark (Extensión: *.$EXT | Límite NX: ${T_LIMIT}s)"
echo "-------------------------------------------------------------------------------------------"
printf "%-30s | %-9s | %-9s | %-9s | %-4s | %-5s\n" "Archivo" "C++" "Py-Orig" "NetX" "Res" "Stat"
echo "-------------------------------------------------------------------------------------------"

for test_file in *."$EXT"; do
    [ -e "$test_file" ] || continue

    # 1. C++
    S_CPP=$(date +%s%N)
    RES_CPP=$(./maxclique < "$test_file" | tr -d '\r' | xargs)
    E_CPP=$(date +%s%N)
    T_CPP=$(( (E_CPP - S_CPP) / 1000000 ))

    # 2. Python
    S_PY=$(date +%s%N)
    RES_PY=$(python3 maxclique.py < "$test_file" | tr -d '\r' | xargs)
    E_PY=$(date +%s%N)
    T_PY=$(( (E_PY - S_PY) / 1000000 ))

    # 3. NetworkX con lógica de Timeout robusta
    S_NX=$(date +%s%N)

    # Ejecutamos en una subshell para aislar el timeout y el código de salida
    RES_NX=$(timeout "$T_LIMIT" python3 -c "
import networkx as nx
import sys
try:
    with open('$test_file', 'r') as f:
        line = f.readline().split()
        if not line: sys.exit(0)
        n, m = map(int, line)
        G = nx.Graph()
        G.add_nodes_from(range(n))
        for l in f:
            p = l.split()
            if len(p) >= 2: G.add_edge(int(p[0]), int(p[1]))
        from networkx.algorithms.clique import graph_clique_number
        print(graph_clique_number(G))
except Exception:
    sys.exit(1) # Error interno, no TLE
" 2>/dev/null)

    EXIT_CODE=$?
    E_NX=$(date +%s%N)
    T_NX=$(( (E_NX - S_NX) / 1000000 ))

    # 4. Determinar Status
    DISPLAY_NX="${T_NX}ms"
    RES_NX=$(echo "$RES_NX" | tr -d '\r' | xargs)

    if [ $EXIT_CODE -eq 124 ]; then
        # CASO TLE: NetworkX fue matado por el sistema
        STATUS="\e[33m[TLE]\e[0m"
        DISPLAY_NX=">${T_LIMIT}s"
        # Verificamos si al menos tu C++ y tu Python coinciden
        if [ "$RES_CPP" != "$RES_PY" ]; then
            STATUS="\e[31m[ERR]\e[0m"
        fi
    elif [ $EXIT_CODE -ne 0 ] || [ -z "$RES_NX" ]; then
        # CASO ERROR: Python falló internamente
        STATUS="\e[31m[ERR]\e[0m"
        DISPLAY_NX="ERROR"
    elif [ "$RES_CPP" != "$RES_PY" ] || [ "$RES_CPP" != "$RES_NX" ]; then
        # CASO DISCORDANCIA: Los resultados no coinciden
        STATUS="\e[31m[ERR]\e[0m"
    else
        # CASO TODO OK
        STATUS="\e[32m[OK]\e[0m"
    fi

    printf "%-30s | %7sms | %7sms | %9s | %4s | %b\n" "$test_file" "$T_CPP" "$T_PY" "$DISPLAY_NX" "$RES_CPP" "$STATUS"
done

echo "-------------------------------------------------------------------------------------------"
