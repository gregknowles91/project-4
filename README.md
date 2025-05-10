# project-4
# Engine-to-Price Ratio Analysis
This module analyzes which car manufacturers and models offer the best
performance value for enthusiasts by calculating the engine size to price
ratio.
## Methodology
1. **Data Preprocessing**:
- Extracts engine size in cc from string descriptions
- Converts price strings to numeric values
- Calculates engine-to-price ratio
2. **Analysis Performed**:
- Brand-level comparison of engine-to-price ratios
- Model-level comparison of engine-to-price ratios

- Analysis by vehicle age
- Analysis by fuel type

3. **Key Visualizations**:
- Bar chart of top brands by engine-to-price ratio
- Bar chart of top models by engine-to-price ratio
- Scatter plot of price vs. engine size
- Comprehensive dashboard combining multiple analyses
## Key Findings
[Fill in your key findings after running the analysis]
## Usage



# Load and preprocess your data
df = pd.read_csv(used_cars.csv)
processed_df = preprocess_engine_data(df)
# Generate analyses
brand_ratios = generate_brand_analysis(processed_df)
model_ratios = generate_model_analysis(processed_df)
# Create visualizations
plot_top_brands(brand_ratios)
