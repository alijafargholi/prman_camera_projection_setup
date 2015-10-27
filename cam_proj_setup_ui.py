import PySide.QtCore as qc
import PySide.QtGui as qg

# Global variable to store the UI status, if it's open or closed
prman_projection_ui = None


class PrmanProjectionUi(qg.QDialog):
    """

    """
    def __init__(self):
        qg.QDialog.__init__(self)

        self.setWindowTitle("Prman Projection Setup")
        # Keep the window on top
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        # Setting the size policy
        self.setFixedHeight(300)
        self.setFixedWidth(500)

        # Setting the MAIN layout
        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(3, 3, 3, 3)
        self.layout().setSpacing(1)
        self.layout().setAlignment(qc.Qt.AlignTop)
        self.layout().setAlignment(qc.Qt.AlignCenter)

        # Creating the frames
        top_frame = qg.QFrame()
        top_frame.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        top_frame.setFixedHeight(220)
        # Creating Layout for top frame
        top_frame_layout = qg.QVBoxLayout()
        top_frame_layout.setContentsMargins(1, 1, 1, 1)
        top_frame_layout.setSpacing(1)
        top_frame_layout.setAlignment(qc.Qt.AlignTop)
        top_frame.setLayout(top_frame_layout)

        # bottom_frame = qg.QFrame()
        # bottom_frame.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        #
        # bottom_frame.setLayout(qg.QVBoxLayout)
        # bottom_frame.layout(qg.Q)
        # middle_frame.setLayout(qg.QGridLayout())

        # Adding the frames to the layout
        self.layout().addWidget(top_frame)
        # self.layout().addWidget(middle_frame)

        # Creating the UI elements
        projector_name = qg.QLineEdit()
        projector_name.setPlaceholderText("Enter the name of the "
                                          "PxrProjector....")

        projection_camera_name = qg.QLineEdit()
        projection_camera_name.setPlaceholderText("Enter the name of the "
                                                  "camera projection....")
        projection_layout.addWidget(projection_camera_label)
        projection_layout.addWidget(projection_camera_name)

        place3d_label = qg.QLabel('Place3DTexture:')
        place3d_name = qg.QLineEdit()
        place3d_name.setPlaceholderText("Enter the name of the "
                                          "place3dTexture....")

        place3d_name_button = qg.QPushButton('Get it from selection')

        link_radio_btn = qg.QRadioButton('Link')
        copy_radio_btn = qg.QRadioButton('Copy')
        copy_or_link_layout = qg.QHBoxLayout()
        copy_or_link_layout.addWidget(link_radio_btn)
        copy_or_link_layout.addWidget(copy_radio_btn)

        # Adding the elements to the top frame layout
        top_frame_layout.addLayout(copy_or_link_layout)


def create_ui():
    """

    :return: Create a instance of the PrmanProjectionUi and shows the window
    """
    global prman_projection_ui
    if prman_projection_ui is None:
        prman_projection_ui = PrmanProjectionUi()
    prman_projection_ui.show()


def delete_ui():
    """
    If the UI exists in memory, delete it.
    :return: None
    """
    global prman_projection_ui
    if prman_projection_ui is None:
        return

    prman_projection_ui.deleteLater()
    prman_projection_ui = None
