
import math
from fpdf import FPDF

#page_width = 297
#page_height = 210

page_width = 450
page_height = 300
margins = 8
Space = 5

def NewPage():
    pdf.add_page(orientation = 'L')

def PrintText(X, Y, T):
    pdf.text(X+5, Y+20, T)

def Line(X1, Y1, X2 = None, Y2 = None, dashed = False):
    global Xlast
    global Ylast

    if X2 == None:
        X2 = X1
        X1 = Xlast
    if Y2 == None:
        Y2 = Y1
        Y1 = Ylast

    # print line
    if dashed:
        pdf.dashed_line(X1, Y1, X2, Y2)
    else:
        pdf.line(X1, Y1, X2, Y2)

    Xlast = X2
    Ylast = Y2

def Sqr(a):
    return math.sqrt(a)

def PrintBox(Width, Length, Height, Top_Height, InnerSize):
    global page_width
    global page_height
    global margins
    global Space
    # Page margins
    MinX = 20
    MinY = margins
    MaxX = page_width
    MaxY = page_height - margins

    # Initial position
    PosX = MinX
    PosY = MinY

    NewPage()

    # Outer walls

    TmpW = Width + InnerSize * 2 * Sqr(2)
    TmpH = Length + InnerSize * 2 * Sqr(2)
    TmpY = 0
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    OuterWall (PosX, PosY, Width, Length, InnerSize * Sqr(2), "Outer floor")

    PosX = PosX + TmpW + Space

    TmpW = Width + InnerSize * 2 * Sqr(2)
    TmpH = Height + InnerSize * 2 * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    OuterWall (PosX, PosY, Width, Height, InnerSize * Sqr(2), "Outer Wall, width")

    PosX = PosX + TmpW + Space
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    OuterWall (PosX, PosY, Width, Height, InnerSize * Sqr(2), "Outer Wall, width")

    PosX = PosX + TmpW + Space

    TmpW = Length + InnerSize * 2 * Sqr(2)
    TmpH = Height + InnerSize * 2 * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    OuterWall (PosX, PosY, Length, Height, InnerSize * Sqr(2), "Outer Wall, length")

    PosX = PosX + TmpW + Space
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    OuterWall (PosX, PosY, Length, Height, InnerSize * Sqr(2), "Outer Wall, length")

    PosX = PosX + TmpW + Space

    InnerWall_Width = Width - 2 * InnerSize
    InnerWall_Length = Length - 2 * InnerSize
    InnerWall_Height = Height - 2 * InnerSize

    # Inner Walls

    TmpW = InnerWall_Width + 2 * InnerSize * Sqr(2)
    TmpH = InnerWall_Length + 2 * InnerSize * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    InnerFloor (PosX, PosY, InnerWall_Width, InnerWall_Length, InnerSize * Sqr(2), "Inner Floor")

    PosX = PosX + TmpW + Space

    TmpW = InnerWall_Width + InnerSize * 2 * Sqr(2)
    TmpH = InnerWall_Height + InnerSize * 3 * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    InnerWall (PosX, PosY, InnerWall_Width, InnerWall_Height, InnerSize * Sqr(2), "Inner Wall, width")

    PosX = PosX + TmpW + Space
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    InnerWall (PosX, PosY, InnerWall_Width, InnerWall_Height, InnerSize * Sqr(2), "Inner Wall, width")

    PosX = PosX + TmpW + Space

    TmpW = InnerWall_Length + InnerSize * 2 * Sqr(2)
    TmpH = InnerWall_Height + InnerSize * 3 * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    InnerWall (PosX, PosY, InnerWall_Length, InnerWall_Height, InnerSize * Sqr(2), "Inner Wall, length")

    PosX = PosX + TmpW + Space
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    InnerWall (PosX, PosY, InnerWall_Length, InnerWall_Height, InnerSize * Sqr(2), "Inner Wall, length")

    PosX = PosX + TmpW + Space

    # Ceiling

    Top_Width = Width + 6
    Top_Length = Length + 6

    InnerTop_Width = Top_Width - 2 * InnerSize
    InnerTop_Length = Top_Length - 2 * InnerSize

    TmpW = InnerTop_Width + InnerSize * 2 * Sqr(2)
    TmpH = InnerTop_Length + InnerSize * 2 * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    InnerFloor (PosX, PosY, InnerTop_Width, InnerTop_Length, InnerSize * Sqr(2), "Inner ceiling")

    PosX = PosX + TmpW + Space

    TmpW = Top_Width + 4 * Top_Height + InnerSize * 2 * Sqr(2)
    TmpH = Top_Length + 4 * Top_Height + InnerSize * 2 * Sqr(2)
    (PosX, PosY, TmpY) = CheckSize(PosX, PosY, TmpY, MinX, MinY, MaxX, MaxY, Space, TmpW, TmpH)
    OuterTop (PosX, PosY, Top_Width, Top_Length, Top_Height, InnerSize * Sqr(2), "Outer ceiling")

    PosX = PosX + TmpW + Space

def CheckSize(PosX, PosY, TmpY, MinX,  MinY,  MaxX,  MaxY, Space, W,  H):
    if W > MaxX - MinX or H > MaxY - MinY:
        print ("Image does not fit on page")
        #return None
    if PosX + W > MaxX:
        PosX = MinX
        PosY = TmpY
    if PosY + H > MaxY:
        NewPage()
        PosX = MinX
        PosY = MinY
        TmpY = MinY
    if PosY + H + Space > TmpY:
        TmpY = PosY + H + Space
    return (PosX, PosY, TmpY)

