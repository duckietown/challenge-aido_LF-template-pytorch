# LF PyTorch Template

This repository is the ente PyTorch submission template for `aido-LF-sim-validation`.
The Docker image installs the local ente source contexts for `zuper-typing-z6`, `duckietown-messages`, `duckietown-sdk`, `aido-protocols`, and `gym-duckiematrix`, and it copies embedded maps from the local `dt-duckiematrix` context into the runtime image.

The template keeps the PyTorch runtime in `solution/`. The active entrypoint is `solution/main.py`, preprocessing lives in `solution/wrappers.py`, action conversion lives in `solution/action_wrapper.py`, and the default placeholder policy lives in `solution/policy.py`. Optional model assets live under `models/`. That directory now uses a shared sentinel file instead of fake checkpoint names when no real weights are tracked. The repository also carries a `training/` scaffold so its tree matches the PyTorch baselines, but those training files remain placeholders and do not provide a runnable trainer. The RL and DAgger baselines are still the repositories that add an MVP on top of this template. At evaluation time the runner provides `VEHICLE_NAME`, `DUCKIEMATRIX_ENGINE_HOSTNAME`, `DUCKIEMATRIX_ENGINE_PORT`, and `DTSHELL_SHM_PATH` for the live Duckiematrix session.

The template still includes a minimal runnable `solution/` because a submission template needs to build and run end-to-end against the evaluator while leaving the actual policy behavior for users and baselines to implement.

The default Docker image now copies only the runtime scaffold under `solution/`. If your submission adds assets under `models/`, update the Dockerfile explicitly to copy that path into the image.

The default `PytorchTemplateAgent.predict_action()` implementation returns zero velocity and zero steering. Replace that hook with your own model inference or policy logic when turning the template into a real submission.
