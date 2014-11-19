-- Módulo: Operaciones Listas
-- Diversas operaciones sobre listas en Haskell

module Tarea1 where

sumList [] = 0
sumList (x:xs) = x + sumList xs

-- Funcion generica que zipwith
gF :: (a->b->c) -> [a]->[b]->[c]
gF f (a:as) (b:bs) = f a b : gF f as bs
gF _ _      _      = []

-- Funcion para sumar matrices
sumaMat ::  Num a => [[a]] -> [[a]] -> [[a]]
sumaMat p q = gF (gF (+)) p q

-- Ordenación por QuickSort:
ordenaQS :: Ord a => [a] -> [a]
ordenaQS [] = []
ordenaQS ( x:xs ) = ordenaQS menores ++ [x] ++ ordenaQS mayores
                   where menores = [ e | e <- xs, e < x ]
                         mayores = [ e | e <- xs, e >= x ]

-- checa que los elementos de las dos listas sean iguales
elem_iguales a b = ordenaQS a == ordenaQS b

-- Funciones para invertir listas
-- usando foldr
invertir_lista_der :: Ord a => [a] -> [a]
invertir_lista_der a = foldr (\b c -> c ++ [b] ) [] a
--usando foldl
invertir_lista_izq :: Ord a => [a] -> [a]
invertir_lista_izq a = foldl (\b c -> c : b) [] a 

-- ordenar dos listas 

ordena2listas :: Ord a => [a] -> [a] -> [a]
ordena2listas a [] = a
ordena2listas [] b = b
ordena2listas (x:xs) (b:bs) | (<=) x b = x: ordena2listas xs (b:bs)
			    | otherwise = b: ordena2listas (x:xs) bs


-- ordena2listas a b = ordenaQS (a++b)


-- Ordenar dos listas:
ordena_dos_listas :: Ord a => [a] -> [a] -> [a]
ordena_dos_listas x [] = x
ordena_dos_listas [] y = y
ordena_dos_listas (x:xs) (y:ys) | (<) x y = ordena_dos_listas mins_x mins_y ++ [x] ++ ordena_dos_listas mas_x [y]++mas_y
				| otherwise = ordena_dos_listas mins_y mins_x ++ [y] ++ ordena_dos_listas mas_y [x]++mas_x
				  where mins_x = [ e | e <- xs, e < x ]
					mins_y = [ e | e <- ys, e < y ]
		                 	mas_x = [ e | e <- xs, e >= x ]
		                 	mas_y = [ e | e <- ys, e >= y ]




