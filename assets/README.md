# assets/

Ce dossier contient toutes les captures d'écran du lab, numérotées dans l'ordre des étapes.

## Liste des captures attendues

| Fichier | Description |
|---|---|
| `01_adb_devices.png` | Terminal PowerShell — `adb devices` montrant `emulator-5554 device` |
| `02_adb_install.png` | Terminal PowerShell — `adb install` avec résultat `Success` |
| `03_jadx_overview.png` | JADX ouvert avec l'arborescence complète de l'APK |
| `04_jadx_manifest.png` | Fichier `AndroidManifest.xml` dans JADX (package + activité principale) |
| `05_jadx_mainactivity.png` | Code Java de `MainActivity` dans JADX (bloc static + méthode verify) |
| `06_jadx_codecheck.png` | Classe `CodeCheck` dans JADX — mot-clé `native` visible |
| `07a_7zip_apk_content.png` | APK ouvert dans 7-Zip — dossiers visibles (lib, res, etc.) |
| `07b_libfoo_extracted.png` | Dossier `lib/x86/` dans 7-Zip — fichier `libfoo.so` visible |
| `08_ghidra_import.png` | Ghidra — import de `libfoo.so` et analyse automatique en cours |
| `09_ghidra_jni_symbol.png` | Ghidra Symbol Tree — fonction `Java_sg_vantagepoint_uncrackable2_CodeCheck_bar` |
| `10_ghidra_pseudocode.png` | Ghidra Decompiler — pseudo-code C avec variables `local_30` à `local_1a` et `strncmp` |
| `11_python_decode.png` | Terminal Python — exécution du script affichant `Thanks for all the fish` |
| `12_success_emulator.png` | Émulateur Android — boîte de dialogue `Success! This is the correct secret.` |
