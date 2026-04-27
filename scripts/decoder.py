#!/usr/bin/env python3
"""
Lab 5 — Reverse Engineering Android : OWASP UnCrackable Level 2
Script de décodage du secret extrait de libfoo.so via Ghidra.

Les valeurs hexadécimales ci-dessous proviennent des variables locales
identifiées dans la fonction JNI Java_sg_vantagepoint_uncrackable2_CodeCheck_bar.
Sur architecture x86, ces valeurs sont stockées en little-endian.
"""

def decode_secret():
    print("=" * 55)
    print("  Lab 5 — UnCrackable Level 2 — Décodeur de secret")
    print("=" * 55)

    # --- Étape 1 : Valeurs extraites de Ghidra (little-endian) ---
    hex_values_le = {
        "local_30": 0x6e616854,
        "local_2c": 0x6620736b,
        "local_28": 0x6120726f,
        "local_24": 0x74206c6c,
        "local_20": 0x6568,
        "local_1e": 0x73696620,
        "local_1a": 0x68,
    }

    print("\n[*] Valeurs hexadécimales extraites de Ghidra (little-endian) :")
    for var, val in hex_values_le.items():
        print(f"    {var} = {hex(val)}")

    # --- Étape 2 : Conversion little-endian -> octets dans l'ordre mémoire ---
    # Sur x86, un int 4 octets 0xAABBCCDD est stocké DD CC BB AA en mémoire.
    # struct.pack('<I', val) donne les octets dans l'ordre mémoire (little-endian).
    import struct

    raw_bytes = b""
    sizes = {
        "local_30": 4, "local_2c": 4, "local_28": 4, "local_24": 4,
        "local_20": 2, "local_1e": 4, "local_1a": 1,
    }
    fmt_map = {1: '<B', 2: '<H', 4: '<I'}

    for var, val in hex_values_le.items():
        size = sizes[var]
        raw_bytes += struct.pack(fmt_map[size], val)

    print(f"\n[*] Séquence hexadécimale reconstituée :")
    print(f"    {raw_bytes.hex()}")

    # --- Étape 3 : Décodage ASCII ---
    secret = raw_bytes.decode("ascii")
    print(f"\n[+] Secret décodé : '{secret}'")
    print(f"[*] Longueur      : {len(secret)} caractères (attendu : 23 / 0x17)")

    # --- Vérification ---
    assert len(secret) == 0x17, "Erreur : la longueur ne correspond pas à 0x17 !"
    print("\n[✓] Validation : longueur correcte (0x17 = 23)")
    print("=" * 55)
    return secret


if __name__ == "__main__":
    decode_secret()
