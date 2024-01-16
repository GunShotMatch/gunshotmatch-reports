#! /usr/bin/env python3

# this package
from gunshotmatch_reports.peaks import build_peak_report, load_project

filename = "Western Double A.gsmp"
print(f"Opening project {filename!r}")
project = load_project(filename)
print(f"Generating peak report for {project.name} ({len(project.consolidated_peaks)} peaks)")

pdf_filename = build_peak_report(project, "peak_report_demo.pdf")
print(f"Report written to {pdf_filename!r}")
