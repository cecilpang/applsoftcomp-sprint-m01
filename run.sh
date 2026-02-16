#!/bin/bash
uv sync
uv run python workflow/process_raw_data.py
uv run python workflow/merge_data.py
uv run python workflow/visualization.py