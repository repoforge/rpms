# $Id$
# Authority: matthias

%define desktop_vendor rpmforge
#define pre            rc4
%define final          final

Summary: Downloader for X that supports resuming and many other features
Name: d4x
Version: 2.5.0
Release: %{?pre:0.%{pre}.}1%{?dist}
Group: Applications/Internet
License: Artistic
URL: http://www.krasu.ru/soft/chuchelo/
Source: http://www.krasu.ru/soft/chuchelo/files/d4x-%{version}%{?pre}%{?final}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, glib2-devel >= 2.4.0, gcc-c++, libstdc++-devel
BuildRequires: libao-devel, esound-devel, desktop-file-utils

%description
This program lets you download files from the internet using either the ftp
or http protocols. The main features are : Multithread, user-friendly GTK+
interface, resuming, multiple simultaneous downloads, recursive downloads
with wildcard and filter support, HTML links change for offline browsing,
proxy support, bandwidth limitation, scheduling, mass download, ftp search,
and many others!


%prep
%setup -n %{name}-%{version}%{?pre}%{?final}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Now the menu entry
%{__install} -Dp -m644 share/nt.png %{buildroot}%{_datadir}/pixmaps/nt.png
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category Application                    \
  --add-category Network                        \
  share/nt.desktop


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING NEWS PLANS README TODO
%doc DOC/FAQ* DOC/THANKS DOC/TROUBLES
%{_bindir}/nt
%{_datadir}/applications/%{desktop_vendor}-nt.desktop
%{_datadir}/d4x
%{_datadir}/pixmaps/nt.png
%{_mandir}/man1/nt.1*


%changelog
* Mon Aug  9 2004 Matthias Saou <http://freshrpms.net/> 2.5.0-1
- Update to 2.5.0final.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 2.5.0-0.rc4.4
- Update to 2.5.0rc4.

* Mon May 24 2004 Matthias Saou <http://freshrpms.net/> 2.5.0-0.rc3.4
- Added patch for gtk 2.4 compatibility from Den.

* Tue Apr 20 2004 Matthias Saou <http://freshrpms.net/> 2.5.0-0.rc3.3
- Update to 2.5.0rc3.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 2.5.0-0.rc2.3
- Update to 2.5.0rc2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.5.0-0.beta2.2
- Fix wrong exclude in file list left in by mistake.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.5.0-0.beta2.1
- Update to 2.5.0beta2.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.1.
- Exclude the docs from the datadir.
- Rebuilt for Red Hat Linux 9.

* Wed Aug 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.03.

* Thu Jun  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.01.
- Major spec file cleanup.

* Sat Nov 24 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.30.

* Sun Sep  9 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.29.

* Mon Aug 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.28.1.

* Wed Aug  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.28.

* Wed May  2 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat 7.1.

* Mon Oct 30 2000 Maxim Koshelev <mdem@chat.ru>
- fixed building under RH-70 or Mandrake-7x

