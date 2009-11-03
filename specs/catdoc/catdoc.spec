# $Id$
# Authority: dries
# Upstream: Victor Wagner <vitus$45,free,net>

Summary: Decodes MS Word files into plain text or TeX format
Name: catdoc
Version: 0.94.2
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://www.45.free.net/~vitus/software/catdoc/

Source: http://ftp.45.free.net/pub/catdoc/catdoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tcl, tk

%description
Catdoc is a MS Word file decoding tool that doesn't attempt to
analyze file formatting (it just extracts readable text), but
is able to handle all versions of Word and convert character
encodings. A Tcl/Tk graphical viewer is also included. It can
also read RTF files and convert Excel and PowerPoint files.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall LIB_DIR=%{buildroot}%{_datadir}/catdoc
%{__install} -d %{buildroot}%{_mandir}/man1
%{__mv} %{buildroot}%{_mandir}/*.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS INSTALL NEWS README TODO
%doc %{_mandir}/man1/*
%{_bindir}/catdoc
%{_bindir}/catppt
%{_bindir}/wordview
%{_bindir}/xls2csv
%dir %{_datadir}/catdoc
%{_datadir}/catdoc/*.txt
%{_datadir}/catdoc/*.*chars

%changelog
* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.94.2-1
- Updated to release 0.94.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
