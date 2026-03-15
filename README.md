# Virtual Server Monitoring and Performance Optimization

## Project Overview
This project implements an end-to-end data pipeline to monitor virtual server performance and identify resource bottlenecks. The solution processes server log data and visualizes key performance metrics using Power BI.

The goal is to provide insights into server health, CPU utilization, memory usage, and system availability to support proactive monitoring and optimization.

---

## Architecture

CSV Dataset  
↓  
Python Data Pipeline (Data Ingestion + Transformation)  
↓  
Processed Dataset  
↓  
Power BI Dashboard for Visualization

---

## Data Ingestion

The server log dataset is ingested from a CSV file using Python and Pandas.

Key steps:
- Load server log data
- Validate dataset
- Check missing values
- Remove duplicates

Tools Used:
- Python
- Pandas

---

## Data Transformation

The dataset is processed to generate meaningful insights.

Transformations include:
- CPU utilization monitoring
- Memory usage analysis
- Server availability calculation
- Server health classification
- Encryption of sensitive fields

Sensitive data such as IP address, admin email, and phone number are encrypted for security.

---

## Power BI Dashboard

A Power BI dashboard was developed to visualize server performance metrics.

Dashboard Insights:
- Average CPU utilization
- Average memory usage
- Server availability
- CPU usage trends over time
- Server distribution by location
- OS distribution of servers

Interactive filters allow users to analyze servers by:
- Location
- Operating system
- Hostname

---

## Technologies Used

- Python
- Pandas
- Power BI
- GitHub

---

## Project Structure

```

```
server-monitoring-project
│
├── ingestion.py
├── transformation.py
├── Sample_Data_Ingestion.csv
├── cleaned_data.csv
└── server_monitoring_dashboard.pbix
```

```

---

## Key Insights

- Identification of servers with high CPU utilization
- Monitoring of server uptime and availability
- Analysis of server distribution across locations
- Performance trends for proactive infrastructure monitoring

---

## Future Improvements

- Real-time server log streaming
- Automated anomaly detection
- Integration with cloud storage like Azure Data Lake
- Alert system for critical server conditions

