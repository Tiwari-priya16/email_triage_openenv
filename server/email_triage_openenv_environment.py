# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Email Triage Openenv Environment Implementation.

A simple test environment that echoes back messages sent to it.
Perfect for testing HTTP server infrastructure.
"""

from uuid import uuid4

from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

try:
    from ..models import EmailTriageOpenenvAction, EmailTriageOpenenvObservation
except ImportError:
    from models import EmailTriageOpenenvAction, EmailTriageOpenenvObservation


class EmailTriageOpenenvEnvironment(Environment):
    """
    A simple echo environment that echoes back messages.

    This environment is designed for testing the HTTP server infrastructure.
    It maintains minimal state and simply echoes back whatever message it receives.

    Example:
        >>> env = EmailTriageOpenenvEnvironment()
        >>> obs = env.reset()
        >>> print(obs.echoed_message)  # "Email Triage Openenv environment ready!"
        >>>
        >>> obs = env.step(EmailTriageOpenenvAction(message="Hello"))
        >>> print(obs.echoed_message)  # "Hello"
        >>> print(obs.message_length)  # 5
    """

    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        """Initialize the email_triage_openenv environment."""
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count = 0

    def reset(self) -> EmailTriageOpenenvObservation:
        """
        Reset the environment.

        Returns:
            EmailTriageOpenenvObservation with a ready message
        """
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count += 1

        return EmailTriageOpenenvObservation(
            echoed_message="Email Triage Openenv environment ready!",
            message_length=0,
            done=False,
            reward=0.0,
        )

    def step(self, action: EmailTriageOpenenvAction) -> EmailTriageOpenenvObservation:  # type: ignore[override]
        """
        Execute a step in the environment by echoing the message.
        """
        self._state.step_count += 1

        message = action.message
        length = len(message)

        reward = length * 0.1

        return EmailTriageOpenenvObservation(
            echoed_message=message,
            message_length=length,
            done=False,
            reward=reward,
            metadata={"original_message": message, "step": self._state.step_count},
        )

    @property
    def state(self) -> State:
        """Get the current environment state."""
        return self._state
