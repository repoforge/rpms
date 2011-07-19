# $Id$
# Authority: dag

# ExclusiveDist: el2 el3 el4

Summary: List SCSI devices (or hosts) and associated information
Name: lsscsi
Version: 0.23
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://sg.danny.cz/scsi/lsscsi.html

Source: http://sg.danny.cz/scsi/lsscsi-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

%prep
%setup

%build
autoreconf --force --install --symlink
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL README
%doc %{_mandir}/man8/lsscsi.8*
%{_bindir}/lsscsi

%changelog
* Wed Jun 22 2011 Dag Wieers <dag@wieers.com> - 0.23-1
- Initial package. (from fedora)
