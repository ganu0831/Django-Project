from django.shortcuts import render, redirect
from .forms import UploadCSVForm
import pandas as pd
from .models import Candle

def upload_csv_view(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            timeframe = form.cleaned_data['timeframe']

            # Read the CSV file using pandas
            df = pd.read_csv(csv_file)

            # Process the data and create Candle objects
            candle_objects = []  # This list will hold your Candle objects

            for index, row in df.iterrows():
                candle = Candle(
                    open=row['OPEN'],
                    high=row['HIGH'],
                    low=row['LOW'],
                    close=row['CLOSE'],
                    date=row['DATE']
                )
                candle_objects.append(candle)

            # Save the Candle objects to the database
            Candle.objects.bulk_create(candle_objects)

            # Redirect or render a success page
            return render(request, 'success.html')

    else:
        form = UploadCSVForm()

    return render(request, 'upload_csv.html', {'form': form})

