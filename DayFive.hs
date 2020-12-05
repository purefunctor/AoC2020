module Main where

import Data.List (sort)

type Bounds = (Int, Int)

parseInput :: IO [(String, String)]
parseInput = (splitAt 7 <$>) . lines <$> readFile "./day_5.txt"

binaryPartition_ :: Char -> Bounds -> Bounds
binaryPartition_ c (l, u)
  | c == 'F' || c == 'L' = (l, m)
  | c == 'B' || c == 'R' = (m + 1, u)
  where
    m = u `div` 2 + l `div` 2

binaryPartition :: String -> Bounds -> Bounds
binaryPartition = foldl1 (flip (.)) . map binaryPartition_

getSeats :: [(String, String)] -> [Int]
getSeats lines = [getRow rs + getCol cs | (rs, cs) <- lines]
  where
    getRow rs = fst (binaryPartition rs (0, 127)) * 8
    getCol cs = fst (binaryPartition cs (0, 7))

solution_1 :: [(String, String)] -> Int
solution_1 = maximum . getSeats

solution_2 :: [(String, String)] -> Int
solution_2 = gapped . sort . getSeats
  where
    gapped (x:y:rest) = if x - y == -2 then (y - x - 1) + x else gapped rest

main :: IO ()
main = do
  lines <- parseInput
  print . solution_1 $ lines
  print . solution_2 $ lines
