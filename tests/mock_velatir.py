"""Mock velatir module for testing when the real SDK is not available."""

from typing import Any, Optional
from enum import Enum


class ReviewTaskState(str, Enum):
    """Mock review task states."""

    PENDING = "pending"
    APPROVED = "approved"
    DENIED = "denied"
    REQUIRES_INTERVENTION = "requires_intervention"
    CHANGE_REQUESTED = "change_requested"


class VelatirResponse:
    """Mock Velatir API response."""

    def __init__(
        self,
        review_task_id: str,
        state: ReviewTaskState,
        requested_change: Optional[str] = None,
    ):
        self.review_task_id = review_task_id
        self.state = state
        self.requested_change = requested_change

    @property
    def is_approved(self) -> bool:
        return self.state == ReviewTaskState.APPROVED

    @property
    def is_denied(self) -> bool:
        return self.state == ReviewTaskState.DENIED

    @property
    def is_pending(self) -> bool:
        return self.state == ReviewTaskState.PENDING

    @property
    def is_change_requested(self) -> bool:
        return self.state == ReviewTaskState.CHANGE_REQUESTED

    @property
    def requires_intervention(self) -> bool:
        return self.state == ReviewTaskState.REQUIRES_INTERVENTION

    @property
    def is_rejected(self) -> bool:
        return self.state in (ReviewTaskState.DENIED, ReviewTaskState.CHANGE_REQUESTED)


class TraceResponse:
    """Mock Trace API response."""

    def __init__(
        self,
        trace_id: str,
        status: str = "approved",
        processed_async: bool = False,
        review_task_id: Optional[str] = None,
        requested_change: Optional[str] = None,
    ):
        self.trace_id = trace_id
        self.status = status
        self.processed_async = processed_async
        self.review_task_id = review_task_id
        self.requested_change = requested_change

    @property
    def is_approved(self) -> bool:
        return self.status == "approved"

    @property
    def is_rejected(self) -> bool:
        return self.status in ("denied", "rejected", "change_requested")


class VelatirTimeoutError(Exception):
    """Mock timeout error."""

    pass


class Client:
    """Mock Velatir SDK client."""

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: float = 10.0,
        max_retries: int = 3,
        retry_backoff: float = 0.5,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff

    async def create_review_task(
        self,
        function_name: str,
        args: dict[str, Any],
        doc: Optional[str] = None,
        llm_explanation: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        parent_review_task_id: Optional[str] = None,
    ) -> VelatirResponse:
        """Mock create review task."""
        return VelatirResponse(
            review_task_id="mock-task-id",
            state=ReviewTaskState.APPROVED,
        )

    async def get_review_task_status(self, review_task_id: str) -> VelatirResponse:
        """Mock get review task status."""
        return VelatirResponse(
            review_task_id=review_task_id,
            state=ReviewTaskState.APPROVED,
        )

    async def wait_for_approval(
        self,
        review_task_id: str,
        polling_interval: float = 5.0,
        max_attempts: Optional[int] = None,
    ) -> VelatirResponse:
        """Mock wait for approval."""
        return VelatirResponse(
            review_task_id=review_task_id,
            state=ReviewTaskState.APPROVED,
        )

    def create_review_task_sync(
        self,
        function_name: str,
        args: dict[str, Any],
        doc: Optional[str] = None,
        llm_explanation: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        parent_review_task_id: Optional[str] = None,
    ) -> VelatirResponse:
        """Mock create review task sync."""
        return VelatirResponse(
            review_task_id="mock-task-id",
            state=ReviewTaskState.APPROVED,
        )

    def get_review_task_status_sync(self, review_task_id: str) -> VelatirResponse:
        """Mock get review task status sync."""
        return VelatirResponse(
            review_task_id=review_task_id,
            state=ReviewTaskState.APPROVED,
        )

    def wait_for_approval_sync(
        self,
        review_task_id: str,
        polling_interval: float = 5.0,
        max_attempts: Optional[int] = None,
    ) -> VelatirResponse:
        """Mock wait for approval sync."""
        return VelatirResponse(
            review_task_id=review_task_id,
            state=ReviewTaskState.APPROVED,
        )

    async def create_trace(
        self,
        function_name: str,
        args: dict[str, Any],
        tool_calls: Optional[list[str]] = None,
        doc: Optional[str] = None,
        llm_explanation: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> TraceResponse:
        """Mock create trace."""
        return TraceResponse(
            trace_id="mock-trace-id",
            status="approved",
            processed_async=False,
        )

    def create_trace_sync(
        self,
        function_name: str,
        args: dict[str, Any],
        tool_calls: Optional[list[str]] = None,
        doc: Optional[str] = None,
        llm_explanation: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> TraceResponse:
        """Mock create trace sync."""
        return TraceResponse(
            trace_id="mock-trace-id",
            status="approved",
            processed_async=False,
        )

    async def evaluate_and_wait(
        self,
        function_name: str,
        args: dict[str, Any],
        tool_calls: Optional[list[str]] = None,
        doc: Optional[str] = None,
        llm_explanation: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        polling_interval: float = 5.0,
        max_attempts: Optional[int] = None,
    ) -> TraceResponse:
        """Mock evaluate and wait."""
        return TraceResponse(
            trace_id="mock-trace-id",
            status="approved",
            processed_async=False,
        )

    def evaluate_and_wait_sync(
        self,
        function_name: str,
        args: dict[str, Any],
        tool_calls: Optional[list[str]] = None,
        doc: Optional[str] = None,
        llm_explanation: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        polling_interval: float = 5.0,
        max_attempts: Optional[int] = None,
    ) -> TraceResponse:
        """Mock evaluate and wait sync."""
        return TraceResponse(
            trace_id="mock-trace-id",
            status="approved",
            processed_async=False,
        )

    async def close(self) -> None:
        """Mock close."""
        pass
