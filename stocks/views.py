# import required libraries
from django.shortcuts import render
from django.core.paginator import Paginator
from stock_processing.process import by_sector
from stock_processing.visualize import plot_data
from django.contrib.auth.decorators import login_required
import base64

# function that renders the landing page
def landing(request):
    # render the page
    return render(request, 'stocks/landing.html', {'title': 'Landing'})

# function that renders the about page
@login_required
def about(request):
    # render the page
    return render(request, 'stocks/about.html', {'title': 'About'})

# function that renders the home page
@login_required
def info(request):
    # get the processed data
    uniques, sectors_list = by_sector()

    # get the graphs,html and averages
    graphs = []
    averages = []
    head_html = []
    for sector in sectors_list:
        # convert the dataframes to html
        head_html.append(sector.head().to_html(classes="table table-striped table-bordered", index=False))

        # get the average change for the sector
        averages.append(sector['Day Change'].mean())

        # change the graph to a image that can be shown
        buf = plot_data(sector)
        if buf:
            graph = base64.b64encode(buf.read()).decode('utf-8')
            graph_uri = 'data:image/png;base64,' + graph
        else:
            graph_uri = None
        graphs.append(graph_uri)
    
    # put them together
    sectors = list(zip(uniques, head_html, graphs, averages))

    # handle pagination
    paginator = Paginator(sectors, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # render the page
    return render(request, 'stocks/info.html', {'page_obj': page_obj})
