# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_rpmpubkey 1}
%{?el2:%define _without_rpmpubkey 1}
%{?rh6:%define _without_rpmpubkey 1}

Summary: RPMforge release file and package configuration
Name: rpmforge-release
Version: 0.3.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://rpmforge.net/

Source0: mirrors-rpmforge
Source1: RPM-GPG-KEY-rpmforge-dag
Source2: RPM-GPG-KEY-rpmforge-dries
Source3: RPM-GPG-KEY-rpmforge-matthias
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RPMforge.net release file. This package contains apt, yum and smart
configuration for the RPMforge RPM Repository, as well as the public
GPG keys used to sign them.

%prep
%setup -c

%{?el4:name='Red Hat Enterprise'; version='4'; path="redhat/el"; builder='dag'}
%{?el3:name='Red Hat Enterprise'; version='3'; path="redhat/el"; builder='dag'}
%{?el2:name='Red Hat Enterprise'; version='2'; path="redhat/el"; builder='dag'}
%{?fc5:name='Fedora Core'; version='5'; path="fedora/"; builder='dries'; driesrepomdsuffix='/RPMS'}
%{?fc4:name='Fedora Core'; version='4'; path="fedora/"; builder='dries'; driesrepomdsuffix='/RPMS'}
%{?fc3:name='Fedora Core'; version='3'; path="fedora/"; builder='dag'}
%{?fc2:name='Fedora Core'; version='2'; path="fedora/"; builder='dag'}
%{?fc1:name='Fedora Core'; version='1'; path="fedora/"; builder='dag'}
%{?rh9:name='Red Hat'; version='9';   path="redhat/"; builder='dag'}
%{?rh8:name='Red Hat'; version='8.0'; path="redhat/"; builder='dag'}
%{?rh7:name='Red Hat'; version='7.3'; path="redhat/"; builder='dag'}
%{?rh6:name='Red Hat'; version='6.2'; path="redhat/"; builder='dag'}

%{__cat} <<EOF >rpmforge.apt
# Name: RPMforge RPM Repository for $name $version - $builder
# URL: http://rpmforge.net/
#rpm http://apt.sw.be $path\$(VERSION)/en/\$(ARCH) $builder
repomd http://apt.sw.be $path\$(VERSION)/en/\$(ARCH)/$builder$driesrepomdsuffix
EOF

%{__cat} <<EOF >rpmforge.smart
# Name: RPMforge RPM Repository for $name $version - %{_arch} - $builder
# URL: http://rpmforge.net/
[rpmforge]
name = Extra packages from RPMforge.net for $name $version - %{_arch} - $builder
baseurl = http://apt.sw.be/$path$version/en/%{_arch}/$builder$driesrepomdsuffix
type = rpm-md
EOF

%{__cat} <<EOF >rpmforge.yum
# Name: RPMforge RPM Repository for $name $version - $builder
# URL: http://rpmforge.net/
[rpmforge]
name = $name \$releasever - RPMforge.net - $builder
#baseurl = http://apt.sw.be/$path\$releasever/en/\$basearch/$builder$driesrepomdsuffix
mirrorlist = http://apt.sw.be/$path\$releasever/en/mirrors-rpmforge
#mirrorlist = file:///etc/yum.repos.d/mirrors-rpmforge
enabled = 1
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-$builder
gpgcheck = 1
EOF

%{__cat} <<EOF >rpmforge.up2date
# Name: RPMforge RPM Repository for $name $version - %{_arch} - $builder
# URL: http://rpmforge.net/
#
# Add the following line to /etc/sysconfig/rhn/sources
#
#	yum rpmforge http://apt.sw.be/$path$version/en/%{_arch}/$builder
# or
#	apt rpmforge http://apt.sw.be $path$version/en/%{_arch} $builder

EOF

for mirror in $(%{__cat} %{SOURCE0}); do
	echo "$mirror/$path$version/en/\$ARCH/$builder$driesrepomdsuffix"
done >mirrors-rpmforge.yum

%build

%install
%{__rm} -rf %{buildroot}
%{__cp} -a %{SOURCE1} %{SOURCE2} %{SOURCE3} .
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dries
%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias
%{__install} -Dp -m0644 rpmforge.apt %{buildroot}%{_sysconfdir}/apt/sources.list.d/rpmforge.list
%{__install} -Dp -m0644 rpmforge.smart %{buildroot}%{_sysconfdir}/smart/channels/rpmforge.channel
%{__install} -Dp -m0644 rpmforge.up2date %{buildroot}%{_sysconfdir}/sysconfig/rhn/sources.rpmforge.txt
%{__install} -Dp -m0644 rpmforge.yum %{buildroot}%{_sysconfdir}/yum.repos.d/rpmforge.repo
%{__install} -Dp -m0644 mirrors-rpmforge.yum %{buildroot}%{_sysconfdir}/yum.repos.d/mirrors-rpmforge

%clean
%{__rm} -rf %{buildroot}

%post
rpm -q gpg-pubkey-6b8d79e6-3f49313d &>/dev/null || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dag
rpm -q gpg-pubkey-1aa78495-3eb24301 &>/dev/null || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-dries
rpm -q gpg-pubkey-e42d547b-3960bdf1 &>/dev/null || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias
exit 0

%files
%defattr(-, root, root, 0755)
%doc mirrors-rpmforge.yum RPM-GPG-KEY-rpmforge-* rpmforge.*
%if %{!?_without_rpmpubkey:1}0
%pubkey RPM-GPG-KEY-rpmforge-dag
%pubkey RPM-GPG-KEY-rpmforge-dries
%pubkey RPM-GPG-KEY-rpmforge-matthias
%else
%doc RPM-GPG-KEY-rpmforge-dag
%doc RPM-GPG-KEY-rpmforge-dries
%doc RPM-GPG-KEY-rpmforge-matthias
%endif
%dir %{_sysconfdir}/apt/
%dir %{_sysconfdir}/apt/sources.list.d/
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/rpmforge.list
%dir %{_sysconfdir}/smart/
%dir %{_sysconfdir}/smart/channels/
%config(noreplace) %{_sysconfdir}/smart/channels/rpmforge.channel
%dir %{_sysconfdir}/sysconfig/rhn/
%config %{_sysconfdir}/sysconfig/rhn/sources.rpmforge.txt
%dir %{_sysconfdir}/yum.repos.d/
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmforge.repo
%config %{_sysconfdir}/yum.repos.d/mirrors-rpmforge
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-*

%changelog
* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Improved multi-distro support.
- Added Dries his useless $driesrepomdsuffix. :(

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
