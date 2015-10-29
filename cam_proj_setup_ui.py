import PySide.QtCore as qc
import PySide.QtGui as qg

import functools

import pymel.core as pm

# Global variable to store the UI status, if it's open or closed
prman_projection_ui = None


class PrmanProjectionUi(qg.QDialog):
    """

    """
    def __init__(self, parent=None):
        super(PrmanProjectionUi, self).__init__(parent)

        self.setWindowTitle("Prman Projection Setup")
        # Keep the window on top
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        # Setting the size policy
        self.setMaximumHeight(300)
        self.setFixedWidth(500)

        # Setting the MAIN layout
        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(3, 3, 3, 3)
        self.layout().setSpacing(1)
        self.layout().setAlignment(qc.Qt.AlignTop)

        # Creating the frames
        top_frame = qg.QFrame()
        top_frame.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        top_frame.setFixedHeight(130)
        # Creating Layout for top frame
        top_frame_layout = qg.QVBoxLayout()
        top_frame_layout.setContentsMargins(1, 1, 1, 1)
        top_frame_layout.setSpacing(1)
        top_frame_layout.setAlignment(qc.Qt.AlignTop)
        top_frame.setLayout(top_frame_layout)

        # Creating the UI elements
        info_layout = qg.QGridLayout()

        # Projector Node
        projector_label = qg.QLabel('PxrProjector:')
        projector_name = qg.QLineEdit()
        projector_name.setPlaceholderText("Enter the name of the "
                                          "PxrProjector....")
        projector_name_button = qg.QPushButton('Get it from selection')
        projector_name_button.setToolTip('Select the <b>PxrProjector</b> '
                                         'node and the hit this button to '
                                         'get the name')

        # Camera Projection Node
        projection_camera_label = qg.QLabel('Camera Projection:')
        projection_camera_name = qg.QLineEdit()
        projection_camera_name.setPlaceholderText("Enter the name of the "
                                                  "camera projection....")
        projection_camera_name_button = qg.QPushButton('Get it from selection')
        projection_camera_name_button.setToolTip('Select the '
                                                 '<b>Projection Camera</b> '
                                                 'node  and the hit this '
                                                 'button to get the name')

        # Place3dTexture Node
        place3d_label = qg.QLabel('Place3DTexture:')
        place3d_name = qg.QLineEdit()
        place3d_name.setPlaceholderText("Enter the name of the "
                                          "place3dTexture....")
        place3d_name_button = qg.QPushButton('Get it from selection')
        place3d_name_button.setToolTip('Select the '
                                                 '<b>place3dTexture</b> '
                                                 'node  and the hit this '
                                                 'button to get the name')

        # Node Info Layout
        info_layout.addWidget(projector_label, 0, 0)
        info_layout.addWidget(projector_name, 0, 1)
        info_layout.addWidget(projector_name_button, 0, 2)

        info_layout.addWidget(projection_camera_label, 1, 0)
        info_layout.addWidget(projection_camera_name, 1, 1)
        info_layout.addWidget(projection_camera_name_button, 1, 2)

        info_layout.addWidget(place3d_label, 2, 0)
        info_layout.addWidget(place3d_name, 2, 1)
        info_layout.addWidget(place3d_name_button, 2, 2)

        # Attribute Transfer Mode
        link_radio_btn = qg.QRadioButton('Link')
        link_radio_btn.setChecked(True)
        copy_radio_btn = qg.QRadioButton('Copy')
        transfer_attr_mode = qg.QLabel("Attribute Transfer Mode:")
        copy_or_link_layout = qg.QHBoxLayout()
        copy_or_link_layout.setAlignment(qc.Qt.AlignLeft)
        copy_or_link_layout.addWidget(transfer_attr_mode)
        copy_or_link_layout.addWidget(link_radio_btn)
        copy_or_link_layout.addWidget(copy_radio_btn)

        # Execute Button
        final_button_layout = qg.QHBoxLayout()
        final_button_layout.setContentsMargins(0, 0, 0, 0)
        final_button_layout.setSpacing(1)

        setup_button = qg.QPushButton("Set It Up")
        setup_button.setFixedHeight(35)
        setup_button.setStyleSheet("background-color: green")
        cancel_button = qg.QPushButton("Cancel")
        cancel_button.setFixedHeight(35)
        cancel_button.setStyleSheet("background-color: red")

        final_button_layout.addWidget(setup_button)
        final_button_layout.addWidget(cancel_button)

        # Adding the elements to the top frame layout
        top_frame_layout.addLayout(info_layout)
        top_frame_layout.addLayout(copy_or_link_layout)
        top_frame_layout.addLayout(final_button_layout)

        # Help frame layout
        help_frame = qg.QFrame()
        help_frame_layout = qg.QVBoxLayout()
        help_frame_layout.setContentsMargins(1, 1, 1, 1)
        help_frame_layout.setSpacing(1)
        help_frame_layout.setAlignment(qc.Qt.AlignVCenter)
        help_frame.setLayout(help_frame_layout)

        # Help elements
        help_page = qg.QPushButton('Wiki Page')
        help_page.setToolTip('SHow the wiki page')
        send_error = qg.QPushButton('Send Errors')
        send_error.setToolTip('Email the erros and issues to author')
        send_suggestion = qg.QPushButton('Send Suggestion')
        send_suggestion.setToolTip('Email any suggestion to the author')

        # Adding the help elements to the Help layout
        help_frame_layout.addWidget(help_page)
        help_frame_layout.addWidget(send_error)
        help_frame_layout.addWidget(send_suggestion)

        # Main Layout
        main_tab = qg.QTabWidget()
        main_tab.addTab(top_frame, "Projection Setup")
        main_tab.addTab(help_frame, "Get Help")

        # Adding the widgets to the main layout
        self.layout().addWidget(main_tab)

        # Connecting the functions
        projector_name_button.clicked.connect(
            functools.partial(self._get_selected_name, projector_name))
        projection_camera_name_button.clicked.connect(
            functools.partial(self._get_selected_name, projection_camera_name))
        place3d_name_button.clicked.connect(functools.partial(
            self._get_selected_name, place3d_name))
        cancel_button.clicked.connect(delete_ui)

    def _get_selected_name(self, name):
        """
        Will get the name of the selected node and set it as a text to the
        given field

        :name: reference of the field that the name is going to be set to
        :return: None
        """
        name.setText(str(pm.ls(sl=True)[0].name()))


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
