# CAP - Cyclic Alternating Pattern

A Twitter scraper that scrapes the 1000 most recent tweets that contain a specific keyword hash-tag value that is 
contained in a keyword list.

## Getting Started

These instructions will help you install and run the project on your local machine for development and testing purposes.

### Prerequisites

**Python 3.7** 

**SciPy v1.2.0**: For creating a web service

```
pip install Flask
```

**Tweepy 3.7.0**: For scraping Twitter

```
pip install tweepy
```

### Run

```
python app.py
```

The service starts by default on port **5000** and **/scrape** is the service endpoint in order to start scraping. 
For example if you run it on your local machine, the full URL will be:

```
localhost:5000/scrape
```

