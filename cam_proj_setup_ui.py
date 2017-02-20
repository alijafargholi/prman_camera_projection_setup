"""
V 2.0
PrMan Projection Setup Tool
By Ali Jafargholi - www.alijafargholi.com - ali.jafargholi@gmail.com

The use of this tool is to setup the connection between the projection nodes
in Maya.

Update: Added https://github.com/mottosso/Qt.py to be able to open the tool
within Maya 2017
"""

from Qt import QtWidgets, QtCore

import functools

import pymel.core as pm

# Global variable to store the UI status, if it's open or closed
prman_projection_ui = None


class PrmanProjectionUi(QtWidgets.QDialog):
    """

    """
    def __init__(self, parent=None):
        super(PrmanProjectionUi, self).__init__(parent)

        self.setWindowTitle("Prman Projection Setup")
        # Keep the window on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # Setting the size policy
        self.setFixedHeight(150)
        self.setMinimumWidth(600)

        # Setting the MAIN layout
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(1)
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        # Creating the frames
        top_frame = QtWidgets.QFrame()
        top_frame.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)
        # Creating Layout for top frame
        top_frame_layout = QtWidgets.QVBoxLayout()
        top_frame_layout.setContentsMargins(1, 1, 1, 1)
        top_frame_layout.setSpacing(1)
        top_frame_layout.setAlignment(QtCore.Qt.AlignTop)
        top_frame.setLayout(top_frame_layout)

        # Creating the UI elements
        info_layout = QtWidgets.QGridLayout()

        # Projector Node
        projector_label = QtWidgets.QLabel('PxrProjector:')
        projector_label.setStyleSheet('font-size: 15px;'
                                      'color: #E5FFFF;'
                                      'letter-spacing: 3px;')
        self.projector_name = QtWidgets.QLineEdit()
        self.projector_name.setMinimumHeight(20)
        self.projector_name.setPlaceholderText("Enter the name of the "
                                          "PxrProjector....")
        self.projector_name_button = QtWidgets.QPushButton('GET')
        self.projector_name_button.setMinimumHeight(20)
        self.projector_name_button.setToolTip('Select the '
                                              '<b>PxrProjector</b> node and '
                                              'the hit this button to '
                                              'get the name')
        self.new_projector_button = QtWidgets.QPushButton('Create a New PxrProjector')
        self.new_projector_button.setStyleSheet("background-color: #004444")
        self.new_projector_button.setMinimumHeight(20)

        # Camera Projection Node
        projection_camera_label = QtWidgets.QLabel('Camera Projection:')
        projection_camera_label.setStyleSheet('font-size: 15px;'
                                              'color: #E5FFFF;'
                                              'letter-spacing: 3px;')
        self.projection_camera_name = QtWidgets.QLineEdit()
        self.projection_camera_name.setMinimumHeight(20)
        self.projection_camera_name.setPlaceholderText("Enter name of camera "
                                                       "projection....")
        self.projection_camera_name_button = QtWidgets.QPushButton('GET')
        self.projection_camera_name_button.setMinimumHeight(20)
        self.projection_camera_name_button.setToolTip('Select the '
                                                      '<b>Projection '
                                                      'Camera</b> node  and '
                                                      'the hit this button '
                                                      'to get the name')
        self.new_camera_button = QtWidgets.QPushButton('Create a New Camera')
        self.new_camera_button.setStyleSheet("background-color: #004444")
        self.new_camera_button.setMinimumHeight(20)

        # Place3dTexture Node
        place3d_label = QtWidgets.QLabel('Place3DTexture:')
        place3d_label.setStyleSheet('font-size: 15px;'
                                    'color: #E5FFFF;'
                                    'letter-spacing: 3px;')
        self.place3d_name = QtWidgets.QLineEdit()
        self.place3d_name.setMinimumHeight(20)
        self.place3d_name.setPlaceholderText("Enter the name of the "
                                             "place3dTexture....")
        self.place3d_name_button = QtWidgets.QPushButton('GET')
        self.place3d_name_button.setMinimumHeight(20)
        self.place3d_name_button.setToolTip('Select the '
                                                 '<b>place3dTexture</b> '
                                                 'node  and the hit this '
                                                 'button to get the name')
        self.new_place3d_button = QtWidgets.QPushButton('Create New Place3dTexture')
        self.new_place3d_button.setStyleSheet("background-color: #004444")
        self.new_place3d_button.setMinimumHeight(20)

        # Node Info Layout
        info_layout.addWidget(projector_label, 0, 0)
        info_layout.addWidget(self.projector_name, 0, 1)
        info_layout.addWidget(self.projector_name_button, 0, 2)
        info_layout.addWidget(self.new_projector_button, 0, 3)

        info_layout.addWidget(projection_camera_label, 1, 0)
        info_layout.addWidget(self.projection_camera_name, 1, 1)
        info_layout.addWidget(self.projection_camera_name_button, 1, 2)
        info_layout.addWidget(self.new_camera_button, 1, 3)

        info_layout.addWidget(place3d_label, 2, 0)
        info_layout.addWidget(self.place3d_name, 2, 1)
        info_layout.addWidget(self.place3d_name_button, 2, 2)
        info_layout.addWidget(self.new_place3d_button, 2, 3)

        # Attribute Transfer Mode
        self.link_radio_btn = QtWidgets.QRadioButton('Link')
        self.link_radio_btn.setChecked(True)
        copy_radio_btn = QtWidgets.QRadioButton('Copy')
        transfer_attr_mode = QtWidgets.QLabel("Attribute Transfer Mode:")
        copy_or_link_layout = QtWidgets.QHBoxLayout()
        copy_or_link_layout.setAlignment(QtCore.Qt.AlignLeft)
        copy_or_link_layout.addWidget(transfer_attr_mode)
        copy_or_link_layout.addWidget(self.link_radio_btn)
        copy_or_link_layout.addWidget(copy_radio_btn)

        # Execute Button
        final_button_layout = QtWidgets.QHBoxLayout()
        final_button_layout.setContentsMargins(0, 0, 5, 5)
        final_button_layout.setSpacing(5)
        final_button_layout.setAlignment(QtCore.Qt.AlignRight)

        setup_button = QtWidgets.QPushButton("Set Up Projection")
        setup_button.setFixedHeight(30)
        setup_button.setFixedWidth(150)
        setup_button.setStyleSheet("background-color: #006000")
        cancel_button = QtWidgets.QPushButton("Close")
        cancel_button.setFixedHeight(30)
        cancel_button.setFixedWidth(40)
        cancel_button.setStyleSheet("background-color: #CC2900")

        final_button_layout.addWidget(setup_button)
        final_button_layout.addWidget(cancel_button)

        # Adding the elements to the top frame layout
        top_frame_layout.addLayout(info_layout)
        top_frame_layout.addLayout(copy_or_link_layout)
        top_frame_layout.addLayout(final_button_layout)

        # Help frame layout
        help_frame = QtWidgets.QFrame()
        help_frame_layout = QtWidgets.QVBoxLayout()
        help_frame_layout.setContentsMargins(1, 1, 1, 1)
        help_frame_layout.setSpacing(3)
        help_frame_layout.setAlignment(QtCore.Qt.AlignTop)
        help_frame.setLayout(help_frame_layout)

        # Help elements
        help_page = QtWidgets.QPushButton('Visit the Wiki Page')
        help_page.setToolTip('SHow the wiki page')

        # Adding the help elements to the Help layout
        help_frame_layout.addWidget(help_page)

        # Main Layout
        main_tab = QtWidgets.QTabWidget()
        main_tab.addTab(top_frame, "Projection Setup")
        main_tab.addTab(help_frame, "Get Help")

        # Adding the widgets to the main layout
        self.layout().addWidget(main_tab)

        # Connecting the functions
        self.projector_name_button.clicked.connect(
            functools.partial(self._get_selected_name, self.projector_name))
        self.projection_camera_name_button.clicked.connect(
            functools.partial(self._get_selected_name,
                              self.projection_camera_name))
        self.place3d_name_button.clicked.connect(functools.partial(
            self._get_selected_name, self.place3d_name))
        setup_button.clicked.connect(self._setup_projection)
        cancel_button.clicked.connect(delete_ui)
        self.new_projector_button.clicked.connect(
            functools.partial(self._create_new_node,
                              node_type="PxrProjector",
                              name_field=self.projector_name))
        self.new_camera_button.clicked.connect(
            functools.partial(self._create_new_node,
                              node_type="camera",
                              name_field=self.projection_camera_name))
        self.new_place3d_button.clicked.connect(
            functools.partial(self._create_new_node,
                              node_type="place3dTexture",
                              name_field=self.place3d_name))
        help_page.clicked.connect(self._go_to_wiki)

    def _go_to_wiki(self):
        """
        Opens the browser link and direct it to the help page for this tool
        :return: Node
        """
        link_page = 'http://alijafargholi.com/2015/11/' \
                    'prman-camera-projection-setup-for-maya'
        # link_page = "https://www.google.com/"
        pm.launch(web=link_page)

    def _warning(self, message):
        """
        Popping up a UI showing the warning message
        :param message: string, warning message
        :return: QWidget
        """

        warning_box = QtWidgets.QMessageBox()
        warning_box.setText(message)
        warning_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        warning_box.exec_()

    def _create_new_node(self, node_type="", name_field=""):
        """
        Create a new node

        :param node_type: 'PxrProjector' or 'Camera' or 'Place3dTexture'
        :param name_field: Name of the UI filed to be set with new node's name
        :return: None
        """
        if node_type == "camera":
            new_name = pm.createNode(node_type).getParent().name()
        else:
            new_name = pm.createNode(node_type)
        name_field.setText(str(new_name))

    def _get_selected_name(self, name):
        """
        Will get the name of the selected node and set it as a text to the
        given field

        :name: reference of the field that the name is going to be set to
        :return: None
        """
        try:
            name.setText(str(pm.ls(sl=True)[0].name()))
        except IndexError:
            self._warning(message="It seems no node is selected.\n")

    def _setup_projection(self):
        """
        Will gather name info from the UI and will set up the connection
        between the nodes
        """

        # Collecting the name from UI
        pxr_projector = self.projector_name.text()
        cam_projector = self.projection_camera_name.text()
        place3d = self.place3d_name.text()

        # Check the existence of the nodes
        for node in [pxr_projector, cam_projector, place3d]:
            try:
                pm.PyNode(node)
            except pm.MayaNodeError:
                self._warning(message="can't find <strong>{"
                                      "0}</strong> node".format(node))
                return

        # Getting the camera shape
        try:
            cam_projector_shape = pm.PyNode(str(cam_projector)).getShape()
        except AttributeError as e:
            self._warning(message="It seems there has been a problem with "
                                  "getting the camera's shape name.\nPlease "
                                  "make sure a correct name is assigned")

        # Check for nodes type
        if pm.nodeType(pxr_projector) != "PxrProjector":
            self._warning(message="It seems {0} is not a correct "
                                  "node type.\nPlease make sure correct node "
                                  "is selected.\nIt must be PxrProjector node"
                                  "".format(pxr_projector))
            return

        if pm.nodeType(cam_projector_shape) != "camera":
            self._warning(message="It seems {0} is not a correct "
                                  "node type.\nPlease make sure correct node "
                                  "is selected.\n It must be camera's "
                                  "name".format(cam_projector))
            return

        if pm.nodeType(place3d) != "place3dTexture":
            self._warning(message="It seems {0} is not a correct "
                                  "node type.\nPlease make sure correct node "
                                  "is selected.\n It must be "
                                  "place3dTexture".format(place3d))
            return

        # Accessing the nodes

        place3d_node = pm.PyNode(place3d)
        cam_projector_node = pm.PyNode(cam_projector)
        cam_projector_shape_node = cam_projector_node.getShape()
        pxr_projector_node = pm.PyNode(pxr_projector)

        # Connecting the attributes
        cord_att = '{0}.coordsys'.format(pxr_projector)
        pm.setAttr(cord_att, place3d)

        if self.link_radio_btn.isChecked():
            pm.pointConstraint(cam_projector_node, place3d_node)
            pm.orientConstraint(cam_projector_node, place3d_node)

            cam_projector_shape_node.focalLength.connect(
                pxr_projector_node.focalLength)
            cam_projector_shape_node.horizontalFilmAperture.connect(
                pxr_projector_node.apertureX)
            cam_projector_shape_node.verticalFilmAperture.connect(
                pxr_projector_node.apertureY)
            cam_projector_shape_node.nearClipPlane.connect(
                pxr_projector_node.nearClipPlane)
            cam_projector_shape_node.farClipPlane.connect(
                pxr_projector_node.farClipPlane)
        else:
            pxr_projector_node.focalLength.set(
                cam_projector_shape_node.focalLength.get())
            pxr_projector_node.apertureX.set(
                cam_projector_shape_node.horizontalFilmAperture.get())
            pxr_projector_node.apertureY.set(
                cam_projector_shape_node.verticalFilmAperture.get())
            pxr_projector_node.nearClipPlane.set(
                cam_projector_shape_node.nearClipPlane.get())
            pxr_projector_node.farClipPlane.set(
                cam_projector_shape_node.farClipPlane.get())

            place3d_node.setTranslation(cam_projector_node.getTranslation(
                space='world'), space='world')
            place3d_node.setRotation(cam_projector_node.getRotation(
                space='world'), space='world')


def create_ui():
    """
    Create a instance of the PrmanProjectionUi and shows the window
    :return: QDialog
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
