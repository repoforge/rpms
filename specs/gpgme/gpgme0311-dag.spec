# Authority: atrpms
%define rname gpgme

Summary: GnuPG Made Easy.
Name: gpgme0311
Version: 0.3.11
Release: 0
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/gpgme.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnupg.org/gcrypt/alpha/gpgme/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: gnupg >= 1.0.6
Conflicts: gpgme <= 0.3.11, libgpgme <= 0.3.11

%description
GPGME - GnuPG Made Easy

%prep
%setup -n %{rname}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_bindir} \
		%{buildroot}%{_includedir} \
		%{buildroot}%{_libdir}/*.a \
		%{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/*.so \
		%{buildroot}%{_datadir} \
		%{buildroot}%{_infodir}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%changelog
* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.3.11-0
- Renamed to gpgme0311.

* Sun Sep 29 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.3.11.
- Rebuilt against Red Hat Linux 8.0.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Apr 22 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.3.5.

* Wed Sep 19 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.2.3.

* Thu Aug 30 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
