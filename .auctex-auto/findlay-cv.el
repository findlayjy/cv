(TeX-add-style-hook
 "findlay-cv"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("ulem" "normalem") ("FiraSans" "sfdefault" "scaled=.85") ("geometry" "margin=1.2in" "lmargin=2.3cm" "rmargin=2.3cm" "centering" "marginparsep=0.8cm") ("xcolor" "svgnames") ("hyperref" "breaklinks" "hidelinks")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "graphicx"
    "fontenc"
    "inputenc"
    "microtype"
    "ulem"
    "FiraSans"
    "newtxsf"
    "setspace"
    "multicol"
    "enumitem"
    "layouts"
    "geometry"
    "calc"
    "xcolor"
    "titleps"
    "array"
    "longtable"
    "suffix"
    "hyperref"
    "marginnote"
    "etoolbox"
    "tabularx"
    "fontawesome")
   (TeX-add-symbols
    '("ContactInfo" 1)
    '("pubsubhead" 1)
    '("cvsubsubhead" 1)
    '("rulesubhead" 1)
    '("cvsubhead" 1)
    '("cvheading" 1)
    '("researchsubhead" 1)
    '("Label" 1)
    '("Note" 2)
    '("longdate" 1)
    '("sref" 1)
    '("oa" 2)
    '("slides" 1)
    '("poster" 1)
    '("handout" 1)
    '("publinkout" 2)
    '("Reff" 3)
    '("oicon" 1)
    '("icon" 1)
    '("linkout" 2)
    '("mylink" 2)
    '("REx" 2)
    "name"
    "dateratio"
    "bodyratio"
    "mylink"
    "refmark"
    "Reff"
    "note"
    "LaTeX"
    "TeX"
    "conv")
   (LaTeX-add-labels
    "#1"
    "scholarship")
   (LaTeX-add-environments
    "cvsection"
    "reviewlist")
   (LaTeX-add-pagestyles
    "main"
    "first")
   (LaTeX-add-counters
    "RefNo"
    "dummy")
   (LaTeX-add-lengths
    "rulelength"
    "indentlength"
    "squish")
   (LaTeX-add-xcolor-definecolors
    "gold"
    "green"
    "oxfordblue"
    "hlinkcolor")
   (LaTeX-add-array-newcolumntypes
    "L"
    "R"))
 :latex)

