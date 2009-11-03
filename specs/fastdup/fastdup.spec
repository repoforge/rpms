# $Id$
# Authority: dag

Summary: Tool to find copies of the same file within directory tree(s)
Name: fastdup
Version: 0.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://dev.dereferenced.net/fastdup/

Source: http://www.dereferenced.net/fastdup-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
FastDup is a tool to find copies of the same file within directory tree(s),
designed for maximum speed and efficiency unlike most similar tools. Where
many similar tools rely on checksums or hashes of files, or simple
comparisons, fastdup uses a number of cleverly optimized tricks to reduce
the number of actual comparisons necessary, and as a result can scan large
sets of data extremely quickly compared to alternatives.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 fastdup %{buildroot}%{_bindir}/fastdup

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/fastdup

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
