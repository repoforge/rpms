# $Id$
# Authority: dag
# Upstream: Carlos Hasan <chasan$acm,org>

%define real_name seal
%define real_version 107

Summary: Synthetic Audio Library software development kit
Name: libseal
Version: 1.07
Release: 0.2%{?dist}
Group: System Environment/Libraries
License: LGPL
URL: http://linux.tlk.fr/

Source: http://files1.sonicspot.com/sealsdk/%{real_name}%{real_version}.zip
Patch0: libseal-1.07-debian.patch
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
%setup -n %{real_name}-%{version}
%patch0 -b .debian

%build
#configure
%{__make} %{?_smp_mflags} -C src linux

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -Dp -m0755 src/mp %{buildroot}%{_bindir}/mp
%{__install} -Dp -m0644 src/audio.h %{buildroot}%{_includedir}/seal.h

%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__install} -p -m0755 lib/Linux/* %{buildroot}%{_libdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.TXT README.TXT doc/man.html
%{_bindir}/mp
%{_includedir}/seal.h
%{_libdir}/*.a
%{_libdir}/*.so.*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-0.2
- Rebuild for Fedora Core 5.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 1.07-0
- Initial package. (using DAR)
