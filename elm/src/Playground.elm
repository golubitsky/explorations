module Playground exposing (main)

import Array
import Html
import Regex


revelation =
    """
    It became very clear to me sitting out there today
    that every decision I've made in my entire life has
    been wrong. My life is the complete "opposite" of
    everything I want it to be. Every instinct I have,
    in every aspect of life, be it something to wear,
    something to eat - it's all been wrong.
    """


myArray =
    Array.fromList [ 1, 2, 3, 4 ]


toString bool =
    if bool == True then
        "True"

    else
        "False"


palindrome word =
    let
        isLetter char =
            char /= ' ' && char /= ','

        possiblePalindrome =
            String.filter isLetter (String.toLower word)
    in
    possiblePalindrome == String.reverse possiblePalindrome


descending a b =
    case compare a b of
        LT ->
            GT

        GT ->
            LT

        EQ ->
            EQ


sortDescending list =
    List.sortWith descending list


countShortStrings list maxLength =
    List.map String.length list
        |> List.filter (\x -> x < maxLength)
        |> List.length


validateEmail email =
    let
        emailPattern =
            "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b"

        regex =
            Maybe.withDefault Regex.never <|
                Regex.fromString emailPattern

        isValid =
            Regex.contains regex email
    in
    if isValid then
        ( "Valid email", "green" )

    else
        ( "Invalid email", "red" )


theAnswer =
    42


main =
    theAnswer
        |> Debug.toString
        |> Html.text
