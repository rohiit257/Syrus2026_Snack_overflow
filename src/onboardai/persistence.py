from __future__ import annotations

import json
from pathlib import Path

from onboardai.models import OnboardingState


class SessionStore:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def path_for(self, session_id: str) -> Path:
        return self.root / f"{session_id}.json"

    def save(self, state: OnboardingState) -> Path | None:
        if not state.session_id:
            return None
        path = self.path_for(state.session_id)
        path.write_text(state.model_dump_json(indent=2), encoding="utf-8")
        return path

    def load(self, session_id: str) -> OnboardingState | None:
        path = self.path_for(session_id)
        if not path.exists():
            return None
        return OnboardingState.model_validate(json.loads(path.read_text(encoding="utf-8")))
