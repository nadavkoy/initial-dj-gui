import wx
import chat_client
import threading

FRAME_SIZE = (626, 443)
BACKGROUND = "dj_background.png"


class WelcomePanel(wx.Panel):

    def __init__(self, parent_frame):
        wx.Panel.__init__(self, parent=parent_frame, size=FRAME_SIZE)

        self.parent_frame = parent_frame  # parent frame.
        self.v_box = wx.BoxSizer(wx.VERTICAL)  # setting a vertical box sizer, to arrange objects on panel.

        # Displaying a welcome text.
        self.welcome_text = wx.StaticText(self, label="welcome to the DJ stand!", style=wx.ALIGN_CENTRE | wx.TRANSPARENT_WINDOW)
        self.welcome_text.SetFont(
            wx.Font(30, wx.ROMAN, wx.NORMAL, wx.BOLD, False, u'Arial Rounded MT Bold'))  # setting font.

        self.continue_button = wx.Button(self, label="continue")

        # Binding buttons
        self.continue_button.Bind(wx.EVT_BUTTON, self.button_clicked)

        #  Adding all of the objects in the panel to the sizer.
        self.v_box.AddSpacer(100)
        self.v_box.Add(self.welcome_text, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 40)
        self.v_box.AddSpacer(20)
        self.v_box.Add(self.continue_button, 0, wx.ALIGN_CENTER_HORIZONTAL)

        # Setting our sizer as the panel's sizer.
        self.SetSizer(self.v_box)

    def button_clicked(self, event):
        print 'hi'


class SelectSongs(wx.Panel):

    def __init__(self, parent_frame):
        wx.Panel.__init__(self, parent=parent_frame, size=FRAME_SIZE)

        self.parent_frame = parent_frame  # parent frame.
        self.v_box = wx.BoxSizer(wx.VERTICAL)  # setting a vertical box sizer, to arrange objects on panel.

        # Displaying a welcome text.
        self.welcome_text = wx.StaticText(self, label="welcome to the DJ stand!", style=wx.ALIGN_CENTRE | wx.TRANSPARENT_WINDOW)
        self.welcome_text.SetFont(
            wx.Font(30, wx.ROMAN, wx.NORMAL, wx.BOLD, False, u'Arial Rounded MT Bold'))  # setting font.

        self.continue_button = wx.Button(self, label="continue")

        # Binding buttons
        self.continue_button.Bind(wx.EVT_BUTTON, self.button_clicked)

        #  Adding all of the objects in the panel to the sizer.
        self.v_box.AddSpacer(100)
        self.v_box.Add(self.welcome_text, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 40)
        self.v_box.AddSpacer(20)
        self.v_box.Add(self.continue_button, 0, wx.ALIGN_CENTER_HORIZONTAL)

        # Setting our sizer as the panel's sizer.
        self.SetSizer(self.v_box)

    def button_clicked(self, event):
        print 'hi'

class Frame(wx.Frame):
    """ main frame. """

    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size=FRAME_SIZE,
                                    style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

        self.SetIcon(wx.Icon("icon.ico"))  # setting icon.

        """self.background = BACKGROUND
        bmp1 = wx.Image(BACKGROUND, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))"""

        self.welcome_panel = WelcomePanel(self)  # creating and showing the first panel.

        # initializing the next panels, afterwards they will become actual objects.
        self.user_entrance_panel = wx.Panel(self).Hide()
        self.chat_panel = wx.Panel(self).Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)  # setting a vertical box sizer, to arrange objects on panel.
        self.sizer.Add(self.welcome_panel, 1, wx.EXPAND)  # adding panel to sizer.
        self.SetSizer(self.sizer)  # Setting our sizer as the panel's sizer.

    def switch_panels(self):
        """ responsible for switching panels. """
        if self.welcome_panel.IsShownOnScreen():  # if first panel is shown:
            self.welcome_panel.Hide()  # hide panel
            self.sizer.Remove(0)  # remove panel form the sizer
            self.user_entrance_panel = UserEntrancePanel(self)  # create the next panel
            self.sizer.Add(self.user_entrance_panel, 1, wx.EXPAND)  # add next panel to sizer.
            self.Layout()

        elif self.user_entrance_panel.IsShownOnScreen():
            self.SetTitle(self.username + "'s chat!")  # updating the frame's title according to the client's username.
            self.user_entrance_panel.Hide()  # hide panel
            self.sizer.Remove(0)  # remove panel form the sizer
            self.chat_panel = ChatPanel(self)  # create the next panel
            self.sizer.Add(self.chat_panel, 1, wx.EXPAND)
            self.Layout()  # add next panel to sizer.


def main():
    app = wx.App()
    frame = Frame(None, title="DJ stand")
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
