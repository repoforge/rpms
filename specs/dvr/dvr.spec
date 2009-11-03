# $Id$
# Authority: dag

Summary: Video4Linux Digital Video Recorder
Name: dvr
Version: 3.2
Release: 1.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://dvr.sourceforge.net/

Source: http://dl.sf.net/dvr/dvr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: avifile-devel

%description
DVR is a tool to record movies on a computer equipped with a video
capture card. It can record and compress data in real time, using
recent codecs like DivX 5 or Indeo 5 for example.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	version="%{version}"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	version="%{version}"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%{_bindir}/*
%{_datadir}/dvr/
%{_libdir}/*.so.*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.2-1.2
- Rebuild for Fedora Core 5.

* Sun May 16 2004 Dag Wieers <dag@wieers.com> - 3.2-1
- Updated to release 3.2.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 2.7.9-0
- Initial package. (using DAR)
