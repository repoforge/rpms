# Authority: dag

Summary: Arc archiver 
Name: arc
Version: 5.21e
Release: 0
License: distributable 
Group: Applications/Archiving
URL: ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/arc521e.pl8.tar.Z
Patch: arc-5.21e-timeh.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.

%prep
%setup -c
%patch -p1

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -d %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1
%{__install} -m0755 arc marc %{buildroot}%{_bindir}
%{__install} arc.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Arc521.doc Arcinfo Changes.521 README
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
