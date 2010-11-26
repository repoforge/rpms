# $Id$
# Authority: dag

%{?el5:# Tag: rft}
# ExclusiveDist: el5 el6

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Tool to allow building RPM packages in chroots
Name: mock
Version: 1.1.6
Release: 1%{?dist}
License: GPLv2+
Group: Development/Tools
URL: http://fedoraproject.org/wiki/Projects/Mock

Source: https://fedorahosted.org/mock/attachment/wiki/MockTarballs/mock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4
Requires: createrepo
Requires: pigz
Requires: python >= 2.4
Requires: python-ctypes
Requires: python-decoratortools
Requires: python-hashlib
Requires: shadow-utils
Requires: tar
Requires: usermode
Requires: yum >= 2.4

%description
Mock takes an SRPM and builds it in a chroot

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cache/mock/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/mock/

%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/mock

%{?el5: %{__ln_s} -f centos-5-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el4: %{__ln_s} -f centos-4-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el3: %{__ln_s} -f centos-3-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el2: %{__ln_s} -f centos-2-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}

%{?rh9: %{__ln_s} -f redhat-9-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?rh7: %{__ln_s} -f redhat-7-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}

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
%config %{_sysconfdir}/bash_completion.d/mock.bash
%{_bindir}/mock
%{python_sitelib}/mock/

%defattr(0755, root, root, 0755)
%{_sbindir}/mock

%defattr(0755, root, mock, 02775)
%dir %{_localstatedir}/cache/mock/
%dir %{_localstatedir}/lib/mock/

%changelog
* Fri Nov 19 2010 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Updated to release 1.1.6.

* Fri Nov 19 2010 Dag Wieers <dag@wieers.com> - 1.0.12-3
- Fixed incorrect directory permissions, take 2. (Steve Tindall)

* Thu Nov 18 2010 Dag Wieers <dag@wieers.com> - 1.0.12-2
- Fixed incorrect directory permissions. (Steve Tindall)

* Fri Oct 15 2010 Dag Wieers <dag@wieers.com> - 1.0.12-1
- Updated to release 1.0.12.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.6.13-1
- Updated to release 0.6.13.

* Mon Dec 26 2005 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
