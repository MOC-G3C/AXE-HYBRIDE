#!/bin/bash
# Quick diagnostic for AXE_HYBRIDE synchronization status [cite: 2026-01-26]

echo "🔍 DIAGNOSING RESONANCE ARCHIVE..."
echo "----------------------------------"

# Check last local commit
LAST_COMMIT=$(git log -1 --pretty=format:"%s (%cr)")
echo "Last Archive Entry: $LAST_COMMIT"

# Check file integrity [cite: 2026-01-26]
if [ -f "02Humain/ORACLE_MESSAGES.md" ]; then
    echo "✅ Oracle Stream: Online"
else
    echo "❌ Oracle Stream: Missing"
fi

if [ -f "01_SOFTWARE/Entropic-Zoo-Protocol/MUTATION_JOURNAL.md" ]; then
    echo "✅ Mutation Logs: Online"
else
    echo "❌ Mutation Logs: Missing"
fi

echo "----------------------------------"
echo "SYSTEM TIME: $(date)"