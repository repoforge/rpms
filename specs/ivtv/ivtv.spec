# $Id$
# Authority: dag

Summary: iTVC15/16 and CX23415/16 driver utilities
Name: ivtv
Version: 0.10.6
Release: 1
License: distributable
Group: Applications/Multimedia
URL: http://ivtvdriver.org/

Source: http://dl.ivtvdriver.org/ivtv/archive/0.10.x/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#Requires: perl(Video::Capture::V4l)
#Requires: perl-Video-ivtv, perl-Video-Frequencies

%description
The primary goal of the IvyTV Project is to create a kernel driver for
the iTVC15 familiy of MPEG codecs. The iTVC15 family includes the
iTVC15 (CX24315) and iTVC16 (CX24316). These chips are commonly found
on Hauppauge's WinTV PVR-250 and PVR-350 TV capture cards.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{__make} -C utils PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}

#%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_libdir}/ivtv/
%{__make} -C utils install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"
%{__install} -p -m0755 utils/*.pl %{buildroot}%{_libdir}/ivtv/
%{__ln_s} -f ivtv-radio %{buildroot}%{_bindir}/radio-ivtv

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/* utils/README*
%{_libdir}/ivtv
%{_bindir}/cx25840ctl
%{_bindir}/ivtv-mpegindex
%{_bindir}/ivtv-radio
%{_bindir}/ivtv-tune
%{_bindir}/ivtvctl
%{_bindir}/ivtvfbctl
%{_bindir}/ivtvplay
%{_bindir}/ps-analyzer
%{_bindir}/radio-ivtv
%{_bindir}/v4l2-ctl

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/linux/ivtv.h

%changelog
* Sun Jun 15 2008 Dag Wieers <dag@wieers.com> - 0.10.6-1
- Initial package. (using DAR)
