# $Id$

# Authority: dag

Summary: Quicktime for Linux
Name: quicktime4linux
Version: 1.6.1
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://heroinewarrior.com/quicktime.php3

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: quicktime-%{version}.tar.gz
Patch: quicktime-makefile.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libmpeg3

%description
Quicktime 4 Linux was the first convenient way to read and write
uncompressed Quicktime movies on Linux. Today Quicktime 4 Linux is
intended for content creation and uncompressed movies. These usually
arise during the production phase and not the consumer phase of a
movie. It has improvements in colormodel support, bit depth, accuracy,
reliability, and codecs, while not stressing economy. Users wishing
for a consumer library should use OpenQuicktime or FFMPEG.

%prep
%setup -n quicktime
%patch0 -p1

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
		%{buildroot}%{_includedir}/quicktime
%{__install} -m0755 i686/libquicktime.a %{buildroot}%{_libdir}
%{__install} -m0644 *.h %{buildroot}%{_includedir}/quicktime/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/*
%{_includedir}/quicktime/

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.6.1-0
- Updated to release 1.6.1.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
