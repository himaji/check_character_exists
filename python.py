from fontTools.ttLib import TTFont

def check_character_exists(font_path, character):
    font = TTFont(font_path)
    cmap = font.getBestCmap()
    if ord(character) in cmap:
        return True
    else:
        return False

font_path = "Arial Nova.ttf"
character_to_check = "ș"

if check_character_exists(font_path, character_to_check):
    print("文字が含まれています")
else:
    print("文字が含まれていません")

