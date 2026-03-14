from __future__ import annotations

from onboardai.models import ChecklistTask, OnboardingState
from onboardai.state import mark_completed
from onboardai.ui.dashboard import build_dashboard_props


def test_mark_completed_updates_latest_screenshot_artifact():
    state = OnboardingState(
        task_plan=[
            ChecklistTask(
                task_id="C-07",
                title="Accept GitHub organization invite",
                category="Access",
                source_section="Common Checklist",
            )
        ]
    )
    mark_completed(
        state,
        "C-07",
        "agent",
        "Opened GitHub page",
        artifacts=["/tmp/github-page.png"],
    )
    assert state.dashboard_state.latest_screenshot_artifact == "/tmp/github-page.png"


def test_dashboard_props_include_progress_and_next_action():
    state = OnboardingState()
    state.dashboard_state.progress = {"total": 1, "completed": 0, "pending": 1, "in_progress": 0, "blocked": 0, "skipped": 0}
    state.dashboard_state.next_action = "Complete task C-07"
    state.dashboard_state.persona_label = "Riya Sharma - Backend / Intern"
    state.dashboard_state.completion_ready = False
    props = build_dashboard_props(state)
    assert props["progress"]["total"] == 1
    assert props["nextAction"] == "Complete task C-07"
    assert props["personaLabel"] == "Riya Sharma - Backend / Intern"
