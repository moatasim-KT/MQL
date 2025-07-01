import pandas as pd


def excel_to_long_csv(excel_path, csv_path, sheet_name):
    # Read the Excel file
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Identify the id_vars and value_vars for melting
    id_vars = [
        "Deal ID",
        "Create Date",
        "Deal owner",
        "Deal Stage",
        "MRR",
        "EST MRR ($)",
        "Date entered current stage",
    ]
    value_vars = [col for col in df.columns if col not in id_vars]

    # Melt the DataFrame to transform it from wide to long format
    df_long = df.melt(
        id_vars=id_vars, value_vars=value_vars, var_name="Stage_Raw", value_name="Date"
    )

    # Drop rows where the date is missing
    df_long.dropna(subset=["Date"], inplace=True)

    # Extract the stage and status from the 'Stage_Raw' column
    df_long["Status"] = df_long["Stage_Raw"].apply(
        lambda x: "Entered" if "entered" in x else "Exited"
    )
    df_long["Stage"] = df_long["Stage_Raw"].str.extract(r"\"(.+)\"")

    # Drop the original 'Stage_Raw' column
    df_long.drop(columns=["Stage_Raw"], inplace=True)

    # Save the long format DataFrame to a CSV file
    df_long.to_csv(csv_path, index=False)


if __name__ == "__main__":
    excel_to_long_csv(
        excel_path="New MQLs Dataset.xlsx",
        csv_path="mql.csv",
        sheet_name="MQLs dataset - Maria",
    )
