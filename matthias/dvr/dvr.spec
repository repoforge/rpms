# Authority: dag
# Dists: rh73

Summary: Video4Linux Digital Video Recorder
Name: dvr
Version: 2.7.9
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://dvr.sourceforge.net

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/home-made/apt/

Source: ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
DVR is a tool to record movies on a computer equipped with a video
capture card. It can record and compress data in real time, using
recent codecs like DivX 5 or Indeo 5 for example. 

%prep
%setup

%build
%{__make}-1.4 || %{__make}

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
%{_bindir}/*
%{_datadir}/dvr/
%{_libdir}/lib/*

%changelog
* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 2.7.9-0
- Initial package. (using DAR)
