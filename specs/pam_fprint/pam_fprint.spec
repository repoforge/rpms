# $Id$
# Authority: dag

Summary: Integrate libfprint with existing applications
Name: pam_fprint
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.reactivated.net/fprint/wiki/Main_Page

Source: http://dl.sf.net/fprint/pam_fprint-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libfprint-devel
BuildRequires: pam-devel

%description
To integrate libfprint with existing applications, so that users can use 
their fingerprint reading hardware.

%prep
%setup
%{__perl} -pi.orig -e 's|pammoddir.=./lib/security|pammoddir=/%{_lib}/security|' src/Makefile.*

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
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/pam_fprint_enroll
/%{_lib}/security/pam_fprint.so

%changelog
* Fri Dec 19 2008 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
