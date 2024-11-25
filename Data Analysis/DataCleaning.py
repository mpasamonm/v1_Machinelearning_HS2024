import pandas as pd

# Read Bewegungen 1.1 (WMDT) - only PIC movements, otherwise the file would be too big (50gb+)
df_bewegungen = pd.read_csv(
    '../Data/bewegungen.csv',
    dtype={
        "MOVNUM": "int64",
        "WORNUM": "int64",
        "STATUS": "category",
        "MOVTYP": "category",
        "MOVKEY": "category",
        "SRC_ITEM": "int64",
        "SRC_LOT": "string",
        "SRC_QACODE": "category",
        "DST_LOT": "string",
        "DST_QACODE": "category",
        "SRC_WA": "category",
        "DST_WA": "category",
        "SRC_X": "float64",
        "SRC_Y": "float64",
        "SRC_Z": "float64",
        "DST_X": "float64",
        "DST_Y": "float64",
        "DST_Z": "float64",
        "REQQTY": "float64",
        "CONQTY": "float64",
        "INCNUM": "int64",
        "LISNUM": "int64",
        "USERID": "string",
    },
    parse_dates=["CRTDAT", "TRNDAT"]
)

# Read Warenausgang Kopf 7a
df_wa_kopf = pd.read_csv(
    '../Data/wa_kopf.csv',
    dtype={
        "OUTNUM": "int64",
        "DOCNUM": "int64",
        "ORDNUM": "int64",
        "STATUS": "category",
        "CUSNUM": "int64",
        "SHPTYP": "category",
        "TOUR": "int64",
    },
    parse_dates=["ORDDAT", "DLVDAT", "CRTDAT", "TRNDAT"]
)

# Read Warenausgang Positionen 7b
df_wa_positionen = pd.read_csv(
    '../Data/wa_positionen.csv',
    dtype={
        "OUTNUM": "int64",
        "OUTLIN": "int64",
        "STATUS": "category",
        "ITEM": "int64",
        "LOT": "string",
        "QACODE": "category",
        "ORDQTY": "float64",
        "RELQTY": "float64",
        "FNDQTY": "float64",
        "CONQTY": "float64",
        "SHPQTY": "float64",
        "USERID": "string",
    },
    parse_dates=["CRTDAT", "TRNDAT"]
)

# Read Listen 8
df_listen = pd.read_csv(
    '../Data/listen.csv',
    dtype={
        "LISNUM": "int64",
        "SUMLIS": "int64",
        "STATUS": "category",
        "PRIO": "int64",
        "PZ": "category",
        "RELNUM": "int64",
        "CUSNUM": "int64",
        "DSPADR": "string",
    },
    parse_dates=["CRTDAT", "TRNDAT"]
)

# Read Artikelbestand 5
df_artikelbestand = pd.read_csv(
    '../Data/artikelbestand.csv',
    dtype={
        "OBJNUM": "int64",
        "STATUS": "category",
        "LOCNUM": "int64",
        "PICLCK": "bool",
        "STTLCK": "bool",
        "ITEM": "int64",
        "LOT": "string",
        "INQTY": "float64",
        "OUTQTY": "float64",
        "AVLQTY": "float64",
        "CONQTY": "float64",
    },
    parse_dates=["CRTDAT", "TRNDAT"]
)

# Read Lagerplatz 3
df_lagerplatz = pd.read_csv(
    '../Data/lagerplatz.csv',
    dtype={
        "OBJNUM": "int64",
        "WH": "category",
        "WA": "category",
        "X": "float64",
        "Y": "float64",
        "Z": "float64",
        "STATUS": "category",
        "PUTPRI": "int64",
        "PICPRI": "int64",
    },
    parse_dates=["CRTDAT", "TRNDAT"]
)
