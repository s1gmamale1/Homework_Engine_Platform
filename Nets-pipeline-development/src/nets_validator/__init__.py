"""NETS Post-Hoc Validator (§14).

Separate process from the main pipeline. Reads phase_outputs rows that
haven't been validated yet, calls a cheaper cross-family model (Haiku
or Gemini Flash), and writes results to validation_results.

Never blocks the main pipeline. Flagged items go to a review queue.
"""

__version__ = "0.1.0"
