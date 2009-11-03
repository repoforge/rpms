# $Id: amule.spec 3187 2005-05-04 16:24:16Z thias $
# Authority: matthias

#define prever rc8

Summary: Easy to use client for ED2K Peer-to-Peer Network based on eMule
Name: amule
Version: 2.0.0
Release: 1%{?prever:.%{prever}}.rf%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.aMule.org/

Source: http://download.berlios.de/amule/aMule-%{version}%{?prever}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, wxGTK-devel, curl-devel >= 7.9.7, zlib-devel, gettext
BuildRequires: gd-progs, gd-devel, libidn-devel, libjpeg-devel
# Required on Yellow Dog Linux 3.0
BuildRequires: openssl-devel
# Required for a configure check (curl)
BuildRequires: bc
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives

%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer Network.
It is originally based on eMule, the popular windows-only client for the
same network.

%prep
%setup -n aMule-%{version}%{?prever}

%build
%configure \
    --enable-alc \
    --enable-utf8-systray
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_bindir}/ed2k %{buildroot}%{_bindir}/ed2k.%{name}
%find_lang %{name}
# Move the docs back to be included with %%doc
%{__mv} %{buildroot}%{_defaultdocdir}/aMule-* _docs
# Fix encoding of the desktop entry
for file in %{buildroot}%{_datadir}/applications/*.desktop; do
    iconv -f ISO8859-1 -t UTF-8 -o tmp.desktop ${file}
    %{__mv} tmp.desktop ${file}
done

%post
update-desktop-database -q 2>/dev/null || :
/usr/sbin/alternatives --install %{_bindir}/ed2k ed2k %{_bindir}/ed2k.%{name} 60 || :

%preun
/usr/sbin/alternatives --remove ed2k %{_bindir}/ed2k.%{name} || :

%postun
update-desktop-database -q 2>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc _docs/*
%{_bindir}/*
%{_libdir}/xchat/plugins/xas.pl
%{_datadir}/applications/*.desktop
#{_datadir}/cas/
%{_datadir}/pixmaps/*.xpm
%lang(de) %{_mandir}/de/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(hu) %{_mandir}/hu/man1/*.1*
%{_mandir}/man1/*.1*

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 2.0.0-2
- Rebuild against wxGTK 2.8.8.

* Wed May  4 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Update to 2.0.0 final.
- Add new man pages.
- Explicitly enable alc, as it no longer gets built otherwise.

* Wed Feb  2 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc8.3
- Really fix the UTF-8 alc.desktop problem... it was converted to stdout.

* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc8.2
- Add update-desktop-database calls and convert desktop entry to UTF-8.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc8.1
- Update to 2.0.0rc8.

* Fri Nov 19 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc7.3
- Disable external cryptopp usage, it's a mess :-(

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc7.2
- Disable embedded crypto to use external cryptopp.
- Add gd-progs and gd-devel build dep for gdlib-config to be found.
- Enable UTF8 systray text.
- Enable alcc (aMule link creator for console).

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc7.1
- Update to 2.0.0rc7.

* Fri Jul 30 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-0.rc5.1
- Add "|| :" to alternatives calls to ignore error return codes.

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

