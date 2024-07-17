# Used Car Prices Analysis

![Overview](images/overview.png)

## Table of Contents
- [Project Overview](#project-overview)
- [Data](#data)
- [Analysis](#analysis)
  - [Part 1: Product Segmentation and Demographic Analysis](#part-1-product-segmentation-and-demographic-analysis)
  - [Part 2: Exploratory Data Analysis](#part-2-exploratory-data-analysis)
  - [Part 3: Price Prediction Model](#part-3-price-prediction-model)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [License](#license)

## Project Overview
This project aims to analyze and predict the selling prices of used cars in the USA. By leveraging data cleaning, exploratory data analysis, and machine learning, we uncover key factors influencing car prices and build a predictive model to estimate car values.

## Data
The dataset used in this project is `car_prices.csv`, which includes the following columns:
- year
- make
- model
- trim
- body
- transmission
- vin
- state
- condition
- odometer
- color
- interior
- seller
- mmr (Manheim Market Report)
- sellingprice
- saledate

## Analysis

### Part 1: Product Segmentation and Demographic Analysis
In this part, we segment the car data based on various attributes and perform demographic analysis using Power BI. Key insights include:
- Distribution of car makes and models.
- Analysis of selling prices by car condition, age, and odometer readings.

![EDA Plots](images/eda_plots.png)

### Part 2: Exploratory Data Analysis
We perform a thorough EDA using Python (pandas, matplotlib, seaborn) to identify factors that significantly impact car prices. We examine correlations between price and attributes like make, model, condition, and odometer.

### Part 3: Price Prediction Model
A machine learning model is developed to predict car prices. Using Linear Regression and Random Forest, we assess the performance and interpret the importance of different features.

![Model Results](images/model_results.png)

## Technologies Used
- **Python**: pandas, numpy, matplotlib, seaborn, scikit-learn
- **Power BI**: Visualization and Dashboarding
- **Jupyter Notebooks**: Documentation and Code Presentation

## Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/used-car-prices-analysis.git
    ```
2. Navigate to the project directory:
    ```sh
    cd used-car-prices-analysis
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the notebooks in the `notebooks` directory for detailed analysis.

## Results
- **Top Selling Makes and Models**: Identified popular makes and models.
- **Factors Influencing Prices**: Condition, age, and odometer readings are significant predictors.
- **Model Performance**: Achieved an R-squared score of 0.95 with Random Forest.

## Conclusion
This project provides a comprehensive analysis of used car prices, highlighting key factors affecting car values and offering a predictive model for estimating prices. The insights can be useful for car dealerships, buyers, and sellers to make informed decisions.

## Future Work
- Incorporate more features such as geographic data.
- Explore other machine learning models for better accuracy.
- Develop a web application to make the model accessible to end-users.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
