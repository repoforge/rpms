# Authority: freshrpms
# Archs: i386 i686

Summary: unRAR - extract, test and view RAR archives
Name: unrar
Version: 2.71
Release: 0
License: Freeware
Group: Applications/Archiving
URL: ftp://sunsite.unc.edu/pub/Linux/utils/compress/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%prep
%setup

%build
%{__make} %{?_smp_mflags} clean
%{__make} %{?_smp_mflags} CFLAGS="-D_UNIX %{optflags}"

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 unrar %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/*

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
