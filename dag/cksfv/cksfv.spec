# Authority: newrpms
Summary: Utility to manipulate SFV files.
Name: cksfv
Version: 1.3
Release: 0
License: GPL
Group: Applications/File
URL: http://www.fodder.org/cksfv/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.fodder.org/cksfv/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
cksfv is a utility that can create and use SFV files. SFV (Simple File
Verification) files are used to verify file integrity using CRC32
checksums.

%prep
%setup

### FIXME: Let Makefile use standard autotools directories.
%{__perl} -pi.orig -e 's| /usr/local/bin| \$(bindir)|' src/Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="-Wall %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/*

%changelog
* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
