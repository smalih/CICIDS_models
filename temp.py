import os
import pandas as pd
import codecs

def _to_utf8(filename: str, encoding="latin1", blocksize=1048576):
    tmpfilename = filename + ".tmp"
    with codecs.open(filename, "r", encoding) as source:
        with codecs.open(tmpfilename, "w", "utf-8") as target:
            while True:
                contents = source.read(blocksize)
                if not contents:
                    break
                target.write(contents)

    # replace the original file
    os.rename(tmpfilename, filename)



file_name = os.path.join("dataset", "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv")
# Read dataset
df = pd.read_csv(file_name, skipinitialspace=True, on_bad_lines="skip")

# Show number of NaN rows
print("Removing {} rows that contains only NaN values...".format(df[df.isna().all(axis=1)].shape[0]))

# Remove NaN rows
df = df[~ df.isna().all(axis=1)]

def _renaming_class_label(df: pd.DataFrame):
    labels = {"Web Attack \x96 Brute Force": "Web Attack-Brute Force",
              "Web Attack \x96 XSS": "Web Attack-XSS",
              "Web Attack \x96 Sql Injection": "Web Attack-Sql Injection"}

    for old_label, new_label in labels.items():
        df.Label.replace(old_label, new_label, inplace=True)

# Renaming labels
_renaming_class_label(df)