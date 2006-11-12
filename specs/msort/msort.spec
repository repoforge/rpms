# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Sort files in sophisticated ways
Name: msort
%define real_version 8.29
Version: 8.29
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://billposer.org/Software/msort.html

Source: http://billposer.org/Software/Downloads/msort-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tre-devel

%description
Msort is a program for sorting files in sophisticated ways. Records need not
be single lines. Key fields may be selected by position, tag, or character
range. For each key, distinct exclusions, multigraphs, substitutions. and a
sort order may be defined. Comparisons may be lexicographic, numeric, by
string length, date, or time. Optional keys are supported. Msort uses the
Unicode character set and provides full Unicode case-folding. The basic
program has a somewhat complex command line interface, but may be driven
by an optional GUI.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING Doc/* INSTALL NEWS README
%doc %{_mandir}/man1/msort.1*
%{_bindir}/msg
%{_bindir}/msort

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 8.29-1
- Updated to release 8.29.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 8.28-1
- Updated to release 8.28.

* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 8.27-1
- Updated to release 8.27.

* Thu May 25 2006 Dries Verachtert <dries@ulyssis.org> - 8.26-1
- Updated to release 8.26.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 8.25-1
- Updated to release 8.25.

* Mon May 08 2006 Dries Verachtert <dries@ulyssis.org> - 8.24-1
- Updated to release 8.24.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 8.23-1
- Updated to release 8.23.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 8.22-1
- Updated to release 8.22.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 8.21-1
- Updated to release 8.21.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 8.20-1
- Updated to release 8.20.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 8.19-2
- URL & Source fixed.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 8.19-1
- Updated to release 8.19.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 8.18-1
- Updated to release 8.18.

* Sun Feb 19 2006 Dries Verachtert <dries@ulyssis.org> - 8.16-1
- Updated to release 8.16.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 8.15-1
- Updated to release 8.15.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 8.13-1
- Updated to release 8.13.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org> - 8.10-1
- Updated to release 8.10.

* Tue Oct 18 2005 Dries Verachtert <dries@ulyssis.org> - 8.9-1
- Initial package.
