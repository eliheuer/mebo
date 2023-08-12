from fontTools.ttLib import TTFont

def print_os2_table(font_path):
    try:
        font = TTFont(font_path)
    except Exception as e:
        print("Error loading font:", e)
        return

    if "OS/2" not in font:
        print("Font does not contain an OS/2 table.")
        return

    os2_table = font["OS/2"]
    print(dir(os2_table))
    print("OS/2 Table Contents:")
    print("--------------------")
    print("Version:", os2_table.version)
    print("Weight Class:", os2_table.usWeightClass)
    print("Width Class:", os2_table.usWidthClass)
    print("Typographic Ascent:", os2_table.sTypoAscender)
    print("Typographic Descent:", os2_table.sTypoDescender)
    print("Typographic Line Gap:", os2_table.sTypoLineGap)
    print("Win Ascent:", os2_table.usWinAscent)
    print("Win Descent:", os2_table.usWinDescent)
    print("X Height:", os2_table.sxHeight)
    print("Cap Height:", os2_table.sCapHeight)
    print("Subscript X Size:", os2_table.ySubscriptXSize)
    print("Subscript Y Size:", os2_table.ySubscriptYSize)
    print("Subscript X Offset:", os2_table.ySubscriptXOffset)
    print("Subscript Y Offset:", os2_table.ySubscriptYOffset)
    print("Superscript X Size:", os2_table.ySuperscriptXSize)
    print("Superscript Y Size:", os2_table.ySuperscriptYSize)
    print("Superscript X Offset:", os2_table.ySuperscriptXOffset)
    print("Superscript Y Offset:", os2_table.ySuperscriptYOffset)
    print("Strikeout Size:", os2_table.yStrikeoutSize)
    print("Strikeout Position:", os2_table.yStrikeoutPosition)
    print("Family Class:", os2_table.sFamilyClass)
    print("Panose:", os2_table.panose)
    print("Unicode Range 1:", os2_table.ulUnicodeRange1)
    print("Unicode Range 2:", os2_table.ulUnicodeRange2)
    print("Unicode Range 3:", os2_table.ulUnicodeRange3)
    print("Unicode Range 4:", os2_table.ulUnicodeRange4)
    print("Vendor ID:", os2_table.achVendID)
    print("Selection:", os2_table.fsSelection)
    print("First Char Index:", os2_table.usFirstCharIndex)
    print("Last Char Index:", os2_table.usLastCharIndex)
    # Add more attributes you want to print here

    font.close()

if __name__ == "__main__":
    font_path = "Mebo-Regular.ttf"  # Replace with the actual path to your font file
    print_os2_table(font_path)

