"""Perplexity provider profile.

Perplexity offers a multi-provider Agent API exposed via an OpenAI
SDK-compatible alias at ``POST /v1/responses`` (the same backend as the
native ``POST /v1/agent`` endpoint). Through this single endpoint users
can route to frontier models from multiple providers — e.g.
``openai/gpt-5.4``, ``anthropic/claude-sonnet-4-6`` — in ``provider/model``
format. Configure with ``PERPLEXITY_API_KEY`` (``PPLX_API_KEY`` accepted
as a fallback).

Get an API key at https://www.perplexity.ai/account/api/keys.

Why ``api_mode="codex_responses"`` + ``base_url=".../v1"``: the multi-
provider Agent API lives at ``POST /v1/responses``, not at
``/chat/completions`` (which is Sonar-only and would reject the
``provider/model`` strings in ``fallback_models``). The
``codex_responses`` mode is Hermes' name for the OpenAI Responses API
transport — same dispatch path used by ``xai`` (``api.x.ai/v1``) and
``openai-codex``. See ``hermes_cli/runtime_provider.py``
``_detect_api_mode_for_url`` for the URL-based selection.
"""

from providers import register_provider
from providers.base import ProviderProfile

perplexity = ProviderProfile(
    name="perplexity",
    aliases=("pplx",),
    api_mode="codex_responses",
    env_vars=("PERPLEXITY_API_KEY", "PPLX_API_KEY"),
    display_name="Perplexity",
    description="Perplexity Agent API — OpenAI-compatible multi-model gateway",
    signup_url="https://www.perplexity.ai/account/api/keys",
    # Perplexity Agent API is a model-agnostic gateway — these are
    # representative frontier models exposed through it. The live picker
    # fetches the full catalog via /models.
    fallback_models=(
        "openai/gpt-5.4",
        "anthropic/claude-sonnet-4-6",
        "google/gemini-3-1-pro",
    ),
    base_url="https://api.perplexity.ai/v1",
)

register_provider(perplexity)
