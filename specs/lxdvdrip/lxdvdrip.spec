# $Id$
# Authority: dag

Summary: DVD backup tool
Name: lxdvdrip
Version: 1.76
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://lxdvdrip.berlios.de/

Source: http://download.berlios.de/lxdvdrip/lxdvdrip-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: dvdauthor
#Requires: dvdbackup
Requires: dvd+rw-tools
Requires: mplayer
#Requires: streamdvd
Requires: transcode

%description
lxdvdrip is a tool to make a copy from a Video DVD for private use.  It
automates the process of ripping, authoring, preview and burning a DVD.

%prep
%setup -n %{name}

### I never saw so many Makefiles being inconsistent in 1 project
%{__perl} -pi.orig -e '
        s|(-ldvdread)|$1 -ldl|g;
        s|\$\(INSTALLDIR\)/bin|\$(DESTDIR)%{_bindir}|g;
        s|\$\(INSTALLDIR\)/man/man1|\$(DESTDIR)%{_mandir}/man1|g;
        s|\$\(INSTALLDIR\)/share|\$(DESTDIR)%{_datadir}/lxdvdrip|g;
        s|/etc\b|\$(DESTDIR)%{_sysconfdir}|g;
        s|\$\(PREFIX\)/bin|\$(DESTDIR)%{_bindir}|g;
        s|\$\(INSTBIN\)|\$(DESTDIR)%{_bindir}|g;
    ' Makefile */Makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"
#%{__make} %{?_smp_mflags} -C vamps \
#   CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/lxdvdrip/
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}
%{__make} install DESTDIR="%{buildroot}"
#%{__install} -Dp -m0755 lxdvdrip %{buildroot}%{_bindir}/lxdvdrip
#%{__install} -Dp -m0755 mpgtx/mpgtx %{buildroot}%{_bindir}/mpgtx
#%{__install} -Dp -m0755 vamps/vamps %{buildroot}%{_bindir}/vamps
%{__install} -Dp -m0644 doc-pak/lxdvdrip.conf.EN %{buildroot}%{_sysconfdir}/lxdvdrip.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc-pak/*
%doc %{_mandir}/man1/lxdvdrip.1*
%config(noreplace) %{_sysconfdir}/lxdvdrip.conf
%{_bindir}/lxdvdrip
%{_bindir}/lxac3scan
%{_bindir}/buffer_lxdvdrip
%{_bindir}/dvdbackup_lxdvdrip
%{_bindir}/play_cell_lxdvdrip
%{_bindir}/requant_lxdvdrip
%{_bindir}/vamps_lxdvdrip
%{_datadir}/lxdvdrip/lxdvdrip.wav

%changelog
* Sun May 02 2010 Dag Wieers <dag@wieers.com> - 1.76-2
- Removed dvdbackup and streamdvd requirements. (Akemi Yagi)

* Mon Apr 19 2010 Dag Wieers <dag@wieers.com> - 1.76-1
- Updated to release 1.76.

* Sat Feb 21 2009 Dag Wieers <dag@wieers.com> - 1.74-1
- Updated to release 1.74.

* Sat Mar 31 2007 Dag Wieers <dag@wieers.com> - 1.70-1
- Updated to release 1.70.

* Tue Jan 03 2006 Dag Wieers <dag@wieers.com> - 1.51-1
- Updated to release 1.51.

* Fri Dec 03 2004 Dag Wieers <dag@wieers.com> - 1.40-1
- Initial package. (using DAR)
