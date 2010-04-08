# $Id$
# Authority: shuff
# Upstream: Raph Levien <raph.levien$gmail,com>


%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

Summary: High-resolution programmer's font
Name: inconsolata-fonts
Version: 0.1
Release: 1%{?dist}
License: SIL Open Font License
Group: User Interface/X
URL: http://levien.com/type/myfonts/inconsolata.html

Source0: http://levien.com/type/myfonts/Inconsolata.otf
Source1: http://levien.com/type/myfonts/Inconsolata.pfa
Source2: http://levien.com/type/myfonts/Inconsolata.sfd
Source3: http://levien.com/type/myfonts/textest.pdf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_fontconfig:Requires: fontconfig}

%description
Inconsolata is a monospace font, designed for code listings and the like, in
print. There are a great many "programmer fonts," designed primarily for use on
the screen, but in most cases do not have the attention to detail for high
resolution rendering. 

Inconsolata draws from many inspirations and sources. I was particularly struck
by the beauty of Luc(as) de Groot's Consolas, which is his monospaced design
for Microsoft's upcoming Vista release. This font, similar to his earlier
TheSansMono, demonstrated clearly to me that monospaced fonts do not have to
suck.

First and foremost, Inconsolata is a humanist sans design. I strove for the
clarity and clean lines of Adrian Frutiger's Avenir (the lowercase "a", in
particular, pays homage to this wonderful design), but also looked to Morris
Fuller Benton's Franklin Gothic family for guidance on some of my favorite
glyphs, such as lowercase "g" and "S", and, most especially, the numerals.

Designing a monospace font poses unique challenges. I have carefully studied
many other monospaced fonts to see how they solve these problems. Many of the
available monospace fonts are adaptations of existing proportionally-spaced
fonts, but some, such as Letter Gothic, draw strength from being their own
designs. I hope Inconsolata upholds that tradition.

Some details will be most apparent in print, such as the subtle curves in
lowercase "t", "v", "w", and "y". Inconsolata also borrows "micro-serifs" from
some Japanese Gothic fonts, which enhance the appearance of crispness and
legibility.

%package devel
Summary: FontForge source and spec sheet for Inconsolata
Group: User Interface/X
Requires: %{name} = %{version}
Requires: fontforge

%description devel
Install this package if you want to view or modify the FontForge source for
Inconsolata, or if you'd like to see the spec sheet.

%prep
%setup -T -c %{name}-%{version}

%build
%{__cp} %{_sourcedir}/Inconsolata.* .
%{__cp} %{_sourcedir}/textest.pdf .

%install
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/inconsolata/
%{__install} -p -m0644 *.otf %{buildroot}%{_datadir}/fonts/inconsolata/
%{__install} -p -m0644 *.pfa %{buildroot}%{_datadir}/fonts/inconsolata/

%post
%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
	%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%{_datadir}/fonts/inconsolata/

%files devel
%defattr(-, root, root, 0755)
%doc Inconsolata.sfd textest.pdf

%changelog
* Thu Apr 08 2010 Steve Huff <shuff@vecna.org> - 0.1-1
- Initial package.
