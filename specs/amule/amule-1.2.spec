# $Id$
# Authority: matthias

#define prever rc5

Summary: Easy to use client for ED2K Peer-to-Peer Network based on eMule
Name: amule
Version: 1.2.8
Release: %{?prever:0.%{prever}.}1%{?dist}
License: GPL
Group: Applications/Internet
Source: http://download.berlios.de/amule/aMule-%{version}%{?prever}.tar.bz2
URL: http://www.aMule.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: wxGTK, curl
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
BuildRequires: gcc-c++, wxGTK-devel, curl-devel >= 7.9.7, zlib-devel, gettext
# Required on Yellow Dog Linux 3.0
BuildRequires: openssl-devel

%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer Network.
It is originally based on eMule, the popular windows-only client for the
same network.


%prep
%setup -n aMule-%{version}%{?prever}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_bindir}/ed2k %{buildroot}%{_bindir}/ed2k.%{name}
%find_lang %{name}
# Move the docs back to be included with %%doc
%{__mv} %{buildroot}%{_defaultdocdir}/aMule-* _docs


%post
/usr/sbin/alternatives --install %{_bindir}/ed2k ed2k %{_bindir}/ed2k.%{name} 60 || :

%preun
/usr/sbin/alternatives --remove ed2k %{_bindir}/ed2k.%{name} || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc _docs/*
%{_bindir}/*
%{_datadir}/amuleweb/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm


%changelog
* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 1.2.8-1
- Downgrade to 1.2.8 to provide aMule on platforms where 2.0.x (cryptopp)
  doesn't compile.

* Wed Jul 21 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc5.1
- Update to 2.0.0rc5.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc4a.1
- Update to 2.0.0rc4a.

* Tue Jul 13 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc4.1
- Update to 2.0.0rc4.
- Add workaround for installed docs.

* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc3.1
- Update to 2.0.0rc3.

* Tue Feb 17 2004 Matthias Saou <http://freshrpms.net/> 1.2.6-1.fr
- Update to 1.2.6.

* Tue Feb 10 2004 Matthias Saou <http://freshrpms.net/> 1.2.5-1.fr
- Update to 1.2.5.

* Mon Jan 12 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-2.fr
- Added alternatives support for the ed2k binary between amule and xmule.

* Sun Jan 11 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-1.fr
- Initial RPM package.

