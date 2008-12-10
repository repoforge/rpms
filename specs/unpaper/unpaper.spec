# $Id$
# Authority: dag


Summary: Post-processing of scanned and photocopied book pages
Name: unpaper
Version: 0.3
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://unpaper.berlios.de/

Source: http://download.berlios.de/unpaper/unpaper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
unpaper is a post-processing tool for scanned sheets of paper, especially for
book pages that have been scanned from previously created photocopies. The
main purpose is to make scanned book pages better readable on screen after
conversion to PDF. Additionally, unpaper might be useful to enhance the
quality of scanned pages before performing optical character recognition (OCR).
unpaper tries to clean scanned images by removing dark edges that appeared
through scanning or copying on areas outside the actual page content (e.g. dark
areas between the left-hand-side and the right-hand-side of a double- sided
book-page scan). The program also tries to detect disaligned centering and
rotation of pages and will automatically straighten each page by rotating it to
the correct angle. This process is called "deskewing".

%prep
%setup

%build
%{__cc} %{optflags} -lm -o unpaper src/unpaper.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 unpaper %{buildroot}%{_bindir}/unpaper

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README doc/
%{_bindir}/unpaper

%changelog
* Tue Dec 09 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
