module Main where

import Data.List (sort)

type Bounds = (Int, Int)
type Partition = Char
type Partitions = [Partition]
type SeatNumber = Int

parseInput :: IO [(Partitions, Partitions)]
parseInput = (splitAt 7 <$>) . lines <$> readFile "./day_5.txt"

binaryPartition_ :: Partition -> Bounds -> Bounds
binaryPartition_ c (l, u)
  | c == 'F' || c == 'L' = (l, m)
  | c == 'B' || c == 'R' = (m + 1, u)
  where
    m = u `div` 2 + l `div` 2

binaryPartition :: Partitions -> Bounds -> Bounds
binaryPartition = foldl1 (flip (.)) . map binaryPartition_

partitionSeats :: [(Partitions, Partitions)] -> [Int]
partitionSeats partitions = [getRow row_part + getCol col_part
                      | (row_part, col_part) <- partitions
                      ]
  where
    getRow row_part = fst (binaryPartition row_part (0, 127)) * 8
    getCol col_part = fst (binaryPartition col_part (0, 7))

solution_1 :: [(Partitions, Partitions)] -> SeatNumber
solution_1 = maximum . partitionSeats

solution_2 :: [(Partitions, Partitions)] -> SeatNumber
solution_2 = gapped . sort . partitionSeats
  where
    gapped (x:y:rest) = if x - y == -2 then (y - x - 1) + x else gapped (y : rest)

main :: IO ()
main = do
  partitions <- parseInput
  print . solution_1 $ partitions
  print . solution_2 $ partitions
