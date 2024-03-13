from models.produto import Produto
from sqlalchemy import select
from sqlalchemy.orm import Session

def listar(motor):
    print("Produto cadastradas")
    print(f"Nome                                      # Produtos")
    print(f"----------------------------------------- ----------")
    stmt = select(Produto)
    stmt = stmt.order_by("nome")
    with Session(motor) as sessao:
        rset = sessao.execute(stmt).scalars()
        for produto in rset:
            print(f"{produto.nome:40s}  {len(produto.lista_de_produtos):10d}")
    print(f"----------------------------------------- ----------")
