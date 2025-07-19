#!/usr/bin/env python3
"""
The Data Cleaner
A Python script for cleaning and preprocessing CSV data files.
"""

import pandas as pd
import numpy as np
import re
import argparse
import sys
from pathlib import Path

class DataCleaner:
    def __init__(self, input_file, output_file=None):
        """
        Initialize the Data Cleaner
        
        Args:
            input_file (str): Path to input CSV file
            output_file (str): Path to output CSV file (optional)
        """
        self.input_file = input_file
        self.output_file = output_file or self._generate_output_filename()
        self.df = None
        self.original_shape = None
        self.cleaned_shape = None
        
    def _generate_output_filename(self):
        """Generate output filename based on input filename"""
        path = Path(self.input_file)
        return str(path.parent / f"{path.stem}_cleaned{path.suffix}")
    
    def load_data(self):
        """Load CSV data into DataFrame"""
        try:
            self.df = pd.read_csv(self.input_file)
            self.original_shape = self.df.shape
            print(f"✓ Data loaded successfully: {self.original_shape[0]} rows, {self.original_shape[1]} columns")
            return True
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            return False
    
    def clean_currency_columns(self):
        """Clean currency columns by removing symbols and converting to numeric"""
        print("\n--- Cleaning Currency Columns ---")
        currency_pattern = r'[\$,"]'
        
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Check if column contains currency values
                sample_values = self.df[col].dropna().head(10).astype(str)
                if any('$' in str(val) for val in sample_values):
                    print(f"Cleaning currency column: {col}")
                    # Remove currency symbols and convert to numeric
                    self.df[col] = self.df[col].astype(str).str.replace(currency_pattern, '', regex=True)
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
    
    def clean_numeric_columns(self):
        """Clean numeric columns by removing non-numeric characters"""
        print("\n--- Cleaning Numeric Columns ---")
        
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Try to convert to numeric after cleaning
                original_col = self.df[col].copy()
                cleaned_col = self.df[col].astype(str).str.replace(r'[^\d.]', '', regex=True)
                
                # Check if conversion to numeric is successful for most values
                try:
                    numeric_col = pd.to_numeric(cleaned_col, errors='coerce')
                    non_null_ratio = numeric_col.notna().sum() / len(numeric_col)
                    
                    if non_null_ratio > 0.7:  # If 70% of values can be converted
                        print(f"Converting to numeric: {col}")
                        self.df[col] = numeric_col
                except:
                    continue
    
    def remove_footnote_symbols(self):
        """Remove footnote symbols and references from text columns"""
        print("\n--- Removing Footnote Symbols ---")
        footnote_pattern = r'[\[\]†‡*]|\[[^\]]*\]'
        
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                original_values = self.df[col].dropna().head(5).tolist()
                self.df[col] = self.df[col].astype(str).str.replace(footnote_pattern, '', regex=True)
                self.df[col] = self.df[col].str.strip()
                
                # Check if any changes were made
                cleaned_values = self.df[col].dropna().head(5).tolist()
                if original_values != cleaned_values:
                    print(f"Cleaned footnotes in column: {col}")
    
    def handle_missing_values(self, strategy='drop'):
        """
        Handle missing values in the dataset
        
        Args:
            strategy (str): 'drop', 'fill_mean', 'fill_median', 'fill_mode'
        """
        print(f"\n--- Handling Missing Values (Strategy: {strategy}) ---")
        
        missing_before = self.df.isnull().sum().sum()
        print(f"Missing values before cleaning: {missing_before}")
        
        if strategy == 'drop':
            # Drop rows with any missing values
            self.df = self.df.dropna()
        elif strategy == 'fill_mean':
            # Fill numeric columns with mean
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
        elif strategy == 'fill_median':
            # Fill numeric columns with median
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        elif strategy == 'fill_mode':
            # Fill all columns with mode
            for col in self.df.columns:
                mode_value = self.df[col].mode()
                if len(mode_value) > 0:
                    self.df[col] = self.df[col].fillna(mode_value[0])
        
        missing_after = self.df.isnull().sum().sum()
        print(f"Missing values after cleaning: {missing_after}")
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        print("\n--- Removing Duplicates ---")
        
        duplicates_before = self.df.duplicated().sum()
        print(f"Duplicate rows before cleaning: {duplicates_before}")
        
        self.df = self.df.drop_duplicates()
        
        duplicates_after = self.df.duplicated().sum()
        print(f"Duplicate rows after cleaning: {duplicates_after}")
    
    def standardize_text(self):
        """Standardize text columns (strip whitespace, fix casing)"""
        print("\n--- Standardizing Text ---")
        
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Strip whitespace and standardize
                self.df[col] = self.df[col].astype(str).str.strip()
                # Remove extra whitespace
                self.df[col] = self.df[col].str.replace(r'\s+', ' ', regex=True)
                print(f"Standardized text in column: {col}")
    
    def clean_all(self, missing_strategy='drop'):
        """
        Perform all cleaning operations
        
        Args:
            missing_strategy (str): Strategy for handling missing values
        """
        print("🧹 Starting Data Cleaning Process...")
        print("=" * 50)
        
        if not self.load_data():
            return False
        
        # Perform all cleaning operations
        self.clean_currency_columns()
        self.clean_numeric_columns()
        self.remove_footnote_symbols()
        self.standardize_text()
        self.remove_duplicates()
        self.handle_missing_values(missing_strategy)
        
        self.cleaned_shape = self.df.shape
        
        print("\n" + "=" * 50)
        print("🎉 Data Cleaning Complete!")
        print(f"Original shape: {self.original_shape}")
        print(f"Cleaned shape: {self.cleaned_shape}")
        
        return True
    
    def save_cleaned_data(self):
        """Save cleaned data to CSV file"""
        try:
            self.df.to_csv(self.output_file, index=False)
            print(f"✓ Cleaned data saved to: {self.output_file}")
            return True
        except Exception as e:
            print(f"✗ Error saving data: {e}")
            return False
    
    def generate_report(self):
        """Generate a cleaning report"""
        print("\n📊 DATA CLEANING REPORT")
        print("=" * 50)
        
        print("\nDataset Overview:")
        print(f"  • Original rows: {self.original_shape[0]}")
        print(f"  • Original columns: {self.original_shape[1]}")
        print(f"  • Cleaned rows: {self.cleaned_shape[0]}")
        print(f"  • Cleaned columns: {self.cleaned_shape[1]}")
        
        print("\nColumn Information:")
        for col in self.df.columns:
            dtype = self.df[col].dtype
            non_null = self.df[col].notna().sum()
            print(f"  • {col}: {dtype} ({non_null} non-null values)")
        
        print("\nData Types:")
        print(self.df.dtypes.value_counts())


def main():
    """Main function to run the data cleaner"""
    parser = argparse.ArgumentParser(description="Clean and preprocess CSV data files")
    parser.add_argument("input_file", help="Path to input CSV file")
    parser.add_argument("-o", "--output", help="Path to output CSV file")
    parser.add_argument("-m", "--missing", choices=['drop', 'fill_mean', 'fill_median', 'fill_mode'], 
                       default='drop', help="Strategy for handling missing values")
    parser.add_argument("-r", "--report", action="store_true", help="Generate cleaning report")
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not Path(args.input_file).exists():
        print(f"✗ Error: Input file '{args.input_file}' not found")
        sys.exit(1)
    
    # Create data cleaner instance
    cleaner = DataCleaner(args.input_file, args.output)
    
    # Clean the data
    if cleaner.clean_all(args.missing):
        cleaner.save_cleaned_data()
        
        if args.report:
            cleaner.generate_report()
    else:
        print("✗ Data cleaning failed")
        sys.exit(1)


if __name__ == "__main__":
    main()