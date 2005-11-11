# $Id$
# Authority: dries
# Upstream: Bill Poser <billposer$alum,mit,edu>

Summary: Convert between UTF-8 Unicode and 7-bit ASCII equivalents
Name: uni2ascii
Version: 2.6
Release: 2
License: GPL
Group: Applications/Publishing
URL: http://billposer.org/Software/uni2ascii.html

Source: http://billposer.org/Software/Downloads/uni2ascii.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__make} %{?_smp_mflags} BINDIR=%{_bindir} MANDIR=%{_mandir}/man1 LOCALEDIR=%{_datadir}/locale

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} \
  %{buildroot}%{_mandir}/man1 \
  %{buildroot}%{_datadir}/locale
%makeinstall BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1 LOCALEDIR=%{buildroot}%{_datadir}/locale

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL README
%doc %{_mandir}/man1/ascii2uni*
%doc %{_mandir}/man1/uni2ascii*
%{_bindir}/ascii2uni*
%{_bindir}/uni2ascii*
%{_bindir}/uni2html*

%changelog
* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-2
- Fix files section.

* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Mon Oct 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Initial package.
