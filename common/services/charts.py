# collection/services/charts.py
from django.db.models import Sum
from collection.models.collections import Collection

def get_daily_collection_chart_data():
    """
    Groups collections by date and calculates total amount per day.
    Returns format ready for Chart.js:
    {
        "labels": ["2026-01-10", "2026-01-11"],
        "data": [5000.00, 12000.00]
    }
    """
    # Group by collection_date and sum amounts
    daily_stats = (
        Collection.objects
        .values('collection_date')
        .annotate(total_amount=Sum('amount'))
        .order_by('collection_date')
    )
    print(daily_stats)  # Debugging line to check the output of the query


    labels = [str(item['collection_date']) for item in daily_stats]
    data = [float(item['total_amount']) for item in daily_stats]

    return {
        "labels": labels,
        "data": data,
    }


def get_payment_details_chart_data():   
    daily_stats = (
        Collection.objects
        .values('payment_status')
        .annotate(total_amount=Sum('amount'))
    )
    print(daily_stats)  # Debugging line to check the output of the query


    labels = [str(item['payment_status']) for item in daily_stats]
    data = [float(item['total_amount']) for item in daily_stats]

    return {
        "labels": labels,
        "data": data,
    }