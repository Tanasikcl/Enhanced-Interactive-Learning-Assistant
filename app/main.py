from app.research import get_research_insights
from app.report_generator import format_report

def generate_learning_report(topic, objectives, subtopics, knowledge_level, learning_format):
    raw_data = get_research_insights(
        topic=topic,
        objectives=objectives,
        subtopics=subtopics,
        knowledge_level=knowledge_level,
        learning_format=learning_format
    )
    return format_report(raw_data)
