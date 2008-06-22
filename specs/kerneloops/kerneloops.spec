# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Tool to automatically collect and submit kernel crash signatures
Name: kerneloops
Version: 0.11
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.kerneloops.org/

Source: http://www.kerneloops.org/download/kerneloops-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: dbus-glib-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: libnotify-devel
Requires: chkconfig
Requires: initscripts

%description
This package contains the tools to collect kernel crash signatures,
and to submit them to the kerneloops.org website where the kernel
crash signatures get collected and grouped for presentation to the
Linux kernel developers.

%prep
%setup

%{__perl} -pi.orig -e 's|\tdesktop-file-install |\tdesktop-file-install --vendor="%{desktop_vendor}" |' Makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 kerneloops.init %{buildroot}%{_initrddir}/kerneloops
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add kerneloops

%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop &> /dev/null || :
    /sbin/chkconfig --del %{name}
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc Changelog COPYING
%doc %{_mandir}/man8/kerneloops.8*
%config(noreplace) %{_sysconfdir}/kerneloops.conf
%config %{_initrddir}/kerneloops
%{_sysconfdir}/dbus-1/system.d/kerneloops.dbus
%{_sysconfdir}/xdg/autostart/rpmforge-kerneloops-applet.desktop
%{_bindir}/kerneloops-applet
%{_datadir}/kerneloops/
%{_sbindir}/kerneloops

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
