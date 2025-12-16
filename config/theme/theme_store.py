import json
from pathlib import Path


class ThemeStore:
    _path = Path(__file__).parent / "theme.json"

    _default = {
        "current_theme": "dark"
    }

    @classmethod
    def load(cls) -> dict:
        if cls._path.exists():
            try:
                return json.loads(cls._path.read_text(encoding="utf-8"))
            except Exception:
                return cls._default.copy()
        return cls._default.copy()

    @classmethod
    def save(cls, data: dict):
        cls._path.parent.mkdir(parents=True, exist_ok=True)
        cls._path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8"
        )
