# $Id: subtitleripper.spec 700 2004-05-18 21:48:21Z dag $
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}
%define real_version 0.3-2

Summary: DVD subtitle ripper
Name: subtitleripper
Version: 0.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://subtitleripper.sourceforge.net/

Source: http://dl.sf.net/subtitleripper/subtitleripper-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: netpbm, netpbm-devel, zlib-devel
Requires: netpbm, zlib, transcode

%description
Converts DVD subtitles into text format (e.g. subrip) or VobSub.

%prep
%setup -n %{name}

### Make subtitleripper work with newer netpbm
%{?fc3:%{__perl} -pi.orig -e 's|^(LIBS)\s+\+=\s+-lppm$|$1 += -lnetpbm|' Makefile}
%{?fc2:%{__perl} -pi.orig -e 's|^(LIBS)\s+\+=\s+-lppm$|$1 += -lnetpbm|' Makefile}

%build
%{__make} %{?_smp_mflags} \
	COPT="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 pgm2txt srttool subtitle2pgm subtitle2vobsub %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README*
%{_bindir}/*

%changelog
* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.3.2-1.fr
- Update to 0.3-2 (numbered as 0.3.2).
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.
- Rebuilt for Red Hat Linux 9.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Thu Oct 17 2002 Michel Alexandre Salim <salimma@freeshell.org>
- Initial RPM release.

