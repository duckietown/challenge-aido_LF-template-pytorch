
build:
	dt-build_utils-cli aido-container-build --use-branch daffy --ignore-dirty --ignore-untagged --push --buildx --platforms linux/amd64,linux/arm64




submit:
	dts challenges submit


submit-bea:
	dts challenges submit --impersonate 1639  --retire-same-label
