# $Id$
# Authority: dag
# Upstream: Jutta Degener <jutta$pobox,com>

%define srcver 1.0-pl12

Summary: Shared libraries for GSM speech compressor
Name: gsm
Version: 1.0.12
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://kbs.cs.tu-berlin.de/~jutta/toast.html

#Source: ftp://ftp.cs.tu-berlin.de/pub/local/kbs/tubmik/gsm/gsm-%{version}.tar.gz
Source: http://kbs.cs.tu-berlin.de/~jutta/gsm/gsm-1.0.12.tar.gz
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
%{__make} %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" libdir="%{_libdir}"

%{__ln_s} -f toast %{buildroot}%{_bindir}/untoast
%{__ln_s} -f toast %{buildroot}%{_bindir}/tcat

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYRIGHT MACHINES MANIFEST README
#%doc %{_mandir}/man1/bitter.1*
%doc %{_mandir}/man1/toast.1*
#%{_bindir}/bitter
%{_bindir}/tcat
%{_bindir}/toast
%{_bindir}/untoast
%{_libdir}/libgsm.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/gsm.3*
%doc %{_mandir}/man3/gsm_explode.3*
%doc %{_mandir}/man3/gsm_option.3*
%doc %{_mandir}/man3/gsm_print.3*
%{_includedir}/gsm/
%{_libdir}/libgsm.so
%exclude %{_libdir}/libgsm.a

%changelog
* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 1.0.12-1
- Update to 1.0.12.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.10-6
- Release bump to drop the disttag number in FC5 build.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 1.0.10-5
- Update patch and spec to fix x86_64 build (-fPIC).

* Tue May 04 2004 Dag Wieers <dag@wieers.com> - 1.0.10-4
- Fixed bad symlinks. (Russ Herrold)

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 1.0.10-3
- Increased release to get elected.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.0.10-0
- Initial package. (using DAR)

