#! /usr/bin/env python

import numpy as np
import pandas as pd
import pytest
  

def main():
	print(f"Numpy version: {np.__version__}")
	print(f"Pandas version: {pd.__version__}")
	print(f"Pytest version: {pytest.__version__}")


if __name__ == "__main__":
    main()
