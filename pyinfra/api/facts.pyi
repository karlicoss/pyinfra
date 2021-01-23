from typing import Any, Callable, Generic, Optional, Type, Union

FACTS: Any
FACT_LOCK: Any
SUDO_REGEX: str
SU_REGEXES: Any


def is_fact(name: str):
    ...


def get_fact_class(name: str):
    ...


def get_fact_names():
    ...


class FactMeta(type):
    def __init__(cls, name: str, bases: Any, attrs: dict) -> None:
        ...


class FactBase(Generic, metaclass=FactMeta):
    abstract: bool = ...
    shell_executable: Optional[Union[str, Callable]] = ...
    requires_command: Optional[Union[str, Callable]] = ...

    @staticmethod
    def default() -> Any:
        ...

    @staticmethod
    def process(output: list[str]) -> Any:
        ...

    def process_pipeline(self, args: Any, output: Any):
        ...


class ShortFactBase(metaclass=FactMeta):
    fact: Type[FactBase] = ...


def get_short_facts(state: Any, short_fact: Any, **kwargs: Any):
    ...


def get_facts(
    state: Any,
    name: Any,
    args: Optional[Any] = ...,
    ensure_hosts: Optional[Any] = ...,
    apply_failed_hosts: bool = ...,
):
    ...


def get_host_fact(state: Any, host: Any, name: Any):
    ...


def create_host_fact(
    state: Any,
    host: Any,
    name: Any,
    data: Any,
    args: Optional[Any] = ...,
) -> None:
    ...


def delete_host_fact(
    state: Any,
    host: Any,
    name: Any,
    args: Optional[Any] = ...,
) -> None:
    ...
