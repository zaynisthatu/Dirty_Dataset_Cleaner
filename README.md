# The Data Cleaner 🧹

## Project Description / پروجیکٹ کی تفصیل

**English:** The Data Cleaner is a powerful Python script designed to automatically clean and preprocess CSV data files. It handles common data cleaning tasks such as removing currency symbols, cleaning numeric data, handling missing values, removing duplicates, and standardizing text formats.

**Urdu:** ڈیٹا کلینر ایک طاقتور Python script ہے جو CSV data files کو خودکار طور پر صاف اور preprocess کرنے کے لیے بنایا گیا ہے۔ یہ عام data cleaning کے کام جیسے currency symbols ہٹانا، numeric data صاف کرنا، missing values handle کرنا، duplicates ہٹانا، اور text formats کو standardize کرنا وغیرہ کرتا ہے۔

## Features / خصوصیات

✅ **Currency Cleaning** - Remove $ symbols and convert to numbers / $ symbols ہٹا کر numbers میں convert کرنا  
✅ **Numeric Data Cleaning** - Clean and standardize numeric columns / Numeric columns کو صاف اور standardize کرنا  
✅ **Footnote Removal** - Remove footnote symbols (†, ‡, *, []) / Footnote symbols (†, ‡, *, []) ہٹانا  
✅ **Missing Value Handling** - Multiple strategies for missing data / Missing data کے لیے مختلف strategies  
✅ **Duplicate Removal** - Remove duplicate rows / Duplicate rows ہٹانا  
✅ **Text Standardization** - Clean and standardize text columns / Text columns کو صاف اور standardize کرنا  
✅ **Detailed Reports** - Generate cleaning reports / Cleaning reports بنانا  

## Installation / انسٹالیشن

### Requirements / ضروری چیزیں

```bash
pip install pandas numpy
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

## How to Run / کیسے چلائیں

### Basic Usage / بنیادی استعمال

**English:** To clean a CSV file with default settings:

**Urdu:** Default settings کے ساتھ CSV file صاف کرنے کے لیے:

```bash
python data_cleaner.py your_data.csv
```

### Advanced Usage / اعلیٰ درجے کا استعمال

**English:** With custom output file and missing value strategy:

**Urdu:** Custom output file اور missing value strategy کے ساتھ:

```bash
python data_cleaner.py input_data.csv -o cleaned_data.csv -m fill_mean -r
```

### Command Line Options / Command Line کے اختیارات

| Option | Description (English) | تفصیل (Urdu) |
|--------|----------------------|--------------|
| `input_file` | Path to input CSV file | Input CSV file کا path |
| `-o, --output` | Path to output CSV file | Output CSV file کا path |
| `-m, --missing` | Missing value strategy | Missing values کی strategy |
| `-r, --report` | Generate detailed report | تفصیلی report بنائیں |

### Missing Value Strategies / Missing Values کی Strategies

| Strategy | Description (English) | تفصیل (Urdu) |
|----------|----------------------|--------------|
| `drop` | Remove rows with missing values | Missing values والی rows ہٹا دیں |
| `fill_mean` | Fill with column mean | Column کے mean سے fill کریں |
| `fill_median` | Fill with column median | Column کے median سے fill کریں |
| `fill_mode` | Fill with most frequent value | سب سے زیادہ آنے والی value سے fill کریں |

## Example Usage / استعمال کی مثال

### Sample Data / نمونہ ڈیٹا

Your CSV file might look like this:
```csv
Rank,Peak,Actual gross,Artist,Tour title,Year(s),Shows
1,1,"$780,000,000",Taylor Swift,The Eras Tour †,2023–2024,56
2,1,"$579,800,000",Beyoncé,Renaissance World Tour,2023,56
```

### Running the Script / Script چلانا

```bash
# Basic cleaning / بنیادی صفائی
python data_cleaner.py concert_data.csv

# With custom output and report / Custom output اور report کے ساتھ
python data_cleaner.py concert_data.csv -o clean_concerts.csv -r

