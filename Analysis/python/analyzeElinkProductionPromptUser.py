# analyzeElinkProductionPromptUser.py
#
# Developed by the KU CMS group.
#
# -------------------------- #
# Author:   Caleb Smith
# Date:     January 16, 2026
# -------------------------- #

from analyzeElinkProduction import analyzeElinkProductionDataMultiStage

def main():
    # Prompt user for required inputs; remove leading and trailing whitespace
    start_date  = input("Please provide a start date (YYYY-MM-DD): ").strip()
    end_date    = input("Please provide an end date (YYYY-MM-DD): ").strip()
    input_file  = input("Please provide an input file (csv): ").strip()

    # Directory to save plots
    plot_dir    = "elink_production_plots"

    # Analyze e-link production data
    analyzeElinkProductionDataMultiStage(start_date, end_date, input_file, plot_dir)

if __name__ == "__main__":
    main()
