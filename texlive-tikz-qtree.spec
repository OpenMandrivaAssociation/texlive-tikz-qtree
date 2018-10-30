# revision 26108
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-qtree
# catalog-date 2012-04-23 11:23:52 +0200
# catalog-license gpl
# catalog-version 1.2
Name:		texlive-tikz-qtree
Version:	1.2
Release:	2
Summary:	Use existing qtree syntax for trees in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-qtree
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-qtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-qtree.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.20-1
+ Revision: 805126
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.12-2
+ Revision: 756913
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.12-1
+ Revision: 719746
- texlive-tikz-qtree
- texlive-tikz-qtree
- texlive-tikz-qtree

