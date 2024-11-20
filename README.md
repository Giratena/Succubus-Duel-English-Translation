# Succubus-Duel-English-Translation
This is a translation project for Succubus Duel, a card game featuring many succubi and temptations...
[You can buy and support the game here!](https://www.dlsite.com/maniax/work/=/product_id/RJ01149693.html)

# How to contribute/test the translation
- Clone the Repo and then copy your game files into the repo and you're done!
  - Any edits or change in the repo will also be reflected in your game.
  - Push and pull from "Develop" to get updates as they happen.
# How to put the translation into your game
- Download the repo as a zip then paste everything into your game folder (where SuccubusDuel.exe is located) and you're done!
- Alternatively, grab a stable copy from the releases tab!

 # How to support:
 - Support my work on Patreon! https://www.patreon.com/Giratena
 - Join the Translation Server discord for wholesome translation help and updates! https://discord.gg/fYPg7KX

# Special Translation information
## General
### Punctuation
- Any ❤, must be prefixed with puncuation. Eg: ".❤", "!❤", "?❤", "~❤", or "...❤" 
- Any "," must be replaced with ";". This is because the scripts are comma-delimited CSVs. They will render as "," in game.
- Don't use "…". Use "..."!
### Japanese SFX
Japanese words often have lots of sfx. The Japanese language is great with sfx but not so much for English! So you'll want to substitute with an adjective English description instead if necessary. If sfx is used, be sure to wrap them in "*". EG: "*Suck, slurp*"

DO:
> "ほら、さわさわ❤さわさわ・・・❤" -\> "See how I'm gently brushing my fingers over your nipples?\~❤"

DON'T: 
> "ほら、さわさわ❤さわさわ・・・❤" -\> "Look; brush~❤ brush...❤"
### Japanese laughter/Other Terms
Retain any laughter as follows while preserving the nuanced Japanese:
> You can add an "!" or "~" after it if it feels appropriate!
- うふふ -> Ufufu
- くすくす -> "\*Giggle\*", "Hehe", "Teehee", "Kuhuhu", or "\*snicker\*"
- あは -> Aha
- あはは -> Ahaha
- エナジー -> Mana

## Card terminology
- The elements a card can be (EG: Water, Fire Dark etc) is called "Attribute"
- The type of card (EG: Rouge, Warrior, Hunter etc) is called "Type".
- Attributes and Types are always capitalized. EG: "Hunter Type" or "Fire Attribute".
- Removing a card from the game is called "banishing" a card.
- The discard pile is called the "Graveyard". This word should be capitalized.
- Statuses are labeled as [Status Name (X)] where X is the effect number if any.

## Translating Enemy Cards:
Some cards don't have all the text available to translate (such as card descriptions) but they can be translated through the following:
1. Open CSV/place/MorugenInn.txt
2. Replace "\<Card id>" with the ID of the card you want to translate.
3. When you visit the Inn in the game, the card description text will copy to your clipboard.
4. Paste the clipboard text in the the "\<Card id>".txt
5. The text can now be translated!

## Card description formating
-  Effects are marked as [X]. where X is the effect number
-  Effects that depend on the number must be described as X, and then defining what X is equal to.
   - EG: "[1]. Select a character on the field. Increase that character's attack power by 400 x X (X = the number of cards equipped)."
- If a trap/ability card has an activation condition, the description must with "If..."If a character or equipment card has an activation condition, the description must start with "When..."
