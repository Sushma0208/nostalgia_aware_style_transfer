# Initial architecture (proposal)

```text
Flutter client (later) -> FastAPI job API -> job queue -> generation adapter
                                    |                |-> mock adapter first
                                    |                |-> GPU adapter only after audit
                                    -> metadata DB / private object store
```

The API should return job IDs and status rather than block on long inference. Original and generated media use separate object keys; deletion must cover both and associated metadata. The mobile app never receives storage credentials or model-provider secrets. Research feedback references candidate IDs and recorded settings. The ranking service remains distinct from image rendering, allowing preference experiments without retraining or conflating the diffusion model.

Phase 1 creates only config/schema foundations; no server or mobile app is implemented.
