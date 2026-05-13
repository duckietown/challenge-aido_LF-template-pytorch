# LF PyTorch Template

This repository is the ente PyTorch submission template for `aido-LF-sim-validation`.
The Docker image installs all Python dependencies from `dependencies.txt`. That file uses PyPI for published packages such as `zuper-typing-z6` and `aido-protocols`, and it pulls the maintained Duckietown repos from GitHub instead of copying from local source trees.

The template keeps the PyTorch runtime in `solution/`. The active entrypoint is `solution/main.py`, preprocessing lives in `solution/wrappers.py`, action conversion lives in `solution/action_wrapper.py`, and the default placeholder policy lives in `solution/policy.py`. Optional model assets live under `models/`. That directory now uses a shared sentinel file instead of fake checkpoint names when no real weights are tracked. The repository also carries a `training/` scaffold so its tree matches the PyTorch baselines, but those training files remain placeholders and do not provide a runnable trainer. The RL and DAgger baselines are still the repositories that add an MVP on top of this template. At evaluation time the runner provides `VEHICLE_NAME`, `DUCKIEMATRIX_ENGINE_HOSTNAME`, `DUCKIEMATRIX_ENGINE_PORT`, and `DTSHELL_SHM_PATH` for the live Duckiematrix session.

Like the other LF ML repositories, this template now also carries a top-level `config.yaml` so the Duckietown exercise tooling sees the same basic metadata across templates and baselines. It does not need ROS-specific paths such as `launchers/` or `assets/` because the runtime is a direct Python entrypoint rather than a ROS graph.

The template still includes a minimal runnable `solution/` because a submission template needs to build and run end-to-end against the evaluator while leaving the actual policy behavior for users and baselines to implement.

The default Docker image copies `solution/`, `training/`, and `models/` into `/workspace`. `dependencies.txt` is intentionally kept as the user-editable place to add extra Python packages and now also defines the template's Duckietown Git dependencies.

The default `PytorchTemplateAgent.predict_action()` implementation returns zero velocity and zero steering. Replace that hook with your own model inference or policy logic when turning the template into a real submission.
