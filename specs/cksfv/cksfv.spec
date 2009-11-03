# $Id$
# Authority: dag

Summary: Tool to create and check SFV files
Name: cksfv
Version: 1.3.12
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://zakalwe.fi/~shd/foss/cksfv/

Source: http://zakalwe.fi/~shd/foss/cksfv/files/cksfv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cksfv is a tool to create and check SFV files. SFV (Simple File
Verification) files are used for verifying file integrity using
CRC32 checksums.

%prep
%setup
#%{__perl} -pi.orig -e 's|/usr/local/bin|\$(bindir)|' src/Makefile

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__install} -d -m0755 %{buildroot}%{_bindir}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 src/cksfv %{buildroot}%{_bindir}/cksfv
%{__install} -Dp -m0644 cksfv.1 %{buildroot}%{_mandir}/man1/cksfv.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man1/cksfv.1*
%{_bindir}/cksfv

%changelog
* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 1.3.12-1
- Updated to release 1.3.12.

* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 1.3.9-1
- Updated to release 1.3.9.

* Sun Aug 14 2005 Dag Wieers <dag@wieers.com> - 1.3-1
- Rebuild.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
