# $Id$
# Authority: matthias

%define real_version 0.3-4

Summary: DVD subtitle ripper
Name: subtitleripper
Version: 0.3.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://subtitleripper.sf.net/
Source: http://dl.sf.net/subtitleripper/subtitleripper-%{real_version}.tgz
Patch: subtitleripper-0.3.4-libnetpbm.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: netpbm, transcode
BuildRequires: netpbm, netpbm-devel, libpng-devel zlib-devel

%description
Converts DVD subtitles into text format (e.g. subrip) or VobSub.


%prep
%setup -n %{name}
%patch -p1 -b .libnetpbm


%build
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 pgm2txt srttool subtitle2pgm subtitle2vobsub \
    %{buildroot}%{_bindir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog README*
%{_bindir}/*


%changelog
* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.3.4-1
- Update to 0.3-4.
- Added patch to fix libppm vs. libnetpbm issue.
- Rebuild for Fedora Core 2.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3-2 (numbered as 0.3.2).
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.
- Rebuilt for Red Hat Linux 9.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Thu Oct 17 2002 Michel Alexandre Salim <salimma@freeshell.org>
- Initial RPM release.

