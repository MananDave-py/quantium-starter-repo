from dashapp import app

def test_header_present(dash_duo):
    """
    Test to check if the header component is present in the layout.
    """
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

def test_visualisation_present(dash_duo):
    """
    Test to check if the visualisation (graph) component is present in the layout.
    """
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#main-chart", timeout=10)

def test_region_picker_present(dash_duo):
    """
    Test to check if the region picker (radio items) component is present in the layout.
    """
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=10)
