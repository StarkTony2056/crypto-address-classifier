# Cryptocurrency Address Classification

The problem is to develop a machine learning algorithm that can accurately classify cryptocurrency addresses into different types, such as BTC (bitcoin), Ethereum (ETH), Tron (TRX), or any other type.

The provided model classifies the input cryptocurrency addresses into BTC (bitcoin), Ethereum (ETH), DOGE (Dogecoin), and LTC (litecoin). The addresses of type Tron could not be acquired and hence it has been excluded. But there is considerable area of improvement in the model as more data can be collected on other cryptocurrency types.

The dataset that was finally used is in the `./dataset` folder in the `crypto-dataset.csv` file. The raw data is contained in the other files and has been obtained from Google's [BigQuery platform](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=crypto_bitcoin_cash&page=dataset&project=sunlit-center-424211-p6&ws=!1m10!1m4!4m3!1sbigquery-public-data!2scrypto_bitcoin_cash!3sinputs!1m4!4m3!1sbigquery-public-data!2scrypto_dogecoin!3sinputs).

## How to run?
First install the requirement:
```pip install -r requirements.txt```

Then, run the Flask server:
```python app.py```

Next, run the application frontend:
```python -m http.server```

Go to `http://localhost:8000/` to use the app.

### All the steps of the ML pipeline will be found in `crypto_datacollection.ipynb` and `crypto_address_classification.ipynb` files.

## Insights:

1. Accuracy: The RandomForest model had the best and perfect precision and recall on the validation dataset. The confusion matrix indicated the same.
2. Feature Importance: The feature importance showed that features that show the prefix of the addresses, and certain characters in the addresses hold the most importnace when determining features by the RandomForest model.

## Deployment testing:


https://github.com/StarkTony2056/crypto-address-classifier/assets/91143608/fd285f2b-1176-4ec4-9cb4-996c4428d7f5




## Scope for Future Improvement:

1. **Enhanced Feature Engineering**

-   **Advanced Textual Features:** Explore additional text-based features, such as n-grams or sequence patterns, which might capture subtle differences between address types.
-   **Blockchain-Specific Metadata:** Incorporate metadata from blockchain explorers, such as transaction volume, age of the address, or network activity, to provide context beyond the address string itself.
-   **Graph-Based Features:** Analyze the transaction graph associated with addresses to derive features related to address connectivity, clustering, and network centrality.

2. **Increased Dataset Diversity and Size**

-   **Additional Cryptocurrencies:** Include a broader range of cryptocurrencies in the dataset to improve the model's generalization and robustness.
-   **Larger Dataset:** Collect a more extensive dataset to provide the model with more examples, which can enhance its learning capabilities and reduce overfitting.
-   **Synthetic Data Generation:** Use techniques like data augmentation or generative adversarial networks (GANs) to create synthetic addresses that can help balance the dataset and introduce more variability.

3. **Model Enhancements**

-   **Ensemble Methods:** Combine multiple models (e.g., bagging, boosting, stacking) to leverage their strengths and improve overall classification performance.
-   **Deep Learning:** Experiment with deep learning architectures, such as recurrent neural networks (RNNs) or transformers, which can capture sequential and contextual information in address strings more effectively.
-   **AutoML Tools:** Utilize automated machine learning (AutoML) tools to automatically search for the best model architecture and hyperparameters.

4. **Model Interpretability and Explainability**

-   **SHAP Values:** Use SHapley Additive exPlanations (SHAP) to understand the contribution of each feature to the model's predictions, enhancing transparency.
-   **LIME:** Implement Local Interpretable Model-agnostic Explanations (LIME) to provide localized interpretations of model predictions, helping to identify specific features influencing each classification.

5. **Improved Validation and Testing**

-   **Cross-Validation:** Use k-fold cross-validation to ensure that the model's performance is consistent across different subsets of the data.
-   **Robust Testing:** Test the model on unseen data from different sources or time periods to assess its generalization capabilities and robustness.

6. **Scalability and Deployment Enhancements**

-   **Optimized Deployment:** Optimize the model for faster inference times using techniques like model quantization or distillation.
-   **Scalable Infrastructure:** Deploy the model using scalable cloud-based solutions (e.g., AWS SageMaker, Google AI Platform) to handle high volumes of requests.
-   **Monitoring and Maintenance:** Implement monitoring tools to track the model's performance in production and set up automated alerts for significant performance degradation.

7. **User Interface and Integration**

-   **API Enhancements:** Develop a comprehensive API with detailed documentation, examples, and error handling to facilitate integration with other systems.
-   **User Interface:** Create a user-friendly web interface or mobile app that allows users to input addresses and receive real-time classification results.

8. **Security and Privacy Considerations**

-   **Data Privacy:** Ensure that the handling of addresses complies with relevant data privacy regulations and best practices.
-   **Security:** Implement robust security measures to protect the deployed model and API from malicious attacks and unauthorized access.

9. **Community and Feedback**

-   **Community Involvement:** Engage with the cryptocurrency and machine learning communities to gather feedback, validate results, and identify new features or improvements.
-   **Continuous Learning:** Implement mechanisms for the model to learn continuously from new data, adapting to changes in address patterns and emerging cryptocurrencies.

By focusing on these areas, the model can be continually improved to deliver more accurate, reliable, and insightful classifications of cryptocurrency addresses.
