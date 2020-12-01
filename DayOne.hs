module Main where

import Data.Set as S

parseInputs :: IO (S.Set Int)
parseInputs = S.fromList . (read <$>) . lines <$> readFile "./day_1.txt"

solution :: S.Set Int -> Int
solution xs = S.foldl' (*) 1 . S.filter (`S.member` xs) . S.map (2020 -) $ xs

main :: IO ()
main = parseInputs >>= (print . solution)
