# $Id$

# Authority: dag

%define srcver 1.0-pl10

Summary: Shared libraries for GSM speech compressor
Name: gsm
Version: 1.0.10
Release: 3.0
License: MIT
Group: System Environment/Libraries
URL: http://kbs.cs.tu-berlin.de/~jutta/toast.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/%{name}-%{version}.tar.gz
Patch: gsm-makefile-dag.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.
                                                                                
%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{srcver}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%patch0 -b .orig

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYRIGHT MACHINES MANIFEST README
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/gsm/

%changelog
* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 1.0.10-3.0
- Increased release to get elected.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.0.10-0
- Initial package. (using DAR)
