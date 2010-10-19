# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Tool to allow building packages in chroots
Name: mock
Version: 1.0.12
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://fedoraproject.org/wiki/Projects/Mock

Source: https://fedorahosted.org/mock/attachment/wiki/MockTarballs/mock-%{version}.tar.gz
#Source: http://fedoraproject.org/projects/mock/releases/mock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4
Requires: gzip
Requires: python >= 2.4
Requires: python-ctypes
Requires: python-decoratortools
Requires: python-hashlib
Requires: shadow-utils
Requires: tar
Requires: usermode
Requires: yum >= 2.4

%description
Mock builds SRPMs in a chroot.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/mock/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cache/mock/
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/mock

%{?el5: %{__ln_s} -f centos-5-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el4: %{__ln_s} -f centos-4-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el3: %{__ln_s} -f centos-3-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el2: %{__ln_s} -f centos-2-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}

%{?rh9: %{__ln_s} -f redhat-9-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?rh7: %{__ln_s} -f redhat-7-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}

%{?fc7: %{__ln_s} -f fedora-7-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?fc6: %{__ln_s} -f fedora-6-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?fc5: %{__ln_s} -f fedora-5-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?fc4: %{__ln_s} -f fedora-4-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?fc3: %{__ln_s} -f fedora-3-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?fc2: %{__ln_s} -f fedora-2-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?fc1: %{__ln_s} -f fedora-1-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}

%clean
%{__rm} -rf %{buildroot}

%pre
if [ $1 -eq 1 ]; then
    groupadd -r mock &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL docs/*.txt
%doc %{_mandir}/man1/mock.1*
%config(noreplace) %{_sysconfdir}/mock/
%config(noreplace) %{_sysconfdir}/pam.d/mock
%config(noreplace) %{_sysconfdir}/security/console.apps/mock
%{_bindir}/mock
%{python_sitelib}/*

%defattr(0755, root, root, 0755)
%{_sbindir}/mock

%defattr(02775, root, mock, 0755)
%dir %{_localstatedir}/lib/mock/
%dir %{_localstatedir}/cache/mock/

%changelog
* Fri Oct 15 2010 Dag Wieers <dag@wieers.com> - 1.0.13-1
- Updated to release 1.0.13.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.6.13-1
- Updated to release 0.6.13.

* Mon Dec 26 2005 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
