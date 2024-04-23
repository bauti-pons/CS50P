from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering image
        self.image("./shirtificate.png", 10, 70, 190)
        # Setting font: helvetica bold 40
        self.set_font("helvetica", "B", 40)
        # Printing title
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        # Performing a line break
        self.ln(20)


def main():
    shirt(input("Name: "))


def shirt(n):
    # Instantiation of inherited class
    pdf = PDF()

    pdf.add_page(orientation="P", format="A4")
    # Removing margins
    pdf.set_margin(0)
    # Setting font: helvetica 22
    pdf.set_font("helvetica", size=22)
    # Setting text color: white
    pdf.set_text_color(255)
    # Printing name
    pdf.cell(0, 220, f'{n} took CS50', align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
