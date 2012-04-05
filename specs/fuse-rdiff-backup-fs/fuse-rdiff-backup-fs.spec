%define real_name rdiff-backup-fs
Summary:	Filesystem in userspace for rdiff-backup repositories
Name:		fuse-rdiff-backup-fs
Version:	1.0.0
Release:	1%{?dist}
License:	GPLv3
Group:		Applications/System
URL:            http://www.rdiff-backup-fs.com
Source:         https://rdiff-backup-fs.googlecode.com/files/%{real_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  fuse-devel
BuildRequires:  zlib-devel
Requires: fuse

Obsoletes: %{real_name} <= %{name}-%{version}
Provides: %{real_name} = %{name}-%{version}

%description
Filesystem in userspace for rdiff-backup repositories.

%prep
%setup -q -n %{real_name}-%{version}

%build

%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_libdir}/lib%{name}.a

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc ChangeLog COPYING README
%{_bindir}/rdiff-backup-fs
%{_mandir}/man1/rdiff-backup-fs*

%changelog
* Sat Feb 11 2012 David Hrbáč <david@hrbac.cz> - 1.0.0-1
- initial build
