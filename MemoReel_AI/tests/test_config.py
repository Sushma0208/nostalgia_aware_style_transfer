import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from memoreel.config import load_project_config


class ConfigTests(unittest.TestCase):
    def test_loads_project_metadata(self):
        root = Path(__file__).resolve().parents[1]
        config = load_project_config(root / "pyproject.toml")
        self.assertEqual(config.name, "memoreel-ai")
        self.assertTrue(config.python_requires.startswith(">="))

    def test_rejects_missing_project_table(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "pyproject.toml"
            path.write_text("[tool.other]\nvalue=1\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_project_config(path)


if __name__ == "__main__":
    unittest.main()
