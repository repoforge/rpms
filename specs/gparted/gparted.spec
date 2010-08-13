# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Gnome Partition Editor
Name: gparted
Version: 0.4.8
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://gparted.sourceforge.net/

Source: http://dl.sf.net/gparted/gparted-%{version}.tar.bz2
Patch0: gparted-0.4.8-icon.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: e2fsprogs-devel
BuildRequires: gettext
BuildRequires: gnome-doc-utils
BuildRequires: gtkmm24-devel
BuildRequires: parted-devel 
BuildRequires: perl(XML::Parser) 
BuildRequires: scrollkeeper
Requires: scrollkeeper

%description
GParted stands for Gnome Partition Editor and is a graphical frontend to
libparted. Among other features it supports creating, resizing, moving
and copying of partitions. Also several (optional) filesystem tools provide
support for filesystems not included in libparted. These optional packages
will be detected at runtime and don't require a rebuild of GParted

%prep
%setup
%patch0 -p0 -b .icon

%{__perl} -pi -e '
        s|\bsbin\b|\bbin\b|;
        s|_X-GNOME-FullName|X-GNOME-FullName|;
    ' gparted.desktop

grep -v '^lv$' po/LINGUAS >po/LINGUAS

%{__cat} <<EOF >gparted.pam
#%PAM-1.0
auth       sufficient   /%{_lib}/security/pam_rootok.so
auth       sufficient   /%{_lib}/security/pam_timestamp.so
auth       required     /%{_lib}/security/pam_stack.so service=system-auth
session    required     /%{_lib}/security/pam_permit.so
session    optional     /%{_lib}/security/pam_xauth.so
session    optional     /%{_lib}/security/pam_timestamp.so
account    required     /%{_lib}/security/pam_permit.so
EOF

%{__cat} <<EOF >gparted.console-apps
USER=root
PROGRAM=%{_sbindir}/gparted
SESSION=true
FALLBACK=false
EOF

%build
%configure
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original             \
        --vendor %{desktop_vendor}                 \
        --dir %{buildroot}%{_datadir}/applications \
        --mode 0644                                \
        %{buildroot}%{_datadir}/applications/gparted.desktop

#### consolehelper stuff
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/gparted
%{__install} -Dp -m0644 gparted.console-apps %{buildroot}%{_sysconfdir}/security/console.apps/gparted
%{__install} -Dp -m0644 gparted.pam %{buildroot}%{_sysconfdir}/pam.d/gparted

%preun
if [ $1 -ge 0 ]; then
    if [ -a %{_datadir}/hal/fdi/policy/gparted-disable-automount.fdi ]; then
        %{__rm} -rf %{_datadir}/hal/fdi/policy/gparted-disable-automount.fdi
    fi
fi

%post
scrollkeeper-update -q -o %{_datadir}/omf/gparted || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%postun
scrollkeeper-update -q || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man8/gparted.*
%config(noreplace) %{_sysconfdir}/pam.d/gparted
%config(noreplace) %{_sysconfdir}/security/console.apps/gparted
%{_bindir}/gparted
%{_datadir}/applications/%{desktop_vendor}-gparted.desktop
%{_datadir}/icons/hicolor/*/apps/gparted.*
%{_datadir}/gnome/help/gparted/
%{_datadir}/omf/gparted/
%{_sbindir}/gparted
%{_sbindir}/gpartedbin
%exclude %{_localstatedir}/lib/scrollkeeper/

%changelog
* Fri Jul 30 2010 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Updated to release 0.4.8.

* Wed Sep 19 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.3-2
- Only use hal-lock on recent distributions.

* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Added Fedora patches.
- Initial package. (using DAR)
