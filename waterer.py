def svg(depth):
    stack = ""
    increment = 188
    for i in range(0, depth):
        increment = increment - 5
        ellipse = """
        <ellipse
           cx="98.548164"
           cy="{0}"
           rx="34.815063"
           ry="9.3059664"
           id="ellipse3716{1}"
           style="display:inline;fill:#2a7fff;stroke:#2a7fff;stroke-width:0.255774" />
               """
        stack = stack + ellipse.format(increment, i)

    head = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   viewBox="0 0 210 297"
   version="1.1"
   id="svg8"
   inkscape:version="1.0 (4035a4f, 2020-05-01)"
   sodipodi:docname="waterer_ouline.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.6743757"
     inkscape:cx="396.85039"
     inkscape:cy="561.25984"
     inkscape:document-units="mm"
     inkscape:current-layer="layer2"
     inkscape:document-rotation="0"
     showgrid="false"
     inkscape:window-width="1680"
     inkscape:window-height="923"
     inkscape:window-x="0"
     inkscape:window-y="25"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="svg"
     inkscape:groupmode="layer"
     id="layer1"
     style="display:inline">
    <path
       id="path897"
       transform="scale(0.26458333)"
       d="m 372.61523,649.32617 a 176.6609,55.523399 0 0 1 0.98047,0 176.6609,55.523399 0 0 1 176.66211,55.52344 176.6609,55.523399 0 0 1 -176.66211,55.52344 176.6609,55.523399 0 0 1 -176.66015,-55.52344 176.6609,55.523399 0 0 1 175.67968,-55.52344 z"
       style="fill:#999999;stroke:#000000;stroke-width:1.58608" />
    <path
       id="path893"
       transform="scale(0.26458333)"
       d="m 372.4668,641.35742 a 185.96928,63.759753 0 0 0 -185.64258,63.75977 185.96928,63.759753 0 0 0 185.96875,63.75976 185.96928,63.759753 0 0 0 185.96875,-63.75976 185.96928,63.759753 0 0 0 -185.96875,-63.75977 185.96928,63.759753 0 0 0 -0.32617,0 z"
       style="fill:#999999;stroke:#000000;stroke-width:1.58608" />
    <path
       sodipodi:nodetypes="csccscc"
       d="m 140.53399,199.63758 c -2.73221,7.49502 -20.35456,13.27793 -41.686547,13.27793 -22.370852,0 -37.363467,-5.5358 -41.648906,-12.46162 -0.715903,-1.17931 -1.614652,-4.64615 -1.750077,-5.62941 -1.063193,-7.91955 22.906405,-12.53281 43.398983,-12.53281 21.275877,0 41.091137,4.44104 43.894207,11.90733 -0.61616,2.72185 -1.14952,3.22534 -2.20766,5.43858 z"
       style="fill:#b3b3b3;stroke:#000000;stroke-width:0.369617"
       id="ellipse851" />
    <path
       transform="scale(0.26458333)"
       d="M 372.4668 641.35742 A 185.96928 63.759753 0 0 0 186.82422 705.11719 A 185.96928 63.759753 0 0 0 372.79297 768.87695 A 185.96928 63.759753 0 0 0 558.76172 705.11719 A 185.96928 63.759753 0 0 0 372.79297 641.35742 A 185.96928 63.759753 0 0 0 372.4668 641.35742 z M 372.61523 649.32617 A 176.6609 55.523399 0 0 1 373.5957 649.32617 A 176.6609 55.523399 0 0 1 550.25781 704.84961 A 176.6609 55.523399 0 0 1 373.5957 760.37305 A 176.6609 55.523399 0 0 1 196.93555 704.84961 A 176.6609 55.523399 0 0 1 372.61523 649.32617 z "
       style="fill:#999999;stroke:#000000;stroke-width:1.58608"
       id="path841" />
    <path
       sodipodi:nodetypes="ssssssscccccccccssssssss"
       transform="scale(0.26458333)"
       d="m 374.19336,257.67773 c -14.33987,-0.17302 -28.98452,1.23995 -41.26563,4.58008 -4.76626,1.29629 -4.28484,6.5515 -9.28711,8.42774 -6.70886,2.51633 -16.24268,2.91297 -23.25,6.48828 -5.13006,2.61749 -2.89692,5.52968 -8.32617,8.7539 -3.42512,2.03405 -19.21949,5.76549 -22.72656,8.04297 -8.06331,5.2363 -4.81184,3.94456 -7.52734,5.76172 -8.41461,5.63089 -23.44979,5.13418 -32.25977,12.23047 v 0.002 413.1836 0 c 2.8193,17.9892 65.76047,32.22837 141.83984,32.22851 76.07937,-1.4e-4 139.16508,-14.23931 141.98438,-32.22851 v 0 -292.83794 c 0.19805,-37.113 0.64062,-120.34766 0.64062,-120.34766 -8.22028,-5.24041 -20.20757,-5.16479 -28.49804,-10.14453 -2.76367,-1.66 -3.91102,-6.97716 -6.6582,-8.58594 -6.8154,-3.9912 -16.66826,-4.10972 -23.20118,-7.63867 -3.78051,-2.04215 -4.82886,-6.64217 -8.51953,-8.52539 -5.64533,-2.88061 -12.38959,-2.29898 -18.12109,-4.52539 -7.91082,-3.07296 -6.65023,-7.55465 -15.38672,-9.92774 -11.06234,-3.00485 -25.09567,-4.76448 -39.43555,-4.9375 z"
       style="fill:#cccccc;stroke:#000000;stroke-width:0.990399"
       id="rect888" />
    <path
       sodipodi:nodetypes="ccccccccccccccccc"
       transform="scale(0.26458333)"
       d="m 370.79492,294.04297 c -71.90795,0.14585 -129.91493,15.84995 -129.91601,35.17187 8.3e-4,0.25393 0.0119,0.50785 0.0332,0.76172 h -0.0156 v 382.67383 c -0.0114,0.18748 -0.0173,0.37499 -0.0176,0.5625 2e-4,0.18881 0.006,0.37762 0.0176,0.56641 v 0.28125 h 0.0215 c 1.71182,19.09002 59.79767,34.32604 130.86523,34.32617 71.06756,-1.3e-4 130.51475,-15.23615 132.22657,-34.32617 v 0 -384.08399 h -1.35352 c 0.0206,-0.25387 0.0311,-0.50779 0.0312,-0.76172 -0.003,-19.42515 -58.6101,-35.1719 -130.9043,-35.17187 -0.32943,-3.3e-4 -0.65885,-3.3e-4 -0.98828,0 z"
       style="fill:#999999;stroke:#000000;stroke-width:0.998608"
       id="rect4365" />
  </g>
  <g
     style="display:inline"
     inkscape:label="water"
     id="layer2"
     inkscape:groupmode="layer">
    <ellipse
       cx="98.548164"
       cy="188.70412"
       rx="34.815063"
       ry="9.3059664"
       id="ellipse3716"
       style="display:inline;fill:#2a7fff;stroke:#2a7fff;stroke-width:0.255774" />
       """
    tail = """
      </g>
    </svg>"""

    return head + stack + tail



