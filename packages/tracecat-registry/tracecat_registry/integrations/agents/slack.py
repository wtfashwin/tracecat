from typing import Annotated, Any

from typing_extensions import Doc

from tracecat_registry import registry
from tracecat_registry.fields import ActionType, AgentModel, ModelSelection, TextArea
from tracecat_registry.integrations.slack_sdk import slack_secret


@registry.register(
    default_title="AI Slackbot",
    description="Agentic AI Slackbot with tool calling capabilities.",
    display_group="AI",
    doc_url="https://docs.slack.dev/reference/events/app_mention/",
    namespace="ai",
    secrets=[slack_secret],
    deprecated="Use the 'ai.agent' action instead.",
)
async def slackbot(
    event: Annotated[
        dict[str, Any] | None,
        Doc(
            "Slack app mention event or interaction payload (e.g. for button clicks) passed in via Tracecat webhook TRIGGER. If None, the agent will send a message to the channel."
        ),
    ],
    prompt: Annotated[
        str,
        Doc("Initial prompt for the agent. Used when no event is provided."),
        TextArea(),
    ],
    instructions: Annotated[
        str,
        Doc(
            "Instructions for the agent across proactive, app mention, and interaction flows."
        ),
        TextArea(),
    ],
    channel_id: Annotated[str, Doc("Channel ID to send the initial message to.")],
    model: Annotated[
        ModelSelection,
        Doc("Model to use. Pick from the list of models enabled for this workspace."),
        AgentModel(),
    ],
    actions: Annotated[
        list[str] | None,
        Doc(
            "Actions to include in the agent on top of the default Slack actions (e.g. 'tools.slack.post_message')."
        ),
        ActionType(multiple=True),
    ] = None,
    model_settings: Annotated[
        dict[str, Any] | None, Doc("Model settings for the agent.")
    ] = None,
    retries: Annotated[int, Doc("Number of retries for the agent.")] = 6,
    limit_messages: Annotated[
        int, Doc("Max number of messages to look back in the conversation.")
    ] = 5,
) -> Any:
    raise NotImplementedError("Use the 'ai.agent' action instead.")
