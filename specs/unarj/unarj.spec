# $Id$

# Authority: dag

%define rversion 2.63a

Summary: Uncompressor for .arj format archive files.
Name: unarj
Version: 2.63
Release: 0.a
Group: Applications/Archiving
License: distributable


Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ibiblio.org/pub/Linux/utils/compress/unarj-%{rversion}.tar.gz
Patch: unarj-subdir.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
The UNARJ program is used to uncompress .arj format archives.  The
.arj format archive was mostly used on DOS machines.

%prep
%setup -n %{name}-%{rversion}
#%patch -p1

%build
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 unarj %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/*

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 2.43-1
- Initial package. (using DAR)
