# $Id$

# Authority: dag

# Upstream: Carlos Hasan <chasan@acm.org>

%define rname seal
%define rversion 107

Summary: Synthetic Audio Library software development kit
Name: libseal
Version: 1.07
Release: 0
Group: System Environment/Libraries
License: LGPL
URL: http://linux.tlk.fr/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://files1.sonicspot.com/sealsdk/%{rname}%{rversion}.zip
Patch: libseal-1.07-debian.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: unzip

%description
Synthetic Audio Library Software Developers Kit (SEAL SDK) lets you
write applications that are able to play digital audio waveforms and
music modules on many platforms. It provides low-latency mixing,
hardware acceleration and dynamic digital filtering for improved sound
quality. The SDK includes the SEAL API header and library files, SEAL
audio library source code files (commercial license), a set of example
source code files and HTML documentation.

%prep
%setup -n %{rname}-%{version}
%patch0 -b .debian

%build
#configure
%{__make} %{?_smp_mflags} -C src linux

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}
%{__install} -m0755 src/mp %{buildroot}%{_bindir}/
%{__install} -m0755 lib/Linux/* %{buildroot}%{_libdir}/
%{__install} -m0644 src/audio.h %{buildroot}%{_includedir}/seal.h

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.TXT README.TXT doc/man.html
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/*.a

%changelog
* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 1.07-0
- Initial package. (using DAR)
