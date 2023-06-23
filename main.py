from fpdf import FPDF
import pandas
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
df = pandas.read_csv("topics.csv")

for index, row in df.iterrows():
    x1 =10
    y1=20
    x2=200
    y2=20
    step=10

    # Master Page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1, y1, x2, y2)

    # Adding lines to pdf
    for i in range(20, 298, 10):
        pdf.line(x1, i, x2, i)

   # Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Adding lines to pdf
        for i in range(20, 298, 10):
            pdf.line(x1, i, x2, i)


pdf.output("output.pdf")
#pdf.output("output1.pdf")



