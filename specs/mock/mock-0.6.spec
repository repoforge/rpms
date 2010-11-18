# $Id$
# Authority: dag

# ExclusiveDist: el2 el3 el4

%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}

Summary: Tool to allow building packages in chroots
Name: mock
Version: 0.6.13
Release: 2%{?dist}
License: GPL
Group: Development/Tools
URL: http://fedoraproject.org/wiki/Projects/Mock/

Source: http://fedoraproject.org/projects/mock/releases/mock-%{version}.tar.gz
Patch0: mock-0.6.13-centos-configs.patch
Patch1: mock-0.6.13-centos-FunctionalNet.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### FIXME: Make mock work without selinux
#%{!?_without_selinux:BuildRequires: libselinux-devel}
BuildRequires: libselinux-devel
Requires: python, yum >= 2.2.1
Requires: shadow-utils

%description
Mock builds SRPMs in a chroot.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

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
%doc ChangeLog README buildsys-build.spec
%doc %{_mandir}/man1/mock.1*
%config(noreplace) %{_sysconfdir}/mock/
%{_bindir}/mock
%{_libexecdir}/mock-yum/
%{_libdir}/libselinux-mock.so

%defattr(4750, root, mock, 0755)
%{_sbindir}/mock-helper

%defattr(0775, root, mock, 02755)
%dir %{_localstatedir}/lib/mock

%changelog
* Thu Nov 18 2010 Dag Wieers <dag@wieers.com> - 0.6.13-2
- Fixed incorrect directory permissions. (Steve Tindall)

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.6.13-1
- Updated to release 0.6.13.

* Mon Dec 26 2005 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
