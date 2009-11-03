# $Id$
# Authority: matthias

# ExcludeDist: fc3 el4

Summary: Graphical user interface for the yum package manager
Name: yumi
Version: 2.0.7
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.cobind.com/yumgui.html
# Only available as .src.rpm, no remote path for the source :-(
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: yum >= 2.0.7, pygtk2 >= 1.99, usermode
BuildRequires: python, gettext, pygtk2 >= 1.99

%description
Graphical user interface for the yum package manager.


%prep
%setup


%build


%install
%{__rm} -rf %{buildroot}

# The main install
%{__mkdir_p} %{buildroot}%{_datadir}/yum
%{__install} -p -m0644 yumgui.py progress_bar.py yumi.png \
    %{buildroot}%{_datadir}/yum/
%{__install} -p -m0755 yumi \
    %{buildroot}%{_datadir}/yum/
# Actually, replace .pyc with .py to make a true .noarch.rpm
%{__perl} -pi.orig -e 's|\.pyc$|\.py|g' %{buildroot}%{_datadir}/yum/yumi

# The helper stuff
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} %{_bindir}/consolehelper %{buildroot}%{_bindir}/yumi
%{__install} -Dp -m0644 yumi.pam \
    %{buildroot}%{_sysconfdir}/pam.d/yumi
%{__install} -Dp -m0644 yumi.console.app \
    %{buildroot}%{_sysconfdir}/security/console.apps/yumi


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/pam.d/yumi
%config %{_sysconfdir}/security/console.apps/yumi
%{_bindir}/yumi
%{_datadir}/yum/


%changelog
* Fri Aug 06 2004 Dag Wieers <dag@wieers.com> - 2.0.7-2
- Added missing usermode requirement.
- Added BuildRequirement for pygtk2, to prevent building. (R. A. Rivas Diaz)

* Tue Jun 15 2004 Matthias Saou <http://freshrpms.net> 2.0.7-1
- Spec file cleanup and fixes.

* Sat Jun 12 2004 Bryan Mills <bryan@cobind.com>
- First packaging

