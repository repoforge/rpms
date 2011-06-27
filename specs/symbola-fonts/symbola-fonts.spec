# $Id$
# Authority: shuff
# Upstream: George Douros <g1951d$teilar,gr>

%{?el2:%define _without_fontconfig 1}

%define real_version 605

Summary: Unicode symbol font
Name: symbola-fonts
Version: 6.05
Release: 1%{?dist}
License: Public Domain
Group: User Interface/X
URL: http://users.teilar.gr/~g1951d/

Source0: http://users.teilar.gr/~g1951d/Symbola%{real_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_fontconfig:Requires: fontconfig}

%description
Symbola covers the following scripts and symbols supported by Unicode: Basic
Latin, IPA Extensions, Spacing Modifier Letters, Combining Diacritical Marks,
Greek and Coptic, Cyrillic, Cyrillic Supplement, General Punctuation,
Superscripts and Subscripts, Currency Symbols, Combining Diacritical Marks for
Symbols, Letterlike Symbols, Number Forms, Arrows, Mathematical Operators,
Miscellaneous Technical, Control Pictures, Optical Character Recognition, Box
Drawing, Block Elements, Geometric Shapes, Miscellaneous Symbols, Dingbats,
Miscellaneous Mathematical Symbols-A, Supplemental Arrows-A, Supplemental
Arrows-B, Miscellaneous Mathematical Symbols-B, Supplemental Mathematical
Operators, Miscellaneous Symbols and Arrows, Supplemental Punctuation, Yijing
Hexagram Symbols, Combining Half Marks, Specials, Byzantine Musical Symbols,
Musical Symbols, Ancient Greek Musical Notation, Tai Xuan Jing Symbols,
Counting Rod Numerals, Mathematical Alphanumeric Symbols, Mahjong Tiles, Domino
Tiles, Playing Cards, Miscellaneous Symbols And Pictographs, Emoticons,
Transport And Map Symbols, Alchemical Symbols, et al.

%prep
%setup -c %{name}-%{version}

%build

%install
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/symbola/
%{__install} -p -m0644 *.ttf %{buildroot}%{_datadir}/fonts/symbola/

%post
%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
	%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc Symbola%{real_version}.pdf
%doc Symbola%{real_version}.txt
%{_datadir}/fonts/symbola/

%changelog
* Mon Jun 27 2011 Steve Huff <shuff@vecna.org> - 6.05-1
- Initial package.
