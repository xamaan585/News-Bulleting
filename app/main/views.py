from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_headlines,get_category,get_source,get_source_aricles,search_topic

@main.route('/')
def index():
    '''
    method to render home page
    '''
    sources= get_source()
    categories= get_category('business')
    headlines = get_headlines()
    
    search_topic = request.args.get('q')

    if search_topic:
        return redirect(url_for('.search',topic_name=search_topic))
    else:
        return render_template('index.html',categories=categories,headlines=headlines,sources=sources)

@main.route('/categories/<category>')
def category(category):
    '''
    method to render category page
    '''
    category = get_category(category)
    sources= get_source()

    return render_template('categories.html',category = category,sources=sources)

@main.route('/article/<id>')
def article(id):

    '''
    method to render articles in a source
    '''
    # title= 'Articles'
    articles = get_source_aricles(id)
    sources= get_source()
    category = get_category('health')
    return render_template('article.html',articles= articles,id=id,sources=sources,category=category)   


@main.route('/search/<topic_name>')
def search(topic_name):
    '''
    View function to display the search results
    '''
    # searched_topics = search_topic(topic_name)
    topic_name_list = topic_name.split(" ")
    topic_name_format = "+".join(topic_name_list)
    searched_topics = search_topic(topic_name_format)
    return render_template('search.html',topics = searched_topics)