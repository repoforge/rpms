# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

Summary: RPMforge release file and RPM repository configuration
Name: rpmforge-release
Version: 0.5.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://rpmforge.net/

Source0: mirrors-rpmforge
Source1: RPM-GPG-KEY-rpmforge-dag
Source2: RPM-GPG-KEY-rpmforge-fabian
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RPMforge.net release file. This package contains apt, yum and smart
configuration for the RPMforge RPM Repository, as well as the public
GPG keys used to sign them.

%prep
%setup -c

%{?el6:version='6'}
%{?el5:version='5'}
%{?el4:version='4'}
%{?el3:version='3'}
%{?el2:version='2.1'}

%ifarch ppc ppc64
builder='fabian'
%else
builder='dag'
%endif

### #rpm http://rpmforge.sw.be redhat/el\$(VERSION)/en/\$(ARCH) $builder
### repomd http://rpmforge.sw.be redhat/el\$(VERSION)/en/\$(ARCH)/rpmforge
%{__cat} <<EOF >rpmforge.apt
### Name: RPMforge RPM Repository for RHEL $version - $builder
### URL: http://rpmforge.net/
#rpm http://apt.sw.be redhat/el\$(VERSION)/en/\$(ARCH) $builder
repomd http://apt.sw.be redhat/el\$(VERSION)/en/\$(ARCH)/rpmforge
EOF

%{__cat} <<EOF >rpmforge-testing.apt
### Name: RPMforge RPM Repository for RHEL $version - test
### URL: http://rpmforge.net/
#rpm http://apt.sw.be redhat/el\$(VERSION)/en/\$(ARCH) test
#repomd http://apt.sw.be redhat/el\$(VERSION)/en/\$(ARCH)/test
EOF

### baseurl = http://rpmforge.sw.be/redhat/el$version/en/%{_arch}/rpmforge
%{__cat} <<EOF >rpmforge.smart
### Name: RPMforge RPM Repository for RHEL $version - %{_arch} - $builder
### URL: http://rpmforge.net/
[rpmforge]
name = Extra packages from RPMforge.net for RHEL $version - %{_arch} - $builder
baseurl = http://apt.sw.be/redhat/el$version/en/%{_arch}/rpmforge
type = rpm-md
EOF

%{__cat} <<EOF >rpmforge-testing.smart
### Name: RPMforge RPM Repository for RHEL $version - %{_arch} - test
### URL: http://rpmforge.net/
#[rpmforge]
#name = Test packages from RPMforge.net for RHEL $version - %{_arch} - test
#baseurl = http://apt.sw.be/redhat/el$version/en/%{_arch}/test
#type = rpm-md
EOF

### baseurl = http://rpmforge.sw.be/redhat/el$version/en/\$basearch/rpmforge
### #mirrorlist = http://mirrorlist.sw.be/mirrors-rpmforge-$dtag-\$basearch
### Yum needs hardcoded version as on RHEL4AS releasever translates to 4AS :(
%{__cat} <<EOF >rpmforge.yum
### Name: RPMforge RPM Repository for RHEL $version - $builder
### URL: http://rpmforge.net/
[rpmforge]
name = RHEL \$releasever - RPMforge.net - $builder
baseurl = http://apt.sw.be/redhat/el$version/en/\$basearch/rpmforge
mirrorlist = http://apt.sw.be/redhat/el$version/en/mirrors-rpmforge
#mirrorlist = file:///etc/yum.repos.d/mirrors-rpmforge
enabled = 1
protect = 0
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-$builder
gpgcheck = 1
EOF

%{__cat} <<EOF >rpmforge-testing.yum
### Name: RPMforge RPM Repository for RHEL $version - $builder
### URL: http://rpmforge.net/
[rpmforge-testing]
name = RHEL \$releasever - RPMforge.net - test
baseurl = http://apt.sw.be/redhat/el$version/en/\$basearch/test
enabled = 0
protect = 0
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-$builder
gpgcheck = 0
EOF

%{__cat} <<EOF >rpmforge.up2date
### Name: RPMforge RPM Repository for RHEL $version - %{_arch} - $builder
### URL: http://rpmforge.net/
#
# Add the following line to /etc/sysconfig/rhn/sources
#
#   yum rpmforge http://apt.sw.be/redhat/el$version/en/%{_arch}/rpmforge
# or
#   apt rpmforge http://apt.sw.be redhat/el$version/en/%{_arch} rpmforge
EOF

