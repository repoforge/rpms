# $Id$

# Authority: dag
# Upstream: CamStream Author <camstream@smcc.demon.nl>
# Dists: rh80

Summary: A collection of tools for webcams and other video-devices.
Name: camstream
Version: 0.26.2
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://www.smcc.demon.nl/camstream/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.smcc.demon.nl/camstream/download/camstream-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
A collection of tools for webcams and other video-devices, enxtending
your Linux system with multimedia video. All written in C++ and with
a nice GUI frontend. The interface is based on Qt, an excellent GUI
framework.

%prep
%setup

%build
#configure
export CXX="g++296"
./configure \
	--program-prefix="" --prefix="%{_prefix}" --exec-prefix="%{_prefix}" \
	--bindir="%{_bindir}" --sbindir="%{_sbindir}" --sysconfdir="%{_sysconfdir}" \
	--datadir="%{_datadir}" --includedir="%{_includedir}" --libdir="%{_libdir}" \
	--libexecdir="%{_libexecdir}" --localstatedir="%{_localstatedir}" \
	--sharedstatedir="%{_sharedstatedir}" --mandir="%{_mandir}" --infodir="%{_infodir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/pixmaps/gv4l/gv4l.png

%changelog
* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 0.26.2
- Initial package. (using DAR)
