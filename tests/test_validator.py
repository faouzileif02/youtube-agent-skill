import importlib.util
import tempfile
import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "tools" / "validate_skills.py")
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)

VALID = '''---
name: yt-demo
description: >-
  Use this skill when the user wants a deterministic YouTube demonstration workflow with explicit activation behavior.
---
# yt-demo
## Mission
A narrow mission for testing.
## Required inputs
- Topic.
## Optional inputs
- Context.
## Workflow
1. Validate the topic.\n2. Produce the result.\n3. Check it.
## Output contract
Return one structured result.
## Quality gates
- Never fabricate analytics or results; identify assumptions and unsupported claims before returning the output.
## Interoperability
Run after another relevant skill when needed.
## Failure handling
If a required input is missing, identify it and return only the supported partial result without guessing.
## Community contribution rule
Preserve the mission and output contract when changing this skill.
'''

class ValidatorTests(unittest.TestCase):
    def test_valid_skill_passes_core_checks(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "yt-demo" / "SKILL.md"
            p.parent.mkdir()
            p.write_text(VALID, encoding="utf-8")
            r = validator.validate_skill(p)
            self.assertFalse(r.errors)
            self.assertGreaterEqual(r.score, 85)

    def test_folder_name_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "yt-wrong" / "SKILL.md"
            p.parent.mkdir()
            p.write_text(VALID, encoding="utf-8")
            r = validator.validate_skill(p)
            self.assertTrue(any("folder name" in e for e in r.errors))

if __name__ == "__main__":
    unittest.main()
