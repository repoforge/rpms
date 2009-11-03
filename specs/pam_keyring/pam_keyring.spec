# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: PAM module that execute gnome-keyring-daemon and unlock the default keyring
Name: pam_keyring
Version: 0.0.9
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
Source: http://www.hekanetworks.com/opensource/pam_keyring/pam_keyring-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.hekanetworks.com/

BuildRequires: gnome-keyring-devel
BuildRequires: libtool
BuildRequires: pam-devel
Requires: gnome-keyring >= 0.4.8
Requires: gnome-session >= 2.10.0
Requires: pam >= 0.99.3

%description
The pam_keyring module allows GNOME users to automatically unlock 
their default keyring using their system password when they log in. 
This allows the data in the default keyring to be used more 
transparently. Ideally, users should only every have to enter one 
password (or physical token, etc.): the password they use to 
authenticate themselves to the system when they log in.

%prep
%setup

%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man8/pam_keyring.8*
%{_libdir}/security/pam_keyring.so
%{_libdir}/security/pam_keyring_auth.so
%{_libdir}/security/pam_keyring_passwd.so
%{_libdir}/security/pam_keyring_session.so
%{_libexecdir}/pam-keyring-tool
%exclude %{_libdir}/security/pam_keyring.la

%changelog
* Tue Jun 17 2008 Dag Wieers <dag@wieers.com> - 0.0.9-1
- Initial package. (using DAR)
