# $Id$
# Authority: matthias

Summary: MPEG ToolboX
Name: mpgtx
Version: 1.3.1
Release: 1%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://mpgtx.sourceforge.net/
Source: http://dl.sf.net/mpgtx/mpgtx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mpgtx a command line MPEG audio/video/system file toolbox, that slices and
joins audio and video files, including MPEG1, MPEG2 and MP3.


%prep
%setup


%build
./configure \
    --prefix=%{_prefix} \
    --manprefix=%{_datadir}
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    PREFIX=%{buildroot}%{_prefix} \
    manprefix=%{buildroot}%{_datadir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_mandir}/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*


%changelog
* Fri Jan 19 2007 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Initial RPM release.

