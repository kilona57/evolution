from django.shortcuts import render
from website.models import *
from neomodel import db
from neo4j import GraphDatabase
from math import sqrt, erf, log
from py2neo import Graph, Node, Relationship
# Create your views here.
def veiw_all_nodes(request):
    all_nodes, list_all_nodes = allNodes()
    return render(request, 'index.html', {'all_nodes': all_nodes})

def allNodes():
    all_nodes = [] 
    category = Category.nodes.all()
    entity = Entity.nodes.all()
    geoEra = GeoEra.nodes.all() 
    geoEonEra = GeoEonEra.nodes.all()
    geoPeriod = GeoPeriod.nodes.all()
    geologicalPeriod = GeologicalPeriod.nodes.all() 
    bacteria = Бактерии.nodes.all() 
    arhei = Археи.nodes.all() 
    mashrooms = Грибы.nodes.all() 
    green_algae = Зеленые_водоросли.nodes.all() 
    sagovnicovid = Саговниковидные.nodes.all() 
    ginkgovid = Гинкговидные.nodes.all() 
    xvoinie = Хвойные.nodes.all() 
    gnatvid = Гнетовидные.nodes.all() 
    hvoshevid = Хвощевидные.nodes.all() 
    plaunovid = Плауновидные.nodes.all() 
    mohovid = Моховидные.nodes.all() 
    paporotnicovid = Папоротниковидные.nodes.all() 
    flowervid = Цветковые.nodes.all() 
    minshit = Малощетниковые.nodes.all() 
    maxshit = Многощетниковые.nodes.all() 
    circle_cherv = Круглые_черви.nodes.all() 
    gubci = Губки.nodes.all() 
    infuzori = Инфузории.nodes.all() 
    bruchonogie = Брюхоногие.nodes.all() 
    lento_cherv = Ленточные_черви.nodes.all() 
    sea_ech = Морские_ежи.nodes.all() 
    dvustvorchatie = Двустворчатые.nodes.all() 
    sosalshici = Сосальщики.nodes.all() 
    costnie = Костные.nodes.all() 
    xriashevie = Хрящевые.nodes.all() 
    sea_lilia = Морские_лилии.nodes.all() 
    sea_star = Морские_звезды.nodes.all() 
    golovonogie = Головоногие.nodes.all() 
    cancervid = Ракообразные.nodes.all() 
    nasecomie = Насекомые.nodes.all()    
    spider = Паукообразные.nodes.all() 
    primati = Приматы.nodes.all() 
    
    models = [category, entity, geoEra, geoEonEra, geoPeriod, geologicalPeriod, bacteria, arhei, mashrooms, green_algae,
              sagovnicovid, ginkgovid, xvoinie, gnatvid, hvoshevid, plaunovid, mohovid, paporotnicovid, flowervid, 
              minshit, maxshit, circle_cherv, gubci, infuzori, bruchonogie, lento_cherv, sea_ech, dvustvorchatie, sosalshici,
              costnie, xriashevie, sea_lilia, sea_star, golovonogie, cancervid, nasecomie, spider, primati]
    
    all_nodes = set(item.name for items in models for item in items)
    all_nodes = sorted(all_nodes)
    all_nodes_list = all_nodes
    all_nodes = grouped_terms(all_nodes)
    return all_nodes, all_nodes_list

def grouped_terms(all_nodes):
    grouped_terms = {}
    for node in all_nodes:
        first_letter = node[0].upper()
        if first_letter not in grouped_terms:
            grouped_terms[first_letter] = []
        grouped_terms[first_letter].append(node)
    return grouped_terms

