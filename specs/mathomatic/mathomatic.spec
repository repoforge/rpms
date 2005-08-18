# $Id$
# Upstream: George J. Gesslein II <gesslein$panix,com>
# Authority: dries
# Screenshot: http://images.freshmeat.net/screenshots/37777.gif

Summary: Small, portable symbolic math program
Name: mathomatic
Version: 12.4.9
Release: 1
License: LGPL
Group: Applications/Engineering
URL: http://www.mathomatic.com/

Source: http://www.panix.com/~gesslein/mathomatic-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Mathomatic is a small, portable symbolic math program that can automatically
solve, simplify, differentiate, combine, and compare algebraic equations,
perform polynomial and complex arithmetic, etc. It was written by George
Gesslein II and has been under development since 1986.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt doc/*.htm
%doc %{_mandir}/man1/mathomatic.1*
%{_bindir}/mathomatic
%exclude %{_usr}/doc/

%changelog
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
