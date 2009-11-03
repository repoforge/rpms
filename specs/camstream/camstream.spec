# $Id$
# Authority: dag
# Upstream: CamStream Author <camstream$smcc,demon,nl>

Summary: collection of tools for webcams and other video-devices
Name: camstream
Version: 0.26.3
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://www.smcc.demon.nl/camstream/

Source: http://www.smcc.demon.nl/camstream/download/camstream-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, qt-devel

%description
A collection of tools for webcams and other video-devices, enxtending
your Linux system with multimedia video. All written in C++ and with
a nice GUI frontend. The interface is based on Qt, an excellent GUI
framework.

%prep
%setup

%build
%{?fc1:export CXX="g++296"}
%{?rh9:export CXX="g++296"}
./configure \
	--program-prefix="" --prefix="%{_prefix}" --exec-prefix="%{_prefix}" \
	--bindir="%{_bindir}" --sbindir="%{_sbindir}" --sysconfdir="%{_sysconfdir}" \
	--datadir="%{_datadir}" --includedir="%{_includedir}" --libdir="%{_libdir}" \
	--libexecdir="%{_libexecdir}" --localstatedir="%{_localstatedir}" \
	--sharedstatedir="%{_sharedstatedir}" --mandir="%{_mandir}" --infodir="%{_infodir}"
%{__make} %{?_smp_mflags} SHARE_DIR=%{_datadir} SHAREDIR=%{_datadir} BIN_DIR=%{_bindir}

%install
%{__rm} -rf %{buildroot}
%makeinstall SHARE_DIR=%{buildroot}%{_datadir} SHAREDIR=%{buildroot}%{_datadir} BIN_DIR=%{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/camstream
%{_datadir}/icons/*.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.26.3-0.2
- Rebuild for Fedora Core 5.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.26.3-0
- Update to release 0.26.3.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 0.26.2
- Initial package. (using DAR)
