# $Id$
# Authority: matthias
# ExclusiveDist: fc6 fc7

Summary: RSA encryption support for Pidgin
Name: pidgin-encryption
Version: 3.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://pidgin-encrypt.sourceforge.net/
Source: http://downloads.sf.net/pidgin-encrypt/pidgin-encryption-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: pidgin
BuildRequires: pidgin-devel, gtk2-devel, nss-devel, nspr-devel
Obsoletes: gaim-encryption < 3.0-1

%description
Pidgin-Encryption transparently encrypts your instant messages with RSA
encryption. Easy-to-use, but very secure.


%prep
%setup
# Some files are executable for no good reason
%{__chmod} -x *.h *.c README


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG COPYING NOTES README TODO WISHLIST
%{_libdir}/pidgin/encrypt.so
%exclude %{_libdir}/pidgin/encrypt.a
%exclude %{_libdir}/pidgin/encrypt.la
%{_datadir}/pixmaps/pidgin/pidgin-encryption/


%changelog
* Tue Jun  5 2007 Matthias Saou <http://freshrpms.net/> 3.0-1
- Initial RPM releases, based in the gaim-encryption spec file.

