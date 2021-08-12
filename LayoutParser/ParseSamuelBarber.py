import layoutparser as lp
import pytesseract
from pdf2image import convert_from_path

# Parse Despite and Still by Samuel Barber
# => From the Library of Congress: https://www.loc.gov/item/2001542478/
ScorePageImageArr = convert_from_path("PDFToParse\\service-music-vaultscan.3-200183221-200183221.pdf",
    poppler_path=r'C:\\Program Files\\Poppler21.03.0\\Library\\bin')

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
ocr_agent = lp.TesseractAgent(languages='eng')

for i in range(1, len(ScorePageImageArr)):
    ScorePageImage = ScorePageImageArr[i - 1]
    ScorePageImage.save(f"ParsedSamuelBarber\\SamuelBarberP{i}.png")

    res = ocr_agent.detect(ScorePageImage, return_response=True)
    layout = ocr_agent.gather_data(res, agg_level=lp.TesseractFeatureType.WORD)

    ScorePageLayoutTextImage = lp.draw_text(ScorePageImage, layout,
        font_size=12, with_box_on_text=True, text_box_width=1)
    ScorePageLayoutTextImage.save(f"ParsedSamuelBarber\\SamuelBarberP{i}LayoutTextImage.png")
    ScorePageLayoutBoxImage = lp.draw_box(ScorePageImage, layout, box_width=3)
    ScorePageLayoutBoxImage.save(f"ParsedSamuelBarber\\SamuelBarberP{i}LayoutBoxImage.png")
