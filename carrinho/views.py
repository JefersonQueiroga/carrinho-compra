from django.shortcuts import render,redirect
from .models import Pedido,Produto
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    return render(request,'index.html')

def lista(request):
    produtos = Produto.objects.all()
    return render(request,'lista.html',{'produtos':produtos})

def pedido(request):
    return render(request,'pedido.html')

def adicionar(request,pk):
    produto = get_object_or_404(Produto, pk=pk)
    valor = request.session.get(str(produto.id), 0)
    print("Produto: ", produto.nome, "- Qtd: ",valor)
    request.session[str(produto.id)]=valor + 1
    return redirect('lista')


#pega dados da session e manda para lista de pedido
def mostrar_pedido(request):
    #pegando os produtos em sessão
    list_produtos=[]
    for key, value in request.session.items():
        print(key,value)
        produto = Produto.objects.get(id=int(key))
        produto.quantidade = value
        list_produtos.append(produto)
    return render(request,'pedido.html',{'list_produtos':list_produtos}) 


# função para limpar sessão, ou seja apagar a session 
def fechar_pedido(request):
    request.session.clear()
    return redirect('index')