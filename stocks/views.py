# import required libraries
from django.shortcuts import render
from django.core.paginator import Paginator
from stock_processing.process import process_data
from stock_processing.visualize import plot_data
from django.contrib.auth.decorators import login_required

# function that renders the about page
@login_required
def about(request):
    # render the page
    return render(request, 'blog/about.html', {'title': 'About'})

# function that renders the home page
@login_required
def home(request):
    # get the processed data
    processed_df = process_data()

    # turn the panda into html
    table_html = processed_df.to_html(classes='table table-striped')

    # handle pagination
    paginator = Paginator(processed_df.to_dict('records'), 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # render the page
    return render(request, 'home.html', {
                  'table_html' : table_html,
                  'page_obj' : page_obj,
                  'title' : 'Home'
    })

# function that renders the plotted data
@login_required
def plots(request):
    # get the plot data
    processed_df = process_data()
    data_img = plot_data(processed_df)

    # turn the plot into a renderable image
    plot = base64.b64encode(data_img.getvalue()).decode('utf-8')

    # render the page
    return render(request, 'plots.html', { 
                  'plot' : plot, 
                  'title' : 'Plot'
    })