def Wall( X1,  X2,  Y1,  Y2, XC,  YC,  OW,  OH,  I):
    
    Line (X1, Y1, X2, Y1, True)
    Line (X2, Y1, X2, Y2, True)
    Line (X2, Y2, X1, Y2, True)
    Line (X1, Y2, X1, Y1, True)

    Line (X1, Y1, XC - OW, Y1 - I)
    Line (XC + OW, Y1 - I)
    Line (X2, Y1)
    Line (X2 + I, YC - OH)
    Line (X2 + I, YC + OH)
    Line (X2, Y2)
    Line (XC + OW, Y2 + I)
    Line (XC - OW, Y2 + I)
    Line (X1, Y2)
    Line (X1 - I, YC + OH)
    Line (X1 - I, YC - OH)
    Line (X1, Y1)

def OuterWall( X,  Y,  W,  H, I, Text = ""):
    X1 = X + I
    Y1 = Y + I
    Wall (X1, 
        X1 + W, 
        Y1, 
        Y1 + H, 
        X1 + W / 2, 
        Y1 + H / 2, 
        (W - I * Sqr(2)) / 2, 
        (H - I * Sqr(2)) / 2, 
        I)
    # print text
    PrintText(X1, Y1, Text)

def InnerFloor( X,  Y,  W,  H, I, Text = ""):
    X1 = X + I
    Y1 = Y + I
    Wall (X1, 
        X1 + W, 
        Y1, 
        Y1 + H, 
        X1 + W / 2, 
        Y1 + H / 2, 
        (W + I * Sqr(2)) / 2, 
        (H + I * Sqr(2)) / 2, 
        I)
    # print text
    PrintText(X1, Y1, Text)

def InnerWall( X,  Y,  W,  H, I, Text = ""):
    X1 = X + I
    Y1 = Y + I
    XC = X1 + W / 2
    OW = (W + I * Sqr(2)) / 2
    InnerFloor(X, Y + I, W, H, I, Text)
    Line (XC - OW, Y1, XC - OW, Y1 - I)
    Line (XC + OW, Y1 - I)
    Line (XC + OW, Y1)

def OuterTop( X,  Y,  W,  L, H,  I, Text = ""):
    X1 = X + I + 2 * H
    Y1 = Y + I + 2 * H
    X2 = X1 + W
    Y2 = Y1 + L
    XC = X1 + W / 2
    YC = Y1 + L / 2
    OW = (W - I * Sqr(2)) / 2
    OH = (L - I * Sqr(2)) / 2
    
    Line (X1, Y1, X2, Y1, True)
    Line (X2, Y1, X2, Y2, True)
    Line (X2, Y2, X1, Y2, True)
    Line (X1, Y2, X1, Y1, True)
    Line (X1, Y1 - 2 * H, X1, Y1 - H, True)
    Line (X2, Y1 - 2 * H, X2, Y1 - H, True)
    Line (X1, Y2 + 2 * H, X1, Y2 + H, True)
    Line (X2, Y2 + 2 * H, X2, Y2 + H, True)
    Line (X1, Y1 - 2 * H, X2, Y1 - 2 * H, True)
    Line (X1, Y1 - H, X2, Y1 - H, True)
    Line (X2 + 2 * H, Y1, X2 + 2 * H, Y2, True)
    Line (X2 + H, Y1, X2 + H, Y2, True)
    Line (X1, Y2 + 2 * H, X2, Y2 + 2 * H, True)
    Line (X1, Y2 + H, X2, Y2 + H, True)
    Line (X1 - 2 * H, Y1, X1 - 2 * H, Y2, True)
    Line (X1 - H, Y1, X1 - H, Y2, True)
    
    Line (X1, Y1, X1, Y1 - H)
    Line (X1 - H, Y1 - H)
    Line (X1 - H, Y1 - 2 * H)
    Line (X1, Y1 - 2 * H)
    Line (XC - OW, Y1 - 2 * H - I)
    Line (XC + OW, Y1 - 2 * H - I)
    Line (X2, Y1 - 2 * H)
    Line (X2 + H, Y1 - 2 * H)
    Line (X2 + H, Y1 - H)
    Line (X2, Y1 - H)
    Line (X2, Y1)
    Line (X2 + 2 * H, Y1)
    Line (X2 + 2 * H + I, YC - OH)
    Line (X2 + 2 * H + I, YC + OH)
    Line (X2 + 2 * H, Y2)
    Line (X2, Y2)
    Line (X2, Y2 + H)
    Line (X2 + H, Y2 + H)
    Line (X2 + H, Y2 + 2 * H)
    Line (X2, Y2 + 2 * H)
    Line (XC + OW, Y2 + 2 * H + I)
    Line (XC - OW, Y2 + 2 * H + I)
    Line (X1, Y2 + 2 * H)
    Line (X1 - H, Y2 + 2 * H)
    Line (X1 - H, Y2 + H)
    Line (X1, Y2 + H)
    Line (X1, Y2)
    Line (X1 - 2 * H, Y2)
    Line (X1 - 2 * H - I, YC + OH)
    Line (X1 - 2 * H - I, YC - OH)
    Line (X1 - 2 * H, Y1)
    Line (X1, Y1)
    # print text
    PrintText(X1, Y1, Text)


pdf = FPDF(format = (page_height, page_width))
pdf.set_font('Arial', 'B', 8)
pdf.set_margins(0, 0, 0)

PrintBox(320, 170, 230, 16, 14)
#PrintBox(100, 80, 50, 20, 8)

pdf.output('box.pdf', 'F')
