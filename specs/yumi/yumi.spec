# $Id$
# Authority: matthias

Summary: Graphical user interface for the yum package manager
Name: yumi
Version: 2.0.7
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.cobind.com/yumgui.html
# Only available as .src.rpm, no remote path for the source :-(
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: yum >= 2.0.7, pygtk2 >= 2.0
BuildRequires: python, gettext
Requires: usermode

%description
Graphical user interface for the yum package manager.


%prep
%setup


%build


%install
%{__rm} -rf %{buildroot}

# The main install
%{__mkdir_p} %{buildroot}%{_datadir}/yum
%{__install} -m 0644 yumgui.py progress_bar.py yumi.png \
    %{buildroot}%{_datadir}/yum/
%{__install} -m 0755 yumi \
    %{buildroot}%{_datadir}/yum/
# Actually, replace .pyc with .py to make a true .noarch.rpm
%{__perl} -pi.orig -e 's|\.pyc$|\.py|g' %{buildroot}%{_datadir}/yum/yumi

# The helper stuff
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} %{_bindir}/consolehelper %{buildroot}%{_bindir}/yumi
%{__install} -m 0644 -D yumi.pam \
    %{buildroot}%{_sysconfdir}/pam.d/yumi
%{__install} -m 0644 -D yumi.console.app \
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
* Tue Jun 15 2004 Matthias Saou <http://freshrpms.net> 2.0.7-1
- Spec file cleanup and fixes.

* Sat Jun 12 2004 Bryan Mills <bryan@cobind.com>
- First packaging

