# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Sort files in sophisticated ways
Name: msort
Version: 8.53
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://billposer.org/Software/msort.html

Source: http://billposer.org/Software/Downloads/msort-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tre-devel, libuninum-devel >= 2.5, utf8proc-devel, gmp-devel

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
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING Doc/* INSTALL NEWS README
%doc %{_mandir}/man1/msort.1*
%{_bindir}/msg
%{_bindir}/msort

%changelog
* Tue Jan 12 2010 Dag Wieers <dag@wieers.com> - 8.53-1
- Updated to release 8.53.

* Thu Dec 11 2008 Dries Verachtert <dries@ulyssis.org> - 8.52-1
- Updated to release 8.52.

* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 8.51-1
- Updated to release 8.51.

* Tue Sep 30 2008 Dag Wieers <dag@wieers.com> - 8.50-1
- Updated to release 8.50.

* Sun Sep 21 2008 Dries Verachtert <dries@ulyssis.org> - 8.48-1
- Updated to release 8.48.

* Sun Jul  6 2008 Dries Verachtert <dries@ulyssis.org> - 8.47-1
- Updated to release 8.47.

* Fri May 30 2008 Dries Verachtert <dries@ulyssis.org> - 8.46-1
- Updated to release 8.46.

* Tue May 20 2008 Dries Verachtert <dries@ulyssis.org> - 8.45-1
- Updated to release 8.45.

* Sat Apr 12 2008 Dries Verachtert <dries@ulyssis.org> - 8.44-1
- Updated to release 8.44.

* Sun Jan 27 2008 Dries Verachtert <dries@ulyssis.org> - 8.43-1
- Updated to release 8.43.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 8.40-1
- Rebuild against libuninum 2.5.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 8.40-1
- Updated to release 8.40.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 8.38-1
- Updated to release 8.38.

* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 8.37-1
- Updated to release 8.37.

* Sat Jan 27 2007 Dries Verachtert <dries@ulyssis.org> - 8.36.1-1
- Updated to release 8.36.1.

* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 8.35-1
- Updated to release 8.35.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 8.34-1
- Updated to release 8.34.

* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 8.33-1
- Updated to release 8.33.

* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 8.32-1
- Updated to release 8.32.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 8.31.2-1
- Updated to release 8.31.2.

* Sun Dec 10 2006 Dries Verachtert <dries@ulyssis.org> - 8.31-1
- Updated to release 8.31.

* Thu Nov 30 2006 Dries Verachtert <dries@ulyssis.org> - 8.30-1
- Updated to release 8.30.

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
