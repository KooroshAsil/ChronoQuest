# Overview — Time Series Concepts

This quick overview highlights the core ideas you will see across the repository.

- **Time series**: observations indexed by time (e.g., daily prices, monthly sales).  
- **Stationarity**: a process whose statistical properties (mean, variance, autocovariance) do not change over time. Useful for modeling and forecasting.  
- **AR(p)**: autoregressive models where current value depends on past p values.  
- **MA(q)**: moving-average models that depend on past q noise terms.  
- **ARMA / ARIMA**: combinations of AR and MA, with differencing (I) when needed to remove trends.  
- **ACF / PACF**: tools to identify model orders; look at decay patterns.  
- **Modeling recipe (brief)**:
  1. Visualize & check for trend/seasonality.
  2. Difference if non-stationary.
  3. Inspect ACF/PACF for orders.
  4. Fit simple models first; check residuals.
  5. Iterate and document findings.

This file is intentionally compact — expand sections into separate notes when you feel like it.
