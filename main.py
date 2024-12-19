from gnews import GNews
import pandas as pd
from datetime import datetime, timedelta
import time
import logging
from typing import List, Dict

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_gnews() -> GNews:
    """Initialize GNews with desired settings."""
    return GNews(
        language='pt',
        country='BR',
        max_results=1000,
        period='5d'
    )

def is_within_date_range(published_date: str, days: int = 5) -> bool:
    """Check if the article is within the specified date range."""
    try:
        article_date = datetime.strptime(published_date, '%a, %d %b %Y %H:%M:%S GMT')
        cutoff_date = datetime.now() - timedelta(days=days)
        return article_date >= cutoff_date
    except Exception as e:
        logger.warning(f"Date parsing error: {e}")
        return False

def fetch_articles(keywords: List[str]) -> List[Dict]:
    """Fetch articles for given keywords with rate limiting and error handling."""
    gn = setup_gnews()
    articles = []
    
    for keyword in keywords:
        try:
            logger.info(f"Fetching articles for keyword: {keyword}")
            news_items = gn.get_news(keyword)
            
            for item in news_items:
                if is_within_date_range(item['published date']):
                    article = {
                        'Keyword': keyword,
                        'Title': item['title'],
                        'Link': item['url'],
                        'Published': item['published date'],
                        'Description': item['description'],
                        'Source': item['publisher']['title']
                    }
                    articles.append(article)
            
            time.sleep(1)
            
        except Exception as e:
            logger.error(f"Error fetching articles for keyword '{keyword}': {e}")
            continue
    
    return articles

def main():
    
    keywords = [
        "insira aqui suas palavras-chave"
    ]

    try:
        # Fetch articles
        articles = fetch_articles(keywords)

        # Create DataFrame and remove duplicates
        df = pd.DataFrame(articles)
        df = df.drop_duplicates(subset=['Title', 'Link'])  # Remove duplicate articles

        # Convert published date to datetime
        df['Published'] = pd.to_datetime(df['Published'], format='%a, %d %b %Y %H:%M:%S GMT')
        
        # Sort by published date (newest first)
        df = df.sort_values('Published', ascending=False)

        # Save to Excel with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f'agros_{timestamp}.xlsx'
        
        df.to_excel(filename, index=False)
        logger.info(f"Successfully exported {len(df)} articles to {filename}")
        
        # Print some basic stats
        logger.info(f"Total articles found: {len(df)}")
        logger.info(f"Articles per keyword: {df['Keyword'].value_counts().to_dict()}")

    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()