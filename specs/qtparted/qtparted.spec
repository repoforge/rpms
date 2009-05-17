# $Id$
# Authority: dries

# Screenshot: http://qtparted.sourceforge.net/images/screenshot-001-a.jpg
# ScreenshotURL: http://qtparted.sourceforge.net/screenshots.en.html

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _without_jfs 1}
%{?el5:%define _without_xfs 1}

%{?el4:%define _without_jfs 1}

%define desktop_vendor rpmforge

Summary: Graphical frontend for parted
Name: qtparted
Version: 0.4.5
Release: 2
License: GPL
Group: Applications/System
URL: http://qtparted.sourceforge.net/

Source: http://dl.sf.net/qtparted/qtparted-%{version}.tar.bz2
Patch0: qtparted-0.4.5-PED_SECTOR_SIZE.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs
BuildRequires: parted-devel >= 1.6
BuildRequires: qt-designer
%{!?_without_jfs:BuildRequires: jfsutils}
%{!?_without_ntfs:BuildRequires: ntfsprogs}
%{!?_without_reiserfs:BuildRequires: progsreiserfs-devel}
%{!?_without_xfs:BuildRequires: xfsprogs}
Requires: parted >= 1.6

%description
A graphical frontend for parted.

%prep
%setup
%patch0 -p1

%{__cat} <<EOF >data/qtparted.desktop
[Desktop Entry]
Name=QTParted Partition Editor
Comment=Create and manage disk partitions
Exec=qtparted
Icon=qtparted.xpm
Terminal=false
Type=Application
Encoding=UTF-8
Categories=QT;Application;System;
EOF

%{__cat} <<EOF >qtparted.console
USER=root
PROGRAM=%{_sbindir}/qtparted
SESSION=true
EOF

%{__cat} <<EOF >qtparted.pam
#%PAM-1.0
auth       sufficient   /lib/security/pam_rootok.so
auth       sufficient   /lib/security/pam_timestamp.so
auth       required     /lib/security/pam_stack.so service=system-auth
session    required     /lib/security/pam_permit.so
session    optional     /lib/security/pam_timestamp.so
session    optional     /lib/security/pam_xauth.so
account    required     /lib/security/pam_permit.so
EOF

%build
source /etc/profile.d/qt.sh
%{__aclocal}
%{__automake} --add-missing --gnu
%{__perl} admin/am_edit
%{__autoconf}
%configure \
    --with-log-dir="%{_localstatedir}/log" \
    --with-xinerama \
%{?_without_ntfs:--disable-ntfs} \
%{?_without_reiserfs:--disable-reiserfs} \
%{?_without_xfs:--disable-xfs}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/qtparted
%{__install} -Dp -m0644 qtparted.console %{buildroot}%{_sysconfdir}/security/console.apps/qtparted
%{__install} -Dp -m0644 qtparted.pam %{buildroot}%{_sysconfdir}/pam.d/qtparted

%if %{!?_without_freedesktop:1}0
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --delete-original                          \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category X-Red-Hat-Base              \
        %{buildroot}%{_datadir}/applnk/System/qtparted.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README TODO
%doc %{_mandir}/man1/qtparted.1*
%config(noreplace) %{_sysconfdir}/pam.d/qtparted
%config(noreplace) %{_sysconfdir}/security/console.apps/qtparted
%{_bindir}/qtparted
%{_sbindir}/qtparted
%{_datadir}/qtparted/
%{_datadir}/pixmaps/*.xpm
%{?_without_freedesktop:%{_datadir}/applnk/System/qtparted.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-qtparted.desktop}
%exclude %{_sbindir}/run_qtparted

%changelog
* Thu Apr 30 2009 Dag Wieers <dag@wieers.com> - 0.4.5-2
- Added patch from Fedora.

* Sat Aug 13 2005 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.

* Sun Jan 09 2005 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Updated to release 0.4.4.

* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 0.4.1-1
- First packaging for Fedora Core 1
