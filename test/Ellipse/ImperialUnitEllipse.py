from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit

from super_scad_circle_plus.Ellipse import Ellipse


class ImperialUnitEllipse(ScadWidget):
    """
    Class for an imperial unit ellipse.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self.imperial_ellipse: Ellipse | None = None
        """
        The imperial unit ellipse.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_ellipse = Ellipse(radius_x=2.0, radius_y=1.0)

        return self.imperial_ellipse

# ----------------------------------------------------------------------------------------------------------------------
