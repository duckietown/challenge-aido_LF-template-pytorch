"""Template placeholder for user-provided training code."""

TRAINING_NOT_AVAILABLE_MESSAGE = (
    "The PyTorch template does not ship training code. "
    "Start from a baseline repository or add your own trainer."
)


def main() -> None:
    """Explain that the template does not ship training code."""
    message = TRAINING_NOT_AVAILABLE_MESSAGE
    raise SystemExit(message)


if __name__ == "__main__":
    main()