def term_detail_view(request, term_name):
    models = [Category, Entity, GeoEra, GeoEonEra, GeoPeriod, GeologicalPeriod, Бактерии, Археи, Грибы, Зеленые_водоросли, 
              Саговниковидные, Гинкговидные, Хвойные, Гнетовидные, Хвощевидные, Плауновидные, Моховидные, Папоротниковидные,
              Цветковые, Малощетниковые, Многощетниковые, Круглые_черви, Губки, Инфузории, Брюхоногие, Ленточные_черви,
              Морские_ежи, Двустворчатые, Сосальщики, Костные, Хрящевые, Морские_лилии, Морские_звезды, Головоногие,
              Ракообразные, Насекомые, Паукообразные, Приматы]
    
    term = None
    all_nodes, list_all_nodes = allNodes()
    for model in models:
        try:
            term = model.nodes.filter(name=term_name).first()
            # return render(request, 'search.html', {'term': term, 'all_nodes': allNodes()})
            #term.name = term.name.capitalize()
            # if term.text == None:
            #     return render(request, 'search.html', {'term': 'Term not found'})
        except:
            continue
    if term == None:
        
        return render(request, 'terms.html', {'name': term_name, 'all_nodes': all_nodes}) 
    else:
        return render(request, 'terms.html', {'term': term, 'all_nodes': all_nodes}) 


    
        

def search(request):
    models = [Entity, Category, GeoEra, GeoEonEra, GeoPeriod, GeologicalPeriod, Бактерии, Археи, Грибы, Зеленые_водоросли, 
              Саговниковидные, Гинкговидные, Хвойные, Гнетовидные, Хвощевидные, Плауновидные, Моховидные, Папоротниковидные,
              Цветковые, Малощетниковые, Многощетниковые, Круглые_черви, Губки, Инфузории, Брюхоногие, Ленточные_черви,
              Морские_ежи, Двустворчатые, Сосальщики, Костные, Хрящевые, Морские_лилии, Морские_звезды, Головоногие,
              Ракообразные, Насекомые, Паукообразные, Приматы]
    all_nodes, list_all_nodes = allNodes()
    if request.method == 'POST':
        name = request.POST.get('name')
        #text = 'Term not found'
        term = None
        for model in models:
            try:
                term = model.nodes.filter(name=name).first()
                # return render(request, 'search.html', {'term': term, 'all_nodes': allNodes()})
                #term.name = term.name.capitalize()
                # if term.text == None:
                #     return render(request, 'search.html', {'term': 'Term not found'})
            except:
                continue
        if term == None:
            
            return render(request, 'search.html', {'name': name, 'all_nodes': all_nodes}) 
        else:
            return render(request, 'search.html', {'term': term, 'all_nodes': all_nodes}) 
    else:
        return render(request, 'search.html')
    
def add_node(request):
    # uri = "bolt://localhost:7687"
    # username = "neo4j"
    password = "Kiokushin_2021"
    all_nodes = [] 
    category = Category.nodes.all()
    entity = Entity.nodes.all()
    models = [category, entity]
    all_nodes = set(item.name for items in models for item in items)
    all_nodes = sorted(all_nodes)
    if request.method == "POST":
    # # Установка соединения с базой данных Neo4j
    #     driver = GraphDatabase.driver(uri, auth=(username, password))
        graph = Graph("bolt://localhost:7687", auth=("neo4j", password))
        selected_node_name = request.POST.get('selected_node_name')
        selected_relationship = request.POST.get('selected_relationship')
        name = request.POST.get('name')
        text = request.POST.get("text")
        kingdom = request.POST.get("kingdom")
        part = request.POST.get("part")
        type = request.POST.get("type")
        class_node = request.POST.get("class")
        trop = request.POST.get("trop")
        order = request.POST.get("order")
        family = request.POST.get("family")
        genus = request.POST.get("genus")
        view = request.POST.get("view")
        properties = {"name":name, "text": text, 'Царство': kingdom, "Отдел": part, "Тип": type, "Класс": class_node, 
                    "Отряд": trop, "Порядок": order, "Семейство": family, "Род": genus, "Вид":view}
        
        items_to_remove = [key for key, value in properties.items() if value == '']

        for key in items_to_remove:
            del properties[key]
            
        selected_node = graph.nodes.match(name=selected_node_name).first()

        if selected_node is None:
            return render(request, "Selected node not found.")

        # Create a new node
        new_node = Node(selected_node_name, **properties)
        graph.create(new_node)

        # Create a relationship between the selected node and the new node
        relationship = Relationship(new_node, selected_relationship, selected_node)
        graph.create(relationship)
        
        return render(request, 'add_new_nodes.html', {'all_nodes': all_nodes})
    else:
        return render(request, "add_new_nodes.html", {'all_nodes': all_nodes})