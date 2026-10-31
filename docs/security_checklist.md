# Security checklist before publishing

- [ ] `.env` is ignored and not tracked.
- [ ] No Hugging Face token, API key, password, OTP, or private key is present.
- [ ] No adapter weights, model weights, checkpoints, or caches are staged.
- [ ] No real customer tickets, employee data, internal IPs, hostnames, or topology.
- [ ] Sample dataset is synthetic and labeled as such.
- [ ] Notebook outputs and screenshots are reviewed for secrets and private data.
- [ ] Model and adapter redistribution terms have been reviewed.
- [ ] `git diff --check` passes.
- [ ] Every staged file is reviewed with `git diff --cached`.
- [ ] Repository URL and visibility are correct.

If a secret was committed, revoke/rotate it. Removing it in a later commit is not
sufficient; history cleanup may also be required.
