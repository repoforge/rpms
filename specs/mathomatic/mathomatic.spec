# $Id$
# Upstream: George J. Gesslein II <gesslein$panix,com>
# Authority: dries
# Screenshot: http://mathomatic.orgserve.de/math/png/mathomatic_snapshot.png

Summary: Small, portable symbolic math program
Name: mathomatic
Version: 14.0.7
Release: 1
License: LGPL
Group: Applications/Engineering
URL: http://www.mathomatic.org/

Source: http://www.panix.com/~gesslein/mathomatic-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Mathomatic is a small, portable symbolic math program that can automatically
solve, simplify, differentiate, combine, and compare algebraic equations,
perform polynomial and complex arithmetic, etc. It was written by George
Gesslein II and has been under development since 1986.

%prep
%setup

%build
%{__make} %{?_smp_mflags} prefix=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%{__make} install prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir}
%{__rm} -rf %{buildroot}%{_datadir}/doc/mathomatic

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt doc/*.html
%doc %{_mandir}/man1/mathomatic.1*
%{_bindir}/mathomatic
%{_datadir}/pixmaps/mathomatic.png
%{_datadir}/applications/mathomatic.desktop

%changelog
* Sun Jul  6 2008 Dries Verachtert <dries@ulyssis.org> - 14.0.7-1
- Updated to release 14.0.7.

* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 14.0.5-1
- Updated to release 14.0.5.

* Mon May 12 2008 Dries Verachtert <dries@ulyssis.org> - 14.0.2-1
- Updated to release 14.0.2.

* Wed Apr 23 2008 Dries Verachtert <dries@ulyssis.org> - 14.0.0-1
- Updated to release 14.0.0.

* Tue Mar 18 2008 Dries Verachtert <dries@ulyssis.org> - 12.9.0-1
- Updated to release 12.9.0.

* Thu Feb 28 2008 Dries Verachtert <dries@ulyssis.org> - 12.8.8-1
- Updated to release 12.8.8.

* Sun Feb  3 2008 Dries Verachtert <dries@ulyssis.org> - 12.8.6-1
- Updated to release 12.8.6.

* Wed Jan  9 2008 Dries Verachtert <dries@ulyssis.org> - 12.8.4-1
- Updated to release 12.8.4.

* Sun Dec 16 2007 Dries Verachtert <dries@ulyssis.org> - 12.8.2-1
- Updated to release 12.8.2.

* Mon Nov 19 2007 Dries Verachtert <dries@ulyssis.org> - 12.8.0-1
- Updated to release 12.8.0.

* Mon Nov  5 2007 Dries Verachtert <dries@ulyssis.org> - 12.7.9-1
- Updated to release 12.7.9.

* Mon Sep 10 2007 Dries Verachtert <dries@ulyssis.org> - 12.7.6-1
- Updated to release 12.7.6.

* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 12.7.5-1
- Updated to release 12.7.5.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 12.7.3-1
- Updated to release 12.7.3.

* Fri May 11 2007 Dries Verachtert <dries@ulyssis.org> - 12.7.0-1
- Updated to release 12.7.0.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 12.6.11-1
- Updated to release 12.6.11.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 12.6.9-1
- Updated to release 12.6.9.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 12.6.7-1
- Updated to release 12.6.7.

* Wed Oct 11 2006 Dries Verachtert <dries@ulyssis.org> - 12.6.5-1
- Updated to release 12.6.5.

* Wed Oct 11 2006 Dries Verachtert <dries@ulyssis.org> - 12.6.4-1
- Updated to release 12.6.4.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 12.6.1-1
- Updated to release 12.6.1.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 12.6.0-1
- Updated to release 12.6.0.

* Fri Aug 04 2006 Dries Verachtert <dries@ulyssis.org> - 12.5.23-1
- Updated to release 12.5.23.

* Wed Jul 26 2006 Dries Verachtert <dries@ulyssis.org> - 12.5.22-1
- Updated to release 12.5.22.

* Thu May 25 2006 Dries Verachtert <dries@ulyssis.org> - 12.5.17-1
- Updated to release 12.5.17.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 12.5.15-1
- Updated to release 12.5.15.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> 12.5.14-1
- Updated to release 12.5.14.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> 12.5.12-1
- Updated to release 12.5.12.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> 12.5.11-1
- Updated to release 12.5.11.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> 12.5.10-1
- Updated to release 12.5.10.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> 12.5.8-1
- Updated to release 12.5.8.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> 12.5.6-1
- Updated to release 12.5.6.

* Thu Dec 29 2005 Dries Verachtert <dries@ulyssis.org> 12.5.5-1
- Updated to release 12.5.5.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> 12.5.4-1
- Update to release 12.5.4.

* Thu Dec 01 2005 Dries Verachtert <dries@ulyssis.org> 12.5.3-1
- Update to release 12.5.3.

* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> 12.5.2-1
- Update to release 12.5.2.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> 12.5.1-1
- Update to release 12.5.1.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> 12.5.0-1
- Update to release 12.5.0.

* Sun Oct 09 2005 Dries Verachtert <dries@ulyssis.org> 12.4.12-1
- Update to release 12.4.12.

* Sat Sep 17 2005 Dries Verachtert <dries@ulyssis.org> 12.4.11-1
- Update to release 12.4.11.

* Tue Aug 30 2005 Dries Verachtert <dries@ulyssis.org> 12.4.10-1
- Update to release 12.4.10.

* Thu Aug 18 2005 Dries Verachtert <dries@ulyssis.org> 12.4.9-1
- Update to release 12.4.9.

* Sat Aug 06 2005 Dries Verachtert <dries@ulyssis.org> 12.4.7-1
- Update to release 12.4.7.

* Sat Jul 30 2005 Dries Verachtert <dries@ulyssis.org> 12.4.6-1
- Update to release 12.4.6.

* Mon Jul 25 2005 Dries Verachtert <dries@ulyssis.org> 12.4.5-2
- Fixed the url (thanks to George John Gesslein II)

* Thu Jul 21 2005 Dries Verachtert <dries@ulyssis.org> 12.4.5-1
- Update to release 12.4.5.

* Wed Jul 06 2005 Dries Verachtert <dries@ulyssis.org> 12.4.4-1
- Update to release 12.4.4.

* Tue Jun 21 2005 Dries Verachtert <dries@ulyssis.org> 12.4.3-1
- Update to release 12.4.3.

* Mon Jun 13 2005 Dries Verachtert <dries@ulyssis.org> 12.4.2-1
- Update to release 12.4.2.

* Sun Apr 10 2005 Dries Verachtert <dries@ulyssis.org> 12.2c-1
- Update to version 12.2c.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> 12.2b-1
- Update to version 12.2b.

* Fri Mar 11 2005 Dries Verachtert <dries@ulyssis.org> 12.1e-1
- Update to version 12.1e.

* Fri Mar 04 2005 Dries Verachtert <dries@ulyssis.org> 12.1d-1
- Update to version 12.1d.

* Sun Feb 20 2005 Dries Verachtert <dries@ulyssis.org> 12.1b-1
- Update to version 12.1b.

* Tue Feb 08 2005 Dries Verachtert <dries@ulyssis.org> 12.0-1
- Update to version 12.0.

* Sat Jan 29 2005 Dries Verachtert <dries@ulyssis.org> 11.7-1
- Update to version 11.7.

* Fri Jan 23 2005 Dries Verachtert <dries@ulyssis.org> 11.6e-1
- Update to version 11.6e.

* Fri Jan 14 2005 Dries Verachtert <dries@ulyssis.org> 11.6d-1
- Update to version 11.6d.

* Sat Jan 06 2005 Dries Verachtert <dries@ulyssis.org> 11.6c-1
- Update to version 11.6c.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> 11.6b-1
- Update to version 11.6b.

* Thu Dec 23 2004 Dries Verachtert <dries@ulyssis.org> 11.6-1
- Update to version 11.6.

* Sun Dec 12 2004 Dries Verachtert <dries@ulyssis.org> 11.5d-1
- Update to version 11.5d.

* Mon Nov 29 2004 Dries Verachtert <dries@ulyssis.org> 11.5c-1
- Update to version 11.5c.

* Tue Nov 23 2004 Dries Verachtert <dries@ulyssis.org> 11.5b-1
- Update to version 11.5b.

* Wed Nov 10 2004 Dries Verachtert <dries@ulyssis.org> 11.5-1
- Update to version 11.5.

* Sat Oct 30 2004 Dries Verachtert <dries@ulyssis.org> 11.4d-1
- Update to version 11.4d.

* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> 11.4c-1
- Update to version 11.4c.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> 11.3f-1
- Update to version 11.3f.

* Sat Aug 21 2004 Dries Verachtert <dries@ulyssis.org> 11.3d-1
- Update to version 11.3d.

* Sun Jul 25 2004 Dries Verachtert <dries@ulyssis.org> 11.3b-1
- Update to version 11.3b.

* Mon Jul 12 2004 Dries Verachtert <dries@ulyssis.org> 11.3-1
- Update to version 11.3.

* Wed Jun 30 2004 Dries Verachtert <dries@ulyssis.org> 11.2d-1
- Update to version 11.2d.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 11.2c-1
- Update to 11.2c.

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> 11.2b-1
- Update to 11.2b.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> 11.1d-1
- Update to 11.1d.

* Tue Apr 27 2004 Dries Verachtert <dries@ulyssis.org> 11.0e-1
- Initial package.
