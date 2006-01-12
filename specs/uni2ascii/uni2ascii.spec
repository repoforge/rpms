# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Convert between UTF-8 Unicode and 7-bit ASCII equivalents
Name: uni2ascii
Version: 3.1
Release: 1
License: GPL
Group: Applications/Text
URL: http://billposer.org/Software/uni2ascii.html

Source: http://billposer.org/Software/Downloads/uni2ascii-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

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
%{__make} %{?_smp_mflags} BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1" LOCALEDIR="%{_datadir}/locale"

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1 %{buildroot}%{_datadir}/locale
%makeinstall BINDIR=%{buildroot}%{_bindir} MANDIR="%{buildroot}%{_mandir}/man1" LOCALEDIR="%{buildroot}%{_datadir}/locale"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL README
%doc %{_mandir}/man1/ascii2uni.1*
%doc %{_mandir}/man1/uni2ascii.1*
%{_bindir}/u2a
%{_bindir}/ascii2uni*
%{_bindir}/uni2ascii*
# isn't included anymore in 2.6 ?
#%{_bindir}/uni2html*

%changelog
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
