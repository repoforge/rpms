# $Id$

# Authority: dag

Summary: Archiver and compressor
Name: freeze
Version: 2.5
Release: 1
License: distributable
Group: Utilities/Archiving

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.std.com/src/util/freeze%{version}/freeze-%{version}.tar.gz
Patch: freeze-2.5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Freeze is an old file compressor and decompressor that is not in
common use anymore, but can be useful if the need ever arises to
dearchive files compressed with it.

%prep
%setup
%patch

%build
%{__chmod} u+x configure
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall \
	MANDEST="%{buildroot}%{_mandir}/man1/"

### Fix symlinks properly
for bin in fcat melt unfreeze; do
	%{__ln_s} -f freeze %{buildroot}%{_bindir}/$bin
	%{__rm} -f %{buildroot}%{_mandir}/man1/$bin.1
	%{__ln_s} -f freeze.1.gz %{buildroot}%{_mandir}/man1/$bin.1.gz
done

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
