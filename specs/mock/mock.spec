# $Id$
# Authority: dag

# ExclusiveDist: el5 el6

%{?el5:%define _with_python_hashlib 1}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Tool to allow building RPM packages in chroots
Name: mock
Version: 1.1.11
Release: 1%{?dist}
License: GPLv2+
Group: Development/Tools
URL: http://fedoraproject.org/wiki/Projects/Mock

Source: https://fedorahosted.org/mock/attachment/wiki/MockTarballs/mock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.4
Requires(post): coreutils
Requires(pre): shadow-utils
Requires: createrepo
Requires: pigz
Requires: python >= 2.4
Requires: python-ctypes
Requires: python-decoratortools
%{?_with_python_hashlib:Requires: python-hashlib}
Requires: tar
Requires: usermode
Requires: yum >= 2.4
Requires: yum-utils >= 1.1.9

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

%{__install} -d -m2775 %{buildroot}%{_localstatedir}/cache/mock/
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mock/

%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/mock

%{?el6: %{__ln_s} -f epel-6-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el5: %{__ln_s} -f epel-5-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}
%{?el4: %{__ln_s} -f epel-4-%{_arch}.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg}

%clean
%{__rm} -rf %{buildroot}

%pre
if [ $1 -eq 1 ]; then
    groupadd -r mock >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, 0755)

%config(noreplace) %{_sysconfdir}/mock/
%config(noreplace) %{_sysconfdir}/pam.d/mock
%config(noreplace) %{_sysconfdir}/security/console.apps/mock
%config %{_sysconfdir}/bash_completion.d/mock.bash

# executables
%{_bindir}/mock
%attr(0755, root, root) %{_sbindir}/mock

# python stuff
%{python_sitelib}/mock

# docs
%doc AUTHORS ChangeLog COPYING INSTALL docs/*.txt
%doc %{_mandir}/man1/mock.1*

# cache & build dirs
%defattr(0775, root, mock, 02775)
%dir /var/cache/mock
%dir /var/lib/mock

%changelog
* Thu Jun 23 2011 Yury V. Zaytsev <yury@shurup.com> - 1.1.11-1
- More fixes to the default directory permissions.
- Updated to release 1.1.11.

* Wed Jun 22 2011 Yury V. Zaytsev <yury@shurup.com> - 1.1.10-2
- Fixed directory permissions and default configuration.

* Thu May 19 2011 Dag Wieers <dag@wieers.com> - 1.1.10-1
- Updated to release 1.1.10.

* Mon Mar 07 2011 Dag Wieers <dag@wieers.com> - 1.1.9-1
- Updated to release 1.1.9.

* Mon Feb 14 2011 Dag Wieers <dag@wieers.com> - 1.1.8-1
- Updated to release 1.1.8.

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
