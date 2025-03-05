from fastapi import FastAPI

app=FastAPI()

vendas ={
 1: {"item":"cerveja brahma","preco unitario": 4, "quantidade": 20 },
 2: {"item":"vodka smirk","preco unitario":20,"quantidad":3},
 3: {"aluguel":"mesa","preco unitario":200,"quantidade":3},
}

@app.get("/")
def home():
   return {"vendas":len(vendas)} 


@app.get("/vendas/{id_vendas}")
def retorn_venda(id_vendas:int):
  if id_vendas in vendas:
    	return vendas[id_vendas]
  else:
  	return {"erro":"nao vendido"}


#"api online" 
