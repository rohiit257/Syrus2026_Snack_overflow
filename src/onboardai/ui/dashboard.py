from __future__ import annotations

from onboardai.models import OnboardingState


def build_dashboard_props(state: OnboardingState) -> dict:
    return {
        "streamUrl": state.dashboard_state.stream_url,
        "personaLabel": state.dashboard_state.persona_label,
        "currentTask": state.dashboard_state.current_task,
        "latestStatus": state.dashboard_state.latest_status,
        "latestScreenshotArtifact": state.dashboard_state.latest_screenshot_artifact,
        "nextAction": state.dashboard_state.next_action,
        "completionReady": state.dashboard_state.completion_ready,
        "progress": state.dashboard_state.progress,
        "health": state.dashboard_state.health,
        "items": [
            {
                "taskId": item.task_id,
                "title": item.title,
                "status": item.status.value,
                "detail": item.detail,
                "timestamp": item.timestamp,
            }
            for item in state.dashboard_state.items
        ],
    }
