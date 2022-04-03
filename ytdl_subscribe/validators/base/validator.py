from typing import Any
from typing import Optional
from typing import Type

from ytdl_subscribe.validators.exceptions import ValidationException


class Validator:
    # The python type that value should be
    expected_value_type: Type = object

    # When raising an error, call the type this value instead of its python name
    expected_value_type_name: Optional[str] = None

    def __validate_value(self):
        """
        Returns
        -------
        Validation exception to raise when the value's type is not the expected type
        """
        if not isinstance(self._value, self.expected_value_type):
            expected_value_type_name = self.expected_value_type_name or str(
                self.expected_value_type
            )
            raise self._validation_exception(
                error_message=f"should be of type {expected_value_type_name}."
            )

    def __init__(self, name: str, value: Any):
        self.name = name
        self._value = value

        self.__validate_value()

    @property
    def value(self) -> object:
        return self._value

    def _validation_exception(self, error_message: str):
        prefix = f"Validation error in {self.name}: "
        return ValidationException(f"{prefix}{error_message}")