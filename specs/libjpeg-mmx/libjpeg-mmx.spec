# $Id$

# Authority: dag

%define real_name jpeg-mmx

Summary: Tools for the movtar MJPEG video format
Name: libjpeg-mmx
Version: 0.1.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/mjpeg/jpeg-mmx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libjpeg-devel, nasm

%description
This package contains static libraries and C system header files
needed to compile applications that use part of the libraries
of the libjpeg-mmx package.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}
%{__install} -m0755 libjpeg-mmx.a %{buildroot}%{_libdir}/
%{__install} -m0644 jpegint.h jinclude.h %{buildroot}%{_includedir}/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README jconfig.doc usage.doc
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 0.1.4-0
- Split from earlier "mjpegtools" package.
- Initial package. (using DAR)
