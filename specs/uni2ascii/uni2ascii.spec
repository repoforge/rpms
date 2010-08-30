# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Convert between UTF-8 Unicode and 7-bit ASCII equivalents
Name: uni2ascii
Version: 4.15
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.billposer.org/Software/uni2ascii.html

Source: http://billposer.org/Software/Downloads/uni2ascii-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

%description
uni2ascii and ascii2uni convert between UTF-8 Unicode and more than a
dozen 7-bit ASCII equivalents including: hexadecimal and decimal HTML
numeric character references, \u-escapes, standard hexadecimal, raw
hexadecimal, and RFC2396 URI format. Such ASCII equivalents are
encountered in a variety of circumstances, such as when Unicode text is
included in program source, when entering text into Web programs that can
handle the Unicode character set but are not 8-bit safe, and when debugging.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__install} -d -m0755 %{buildroot}%{_bindir}
#%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
#%{__install} -d -m0755 %{buildroot}%{_datadir}/locale/
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL README
%doc %{_mandir}/man1/ascii2uni.1*
%doc %{_mandir}/man1/uni2ascii.1*
%{_bindir}/ascii2uni
%{_bindir}/u2a
%{_bindir}/uni2ascii

%changelog
* Mon Aug 30 2010 Dag Wieers <dag@wieers.com> - 4.15-1
- Updated to release 4.15.

* Wed Aug 12 2009 Dag Wieers <dag@wieers.com> - 4.14-1
- Updated to release 4.14.

* Sun Apr 26 2009 Dries Verachtert <dries@ulyssis.org> - 4.13-1
- Updated to release 4.13.

* Sat Apr 04 2009 Dag Wieers <dag@wieers.com> - 4.12-1
- Updated to release 4.12.

* Sun Oct 05 2008 Dag Wieers <dag@wieers.com> - 4.11-1
- Updated to release 4.11.

* Mon Sep  1 2008 Dries Verachtert <dries@ulyssis.org> - 4.10-1
- Updated to release 4.10.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 4.9-1
- Updated to release 4.9.

* Sun May 04 2008 Dag Wieers <dag@wieers.com> - 4.8-1
- Updated to release 4.8.

* Sun Apr 27 2008 Dag Wieers <dag@wieers.com> - 4.7-1
- Updated to release 4.7.

* Sun Apr  6 2008 Dries Verachtert <dries@ulyssis.org> - 4.6-1
- Updated to release 4.6.

* Thu Mar 20 2008 Dries Verachtert <dries@ulyssis.org> - 4.5-1
- Updated to release 4.5.

* Tue Jan 15 2008 Dries Verachtert <dries@ulyssis.org> - 4.4-1
- Updated to release 4.4.

* Mon Aug 13 2007 Dries Verachtert <dries@ulyssis.org> - 4.3.2-1
- Updated to release 4.3.2.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 4.3-1
- Updated to release 4.3.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 4.2-1
- Updated to release 4.2.

* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 4.1-1
- Updated to release 4.1.

* Sat Feb 24 2007 Dries Verachtert <dries@ulyssis.org> - 4.0-1
- Updated to release 4.0.

* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 3.13-1
- Updated to release 3.13.

* Thu Jan 11 2007 Dag Wieers <dag@wieers.com> - 3.12-1
- Updated to release 3.12.

* Thu Dec 21 2006 Dries Verachtert <dries@ulyssis.org> - 3.11-1
- Updated to release 3.11.

* Tue Dec 05 2006 Dries Verachtert <dries@ulyssis.org> - 3.10-1
- Updated to release 3.10.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.9.5-1
- Updated to release 3.9.5.

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 3.9.3-1
- Updated to release 3.9.3.

* Wed May 17 2006 Dag Wieers <dag@wieers.com> - 3.9-1
- Updated to release 3.9.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 3.8-1
- Updated to release 3.8.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 3.7-1
- Updated to release 3.7.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 3.6-1
- Updated to release 3.6.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 3.5.2-1
- Updated to release 3.5.2.

* Sun Mar 12 2006 Dag Wieers <dag@wieers.com> - 3.5-1
- Updated to release 3.5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 3.4-1
- Updated to release 3.4.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Updated to release 3.3.

* Tue Jan 17 2006 Dag Wieers <dag@wieers.com> - 3.2-1
- Updated to release 3.2.

* Thu Jan 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.1-1
- Updated to release 3.1.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-2
- Fix files section.

* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Mon Oct 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Initial package.
