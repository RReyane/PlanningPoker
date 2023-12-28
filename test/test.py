from unittest.mock import mock_open, patch
from main import lireBacklog, saveJson


def test_lectureJson():
    backlog = lireBacklog()
    assert isinstance(backlog,list)

def test_SauvegardeJson(monkeypatch):
    mock_data = {'backlog': [{'id': 1, 'feature': 'Test', 'description': 'Description'}]}
    mock_listeJoueurs = ['Joueur1', 'Joueur2']
    mock_typeJeu = 0
    mock_indexFeature = 0
    mock_votes = [1, 2]

    with monkeypatch.context() as m:
        # Remplacez la fonction open avec une fonction de simulation (mock_open)
        m.setattr("builtins.open", mock_open())
        saveJson(mock_data, mock_listeJoueurs, mock_typeJeu, mock_indexFeature, mock_votes)