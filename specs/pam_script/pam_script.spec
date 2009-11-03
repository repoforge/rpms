# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: PAM module for executing scripts
%define real_name pam-script
Name: pam_script
Version: 0.1.7
Release: 1%{?dist}
Group: Applications/System
License: GPL
URL: http://www.bofs.co.za/~iburger/pam_script/

Source: http://www.bofs.co.za/~iburger/pam_script/pam-script-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pam-devel 
Requires: pam       

%description
pam_script is a module which allows to execute scripts after opening
and/or closing a session using PAM.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|^CFLAGS\s*=\s*(.*)$|override CFLAGS += $1|' Makefile
%{__perl} -pi.orig -e 's|^(#include <signal.h>)$|$1\n#include <syslog.h>|' pam_script.c

%build
export CC="%{__cc}"
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pam_script.so %{buildroot}%{_libdir}/security/pam_script.so
%{__install} -Dp -m0644 pam-script.5 %{buildroot}%{_mandir}/man5/pam_script.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README
%doc %{_mandir}/man5/pam_script.5*
%dir %{_libdir}/security/
%{_libdir}/security/pam_script.so

%changelog
* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 0.1.7-1
- Initial package. (using DAR)
