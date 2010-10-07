# $Id$
# Authority: dag

%{?el5:%define version 3.0.33}
%{?el4:%define version 3.0.33}
%{?el3:%define version 3.0.9}
%{?el2:%define version 2.2.8}

%define real_version 0.3.6c-beta5

%define _prefix /usr/samba

Summary: On-access virus scanning for samba using ClamAV
Name: samba-vscan
Version: %{version}
Release: 1%{?dist}
License: GPLv3
Group: Applications/File
URL: http://www.openantivirus.org/

Source0: http://www.openantivirus.org/download/samba-vscan-%{real_version}.tar.gz
Source1: http://www.samba.org/samba/ftp/stable/samba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: samba
Requires: samba-common = %{version}

%description
A vfs-module for samba to implement on-access scanning using the
ClamAV antivirus software (which must be installed to use this).

%prep
%setup -a1 -n %{name}-%{real_version}

%build
### Prepare Samba
cd samba-%{version}/source
./autogen.sh
./configure
make proto
cd -

%configure \
    --with-fsh="yes" \
    --with-samba-source="samba-%{version}/source/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}"

for conf in */vscan-*.conf; do
    %{__install} -Dp -m0644 $conf %{buildroot}%{_sysconfdir}/samba/${conf##*/}
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README TODO
%config(noreplace) %{_sysconfdir}/samba/vscan-antivir.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-clamav.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-fprotd.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-fsav.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-icap.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-kavp.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-mcdaemon.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-mks32.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-oav.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-sophos.conf
%config(noreplace) %{_sysconfdir}/samba/vscan-trend.conf
%dir %{_prefix}/lib/vfs/
%{_prefix}/lib/vfs/vscan-antivir.so
%{_prefix}/lib/vfs/vscan-clamav.so
%{_prefix}/lib/vfs/vscan-fprotd.so
%{_prefix}/lib/vfs/vscan-fsav.so
%{_prefix}/lib/vfs/vscan-icap.so
%{_prefix}/lib/vfs/vscan-kavp.so
%{_prefix}/lib/vfs/vscan-mcdaemon.so
%{_prefix}/lib/vfs/vscan-mksd.so
%{_prefix}/lib/vfs/vscan-oav.so
%{_prefix}/lib/vfs/vscan-sophos.so
%{_prefix}/lib/vfs/vscan-trend.so
%exclude %{_sysconfdir}/samba/vscan-symantec.conf

%changelog
* Thu Oct 07 2010 Dag Wieers <dag@wieers.com> - 3.0.33-1
- Initial package. (using DAR)
