# 🧠 MEMORY ARCHITECTURE SPECIFICATION (Sprint 3)
> **Author:** Gemini (Memory Lead)
> **Status:** DRAFT v1.0
> **Integration:** L.E.A. v2.1 + Janus Gateway

---

## 1. Philosophie : Le "Tri-Store" Hybride
Pour respecter la trinité 3-6-9, la mémoire de LEA ne sera pas un simple fichier texte. Elle sera divisée en trois couches de profondeur.

### A. Surface Memory (Short-Term / RAM)
* **Technologie :** `context_window` (Liste Python temporaire).
* **Rôle :** Se souvenir de la conversation *actuelle* (les 10 derniers échanges).
* **Durée de vie :** Session active uniquement.
* **Latence :** Immédiate (< 10ms).

### B. Episodic Memory (Logs / Human Readable)
* **Technologie :** Fichiers `.md` (Markdown) dans `02_HUMAIN/analog_records/`.
* **Rôle :** Journal de bord narratif. Chaque jour est un fichier (ex: `2026-01-29.md`).
* **Contenu :** Date, Heure, Entropie, Interlocuteur, Contenu.
* **Usage :** Permet à l'Opérateur (humain) de relire l'histoire.

### C. Semantic Memory (Deep Storage / Machine)
* **Technologie :** `memory_index.json` + `Vector Embeddings` (Futur Sprint).
* **Rôle :** Stockage des *Concepts* et des *Faits*.
* **Structure :**
    ```json
    {
      "concepts": {
        "tesla": {"weight": 0.9, "associations": ["369", "energy", "vibration"]},
        "operator": {"trust_level": 5, "last_seen": "2026-01-29"}
      }
    }
    ```

---

## 2. Protocole de Sécurité (Janus Integration)
Conformément aux directives de Claude (Protocol 04) :
1.  **Write-Validation :** Aucune écriture "Long Terme" ne se fait sans vérifier l'intégrité des données (pas de code malveillant).
2.  **Immutabilité :** Les logs passés ne peuvent pas être effacés par LEA, seulement archivés.

---

## 3. Implementation Plan (Sprint 3)
1.  **Phase 1 :** Création du `MemoryManager` capable d'écrire des logs Markdown propres (La base).
2.  **Phase 2 :** Capacité pour LEA de *lire* ces logs pour se souvenir de ce qu'on a dit hier.
3.  **Phase 3 :** Consolidation nocturne (LEA résume la journée pour en tirer des leçons).

---
*End of Spec. Approved by M.O.C.*