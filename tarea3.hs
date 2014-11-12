-- Módulo: Operaciones Listas
-- Diversas operaciones sobre listas en Haskell

module Tarea where

sumMat ::  Num a => [[a]] -> [[a]] -> [[a]]
sumMat p q = zipWith (zipWith (+)) p q

