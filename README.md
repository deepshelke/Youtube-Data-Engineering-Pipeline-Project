# 🎥 YouTube Data Engineering Project using AWS

This project demonstrates a **complete end-to-end data engineering pipeline** using AWS services to process, clean, and visualize YouTube video engagement data. The final analytics are displayed in an **interactive dashboard built with Amazon QuickSight**, styled to resemble YouTube's native UI.

---

## 🚀 Project Objective

To build a **cloud-native data pipeline** that:
- Ingests raw JSON data from YouTube (or simulated API dump),
- Processes and enriches the data using AWS Lambda, Glue, and S3,
- Catalogs it for querying via Athena and visualization via QuickSight,
- Delivers business insights such as top-viewed channels, engagement factors, and category-wise performance.

---

## 📊 Final Dashboard (Amazon QuickSight)

The dashboard contains:

- **KPI Cards**: Total Views, Likes, Dislikes, Comments
- **Filters**: Region and Trending Date
- **Charts**:
  - Donut Chart: Engagement by Category
  - Bar Chart: Views by Channel

---

## 🧩 Project Architecture

![AWS Architecture](architecture.png)

- **Source**: JSON structured YouTube data via API/S3
- **Landing Zone**: Raw data dumped into `deep-de-on-youtube-raw/youtube/raw_statistics_reference_data/`
- **Lambda Function**: Triggered on S3 event, processes JSON to flattened Parquet
- **Docker + Lambda Layer**: Includes Pandas and PyArrow for Parquet conversion
- **Cleansed S3 Zone**: Output stored in `deep-de-on-youtube-cleansed`
- **AWS Glue**: Crawls cleansed data, registers in Data Catalog
- **Athena**: SQL querying on curated Parquet data
- **QuickSight**: Final visualization
- **Monitoring**: CloudWatch logging enabled

![355824021-c7c0d6c5-1df9-42ae-a69a-b7922193bc47](https://github.com/user-attachments/assets/29e9ac8f-ef10-440b-b0d9-7cf07c9cdeb3)

---

## 🛠️ Technologies & Services Used

- **AWS S3** – Data Lake (raw & cleansed)
- **AWS Lambda** – Transformation engine
- **AWS Glue & Glue Catalog** – ETL + metadata registry
- **AWS Athena** – Serverless querying
- **Amazon QuickSight** – BI dashboard
- **AWS IAM** – Access and policy control
- **CloudWatch** – Monitoring
- **Docker** – For packaging Python dependencies (PyArrow, Pandas)

---


