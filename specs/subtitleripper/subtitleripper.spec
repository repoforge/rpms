# $Id: subtitleripper.spec,v 1.1 2004/02/26 17:54:30 thias Exp $

%define real_version 0.3-2

Summary: DVD subtitle ripper
Name: subtitleripper
Version: 0.3.2
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://subtitleripper.sourceforge.net
Source: http://dl.sf.net/subtitleripper/%{name}-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: netpbm, zlib, transcode
BuildRequires: netpbm-devel, zlib-devel

%description
Converts DVD subtitles into text format (e.g. subrip) or VobSub.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp -a pgm2txt srttool subtitle2pgm subtitle2vobsub %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
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

