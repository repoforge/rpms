# $Id$
# Authority: dag

Summary: Tool to create and check SFV files
Name: cksfv
Version: 1.3
Release: 1
License: GPL
Group: Applications/File
URL: http://www.fodder.org/cksfv/

Source: http://www.fodder.org/cksfv/cksfv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cksfv is a tool to create and check SFV files. SFV (Simple File
Verification) files are used for verifying file integrity using
CRC32 checksums.

%prep
%setup
%{__perl} -pi.orig -e 's|/usr/local/bin|\$(bindir)|' src/Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/cksfv

%changelog
* Sun Aug 14 2005 Dag Wieers <dag@wieers.com> - 1.3-1
- Rebuild.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
