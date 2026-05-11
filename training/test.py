"""Template placeholder for user-provided evaluation code."""

EVALUATION_NOT_AVAILABLE_MESSAGE = (
    "The PyTorch template does not ship evaluation code. "
    "Start from a baseline repository or add your own test entrypoint."
)


def main() -> None:
    """Explain that the template does not ship evaluation code."""
    message = EVALUATION_NOT_AVAILABLE_MESSAGE
    raise SystemExit(message)


if __name__ == "__main__":
    main()
