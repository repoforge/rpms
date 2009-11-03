# $Id$
# Authority: dag
# Upstream: <broadcast$earthling,net>

Summary: Quicktime for Linux
Name: quicktime4linux
Version: 2.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://heroinewarrior.com/quicktime.php3

Source: http://dl.sf.net/heroines/quicktime4linux-%{version}-src.tar.bz2
Patch: quicktime-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libmpeg3, ffmpeg

%description
Quicktime 4 Linux was the first convenient way to read and write
uncompressed Quicktime movies on Linux. Today Quicktime 4 Linux is
intended for content creation and uncompressed movies. These usually
arise during the production phase and not the consumer phase of a
movie. It has improvements in colormodel support, bit depth, accuracy,
reliability, and codecs, while not stressing economy. Users wishing
for a consumer library should use OpenQuicktime or FFMPEG.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -I%{_includedir}/ffmpeg"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 i686/libquicktime.a %{buildroot}%{_libdir}/libquicktime.a

%{__install} -d -m0755 %{buildroot}%{_includedir}/quicktime/
%{__install} -p -m0644 *.h %{buildroot}%{_includedir}/quicktime/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_includedir}/quicktime/

%changelog
* Tue Sep 13 2005 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Fri Aug 13 2004 Dag Wieers <dag@wieers.com> - 2.0.4-1
- Updated to release 2.0.4.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Updated to release 2.0.3.

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Updated to release 2.0.2.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.6.1-0
- Updated to release 1.6.1.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
