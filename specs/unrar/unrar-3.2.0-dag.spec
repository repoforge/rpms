# Authority: dag

# Archs: i386 i686

%define rname rarlinux
%define rversion 3.2.b3

Summary: unRAR - extract, test and view RAR archives
Name: unrar
Version: 3.1.83
Release: 0
License: Freeware
Group: Applications/Archiving

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.rarlab.com/rar/%{rname}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%prep
%setup -n %{rname}-%{rversion}

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
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 3.1.83
- Updated to release 3.2.b3.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
