import layoutparser as lp
import cv2
import pytesseract

# Table image from the LayoutParser documentation:
# https://layout-parser.readthedocs.io/en/latest/example/parse_ocr/index.html
# => https://stacks.cdc.gov/view/cdc/42482/
image = cv2.imread('table.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
ocr_agent = lp.TesseractAgent(languages='eng')
res = ocr_agent.detect(image, return_response=True)
layout = ocr_agent.gather_data(res, agg_level=lp.TesseractFeatureType.WORD)

layoutTextImage = lp.draw_text(image, layout,
                            font_size=12, with_box_on_text=True, text_box_width=1)
layoutTextImage = layoutTextImage.save("layoutTextImage.png")
layoutBoxImage = lp.draw_box(image, layout, box_width=3)
layoutBoxImage = layoutBoxImage.save("layoutBoxImage.png")
