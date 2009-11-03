# $Id$
# Authority: dag
# Upstream: Moriyoshi Koizumi <moriyoshi$users,sourceforge,net>

Summary: Utility for testing pluggable authentication modules (PAM) facility
Name: pamtester
Version: 0.1.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://pamtester.sourceforge.net/

Source: http://dl.sf.net/pamtester/pamtester-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pam-devel, autoconf, automake, gcc-c++

%description
pamtester is a tiny utility program to test the pluggable
authentication modules (PAM) facility, which is a de facto
standard of unified authentication management mechanism in
many unices and similar OSes.

While specifically designed to help PAM module authors to
test their modules, that might also be handy for system
administrators interested in building a centralised
authentication system using common standards such as NIS,
SASL and LDAP.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%doc %{_mandir}/man1/pamtester.1*
%{_bindir}/pamtester

%changelog
* Tue Jul 11 2006 Dag Wieers <dag@wieers.com> - 0.1.2-1
- Updated to release 0.1.2.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Initial package. (using DAR)
