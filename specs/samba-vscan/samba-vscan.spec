# $Id$
# Authority: dag

%define vfsdir %{_libdir}/samba/vfs

%{?el5:%define samba_version 3.0.33}
%{?el4:%define samba_version 3.0.33}
%{?el3:%define samba_version 3.0.9}
%{?el2:%define samba_version 2.2.8}
%{?el2:%define vfsdir %{_prefix}/samba/lib}

Summary: On-access virus scanning for samba using ClamAV
Name: samba-vscan
%define real_version 0.3.6c-beta5
Version: 0.3.6c
Release: 0.beta5%{?dist}
License: GPLv3
Group: Applications/File
URL: http://www.openantivirus.org/

Source0: http://www.openantivirus.org/download/samba-vscan-%{real_version}.tar.gz
Source1: http://www.samba.org/samba/ftp/stable/samba-%{samba_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: samba-common = %{samba_version}

%description
A vfs-module for samba to implement on-access scanning using the
ClamAV antivirus software (which must be installed to use this).

%prep
%setup -a1 -n %{name}-%{real_version}

%build
### Prepare Samba
cd samba-%{samba_version}/source
./autogen.sh || :
./configure
make proto
cd -

%configure \
    --with-fsh="yes" \
    --with-samba-source="$PWD/samba-%{samba_version}/source"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" LIBDIR="%{_libdir}/samba"

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
%dir %{vfsdir}
%{vfsdir}/vscan-antivir.so
%{vfsdir}/vscan-clamav.so
%{vfsdir}/vscan-fprotd.so
%{vfsdir}/vscan-fsav.so
%{vfsdir}/vscan-icap.so
%{vfsdir}/vscan-kavp.so
%{vfsdir}/vscan-mcdaemon.so
%{vfsdir}/vscan-mksd.so
%{vfsdir}/vscan-oav.so
%{vfsdir}/vscan-sophos.so
%{vfsdir}/vscan-trend.so
%exclude %{_sysconfdir}/samba/vscan-symantec.conf

%changelog
* Thu Oct 07 2010 Dag Wieers <dag@wieers.com> - 0.3.6c-0.beta5
- Initial package. (using DAR)