# Fill missing values with mean / Missing values کو mean سے fill کریں
python data_cleaner.py concert_data.csv -m fill_mean -r
```

### Expected Output / متوقع نتیجہ

After cleaning, your data will be:
- Currency symbols removed / Currency symbols ہٹائے گئے
- Footnotes cleaned / Footnotes صاف کیے گئے
- Missing values handled / Missing values handle کیے گئے
- Duplicates removed / Duplicates ہٹائے گئے
- Text standardized / Text standardize کیا گیا

## What the Script Does / Script کیا کرتا ہے

### 1. Data Loading / ڈیٹا لوڈنگ
- Loads CSV file into pandas DataFrame / CSV file کو pandas DataFrame میں load کرتا ہے
- Shows original data dimensions / اصل data کے dimensions دکھاتا ہے

### 2. Currency Cleaning / Currency کی صفائی
- Removes $ symbols and quotes / $ symbols اور quotes ہٹاتا ہے
- Converts to numeric format / Numeric format میں convert کرتا ہے

### 3. Numeric Data Cleaning / Numeric Data کی صفائی
- Removes non-numeric characters / Non-numeric characters ہٹاتا ہے
- Converts text numbers to actual numbers / Text numbers کو actual numbers میں بدلتا ہے

### 4. Footnote Removal / Footnote ہٹانا
- Removes symbols like †, ‡, *, [] / †, ‡, *, [] جیسے symbols ہٹاتا ہے
- Cleans reference markers / Reference markers صاف کرتا ہے

### 5. Missing Values / Missing Values
- Handles empty cells based on chosen strategy / خالی cells کو منتخب strategy کے مطابق handle کرتا ہے

### 6. Duplicate Removal / Duplicate ہٹانا
- Finds and removes duplicate rows / Duplicate rows تلاش کر کے ہٹاتا ہے

### 7. Text Standardization / Text Standardization
- Removes extra spaces / اضافی spaces ہٹاتا ہے
- Standardizes formatting / Formatting standardize کرتا ہے

## Output / نتیجہ

The script will create:
1. **Cleaned CSV file** - Your data with all cleaning applied / تمام صفائی کے ساتھ آپ کا data
2. **Console Report** - Summary of cleaning operations / Cleaning operations کا خلاصہ
3. **Detailed Report** (with -r flag) - Complete analysis / مکمل analysis

## File Structure / File کی ساخت

```
project/
├── data_cleaner.py          # Main script / اصل script
├── README.md               # This file / یہ file
├── requirements.txt        # Dependencies / Dependencies
├── input_data.csv         # Your input data / آپ کا input data
└── input_data_cleaned.csv # Cleaned output / صاف شدہ نتیجہ
```

## Error Handling / خرابیوں کا حل

The script handles common errors:
- File not found / File نہیں ملی
- Invalid CSV format / غلط CSV format
- Memory issues with large files / بڑی files کے ساتھ memory کے مسائل

## Tips for Best Results / بہترین نتائج کے لیے تجاویز

**English:**
- Backup your original data before cleaning
- Use appropriate missing value strategy for your dataset
- Generate reports to understand what was cleaned
- Test on small sample first for large datasets

**Urdu:**
- صفائی سے پہلے اپنے اصل data کا backup لیں
- اپنے dataset کے لیے مناسب missing value strategy استعمال کریں  
- یہ سمجھنے کے لیے reports generate کریں کہ کیا صاف کیا گیا
- بڑے datasets کے لیے پہلے چھوٹے sample پر test کریں

## Support / مدد

If you encounter any issues:
- Check that your CSV file is properly formatted
- Ensure all required packages are installed
- Try with a smaller sample of your data first

اگر آپ کو کوئی مسئلہ پیش آئے:
- چیک کریں کہ آپ کی CSV file صحیح format میں ہے
- یقینی بنائیں کہ تمام ضروری packages install ہیں
- پہلے اپنے data کے چھوٹے sample کے ساتھ try کریں

## License / لائسنس

This project is open source and available under the MIT License.

یہ project open source ہے اور MIT License کے تحت دستیاب ہے۔