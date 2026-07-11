%global tl_name tikz-qtree
%global tl_revision 26108

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Use existing qtree syntax for trees in TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-qtree
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-qtree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-qtree.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a macro for drawing trees with TikZ using the easy
syntax of Alexis Dimitriadis' Qtree. It improves on TikZ's standard
tree-drawing facility by laying out tree nodes without collisions; it
improves on Qtree by adding lots of features from TikZ (for example,
edge labels, arrows between nodes); and it improves on pst-qtree in
being usable with pdfTeX and XeTeX.