for mirror in $(%{__cat} %{SOURCE0}); do
    echo "$mirror/redhat/el$version/en/\$ARCH/rpmforge"
done >mirrors-rpmforge.yum

%build

%install
%{__rm} -rf %{buildroot}
%{__cp} -a %{SOURCE1} %{SOURCE2} .

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-fabian
#%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias

%{__install} -Dp -m0644 rpmforge.apt %{buildroot}%{_sysconfdir}/apt/sources.list.d/rpmforge.list
%{__install} -Dp -m0644 rpmforge-testing.apt %{buildroot}%{_sysconfdir}/apt/sources.list.d/rpmforge-testing.list
%{__install} -Dp -m0644 rpmforge.smart %{buildroot}%{_sysconfdir}/smart/channels/rpmforge.channel
%{__install} -Dp -m0644 rpmforge-testing.smart %{buildroot}%{_sysconfdir}/smart/channels/rpmforge-testing.channel
%{__install} -Dp -m0644 rpmforge.yum %{buildroot}%{_sysconfdir}/yum.repos.d/rpmforge.repo
%{__install} -Dp -m0644 rpmforge-testing.yum %{buildroot}%{_sysconfdir}/yum.repos.d/rpmforge-testing.repo
%{__install} -Dp -m0644 rpmforge.up2date %{buildroot}%{_sysconfdir}/sysconfig/rhn/sources.rpmforge.txt

%{__install} -Dp -m0644 mirrors-rpmforge.yum %{buildroot}%{_sysconfdir}/yum.repos.d/mirrors-rpmforge

%clean
%{__rm} -rf %{buildroot}

%post
%ifarch ppc ppc64
rpm -q gpg-pubkey-59b9897b-461fe38c &>/dev/null || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-fabian || :
%else
rpm -q gpg-pubkey-6b8d79e6-3f49313d &>/dev/null || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag || :
%endif

%files
%defattr(-, root, root, 0755)
%doc mirrors-rpmforge.yum RPM-GPG-KEY-rpmforge-* rpmforge.*
%pubkey RPM-GPG-KEY-rpmforge-dag
%pubkey RPM-GPG-KEY-rpmforge-fabian
%dir %{_sysconfdir}/apt/
%dir %{_sysconfdir}/apt/sources.list.d/
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/rpmforge.list
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/rpmforge-testing.list
%dir %{_sysconfdir}/smart/
%dir %{_sysconfdir}/smart/channels/
%config(noreplace) %{_sysconfdir}/smart/channels/rpmforge.channel
%config(noreplace) %{_sysconfdir}/smart/channels/rpmforge-testing.channel
%dir %{_sysconfdir}/sysconfig/rhn/
%config %{_sysconfdir}/sysconfig/rhn/sources.rpmforge.txt
%dir %{_sysconfdir}/yum.repos.d/
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmforge.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmforge-testing.repo
%config %{_sysconfdir}/yum.repos.d/mirrors-rpmforge
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-*

%changelog
* Thu Nov 11 2010 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Added entries for RHEL6.

* Mon Jan 04 2010 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Added entries for test repositories.

* Mon Jan 04 2010 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Install the GPG keys only for a specific distribution/architecture.

* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Added fabian's ppc repositories and GPG key.
- Removed a lot of cruft.

* Thu Jan 18 2007 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Fixed the reference to the RHEL2.1 repository. (Thanassis)

* Wed Jan 17 2007 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Add 'protect = 0' by default to yum configuration.
- Don't import GPG key for older distributions.

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 0.3.4-1
- Fix for Yum rpmforge.repo on Red Hat Enterprise Linux.

* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Added Dries his useless $driesrepomdsuffix. :(

* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Improved multi-distro support.

* Sat Jun 03 2006 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Added support for EL2 and RH7.

* Fri Jun 02 2006 Dag Wieers <dag@wieers.com> - 0.3-1
- Default to repomd metadata for Apt.

* Tue Aug 23 2005 Dag Wieers <dag@wieers.com> - 0.2-2
- Included directories too.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.2-1
- Fixes to up2date channel and mirrorlist. (Dries Verachtert)
- Fixes to GPG key location.

* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.1-3
- Improve smart channel.

* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.1-2
- Added mirrors-rpmforge locally.

* Fri Aug 19 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
