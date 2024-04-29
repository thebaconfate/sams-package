from pathlib import Path
import polars as pl


def load_csv(dir: Path, filename: str) -> pl.LazyFrame:
    """reads data from a csv file and returns a DataFrame object"""
    return pl.read_csv(f"{dir.as_posix()}/{filename}").lazy()


def save_csv(lf: pl.LazyFrame, dir: Path, filename: str) -> None:
    """saves a DataFrame object to a csv file"""
    if dir.exists() is False:
        dir.mkdir()
    lf.collect().write_csv(f"{dir.as_posix()}/{filename}")