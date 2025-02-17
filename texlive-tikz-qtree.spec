Name:		texlive-tikz-qtree
Version:	26108
Release:	2
Summary:	Use existing qtree syntax for trees in TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-qtree
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-qtree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-qtree.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro for drawing trees with TikZ using
the easy syntax of Alexis Dimitriadis' Qtree. It improves on
TikZ's standard tree-drawing facility by laying out tree nodes
without collisions; it improves on Qtree by adding lots of
features from TikZ (for example, edge labels, arrows between
nodes); and it improves on pst-qtree in being usable with
pdfTeX and XeTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-qtree/pgfsubpic.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/pgfsubpic.tex
%{_texmfdistdir}/tex/latex/tikz-qtree/pgftree.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/pgftree.tex
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree-compat.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree.sty
%{_texmfdistdir}/tex/latex/tikz-qtree/tikz-qtree.tex
%doc %{_texmfdistdir}/doc/latex/tikz-qtree/README
%doc %{_texmfdistdir}/doc/latex/tikz-qtree/tikz-qtree-manual.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-qtree/tikz-qtree-manual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
