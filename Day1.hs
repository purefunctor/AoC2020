module Main where

import Data.Set as S

parseInputs :: IO (S.Set Int)
parseInputs = S.fromList . (read <$>) . lines <$> readFile "./day_1.txt"

solution_1 :: S.Set Int -> Int
solution_1 xs = S.foldl' (*) 1 . S.filter (`S.member` xs) . S.map (2020 -) $ xs

solution_2 :: S.Set Int -> Int
solution_2 xs = head [ (2020 - y0 - y1) * y0 * y1
                     | y0 <- ys, y1 <- ys, S.member (2020 - y0 - y1) xs
                     ]
  where
    ys = S.toList xs

main :: IO ()
main = do
  xs <- parseInputs
  print . solution_1 $ xs
  print . solution_2 $ xs
