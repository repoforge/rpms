# $Id$
# Authority: matthias

Summary: Easy to use client for ED2K Peer-to-Peer Network based on eMule
Name: amule
Version: 1.2.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.aMule.org/

Source: http://dl.sf.net/amule/aMule-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, wxGTK-devel, curl-devel >= 7.9.7, zlib-devel, gettext
# Required on Yellwo Dog Linux 3.0
BuildRequires: openssl-devel, bc
Requires: wxGTK, curl, /usr/sbin/alternatives

%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer Network.
It is originally based on eMule, the popular windows-only client for the
same network.

%prep
%setup -n aMule-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/ed2k %{buildroot}%{_bindir}/ed2k.%{name}
%find_lang %{name}

%post
/usr/sbin/alternatives --install %{_bindir}/ed2k ed2k %{_bindir}/ed2k.%{name} 60

%preun
/usr/sbin/alternatives --remove ed2k %{_bindir}/ed2k.%{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc docs/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Tue Feb 17 2004 Matthias Saou <http://freshrpms.net/> 1.2.6-1.fr
- Update to 1.2.6.

* Tue Feb 10 2004 Matthias Saou <http://freshrpms.net/> 1.2.5-1.fr
- Update to 1.2.5.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-2.fr
- Added alternatives support for the ed2k binary between amule and xmule.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-1.fr
- Initial RPM package.

