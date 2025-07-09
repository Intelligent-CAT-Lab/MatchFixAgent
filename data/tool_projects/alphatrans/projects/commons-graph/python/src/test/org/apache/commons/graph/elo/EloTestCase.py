from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.elo.KFactorBuilder import *
from src.main.org.apache.commons.graph.elo.PlayersRank import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.test.org.apache.commons.graph.elo.SimplePlayersRank import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.elo.GameResult import *


class EloTestCase(unittest.TestCase):

    def testPerformElo_test5_decomposed(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_tournament())
        )
        players_rank = SimplePlayersRank()
        CommonsGraph.eloRate(tournament)
        CommonsGraph.eloRate(tournament).wherePlayersAreRankedIn(players_rank)
        CommonsGraph.eloRate(tournament).wherePlayersAreRankedIn(
            players_rank
        ).withKFactor(80)
        print(players_rank)

    def _connect_tournament(self) -> None:
        zenio = self.add_vertex("Zenio")
        marineking = self.add_vertex("Marineking")
        hongun = self.add_vertex("Hongun")
        nestea = self.add_vertex("Nestea")
        tester = self.add_vertex("Tester")
        nada = self.add_vertex("Nada")
        rainbow = self.add_vertex("Rainbow")
        thewind = self.add_vertex("Thewind")
        inka = self.add_vertex("Inka")
        maka = self.add_vertex("Maka")
        ensnare = self.add_vertex("Ensnare")
        kyrix = self.add_vertex("Kyrix")
        killer = self.add_vertex("Killer")
        slayersboxer = self.add_vertex("Slayersboxer")
        fruitdealer = self.add_vertex("Fruitdealer")
        genius = self.add_vertex("Genius")

        self.add_edge(GameResult.WIN).from_(zenio).to(marineking)
        self.add_edge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.add_edge(GameResult.WIN).from_(genius).to(nestea)
        self.add_edge(GameResult.WIN).from_(tester).to(nada)
        self.add_edge(GameResult.WIN).from_(thewind).to(rainbow)
        self.add_edge(GameResult.WIN).from_(maka).to(inka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.add_edge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.add_edge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.add_edge(GameResult.WIN).from_(tester).to(genius)
        self.add_edge(GameResult.WIN).from_(thewind).to(maka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.add_edge(GameResult.WIN).from_(marineking).to(tester)
        self.add_edge(GameResult.WIN).from_(kyrix).to(thewind)
        self.add_edge(GameResult.WIN).from_(kyrix).to(marineking)

    def testPerformElo_test4_decomposed(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_tournament())
        )
        players_rank = SimplePlayersRank()
        CommonsGraph.eloRate(tournament)
        CommonsGraph.eloRate(tournament).wherePlayersAreRankedIn(players_rank)
        CommonsGraph.eloRate(tournament).wherePlayersAreRankedIn(
            players_rank
        ).withKFactor(80)

    def _connect_tournament(self) -> None:
        zenio = self.add_vertex("Zenio")
        marineking = self.add_vertex("Marineking")
        hongun = self.add_vertex("Hongun")
        nestea = self.add_vertex("Nestea")
        tester = self.add_vertex("Tester")
        nada = self.add_vertex("Nada")
        rainbow = self.add_vertex("Rainbow")
        thewind = self.add_vertex("Thewind")
        inka = self.add_vertex("Inka")
        maka = self.add_vertex("Maka")
        ensnare = self.add_vertex("Ensnare")
        kyrix = self.add_vertex("Kyrix")
        killer = self.add_vertex("Killer")
        slayersboxer = self.add_vertex("Slayersboxer")
        fruitdealer = self.add_vertex("Fruitdealer")
        genius = self.add_vertex("Genius")

        self.add_edge(GameResult.WIN).from_(zenio).to(marineking)
        self.add_edge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.add_edge(GameResult.WIN).from_(genius).to(nestea)
        self.add_edge(GameResult.WIN).from_(tester).to(nada)
        self.add_edge(GameResult.WIN).from_(thewind).to(rainbow)
        self.add_edge(GameResult.WIN).from_(maka).to(inka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.add_edge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.add_edge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.add_edge(GameResult.WIN).from_(tester).to(genius)
        self.add_edge(GameResult.WIN).from_(thewind).to(maka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.add_edge(GameResult.WIN).from_(marineking).to(tester)
        self.add_edge(GameResult.WIN).from_(kyrix).to(thewind)
        self.add_edge(GameResult.WIN).from_(kyrix).to(marineking)

    def add_vertex(self, name: str) -> str:
        # Placeholder for adding a vertex to the graph
        return name

    def add_edge(self, result: GameResult) -> HeadVertexConnector:
        # Placeholder for adding an edge to the graph
        return HeadVertexConnector(result)

    def testPerformElo_test3_decomposed(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_tournament())
        )
        players_rank = SimplePlayersRank()
        CommonsGraph.eloRate(tournament).wherePlayersAreRankedIn(players_rank)

    def _connect_tournament(self) -> None:
        zenio = self.add_vertex("Zenio")
        marineking = self.add_vertex("Marineking")
        hongun = self.add_vertex("Hongun")
        nestea = self.add_vertex("Nestea")
        tester = self.add_vertex("Tester")
        nada = self.add_vertex("Nada")
        rainbow = self.add_vertex("Rainbow")
        thewind = self.add_vertex("Thewind")
        inka = self.add_vertex("Inka")
        maka = self.add_vertex("Maka")
        ensnare = self.add_vertex("Ensnare")
        kyrix = self.add_vertex("Kyrix")
        killer = self.add_vertex("Killer")
        slayersboxer = self.add_vertex("Slayersboxer")
        fruitdealer = self.add_vertex("Fruitdealer")
        genius = self.add_vertex("Genius")

        self.add_edge(GameResult.WIN).from_(zenio).to(marineking)
        self.add_edge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.add_edge(GameResult.WIN).from_(genius).to(nestea)
        self.add_edge(GameResult.WIN).from_(tester).to(nada)
        self.add_edge(GameResult.WIN).from_(thewind).to(rainbow)
        self.add_edge(GameResult.WIN).from_(maka).to(inka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.add_edge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.add_edge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.add_edge(GameResult.WIN).from_(tester).to(genius)
        self.add_edge(GameResult.WIN).from_(thewind).to(maka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.add_edge(GameResult.WIN).from_(marineking).to(tester)
        self.add_edge(GameResult.WIN).from_(kyrix).to(thewind)
        self.add_edge(GameResult.WIN).from_(kyrix).to(marineking)

    def add_vertex(self, name: str) -> str:
        # Placeholder for adding a vertex to the graph
        return name

    def add_edge(self, result: GameResult) -> HeadVertexConnector:
        # Placeholder for adding an edge to the graph
        return HeadVertexConnector(result)

    def testPerformElo_test2_decomposed(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[str, GameResult](
                connect0=lambda: self._connect_tournament()
            )
        )
        players_rank = SimplePlayersRank()
        CommonsGraph.eloRate(tournament)

    def _connect_tournament(self) -> None:
        zenio = self.add_vertex("Zenio")
        marineking = self.add_vertex("Marineking")
        hongun = self.add_vertex("Hongun")
        nestea = self.add_vertex("Nestea")
        tester = self.add_vertex("Tester")
        nada = self.add_vertex("Nada")
        rainbow = self.add_vertex("Rainbow")
        thewind = self.add_vertex("Thewind")
        inka = self.add_vertex("Inka")
        maka = self.add_vertex("Maka")
        ensnare = self.add_vertex("Ensnare")
        kyrix = self.add_vertex("Kyrix")
        killer = self.add_vertex("Killer")
        slayersboxer = self.add_vertex("Slayersboxer")
        fruitdealer = self.add_vertex("Fruitdealer")
        genius = self.add_vertex("Genius")

        self.add_edge(GameResult.WIN).from_(zenio).to(marineking)
        self.add_edge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.add_edge(GameResult.WIN).from_(genius).to(nestea)
        self.add_edge(GameResult.WIN).from_(tester).to(nada)
        self.add_edge(GameResult.WIN).from_(thewind).to(rainbow)
        self.add_edge(GameResult.WIN).from_(maka).to(inka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.add_edge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.add_edge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.add_edge(GameResult.WIN).from_(tester).to(genius)
        self.add_edge(GameResult.WIN).from_(thewind).to(maka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.add_edge(GameResult.WIN).from_(marineking).to(tester)
        self.add_edge(GameResult.WIN).from_(kyrix).to(thewind)
        self.add_edge(GameResult.WIN).from_(kyrix).to(marineking)

    def testPerformElo_test1_decomposed(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[str, GameResult](
                connect0=lambda: self._connect_tournament()
            )
        )
        players_rank = SimplePlayersRank()

    def _connect_tournament(self) -> None:
        zenio = self.add_vertex("Zenio")
        marineking = self.add_vertex("Marineking")
        hongun = self.add_vertex("Hongun")
        nestea = self.add_vertex("Nestea")
        tester = self.add_vertex("Tester")
        nada = self.add_vertex("Nada")
        rainbow = self.add_vertex("Rainbow")
        thewind = self.add_vertex("Thewind")
        inka = self.add_vertex("Inka")
        maka = self.add_vertex("Maka")
        ensnare = self.add_vertex("Ensnare")
        kyrix = self.add_vertex("Kyrix")
        killer = self.add_vertex("Killer")
        slayersboxer = self.add_vertex("Slayersboxer")
        fruitdealer = self.add_vertex("Fruitdealer")
        genius = self.add_vertex("Genius")

        self.add_edge(GameResult.WIN).from_(zenio).to(marineking)
        self.add_edge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.add_edge(GameResult.WIN).from_(genius).to(nestea)
        self.add_edge(GameResult.WIN).from_(tester).to(nada)
        self.add_edge(GameResult.WIN).from_(thewind).to(rainbow)
        self.add_edge(GameResult.WIN).from_(maka).to(inka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.add_edge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.add_edge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.add_edge(GameResult.WIN).from_(tester).to(genius)
        self.add_edge(GameResult.WIN).from_(thewind).to(maka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.add_edge(GameResult.WIN).from_(marineking).to(tester)
        self.add_edge(GameResult.WIN).from_(kyrix).to(thewind)
        self.add_edge(GameResult.WIN).from_(kyrix).to(marineking)

    def testPerformElo_test0_decomposed(self) -> None:
        tournament = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[str, GameResult](
                connect0=lambda: self._connect_tournament()
            )
        )

    def _connect_tournament(self) -> None:
        zenio = self.add_vertex("Zenio")
        marineking = self.add_vertex("Marineking")
        hongun = self.add_vertex("Hongun")
        nestea = self.add_vertex("Nestea")
        tester = self.add_vertex("Tester")
        nada = self.add_vertex("Nada")
        rainbow = self.add_vertex("Rainbow")
        thewind = self.add_vertex("Thewind")
        inka = self.add_vertex("Inka")
        maka = self.add_vertex("Maka")
        ensnare = self.add_vertex("Ensnare")
        kyrix = self.add_vertex("Kyrix")
        killer = self.add_vertex("Killer")
        slayersboxer = self.add_vertex("Slayersboxer")
        fruitdealer = self.add_vertex("Fruitdealer")
        genius = self.add_vertex("Genius")

        self.add_edge(GameResult.WIN).from_(zenio).to(marineking)
        self.add_edge(GameResult.WIN).from_(fruitdealer).to(hongun)
        self.add_edge(GameResult.WIN).from_(genius).to(nestea)
        self.add_edge(GameResult.WIN).from_(tester).to(nada)
        self.add_edge(GameResult.WIN).from_(thewind).to(rainbow)
        self.add_edge(GameResult.WIN).from_(maka).to(inka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(ensnare)
        self.add_edge(GameResult.WIN).from_(slayersboxer).to(killer)
        self.add_edge(GameResult.WIN).from_(marineking).to(fruitdealer)
        self.add_edge(GameResult.WIN).from_(tester).to(genius)
        self.add_edge(GameResult.WIN).from_(thewind).to(maka)
        self.add_edge(GameResult.WIN).from_(kyrix).to(slayersboxer)
        self.add_edge(GameResult.WIN).from_(marineking).to(tester)
        self.add_edge(GameResult.WIN).from_(kyrix).to(thewind)
        self.add_edge(GameResult.WIN).from_(kyrix).to(marineking)
