# $Id$
# Authority: matthias

### EL6 ships with udftools-1.0.0b3-12.el6
### EL5 ships with udftools-1.0.0b3-0.1.el5
# ExclusiveDist: el2 el3 el4

Summary: Linux UDF Filesystem userspace utilities
Name: udftools
Version: 1.0.0b3
Release: 3%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://sourceforge.net/projects/linux-udf/
Source: http://dl.sf.net/linux-udf/udftools-%{version}.tar.gz
Patch0: udftools-1.0.0b3-pktsetup-chardev.patch
Patch1: udftools-1.0.0b3-mkudffs-bigendian.patch
Patch2: udftools-1.0.0b3-wrudf-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: readline-devel

%description
Linux UDF Filesystem userspace utilities.


%prep
%setup
%patch0 -p1 -b .pktsetup-chardev
%patch1 -p1 -b .mkudffs-bigendian
%patch2 -p1 -b .wrudf-gcc4


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_libdir}/libudffs.a
%exclude %{_libdir}/libudffs.la
%{_mandir}/man?/*


%changelog
* Tue May  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.0b3-3
- Include patches to fix big endian issue and gcc4 compile.

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.0.0b3-1
- Initial RPM release, based on spec file from John Treacy.
- Exclude .la file.
- Remove unneeded /sbin/ldconfig calls (only a static lib for now).

