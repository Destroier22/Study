//Para associar uma palavra a várias outras palavras em JavaScript, você pode usar uma estrutura de dados que mantenha essas associações. Uma das maneiras mais simples de fazer isso é usar um objeto JavaScript, onde as palavras-chave são as chaves do objeto e as palavras associadas são os valores correspondentes. Aqui está um exemplo de como fazer isso:

// Criando um objeto de associação
const associacoes = {
    "cachorro": ["animal", "pet", "amigo"],
    "gato": ["animal", "pet", "companheiro"],
    "carro": ["veículo", "transporte", "máquina"]
};

// Obtendo palavras associadas a "cachorro"
const palavrasAssociadasAoCachorro = associacoes["cachorro"];
console.log("Palavras associadas a 'cachorro':", palavrasAssociadasAoCachorro);

// Obtendo palavras associadas a "carro"
const palavrasAssociadasAoCarro = associacoes["carro"];
console.log("Palavras associadas a 'carro':", palavrasAssociadasAoCarro);
//Neste exemplo, associacoes é um objeto que mapeia palavras-chave para um array de palavras associadas. Você pode acessar as palavras associadas a uma palavra-chave específica simplesmente acessando a propriedade correspondente do objeto.

//Você também pode adicionar, remover ou atualizar associações conforme necessário. Por exemplo, para adicionar uma associação, você pode fazer o seguinte:
associacoes["moto"] = ["veículo", "transporte"];
